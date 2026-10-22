"""Assemble the local review app. Refuses partial or reused question sets."""
import sys,json,random,re,hashlib,collections,unicodedata,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'work'))
from gs_science_geo import build_science_geo
from gs_polity_economy_current import build_polity_economy_current
from gs_history_telangana_society import build_history_telangana_society
from quant_learning import build_quant_lessons
from gs_learning import build_gs_lessons

def normal(s):
    return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',s).casefold()).strip()

def fingerprint(q):
    return normal(q['question'])+'|'+ '|'.join(sorted(normal(o['text']) for o in q['options']))

def build():
    quant=json.loads((ROOT/'work/quant-sets.json').read_text(encoding='utf-8'))
    gs=build_science_geo()+build_polity_economy_current()+build_history_telangana_society()
    assert len(gs)==2000, f'Need 2000 distinct GS questions; found {len(gs)}'
    expected={'General Science':400,'Geography':250,'Indian Polity':300,'Indian Economy':200,'Current affairs':150,'Indian History':250,'Telangana':350,'Environment & Social Awareness':100}
    counts=collections.Counter(q['topic'] for q in gs)
    assert dict(counts)==expected,(counts,expected)
    pools={}
    for topic in expected:
        p=[q for q in gs if q['topic']==topic]
        random.Random('accuracy-v1-'+topic).shuffle(p)
        pools[topic]=p
    sets=[];questions=[]
    for i in range(20):
        quota={'General Science':20,'Geography':13 if i%2==0 else 12,'Indian Polity':15,'Indian Economy':10,'Current affairs':7 if i%2==0 else 8,'Indian History':13 if i%2==0 else 12,'Telangana':17 if i%2==0 else 18,'Environment & Social Awareness':5}
        chosen=[]
        for topic,n in quota.items():
            chosen.extend(pools[topic][:n]);del pools[topic][:n]
        random.Random(4619+i).shuffle(chosen)
        paper=quant[i]+chosen
        assert len(paper)==200
        assert collections.Counter(q['section'] for q in paper)=={'Arithmetic & Reasoning':100,'General Studies':100}
        questions.extend(paper)
        sets.append({'id':f'mock-{i+1:02d}','number':i+1,'title':f'Mock {i+1:02d}','questionIds':[q['id'] for q in paper],'topicAllocation':quota})
    assert all(not p for p in pools.values())
    seen={};stems={};ids=set()
    for q in questions:
        assert q['id'] not in ids, f"Reused ID {q['id']}"
        ids.add(q['id'])
        key=fingerprint(q)
        assert key not in seen,f"Duplicate complete question: {q['id']} and {seen.get(key)}"
        seen[key]=q['id']
        stem=re.sub(r'[^\w\s]','',normal(q['question']))
        assert stem not in stems,f"Duplicate question stem: {q['id']} and {stems.get(stem)}"
        stems[stem]=q['id']
        assert len(q['options'])==4 and len({normal(o['text']) for o in q['options']})==4,q['id']
        assert isinstance(q['answer'],int) and 0<=q['answer']<4,q['id']
        assert all(len(o['explanation'].strip())>=25 for o in q['options']),q['id']
        assert len(q['explanation'].strip())>=25,q['id']
        assert q['question'].strip() and q['skill'].strip() and q['source']['title'].strip(),q['id']
    assert len(ids)==4000
    assert sum(len(s['questionIds']) for s in sets)==4000
    lessons=sorted(build_quant_lessons(quant)+build_gs_lessons(),key=lambda x:x['topic'])
    assert {l['topic'] for l in lessons}=={q['topic'] for q in questions}, 'Every bank topic needs a learning guide'
    assert len(lessons)==len({l['topic'] for l in lessons})
    for lesson in lessons:
        assert lesson['summary'] and lesson['methods']
        for method in lesson['methods']:
            assert len(method['steps'])>=3 and all(len(s.strip())>15 for s in method['steps'])
            assert method['example']['question'] and method['example']['solution'] and method['trap']
            assert method['source']['title']
    sources=json.loads((ROOT/'outputs/source-catalog.json').read_text(encoding='utf-8'))
    sources=[{'name':s['source'],'category':s['category'],'pages':s['pages']} for s in sources]
    data={'version':'accuracy-2026-local-review-v1','builtOn':'2026-10-20','questions':questions,'sets':sets,'sources':sources,'learning':lessons,
          'pattern':json.loads((ROOT/'work/exam-pattern.json').read_text(encoding='utf-8')),
          'topicCounts':dict(collections.Counter(q['topic'] for q in questions)),
          'contentNote':'No complete question is assigned to more than one set. Arithmetic and reasoning use 50 method families with 62 problem forms and distinct numerical/scenario variants, alongside 2,000 General Studies questions. Concepts and methods recur for practice. This is a local content-review edition, not an independently certified exam product.'}
    output=ROOT/'outputs/accuracy';output.mkdir(exist_ok=True)
    payload=json.dumps(data,ensure_ascii=False,separators=(',',':'))
    (output/'data.js').write_text('window.ACCURACY_DATA='+payload+';',encoding='utf-8')
    (output/'question-bank.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    html=(output/'index.html').read_text(encoding='utf-8')
    html=html.replace('<link rel="stylesheet" href="styles.css">','<style>'+(output/'styles.css').read_text(encoding='utf-8')+'</style>')
    for name in ['data.js','core.js','app.js']:
        script=(output/name).read_text(encoding='utf-8').replace('</script','<\\/script')
        html=html.replace(f'<script src="{name}"></script>','<script>'+script+'</script>')
    (ROOT/'outputs/Accuracy.html').write_text(html,encoding='utf-8')
    audit={'sets':20,'questions':4000,'gs':2000,'quant':2000,'questionsPerSet':200,'optionExplanations':16000,
           'learningTopics':len(lessons),'learningMethods':sum(len(l['methods']) for l in lessons),
           'reusedIds':0,'duplicateCompleteQuestions':0,'duplicateNormalizedStems':0,'quantTemplates':50,'quantProblemForms':62,'topicCounts':data['topicCounts'],
           'distribution':[{'set':s['title'],**s['topicAllocation']} for s in sets],
           'answerPositions':dict(collections.Counter(q['answer'] for q in questions)),
           'bankSha256':hashlib.sha256(payload.encode()).hexdigest(),
           'limits':['No independent expert certification of all factual answers.','Methods and concepts recur; numeric variants are included.','Current affairs are a dated selection, not exhaustive.','English only.']}
    (ROOT/'work/accuracy-audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in audit.items() if k not in ['distribution','topicCounts']},indent=2))
    return data
if __name__=='__main__':build()
