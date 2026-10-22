"""Flag possible factual repeats for human review; similarity is not proof."""
import json,re,unicodedata,difflib,collections,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
def norm(s):return re.sub(r'[^\w ]',' ',unicodedata.normalize('NFKC',s).casefold())
def tokens(s):return set(norm(s).split())-set('which what is the a an of in to and for as at by with that this on from was were are has had does do it its most called term describes name known under'.split())
def run(path):
    content=json.loads(Path(path).read_text(encoding='utf-8'))
    qs=content['questions'] if isinstance(content,dict) else content
    qs=[q for q in qs if q['section']=='General Studies']
    findings=[]
    for i,q in enumerate(qs):
        ts=tokens(q['question']);ans=norm(q['options'][q['answer']]['text']).strip()
        for r in qs[i+1:]:
            rs=tokens(r['question']);union=ts|rs
            jac=len(ts&rs)/max(1,len(union));same=ans==norm(r['options'][r['answer']]['text']).strip()
            if (same and jac>=.25) or jac>=.72:
                ratio=difflib.SequenceMatcher(None,norm(q['question']),norm(r['question'])).ratio()
                findings.append({'left':q['id'],'right':r['id'],'sameAnswer':same,'jaccard':round(jac,3),'textRatio':round(ratio,3),'question1':q['question'],'question2':r['question'],'answer1':q['options'][q['answer']]['text'],'answer2':r['options'][r['answer']]['text']})
    findings.sort(key=lambda f:(f['sameAnswer'],f['jaccard']),reverse=True)
    dest=ROOT/'work/similarity-review.json';dest.write_text(json.dumps(findings,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'items':len(qs),'pairsToReview':len(findings),'sameAnswerPairs':sum(f['sameAnswer'] for f in findings),'report':str(dest)}))
if __name__=='__main__':run(sys.argv[1])
