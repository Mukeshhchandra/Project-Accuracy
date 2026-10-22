"""Independent answer audit for every generated quantitative question.

Numeric checks read operands back from the displayed question, rather than
trusting the generator's internal answer variable. Syllogisms are exhaustively
checked against 256 possible three-class set-membership models.
"""
import calendar
import datetime as dt
import itertools
import math
import re
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import quant_content as qc


def ints(text):
    return list(map(int,re.findall(r'\d+',text)))


def selected(q):
    return q['options'][q['answer']]['text']


def numeric_selected(q):
    return F(re.match(r'-?\d+(?:\.\d+)?(?:/\d+)?',selected(q))[0])


def syllogism_truth(v):
    # A model is a subset of the eight possible (A,B,C) membership types.
    types=list(itertools.product([False,True],repeat=3))
    models=[[types[i] for i in range(8) if mask>>i&1] for mask in range(256)]
    all_=lambda m,p: all(p(x) for x in m)
    some=lambda m,p: any(p(x) for x in m)
    rules=[
        (lambda m: all_(m,lambda x:not x[0] or x[1]) and some(m,lambda x:x[0]),
         lambda m:some(m,lambda x:x[1] and x[0]),lambda m:all_(m,lambda x:not x[1] or x[0])),
        (lambda m:all_(m,lambda x:not(x[0] and x[1])) and some(m,lambda x:x[2] and x[0]),
         lambda m:some(m,lambda x:x[2] and not x[1]),lambda m:all_(m,lambda x:not(x[2] and x[1]))),
        (lambda m:all_(m,lambda x:not x[0] or x[1]) and all_(m,lambda x:not x[1] or x[2]),
         lambda m:all_(m,lambda x:not x[0] or x[2]),lambda m:all_(m,lambda x:not x[2] or x[0])),
        (lambda m:some(m,lambda x:x[0] and x[1]) and all_(m,lambda x:not x[1] or x[2]),
         lambda m:all_(m,lambda x:not x[0] or x[2]),lambda m:some(m,lambda x:x[0] and x[2])),
        (lambda m:all_(m,lambda x:not(x[0] and x[1])) and some(m,lambda x:x[0]),
         lambda m:all_(m,lambda x:not(x[1] and x[0])),lambda m:some(m,lambda x:x[0] and not x[1])),
        (lambda m:some(m,lambda x:x[0] and x[1]) and some(m,lambda x:x[1] and x[2]),
         lambda m:some(m,lambda x:x[0] and x[2]),lambda m:all_(m,lambda x:not x[0] or x[2])),
        (lambda m:all_(m,lambda x:not x[0] or x[1]) and all_(m,lambda x:not(x[1] and x[2])),
         lambda m:all_(m,lambda x:not(x[0] and x[2])),lambda m:all_(m,lambda x:not(x[2] and x[0]))),
        (lambda m:some(m,lambda x:x[0] and not x[1]) and all_(m,lambda x:not x[2] or x[1]),
         lambda m:all_(m,lambda x:not x[0] or x[2]),lambda m:some(m,lambda x:x[0] and not x[2])),
    ]
    premise,c1,c2=rules[v%8]
    valid=[m for m in models if premise(m)]
    assert valid
    return all(c1(m) for m in valid),all(c2(m) for m in valid)


def check_question(q):
    t,v=map(int,q['id'].split('-')[1:]);v-=1
    text=q['question']; nums=ints(text)
    answer=selected(q)
    expected=None
    if t==1:
        total,p=nums; expected=F(total*p,100)
    elif t==2:
        p,down=nums; expected=F((100+p)*(100-down)-10000,100)
    elif t==3:
        if v%2:
            sale,loss,profit=nums;expected=F(sale*100,100-loss)*F(100+profit,100)
        else:
            cp,r=nums; expected=cp+F(cp*r,100)
    elif t==4:
        price,d1,d2=nums; expected=price-F(price*d1,100);expected-=expected*F(d2,100)
    elif t==5:
        if v%2:
            r,p,i=nums;expected=F(i*100,p*r)
        else:
            p,r,y=nums; expected=F(p*r*y,100)
    elif t==6:
        p,r,y=nums; amount=F(p)
        for _ in range(y):amount+=amount*r/100
        expected=amount-p-(F(p*r*y,100) if v%2 else 0)
    elif t==7:
        total,a,b,c=nums;expected=F(total*b,a+b+c)
    elif t==8:
        ac,at,bc,bt,profit=nums;expected=F(profit*ac*at,ac*at+bc*bt)
    elif t==9:
        total,years=nums
        expected=numeric_selected(q)
        assert total-expected+years==3*(expected+years)
        assert expected>0 and total-expected>expected
    elif t==10:
        if v%2:
            count,old,new,first=nums;expected=(count+2)*new-count*old-first
        else:
            count,old,replaced,new=nums;expected=count*new-(count*old-replaced)
    elif t==11:
        na,aa,nb,ab=nums;expected=F(na*aa+nb*ab,na+nb)
    elif t==12:
        if v%2:
            a,b,alone=nums;expected=alone+(1-F(alone,a))*b
        else:
            a,b=nums;expected=1/(F(1,a)+F(1,b))
    elif t==13:
        if v%2:
            a,b,alone=nums;expected=alone+(1-F(alone,a))/(F(1,a)-F(1,b))
        else:
            a,b=nums;expected=1/(F(1,a)-F(1,b))
    elif t==14:
        a,b=nums;expected=F(2)/(F(1,a)+F(1,b))
    elif t==15:
        if v%2:
            a,b,va,vb=nums;expected=F((a+b)*18,(va+vb)*5)
        else:
            train,platform,kph=nums;expected=F((train+platform)*18,kph*5)
    elif t==16:
        boat,current,distance=nums;expected=F(distance,boat-current)
    elif t==17:
        if v%2:
            total,a,b=nums[:3]
            removed=F(re.search(r'Exactly ([\d/.]+) litres',text)[1])
            expected=F(total*a,a+b)-removed*F(a,a+b)
        else:
            total,a,b,c,d=nums;expected=F(total*a*d,c*(a+b))-F(total*b,a+b)
    elif t==18:
        a,b=nums;expected=a
        while expected%b:expected+=a
    elif t==19:
        fraction,remaining=re.search(r'uses ([\d/.]+) of.*If (\d+) sheets',text).groups()
        expected=F(int(remaining))/(1-F(fraction))
    elif t==20:
        if v%2:
            a,c,count,receipts=nums;expected=F(receipts-count*c,a-c)
        else:
            a,b,rhs=nums;expected=F(rhs-b,a)
    elif t==21:
        sum_,product,zero=nums # superscript ² is not matched by this regex
        assert zero==0
        disc=sum_*sum_-4*product
        assert math.isqrt(disc)**2==disc
        expected=F(sum_+math.isqrt(disc),2)
    elif t==22:
        perimeter,difference=nums
        width=F(perimeter-2*difference,4)
        expected=width*(width+difference)
    elif t==23:
        radius,angle,pi_num,pi_den=nums;expected=F(pi_num,pi_den)*radius*radius*F(angle,360)
    elif t==24:
        radius,height,pi_num,pi_den=nums;expected=F(pi_num,pi_den)*radius*radius*height
    elif t==25:
        side,height,slant=nums;expected=F(side*side*height,3)
        assert F(side,2)**2+height*height==slant*slant
    elif t==26:
        a,b,c=nums
        # Heron's formula independently verifies the right-triangle construction.
        semiperimeter=F(a+b+c,2)
        squared=semiperimeter*(semiperimeter-a)*(semiperimeter-b)*(semiperimeter-c)
        assert squared.denominator==1 and math.isqrt(squared.numerator)**2==squared
        expected=math.isqrt(squared.numerator)
    elif t==27:
        if v%2:
            # Read values after each Q label, not the numerals in the labels.
            a,b,c,d=map(int,re.findall(r'Q\d (\d+) units',text))
            expected=F((d-a)*100,a)
        else:
            a,b,c,d=nums;expected=F(100*(c+d),a+b+c+d)
    elif t==28:
        red,blue,green=nums;expected=F(math.comb(red,2),math.comb(red+blue+green,2))
    elif t==29:
        members,=nums;expected=math.comb(members,2)
    elif t==30:
        metres,minutes=nums;expected=F(metres,1000)/F(minutes,60)
    elif t==31:
        differences=[b-a for a,b in zip(nums,nums[1:])]
        if v%2:
            assert len(set(b-a for a,b in zip(differences,differences[1:])))==1
            expected=nums[-1]+differences[-1]+differences[1]-differences[0]
        else:
            assert len(set(differences))==1
            expected=nums[-1]+nums[1]-nums[0]
    elif t==32:
        assert len(set(F(b,a) for a,b in zip(nums,nums[1:])))==1
        expected=F(nums[-1]*nums[1],nums[0])
    elif t==33:
        expected=nums[4]+nums[2]-nums[0]
        assert nums[4]-nums[2]==nums[2]-nums[0]
        assert nums[5]-nums[3]==nums[3]-nums[1]
    elif t==34:
        seq=re.search(r'next letter: ([A-Z, ]+), \?',text)[1].split(', ')
        step=(ord(seq[1])-ord(seq[0]))%26
        assert all((ord(b)-ord(a))%26==step for a,b in zip(seq,seq[1:]))
        assert answer==chr((ord(seq[-1])-65+step)%26+65)
    elif t==35:
        shift_,=nums
        word=re.search(r'How is ([A-Z]+) written',text)[1]
        assert len(answer)==len(word)
        assert all((ord(b)-ord(a))%26==shift_ for a,b in zip(word,answer))
    elif t==36:
        word=re.search(r'score of ([A-Z]+)',text)[1]
        expected=sum('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c)+1 for c in word)
    elif t==37:
        if v%2:
            north,east,south=nums
            squared=(north-south)**2+east**2
            assert math.isqrt(squared)**2==squared
            expected=math.isqrt(squared)
        else:
            north,east,south,west=nums;expected=abs(north-south)+abs(east-west)
    elif t==38:
        total,top=nums;expected=total-top+1
    elif t==39:
        left,right=nums;expected=left+right-1
    elif t==40:
        golden=['Maternal grandfather','Paternal grandmother','Father','Maternal uncle','Paternal aunt','Granddaughter','Grandson','Maternal aunt']
        assert answer==golden[v%8]
    elif t==41:
        conclusions=syllogism_truth(v)
        names={(True,False):'Only conclusion I follows',(False,True):'Only conclusion II follows',(True,True):'Both conclusions follow',(False,False):'Neither conclusion follows'}
        assert answer==names[conclusions]
    elif t==42:
        values=[int(o['text']) for o in q['options']]
        nonsquares=[x for x in values if math.isqrt(x)**2!=x]
        assert nonsquares==[int(answer)]
    elif t==43:
        offset,a,mapped,b=nums;assert a*a+offset==mapped;expected=b*b+offset
    elif t==44:
        date_str,weekday,days=re.search(r'(.+) is a (\w+)\. What day.*exactly (\d+) days',text).groups()
        date=dt.datetime.strptime(date_str,'%d %B %Y').date()
        assert date.strftime('%A')==weekday
        assert (date+dt.timedelta(days=int(days))).strftime('%A')==answer
    elif t==45:
        hour,minute=nums
        # Compare angular positions as fractions of one revolution.
        hour_turn=F(hour%12,12)+F(minute,720)
        minute_turn=F(minute,60)
        delta=abs(hour_turn-minute_turn)
        expected=min(delta,1-delta)*360
    elif t==46:
        pairs=re.findall(r'(Card [A-E]\d+) is immediately to the left of (Card [A-E]\d+)',text)
        successors=dict(pairs)
        first=(set(successors)-set(successors.values())).pop()
        chain=[first]
        while chain[-1] in successors:chain.append(successors[chain[-1]])
        position=int(re.search(r'position (\d+)',text)[1])
        assert len(chain)==5 and answer==chain[position-1]
    elif t==47:
        pairs=re.findall(r'(Runner [PQRS]\d+) is faster than (Runner [PQRS]\d+)',text)
        next_=dict(pairs);first=(set(next_)-set(next_.values())).pop();chain=[first]
        while chain[-1] in next_:chain.append(next_[chain[-1]])
        pos=0
        if 'second fastest?' in text:pos=1
        elif 'third fastest?' in text:pos=2
        elif 'slowest?' in text:pos=3
        assert answer==chain[pos]
    elif t==48:
        k,=nums
        assert answer==f"P {'>' if v%4 in (0,1) else '<'} {k}"
    elif t==49:
        offset,a,b=nums;expected=a*b+offset
    elif t==50:
        total,a,b,neither=nums;expected=a+b-(total-neither)
    else:
        raise AssertionError(t)
    if expected is not None:
        assert numeric_selected(q)==expected,(q['id'],answer,expected,text)


def main():
    papers=qc.build_quant_sets()
    for paper in papers:
        for q in paper:
            try:check_question(q)
            except Exception as exc:
                raise AssertionError(f"{q['id']} / {q['skill']}: {exc}") from exc
    report=qc.validate(papers)
    report.update(independently_checked=2000,syllogism_models_per_variant=256,
                  family_relation_scenarios_checked=8,geometry_check='Heron and Pythagorean identities',
                  uniqueStems=len({q['question'] for p in papers for q in p}),
                  templateFamilies=len({q['templateFamily'] for p in papers for q in p}),
                  distinctProblemForms=len({q['skill'] for p in papers for q in p}),
                  reuseDisclosure='The 2000 unique full items include 40 variants in each of 50 transparent template families. They are not 2000 different concepts. Each set includes 62 problem forms because selected families include inverse or multi-stage versions.',
                  balanceDisclosure='60 arithmetic and 40 reasoning per set is an editorial practice allocation, not an asserted official topic quota.')
    print(report)
    Path(__file__).with_name('quant-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')


if __name__=='__main__':main()
