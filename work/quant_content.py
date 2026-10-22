"""Original, deterministic quantitative aptitude and reasoning practice.

The module creates 20 sets of 100 questions. Questions are newly authored;
none is transcribed from the supplied OCR or represented as an official paper.
Each set contains two variants of each of 30 arithmetic and 20 reasoning skills.
All numeric arithmetic uses integers or Fraction, never floating point money.
Run this module to validate the collection and write work/quant-sets.json.
"""
from __future__ import annotations

import calendar
import datetime as dt
import json
import math
import random
import itertools
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

AUDIT = []


def fmt(value):
    value = F(value)
    if value.denominator == 1:
        return str(value.numerator)
    if 1000 % value.denominator == 0:
        return f"{float(value):.3f}".rstrip("0").rstrip(".")
    return f"{value.numerator}/{value.denominator}"


def make(t, v, topic, skill, question, choices, correct, explanation,
         difficulty="Standard"):
    """Choices are (display value, explanation); shuffle answer position."""
    assert len(choices) == 4 and len({str(c[0]) for c in choices}) == 4, (skill, choices)
    assert all(len(c[1]) > 25 for c in choices), skill
    order = list(range(4))
    random.Random(27011 + t * 2003 + v * 97).shuffle(order)
    q = {
        "id": f"A-{t:02d}-{v+1:02d}",
        "section": "Arithmetic & Reasoning",
        "topic": topic,
        "skill": skill,
        "question": question,
        "options": [{"text": str(choices[i][0]), "explanation": choices[i][1]} for i in order],
        "answer": order.index(correct),
        "explanation": explanation,
        "source": {"title": f"Original worked problem · {skill}", "page": None, "url": None},
        "difficulty": difficulty,
        "origin": "Original practice",
        "templateFamily": f"quant-family-{t:02d}",
        "templateVariant": v + 1,
    }
    AUDIT.append({"id": q["id"], "template": t, "variant": v,
                  "answer": str(choices[correct][0]), "question": question})
    return q


def numeric(t, v, topic, skill, question, answer, distractors, explanation,
            unit="", difficulty="Standard"):
    """Distractors are (value, reason for the error); avoid hidden rounding."""
    answer = F(answer)
    candidates = [(answer, f"Correct. {explanation}")]
    used = {answer}
    for value, reason in distractors:
        value = F(value)
        if value not in used:
            candidates.append((value, f"Incorrect. {reason} The required answer is {fmt(answer)}{unit}."))
            used.add(value)
    # A collision can occur for a particular numeric variant. Substitute a
    # documented arithmetic-slip alternative instead of creating duplicate options.
    for delta in (1, -1, 2, -2, 3, 5, 10):
        if len(candidates) >= 4:
            break
        value = answer + delta
        if value not in used and value >= 0:
            candidates.append((value, f"Incorrect. This is {fmt(abs(delta))}{unit} {'above' if delta > 0 else 'below'} the result. {explanation}"))
            used.add(value)
    assert len(candidates) >= 4
    choices = [(f"{fmt(x)}{unit}", why) for x, why in candidates[:4]]
    return make(t, v, topic, skill, question, choices, 0, explanation, difficulty)


def arithmetic(t, v):
    n = v + 1
    if t == 1:
        total, p = 400 + 20 * n, 10 + 5 * (v % 7)
        ans = F(total * p, 100)
        assert ans * 100 == total * p
        exp = f"{p}% of {total} = {total} × {p}/100 = {fmt(ans)}. A percentage is a fraction out of 100."
        return numeric(t,v,"Percentages","Percentage of a quantity",f"A training centre has {total} candidates. {p}% choose the morning session. How many candidates choose that session?",ans,[(total-ans,"This counts candidates who do not choose the morning session."),(ans*10,"The percentage divisor was treated as 10 instead of 100."),(F(total,p),"Dividing the total by the percentage is not the percentage-of calculation.")],exp,difficulty="Foundation")
    if t == 2:
        p, q = 10 + v%9, 5 + v//3
        ans = F((100+p)*(100-q),100)-100
        exp = f"Take the original as 100. After the increase it is {100+p}; after the decrease it is {fmt(F((100+p)*(100-q),100))}. The net percentage increase is {fmt(ans)}%."
        # Keep the question's sign explicit: some variants have a net decrease.
        exp = f"New/original = (1 + {p}/100)(1 − {q}/100). Net change = {p} − {q} − {p}×{q}/100 = {fmt(ans)}%. A negative result denotes a decrease."
        return numeric(t,v,"Percentages","Successive percentage changes",f"A price first increases by {p}% and then decreases by {q}%. What is the signed net percentage change from the original price? Use a negative value for a decrease.",ans,[(p-q,"Subtracting the rates ignores that the decrease applies to the increased base."),(p+q,"Both changes cannot be added as increases."),(F(p-q)+F(p*q,100),"The product term must be subtracted when one change is a decrease.")],exp,unit="%")
    if t == 3:
        if v%2:
            cost=100*(20+n); loss=8+v%9; profit=12+v%7
            sale=cost*(100-loss)//100
            ans=cost*(100+profit)//100
            exp=f"The first selling price is {100-loss}% of cost, so cost = {sale}×100/{100-loss} = ₹{cost}. For a {profit}% profit, the new price is {cost}×{100+profit}/100 = ₹{ans}. Both percentages use cost price."
            return numeric(t,v,"Profit & loss","Recovering cost before repricing",f"An article is sold for ₹{sale} at a loss of {loss}% on cost. At what price should it instead be sold to earn a profit of {profit}% on cost?",ans,[(F(sale*(100+profit),100),"This calculates profit on the old selling price rather than the recovered cost."),(F(sale*(100+loss+profit),100),"Adding the loss and desired profit rates to the discounted base does not restore the cost correctly."),(cost,"This recovers the cost but adds no profit.")],exp,unit=" rupees")
        cost, rate = 600 + 25*n, 8 + v%13
        sell = F(cost*(100+rate),100)
        exp = f"Profit = {rate}% of cost = {cost} × {rate}/100. Selling price = cost × (100 + {rate})/100 = ₹{fmt(sell)}."
        return numeric(t,v,"Profit & loss","Profit on cost price",f"An article costs ₹{cost}. At a profit of {rate}% on cost price, what is its selling price?",sell,[(F(cost*(100-rate),100),"This subtracts a loss instead of adding the stated profit."),(F(cost*100,100-rate),"This treats profit as a percentage of selling price."),(F(cost*rate,100),"This is the profit alone, not cost plus profit.")],exp,unit=" rupees",difficulty="Foundation")
    if t == 4:
        price,a,b = 1500+50*n,10+v%6,5+v%4
        ans=F(price*(100-a)*(100-b),10000)
        exp=f"Apply each discount to the current price: {price} × {100-a}/100 × {100-b}/100 = ₹{fmt(ans)}. The two discount rates cannot simply be added."
        return numeric(t,v,"Profit & loss","Successive discounts",f"A bag is marked at ₹{price}. Successive discounts of {a}% and {b}% are applied. What does a customer pay?",ans,[(F(price*(100-a-b),100),"Adding the discount rates overstates the reduction."),(F(price*(100-a),100),"This applies only the first discount."),(price-ans,"This is the total discount amount, not the price paid.")],exp,unit=" rupees")
    if t == 5:
        principal,rate,years=4000+200*n,5+v%8,2+v%4
        interest=F(principal*rate*years,100)
        if v%2:
            exp=f"From I = PRT/100, time = 100I/(PR) = 100×{fmt(interest)}/({principal}×{rate}) = {years} years. The stated amount is interest alone."
            return numeric(t,v,"Interest","Finding time from simple interest",f"At {rate}% per annum simple interest, an investment of ₹{principal} earns ₹{fmt(interest)} in interest. For how many years was the money invested?",years,[(F(interest*100,principal),"This is the total percentage return; it must be divided by the annual rate."),(F(interest,principal*rate),"The percentage rate needs a factor of 100 in the time formula."),(years+1,"This adds an extra year not supported by the given interest.")],exp,unit=" years")
        exp=f"Simple interest = PRT/100 = {principal} × {rate} × {years}/100 = ₹{fmt(interest)}. Interest is calculated on the original principal each year."
        return numeric(t,v,"Interest","Simple interest",f"Find the simple interest on ₹{principal} at {rate}% per annum for {years} years.",interest,[(principal+interest,"This is the final amount including principal."),(F(principal*rate,100),"This calculates interest for only one year."),(interest*2,"The stated time has already been included; doubling it counts the period twice.")],exp,unit=" rupees",difficulty="Foundation")
    if t == 6:
        p,r=10000+1000*n,5+v%6
        ci=F(p*((100+r)**2-10000),10000)
        if v%2:
            diff=F(p*r*r,10000)
            exp=f"For two years, CI − SI equals interest earned on the first year's interest: P(r/100)² = {p}×({r}/100)² = ₹{fmt(diff)}."
            return numeric(t,v,"Interest","Compound versus simple interest",f"On ₹{p} at {r}% per annum, what is the difference between compound interest compounded annually and simple interest over exactly 2 years?",diff,[(F(p*r,100),"This is one year's simple interest, not the interest-on-interest difference."),(ci,"This is the whole compound interest, before subtracting simple interest."),(F(2*p*r,100),"This is the whole simple interest for two years.")],exp,unit=" rupees")
        exp=f"Amount after two years = {p} × ({100+r}/100)². Subtracting principal gives compound interest ₹{fmt(ci)}. The second year's interest includes interest on the first year's interest."
        return numeric(t,v,"Interest","Annual compound interest",f"₹{p} is invested at {r}% per annum, compounded annually. What is the compound interest after exactly 2 years?",ci,[(F(2*p*r,100),"This uses simple interest and omits interest on the first year's interest."),(p+ci,"This is the maturity amount, not the interest."),(F(p*r,100),"This includes only the first year's interest.")],exp,unit=" rupees")
    if t == 7:
        a,b,c=2+v%3,5+v%4,9+v%5
        unit=25+5*n
        total=(a+b+c)*unit
        ans=b*unit
        exp=f"The ratio has {a+b+c} total parts. One part = {total}/{a+b+c} = {unit}; B receives {b} × {unit} = ₹{ans}."
        return numeric(t,v,"Ratio & proportion","Sharing in a three-part ratio",f"₹{total} is divided among A, B and C in the ratio {a}:{b}:{c}. What is B's share?",ans,[(a*unit,"This is A's share."),(c*unit,"This is C's share."),(F(total,3),"Equal division is inappropriate because the stated shares have a ratio.")],exp,unit=" rupees",difficulty="Foundation")
    if t == 8:
        a,b=20+n,30+n
        ma,mb=8,6
        unit=10+v
        total=(a*ma+b*mb)*unit
        ans=a*ma*unit
        exp=f"Profit is proportional to capital × time. A:B = {a}×{ma}:{b}×{mb} = {a*ma}:{b*mb}. A's share = {total} × {a*ma}/{a*ma+b*mb} = ₹{ans}."
        return numeric(t,v,"Ratio & proportion","Partnership capital and time",f"A invests ₹{a*1000} for {ma} months and B invests ₹{b*1000} for {mb} months. They divide a profit of ₹{total} in proportion to capital × time. Find A's share.",ans,[(F(total*a,a+b),"This weights capital but ignores the different investment periods."),(b*mb*unit,"This is B's share."),(F(total,2),"Equal shares ignore both capital and time.")],exp,unit=" rupees")
    if t == 9:
        child=8+n
        future=5+v%6
        parent=3*(child+future)-future
        total=child+parent
        exp=f"Let the child's present age be x. The parent's present age is {total} − x. Then {total} − x + {future} = 3(x + {future}); hence 4x = {total-2*future}, so x = {child}."
        assert parent+future==3*(child+future)
        return numeric(t,v,"Ages","Present and future ages",f"The present ages of a parent and child total {total} years. After {future} years, the parent will be three times the child's age. What is the child's present age?",child,[(child+future,"This is the child's future age."),(parent,"This is the parent's present age."),(F(total,4),"Dividing the current total in a 3:1 ratio applies the future ratio to the present.")],exp,unit=" years")
    if t == 10:
        count,old,new=8+v%6,45+n,51+n+v%4
        if v%2:
            first=60+v
            second=(count+2)*new-count*old-first
            exp=f"Original total = {count}×{old} = {count*old}. New total = {count+2}×{new} = {(count+2)*new}. The two new scores total {(count+2)*new-count*old}; subtracting {first} gives {second}."
            return numeric(t,v,"Averages","Adding two observations",f"The average score of {count} students is {old}. Two more students join and the average becomes {new}. One new student scored {first}. What did the other new student score?",second,[((count+2)*new-count*old,"This is the sum of both new scores, before subtracting the known score."),(count*(new-old)-first,"This changes the original group's total but ignores the two additional observations in the new average."),(2*new-first,"This assumes the two newcomers average the new class average, which need not be true.")],exp,unit=" marks")
        removed=30+v%7
        added=count*(new-old)+removed
        exp=f"Total increases by {count} × ({new} − {old}) = {count*(new-old)}. Replacing {removed} means the new value is {removed} + {count*(new-old)} = {added}."
        return numeric(t,v,"Averages","Replacing one observation",f"The average of {count} numbers is {old}. One number, {removed}, is replaced and the new average becomes {new}. What number replaces it?",added,[(added-removed,"This is the increase in the total, before adding back the removed number."),(removed+new-old,"The average change must be multiplied by the number of observations."),(added+removed,"Adding the removed value twice overstates the replacement.")],exp)
    if t == 11:
        na,nb=20+v,30+v
        avga,avgb=40+v%8,60+v%9
        ans=F(na*avga+nb*avgb,na+nb)
        exp=f"Combined average = total marks/total students = ({na}×{avga} + {nb}×{avgb})/({na}+{nb}) = {fmt(ans)}. The two group averages need weights."
        return numeric(t,v,"Averages","Weighted average",f"Group A has {na} students with average marks {avga}; group B has {nb} students with average marks {avgb}. What is the average for all students together?",ans,[(F(avga+avgb,2),"This gives equal weight to unequal group sizes."),(avga,"This ignores every student in group B."),(avgb,"This ignores every student in group A.")],exp,unit=" marks")
    if t == 12:
        k=3+n
        a,b=2*k,3*k
        ans=F(a*b,a+b)
        if v%2:
            remaining=1-F(k,a)
            elapsed=k+remaining*b
            exp=f"A completes {k}/{a} = {fmt(F(k,a))} of the job. B must do the remaining {fmt(remaining)}, taking {fmt(remaining*b)} days. Including A's initial {k} days, total time is {fmt(elapsed)} days."
            assert F(k,a)+F(elapsed-k,b)==1
            return numeric(t,v,"Time & work","A worker leaves before completion",f"A alone can finish a job in {a} days and B alone in {b} days. A works alone for {k} days and then stops. B then completes the remaining work alone. What is the total elapsed time from A starting to B finishing?",elapsed,[(remaining*b,"This is B's time only and omits A's initial working period."),(ans,"This would be the time if both worked together from the start."),(a+b,"Both workers do not each complete the whole job.")],exp,unit=" days",difficulty="Challenge")
        exp=f"A completes 1/{a} and B 1/{b} of the job per day. Together their rate is 1/{a} + 1/{b} = {fmt(F(1,a)+F(1,b))}; time is its reciprocal, {fmt(ans)} days."
        assert ans*(F(1,a)+F(1,b))==1
        return numeric(t,v,"Time & work","Combined work rates",f"A alone completes a job in {a} days and B alone in {b} days. At constant independent rates, how long do they take working together?",ans,[(a+b,"Adding completion times does not combine simultaneous work rates."),(F(a+b,2),"The average of completion times is not the joint completion time."),(F(a*b,b-a),"Subtracting rates would model opposition rather than cooperation.")],exp,unit=" days")
    if t == 13:
        k=4+n
        fill,empty=2*k,5*k
        ans=F(fill*empty,empty-fill)
        if v%2:
            remaining=1-F(k,fill)
            after=remaining/(F(1,fill)-F(1,empty))
            elapsed=k+after
            exp=f"The inlet first fills {k}/{fill} = {fmt(F(k,fill))} of the tank. The rest is filled at net rate 1/{fill}−1/{empty}, taking {fmt(after)} hours. Total elapsed time = {k}+{fmt(after)} = {fmt(elapsed)} hours."
            assert F(k,fill)+(elapsed-k)*(F(1,fill)-F(1,empty))==1
            return numeric(t,v,"Time & work","An outlet opens after a delay",f"An inlet fills an empty tank in {fill} hours, and an outlet empties it in {empty} hours. Only the inlet runs for the first {k} hours; then the outlet is also opened and both remain open. What is the total time from the start until the tank becomes full?",elapsed,[(ans,"This assumes the outlet was open from the start."),(after,"This omits the initial period with only the inlet open."),(fill,"This ignores the water lost after the outlet opens.")],exp,unit=" hours",difficulty="Challenge")
        exp=f"Net filling rate = 1/{fill} − 1/{empty} = {fmt(F(1,fill)-F(1,empty))} tank/hour. Time = 1/(net rate) = {fmt(ans)} hours. The outlet opposes filling."
        assert ans*(F(1,fill)-F(1,empty))==1
        return numeric(t,v,"Time & work","Inlet and outlet pipes",f"An inlet fills an empty tank in {fill} hours. An outlet empties a full tank in {empty} hours. Both stay open from the start. How long does it take to fill the tank?",ans,[(F(fill*empty,empty+fill),"This adds the rates as if both pipes were inlets."),(empty-fill,"Subtracting the times does not subtract flow rates."),(fill,"This ignores the open outlet.")],exp,unit=" hours")
    if t == 14:
        a,b=30+n,50+n
        ans=F(2*a*b,a+b)
        exp=f"For equal distances d, total time is d/{a} + d/{b}. Average speed = 2d/(d/{a}+d/{b}) = 2×{a}×{b}/({a}+{b}) = {fmt(ans)} km/h."
        return numeric(t,v,"Speed & distance","Average speed over equal distances",f"A rider travels from P to Q at {a} km/h and returns along the same route at {b} km/h. Excluding stops, what is the average speed for the whole journey?",ans,[(F(a+b,2),"The arithmetic mean is valid for equal travel times, not equal distances."),(b-a,"The difference of the speeds is not distance divided by total time."),(F(a*b,a+b),"This omits the factor of two for the outward and return distances.")],exp,unit=" km/h")
    if t == 15:
        speed=36+18*(v%5)
        length=100+10*n
        platform=80+5*n
        if v%2:
            speed2=18+18*(v%3)
            relative=F((speed+speed2)*5,18)
            time=F(length+platform,relative)
            exp=f"Opposite-direction relative speed = {speed}+{speed2} = {speed+speed2} km/h = {fmt(relative)} m/s. The trains fully cross after covering their combined length {length+platform} m. Time = {fmt(time)} seconds."
            wrongtime=F(length+platform,F(abs(speed-speed2)*5,18)) if speed!=speed2 else time*2
            wrongwhy="Subtracting speeds applies to same-direction overtaking; opposite-direction speeds add." if speed!=speed2 else "This uses only one train's speed; the opposite-direction relative speed is twice that speed."
            return numeric(t,v,"Speed & distance","Two trains crossing in opposite directions",f"Two trains of lengths {length} m and {platform} m travel in opposite directions on parallel tracks at {speed} km/h and {speed2} km/h. How many seconds elapse between their fronts meeting and their rears clearing each other?",time,[(F(length,relative),"Both train lengths must be included before their rears clear."),(F(length+platform,speed+speed2),"The combined speed must be converted from km/h to m/s."),(wrongtime,wrongwhy)],exp,unit=" seconds")
        mps=F(speed*5,18)
        ans=F(length+platform,mps)
        exp=f"Speed = {speed} × 5/18 = {fmt(mps)} m/s. To clear the platform, the train travels its own length plus platform length, {length+platform} m. Time = {length+platform}/{fmt(mps)} = {fmt(ans)} s."
        return numeric(t,v,"Speed & distance","Train passing a platform",f"A {length}-metre train passes a {platform}-metre platform at {speed} km/h. How many seconds elapse from its front entering the platform until its rear leaves?",ans,[(F(length,mps),"This counts only the train length, as for crossing a pole."),(F(platform,mps),"This counts only the platform length and stops when the front exits."),(F(length+platform,speed),"The speed in km/h must first be converted to m/s.")],exp,unit=" seconds")
    if t == 16:
        still,stream=12+n,2+v%5
        distance=(still-stream)*(2+v%3)
        ans=F(distance,still-stream)
        exp=f"Upstream speed = still-water speed − stream speed = {still} − {stream} = {still-stream} km/h. Time = {distance}/{still-stream} = {fmt(ans)} hours."
        return numeric(t,v,"Speed & distance","Boats upstream",f"A boat's speed in still water is {still} km/h; the current is {stream} km/h. How long does the boat take to travel {distance} km upstream?",ans,[(F(distance,still+stream),"Adding the current gives downstream speed."),(F(distance,still),"This ignores the current slowing the boat upstream."),(F(distance,stream),"The current alone is not the boat's upstream speed.")],exp,unit=" hours")
    if t == 17:
        total=40+5*n
        if v%2:
            # One quarter of a homogeneous mixture is removed and replaced.
            remove=F(total,4)
            milk=F(3*total,5)*F(3,4)
            water=total-milk
            exp=f"Initially milk = 3/5 × {total}. Removing one quarter of a well-mixed liquid removes one quarter of its milk, so milk left = (3/5)×{total}×(3/4) = {fmt(milk)} L. Adding pure water does not add milk."
            return numeric(t,v,"Mixtures","Removing and replacing a mixture",f"A well-mixed {total}-litre container has milk and water in the ratio 3:2. Exactly {fmt(remove)} litres of mixture are removed and replaced by the same volume of pure water. How many litres of milk remain?",milk,[(F(3*total,5)-remove,"This assumes the removed mixture was pure milk; it contained milk and water in the original ratio."),(F(3*total,5),"This ignores the milk removed with the mixture."),(water,"This is the final water volume, not the milk volume.")],exp,unit=" litres",difficulty="Challenge")
        a,b=3,2
        milk=F(total*a,a+b)
        water=F(total*b,a+b)
        target=1
        added=milk-water
        exp=f"Milk = {total}×3/5 = {fmt(milk)} L; water = {total}×2/5 = {fmt(water)} L. For a 1:1 ratio, water must equal milk. Add {fmt(milk)} − {fmt(water)} = {fmt(added)} L."
        assert milk==water+added
        return numeric(t,v,"Mixtures","Diluting a mixture",f"A {total}-litre mixture contains milk and water in the ratio 3:2. How many litres of water must be added to make the ratio 1:1?",added,[(water,"This is the initial water volume, not the extra water needed."),(milk,"This is the milk volume; the initial water is already present."),(F(total,2),"Half the initial volume does not account for the existing unequal components.")],exp,unit=" litres")
    if t == 18:
        a,b=12+n,18+n
        lcm=math.lcm(a,b)
        exp=f"A simultaneous ring recurs after a common multiple of {a} and {b} minutes. The least such time is LCM = ({a}×{b})/GCD({a},{b}) = {lcm} minutes."
        assert lcm%a==lcm%b==0
        return numeric(t,v,"Number system","Least common multiple",f"Two bells ring together now. One rings every {a} minutes and the other every {b} minutes. After how many minutes will they first ring together again?",lcm,[(math.gcd(a,b),"The greatest common divisor divides the intervals; it is not their common recurrence period."),(a+b,"Adding intervals does not ensure a multiple of both."),(lcm+a,"This is later than the least common multiple and therefore cannot be the first recurrence.")],exp,unit=" minutes",difficulty="Foundation")
    if t == 19:
        denom=5+v%8
        fraction=F(denom-2,denom)
        extra=4+n
        initial=denom*extra
        remaining=2*extra
        exp=f"The fraction left is 1 − {fmt(fraction)} = 2/{denom}. Thus original quantity = {remaining} ÷ (2/{denom}) = {initial}."
        return numeric(t,v,"Fractions","Finding a whole from the remainder",f"A student uses {fmt(fraction)} of a pack of sheets. If {remaining} sheets remain, how many sheets were originally in the pack?",initial,[(F(remaining,fraction),"This divides the remainder by the used fraction rather than the remaining fraction."),(remaining*denom,"The numerator 2 in the remaining fraction must also be included."),(initial-remaining,"This is the number of used sheets, not the original total.")],exp,difficulty="Foundation")
    if t == 20:
        if v%2:
            adult=50+5*n;child=30+5*n;count=20+v%7;adults=8+v%8
            receipts=adult*adults+child*(count-adults)
            exp=f"If all {count} tickets were child tickets, receipts would be ₹{count*child}. Each adult ticket adds ₹{adult-child}. Extra receipts = {receipts}-{count*child} = {receipts-count*child}; divide by {adult-child} to obtain {adults} adult tickets."
            return numeric(t,v,"Algebra","Two prices and total receipts",f"A museum sells adult tickets for ₹{adult} and child tickets for ₹{child}. It sells {count} tickets in total and collects ₹{receipts}. How many adult tickets were sold?",adults,[(count-adults,"This is the number of child tickets, not adult tickets."),(F(receipts,adult),"This treats every ticket as an adult ticket and ignores the cheaper child tickets."),(F(receipts-count*child,adult),"The excess over all-child receipts must be divided by the price difference, not the adult price.")],exp,difficulty="Challenge")
        a,b=3+v%6,7+n
        x=4+n
        rhs=a*x+b
        exp=f"Subtract {b} from both sides: {a}x = {rhs-b}. Divide by {a}: x = {x}. Substitution gives {a}×{x}+{b} = {rhs}."
        return numeric(t,v,"Algebra","Solving a linear equation",f"Solve for x: {a}x + {b} = {rhs}.",x,[(F(rhs+b,a),"The constant must be subtracted from the right-hand side, not added."),(rhs-b,"This subtracts the constant but omits division by the coefficient of x."),(F(rhs,a)-b,"The whole difference (right-hand side minus constant) must be divided by the coefficient.")],exp,difficulty="Foundation")
    if t == 21:
        a,b=2+n,7+n
        sum_,prod=a+b,a*b
        exp=f"The polynomial factors as (x − {a})(x − {b}), since {a}+{b} = {sum_} and {a}×{b} = {prod}. The roots are {a} and {b}; the larger is {b}."
        assert b*b-sum_*b+prod==0
        return numeric(t,v,"Algebra","Factoring a quadratic",f"What is the larger root of x² − {sum_}x + {prod} = 0?",b,[(a,"This is the smaller root, while the question asks for the larger root."),(sum_,"This is the sum of both roots, not a root."),(b-a,"This is the difference between the roots, not the larger root.")],exp)
    if t == 22:
        width=8+n
        length=width+7
        perimeter=2*(length+width)
        ans=length*width
        exp=f"Let width be w and length w+7. Then 2(w+w+7) = {perimeter}, so w = {width} and length = {length}. Area = {width}×{length} = {ans} m²."
        return numeric(t,v,"Geometry & mensuration","Rectangle from perimeter",f"A rectangular field has perimeter {perimeter} m. Its length exceeds its width by 7 m. What is its area?",ans,[(perimeter,"Perimeter measures boundary length, not area."),(F(perimeter,4)**2,"This assumes the rectangle is a square, contradicting the side difference."),(2*length*width,"Rectangle area is length × width without a factor of two.")],exp,unit=" m²")
    if t == 23:
        radius=7*(1+v%8)
        # A changed fenced arc creates 40 unique variants even when radius repeats.
        angle=90+45*(v//8)
        ans=F(angle,360)*F(22,7)*radius*radius
        exp=f"A sector is {angle}/360 of the circle. Area = {angle}/360 × (22/7) × {radius}² = {fmt(ans)} m²."
        return numeric(t,v,"Geometry & mensuration","Area of a circular sector",f"Find the area of a circular sector with radius {radius} m and central angle {angle}°. Use π = 22/7.",ans,[(F(22,7)*radius*radius,"This is the whole circle's area, not the specified sector."),(F(angle,360)*2*F(22,7)*radius,"This calculates the arc length, not area."),(ans*2,"This doubles the required fraction of the circle.")],exp,unit=" m²")
    if t == 24:
        radius=7*(1+v%4)
        height=10+n
        ans=F(22,7)*radius*radius*height
        exp=f"Cylinder volume = πr²h = (22/7) × {radius}² × {height} = {fmt(ans)} cm³. The circular base area is multiplied by height."
        return numeric(t,v,"Geometry & mensuration","Cylinder volume",f"A right circular cylinder has radius {radius} cm and height {height} cm. What is its volume? Use π = 22/7.",ans,[(F(ans,3),"Dividing by three gives a cone's volume with the same base and height."),(F(22,7)*radius*height,"The radius must be squared in the base area."),(2*F(22,7)*radius*height,"This is the curved surface area, not a volume.")],exp,unit=" cm³")
    if t == 25:
        a=3+n
        base,height,slant=6*a,4*a,5*a
        volume=F(base*base*height,3)
        exp=f"A square pyramid has volume (base area × perpendicular height)/3 = ({base}² × {height})/3 = {fmt(volume)} cm³. Use perpendicular height, not the slant height."
        assert F(base,2)**2+height**2==slant**2
        return numeric(t,v,"Geometry & mensuration","Square pyramid volume",f"A square pyramid has base side {base} cm, perpendicular height {height} cm and slant height {slant} cm. Find its volume.",volume,[(base*base*height,"This is the corresponding prism volume; a pyramid needs the factor 1/3."),(F(base*base*slant,3),"The slant height cannot replace perpendicular height in the volume formula."),(F(base*height,3),"The base is a square, so its area is side squared.")],exp,unit=" cm³",difficulty="Challenge")
    if t == 26:
        scale=2+n
        a,b,h=3*scale,4*scale,5*scale
        ans=F(a*b,2)
        exp=f"The sides {a}, {b}, {h} form a scaled 3–4–5 right triangle. The perpendicular legs are {a} and {b}; area = ½×{a}×{b} = {fmt(ans)} cm²."
        assert a*a+b*b==h*h
        return numeric(t,v,"Geometry & mensuration","Area of a right triangle",f"A triangle has sides {a} cm, {b} cm and {h} cm. What is its area?",ans,[(a*b,"This omits the factor 1/2 in triangle area."),(F(a*h,2),"The hypotenuse is not perpendicular to the shorter leg."),(a+b+h,"This is the perimeter, not the area.")],exp,unit=" cm²")
    if t == 27:
        q1,q2,q3,q4=80+n,100+2*n,90+3*n,110+4*n
        total=q1+q2+q3+q4
        if v%2:
            ans=F((q4-q1)*100,q1)
            exp=f"Increase from first to fourth quarter = {q4}−{q1} = {q4-q1}. The comparison base is first-quarter sales: percentage increase = ({q4-q1}/{q1})×100 = {fmt(ans)}%."
            return numeric(t,v,"Data interpretation","Growth with a specified base",f"Quarterly sales are: Q1 {q1} units, Q2 {q2} units, Q3 {q3} units and Q4 {q4} units. What is the percentage increase from Q1 to Q4? Give the exact value.",ans,[(F((q4-q1)*100,q4),"This divides the increase by final sales instead of the initial base."),(F(q4*100,q1),"This expresses final sales as a percentage of initial sales, without subtracting the original 100%."),(F((q4-q1)*100,total),"Annual sales are not the specified comparison base.")],exp,unit="%")
        ans=F((q3+q4)*100,total)
        exp=f"July–December total = {q3}+{q4} = {q3+q4}. Annual total = {total}. Share = ({q3+q4}/{total})×100 = {fmt(ans)}%."
        return numeric(t,v,"Data interpretation","Share from quarterly data",f"A shop sells the following numbers of units: Jan–Mar {q1}, Apr–Jun {q2}, Jul–Sep {q3}, Oct–Dec {q4}. What percentage of annual sales occurs in July–December? Give the exact value.",ans,[(F(q3*100,total),"This includes only July–September and omits October–December."),(F(q4*100,total),"This includes only October–December and omits July–September."),(F((q3+q4)*100,q1+q2),"This uses first-half sales as denominator instead of annual sales.")],exp,unit="%")
    if t == 28:
        red,blue,green=3+v%7,5+v%9,4+n
        total=red+blue+green
        ans=F(red*(red-1),total*(total-1))
        exp=f"Without replacement, P(two red) = ({red}/{total}) × ({red-1}/{total-1}) = {fmt(ans)}. Both red count and total count fall by one after the first red draw."
        return numeric(t,v,"Probability","Two draws without replacement",f"A bag contains {red} red, {blue} blue and {green} green balls. Two balls are drawn at random without replacement. What is the probability that both are red?",ans,[(F(red*red,total*total),"This assumes replacement, leaving the second draw's counts unchanged."),(F(red,total),"This is the probability for only the first draw to be red."),(F(red*(red-1),total*total),"The total number of balls also decreases on the second draw.")],exp,difficulty="Challenge")
    if t == 29:
        people=6+n
        ans=people*(people-1)//2
        exp=f"An unordered pair is counted by choosing 2 people: C({people},2) = {people}×{people-1}/2 = {ans}. Dividing by two removes the two possible orders of each pair."
        return numeric(t,v,"Counting","Selecting an unordered pair",f"A study club has {people} members. In how many ways can a two-member review team be chosen, with neither member assigned a special role?",ans,[(people*(people-1),"This counts each pair twice, once in each order."),(people*people,"This permits choosing the same person twice and also counts order."),(people-1,"This counts only partners for one fixed member.")],exp)
    if t == 30:
        distance=1250+50*n
        minutes=10+v%7
        speed=F(distance*60,minutes*1000)
        exp=f"Convert distance to kilometres and time to hours: speed = ({distance}/1000)/({minutes}/60) = {fmt(speed)} km/h."
        return numeric(t,v,"Units & measurement","Metres per minute to kilometres per hour",f"A walker covers {distance} metres in {minutes} minutes at constant speed. Find the speed in kilometres per hour.",speed,[(F(distance,minutes),"This gives metres per minute, not kilometres per hour."),(F(distance,minutes*1000),"This converts metres to kilometres but leaves time in minutes."),(speed*10,"The length conversion introduces an extra factor of ten.")],exp,unit=" km/h",difficulty="Foundation")
    raise ValueError(t)


WORDS = ["BIRD","LAMP","FISH","COLD","WARM","SAND","ROAD","TREE","DESK","FROG",
         "BELL","FARM","GATE","HILL","IRON","JUMP","KITE","LAKE","MOON","NEST",
         "OVEN","PARK","QUIZ","RAIN","SHIP","TENT","UNIT","VASE","WIND","YARN",
         "ZINC","BOOK","CAVE","DRUM","EAST","FORK","GOLD","HAND","INCH","JOKE"]


def shift(word, k):
    return "".join(chr((ord(c)-65+k)%26+65) for c in word)


def ordinal(number):
    suffix = "th" if 10 <= number % 100 <= 20 else {1:"st",2:"nd",3:"rd"}.get(number % 10,"th")
    return f"{number}{suffix}"


def reasoning(t,v):
    n=v+1
    if t == 31:
        if v%2:
            start=8+n;step=3+v%7
            diffs=[step+2*i for i in range(4)]
            terms=[start]
            for d in diffs:terms.append(terms[-1]+d)
            ans=terms[-1]+step+8
            exp=f"The successive differences are {', '.join(map(str,diffs))}, increasing by 2 each time. The next difference is {step+8}; hence the next term is {terms[-1]}+{step+8} = {ans}."
            return numeric(t,v,"Number series","Increasing differences",f"Find the next number: {', '.join(map(str,terms))}, ?",ans,[(terms[-1]+diffs[-1],"This repeats the last difference instead of increasing it by two."),(terms[-1]+step,"This reuses the first difference and ignores the increasing pattern."),(ans+2,"This skips one difference and adds two too many.")],exp)
        start,step=8+n,3+v%7
        terms=[start+step*i for i in range(5)]
        ans=start+5*step
        exp=f"Each term increases by {step}: the differences are constant. The next term is {terms[-1]} + {step} = {ans}."
        return numeric(t,v,"Number series","Constant-difference series",f"Find the next number: {', '.join(map(str,terms))}, ?",ans,[(terms[-1],"This repeats the last term instead of applying the common increase."),(ans+step,"This skips the required next term and gives the following one."),(terms[-1]*2,"Doubling does not match the constant differences in the series.")],exp,difficulty="Foundation")
    if t == 32:
        start,ratio=2+n,2+v%3
        terms=[start*ratio**i for i in range(4)]
        ans=start*ratio**4
        exp=f"Every term is multiplied by {ratio}. Therefore the next term is {terms[-1]} × {ratio} = {ans}."
        return numeric(t,v,"Number series","Constant-ratio series",f"What comes next in {', '.join(map(str,terms))}, ?",ans,[(terms[-1]+ratio,"This adds the ratio instead of multiplying by it."),(ans*ratio,"This applies two further multiplications rather than one."),(terms[-1],"This repeats the last term and breaks the constant ratio.")],exp,difficulty="Foundation")
    if t == 33:
        a,b,da,db=10+n,70+n,3+v%4,5+v%3
        terms=[a,b,a+da,b+db,a+2*da,b+2*db]
        ans=a+3*da
        exp=f"Separate odd positions ({a}, {a+da}, {a+2*da}) and even positions ({b}, {b+db}, {b+2*db}). Odd positions increase by {da}. Position 7 is {a+2*da}+{da} = {ans}."
        return numeric(t,v,"Number series","Interleaved sequences",f"Find the missing seventh term: {', '.join(map(str,terms))}, ?",ans,[(b+3*db,"This is the next even-position term, which belongs in position 8."),(a+3*db,"This applies the even-position step to the odd-position sequence."),(a+2*da,"This repeats the previous odd-position term.")],exp)
    if t == 34:
        start=v%26
        step=2+v//13
        letters=[chr((start+i*step)%26+65) for i in range(5)]
        ans=chr((start+5*step)%26+65)
        wrong=[chr((start+k*step)%26+65) for k in (4,6,7)]
        exp=f"Move forward by {step} letters each time, wrapping from Z to A. From {letters[-1]}, the next letter is {ans}."
        choices=[(ans,"Correct. "+exp)]+[(w,f"Incorrect. {w} is not one {step}-letter step after {letters[-1]}. "+exp) for w in wrong]
        return make(t,v,"Letter series","Cyclic alphabet progression",f"Using the English alphabet cyclically (Z is followed by A), find the next letter: {', '.join(letters)}, ?",choices,0,exp)
    if t == 35:
        word,k=WORDS[v],1+v%5
        ans=shift(word,k)
        example=shift("CODE",k)
        exp=f"Each letter is shifted {k} place(s) forward, with Z followed by A: "+", ".join(f"{c}→{d}" for c,d in zip(word,ans))+f". Hence {word} becomes {ans}."
        choices=[(ans,"Correct. "+exp),(shift(word,-k),f"Incorrect. This shifts each letter {k} place(s) backward; the stated rule moves forward."),(shift(word,k+1),f"Incorrect. This moves each letter {k+1} places, one too many."),(word[::-1],"Incorrect. Reversing the order does not apply the required letter substitution.")]
        return make(t,v,"Coding & decoding","Uniform alphabet shift",f"In a code, every letter moves {k} place(s) forward in the English alphabet, cyclically. For example, CODE becomes {example}. How is {word} written?",choices,0,exp,difficulty="Foundation")
    if t == 36:
        word=WORDS[v]
        values=[ord(c)-64 for c in word]
        ans=sum(values)
        exp=f"Using A=1 through Z=26, {word} has letter values {' + '.join(map(str,values))} = {ans}."
        return numeric(t,v,"Coding & decoding","Alphabet-value sum",f"If a word's score is the sum of its letters' positions in the English alphabet (A=1, B=2, …, Z=26), what is the score of {word}?",ans,[(ans-len(word),"This uses A=0 rather than the stated A=1 system."),(ans+len(word),"This shifts every letter value one position too high."),(values[0]+values[-1],"This counts only the first and last letters and omits the middle letters.")],exp,difficulty="Foundation")
    if t == 37:
        if v%2:
            scale=2+n
            north,east,south=5*scale,3*scale,scale
            distance=5*scale
            exp=f"Net north displacement = {north}−{south} = {4*scale} km; net east displacement = {east} km. The straight-line distance is √({4*scale}²+{3*scale}²) = {distance} km, using the 3–4–5 triangle ratio."
            return numeric(t,v,"Directions","Straight-line displacement",f"A traveller moves {north} km north, then {east} km east, then {south} km south. What is the straight-line distance from the starting point to the final position?",distance,[(north+east+south,"This is total path length, not the displacement magnitude."),(north-south+east,"This adds perpendicular components instead of using Pythagoras."),(north-south,"This ignores the eastward component of the displacement.")],exp,unit=" km")
        a,b,c,d=10+n,8+n,4+v%5,3+v%3
        dx,dy=b-d,a-c
        ans=dx+dy
        exp=f"Net east displacement = {b}−{d} = {dx}; net north displacement = {a}−{c} = {dy}. Returning along perpendicular streets takes {dx}+{dy} = {ans} km. This is a street-route distance, not the straight-line distance."
        assert dx>0 and dy>0
        return numeric(t,v,"Directions","Shortest route on a street grid",f"On a rectangular street grid, a walker travels {a} km north, {b} km east, {c} km south and {d} km west. What is the shortest distance back to the starting point when restricted to north–south and east–west streets?",ans,[(a+b+c+d,"This is the whole outward path length; returning need not retrace that path."),(dx,"This corrects only the east–west displacement."),(dy,"This corrects only the north–south displacement.")],exp,unit=" km")
    if t == 38:
        total=60+2*n+v%7
        top=4+(7*v)%29
        ans=total-top+1
        exp=f"Ranks from opposite ends add to total+1. Rank from bottom = {total}−{top}+1 = {ans}; the +1 includes the candidate's own position."
        return numeric(t,v,"Ranking & order","Rank from the opposite end",f"There are {total} candidates in a merit list with no ties. Nila is ranked {top} from the top. What is her rank from the bottom?",ans,[(total-top,"This omits Nila's own position; ranks from both ends sum to total+1."),(total+top,"Ranks from opposite ends are not added this way."),(top,"This repeats the top rank without converting the direction.")],exp,difficulty="Foundation")
    if t == 39:
        left,right=12+n,17+v%14
        ans=left+right-1
        exp=f"The same person's left and right ranks both include that person. Total = {left}+{right}−1 = {ans}."
        return numeric(t,v,"Ranking & order","Total from two ranks",f"In a row, Dev is {ordinal(left)} from the left and {ordinal(right)} from the right. How many people are in the row?",ans,[(left+right,"This counts Dev twice."),(left+right+1,"The overlap must be removed, not increased."),(abs(left-right),"The difference between two ranks does not give the number of people.")],exp,difficulty="Foundation")
    if t == 40:
        names=[("Arun","Bina","Charu","Daya"),("Esha","Farah","Gita","Hari"),("Ira","Jaya","Kiran","Lata"),("Maya","Nila","Omar","Pia"),("Ravi","Sara","Tara","Uma")]
        a,b,c,d=names[v//8]
        variant=v%8
        scenarios=[
          (f"{a} is the father of {b}. {b} is the mother of {c}.","Maternal grandfather",f"{b} is {c}'s mother, and {a} is that mother's father.", ["Paternal grandfather","Father","Maternal uncle"]),
          (f"{a} is the mother of {b}. {b} is the father of {c}.","Paternal grandmother",f"{b} is {c}'s father, and {a} is that father's mother.",["Maternal grandmother","Mother","Paternal aunt"]),
          (f"{b} and {c} are sisters. {a} is the father of {b} and {c}.","Father",f"The statement directly identifies {a} as {c}'s father.",["Uncle","Brother","Grandfather"]),
          (f"{b} is the mother of {c}. {a} is {b}'s brother.","Maternal uncle",f"A mother's brother is the maternal uncle.",["Paternal uncle","Father","Brother"]),
          (f"{b} is the father of {c}. {a} is {b}'s sister.","Paternal aunt",f"A father's sister is the paternal aunt.",["Maternal aunt","Mother","Sister"]),
          (f"{a} is the daughter of {b}. {b} is the daughter of {c}.","Granddaughter",f"{a} is the female child of {c}'s daughter, two generations below {c}.",["Daughter","Grandmother","Niece"]),
          (f"{a} is the son of {b}. {b} is the son of {c}.","Grandson",f"{a} is the male child of {c}'s son, two generations below {c}.",["Son","Grandfather","Nephew"]),
          (f"{a} is the sister of {b}. {b} is the mother of {c}.","Maternal aunt",f"{a} is the sister of {c}'s mother, hence the maternal aunt.",["Paternal aunt","Mother","Grandmother"]),
        ]
        statement,ans,reason,wrong=scenarios[variant]
        exp=reason+" Use only the explicitly stated family links."
        choices=[(ans,"Correct. "+exp)]+[(w,f"Incorrect. {w} does not match the stated links. {reason}") for w in wrong]
        return make(t,v,"Blood relations","Tracing explicit family links",f"{statement} How is {a} related to {c}?",choices,0,exp)
    if t == 41:
        # These relations use explicit existential statements; no assumption that
        # a universal premise alone establishes the existence of an object.
        colors=[("red","blue","green"),("amber","silver","gold"),("white","black","grey"),("violet","orange","pink"),("cyan","brown","yellow")]
        a,b,c=colors[v//8]
        variants=[
         (f"All {a} tokens are {b}. Some {a} tokens exist.",f"Some {b} tokens are {a}.",f"All {b} tokens are {a}.",True,False,"The existing tokens in the first class also belong to the second, but the reverse universal claim need not hold."),
         (f"No {a} token is {b}. Some {c} tokens are {a}.",f"Some {c} tokens are not {b}.",f"No {c} token is {b}.",True,False,"The stated subset of the third class lies outside the second; nothing excludes every other token in the third class."),
         (f"All {a} tokens are {b}. All {b} tokens are {c}.",f"All {a} tokens are {c}.",f"All {c} tokens are {a}.",True,False,"Containment is transitive in the forward direction; it does not reverse."),
         (f"Some {a} tokens are {b}. All {b} tokens are {c}.",f"All {a} tokens are {c}.",f"Some {a} tokens are {c}.",False,True,"The identified overlapping tokens are in the third class, but other tokens in the first class may lie outside it."),
         (f"No {a} token is {b}. Some {a} tokens exist.",f"No {b} token is {a}.",f"Some {a} tokens are not {b}.",True,True,"Disjointness is symmetric, and the explicit existence statement supplies tokens outside the second class."),
         (f"Some {a} tokens are {b}. Some {b} tokens are {c}.",f"Some {a} tokens are {c}.",f"All {a} tokens are {c}.",False,False,"The two overlaps may involve different tokens. Neither an overlap of the first and third classes nor full inclusion is guaranteed."),
         (f"All {a} tokens are {b}. No {b} token is {c}.",f"No {a} token is {c}.",f"No {c} token is {a}.",True,True,"The first class is contained in a class disjoint from the third; the resulting disjointness works in both directions."),
         (f"Some {a} tokens are not {b}. All {c} tokens are {b}.",f"All {a} tokens are {c}.",f"Some {a} tokens are not {c}.",False,True,"The first-class tokens outside the second class cannot be in the third, because every third-class token is inside the second."),
        ]
        premise,c1,c2,i,ii,reason=variants[v%8]
        answers=["Only conclusion I follows","Only conclusion II follows","Both conclusions follow","Neither conclusion follows"]
        correct=0 if i and not ii else 1 if ii and not i else 2 if i and ii else 3
        exp=f"Conclusion I: {'follows' if i else 'does not necessarily follow'}. Conclusion II: {'follows' if ii else 'does not necessarily follow'}. {reason}"
        choices=[(x,('Correct. ' if j==correct else 'Incorrect. ')+exp) for j,x in enumerate(answers)]
        return make(t,v,"Logical reasoning","Syllogisms with explicit existence",f"Treat the statements as true and judge only what must follow. Statements: {premise} Conclusion I: {c1} Conclusion II: {c2}",choices,correct,exp,difficulty="Challenge")
    if t == 42:
        k=3+n
        squares=[k*k,(k+1)**2,(k+2)**2]
        odd=(k+3)**2+1
        assert math.isqrt(odd)**2!=odd
        exp=f"{squares[0]}={k}², {squares[1]}={k+1}² and {squares[2]}={k+2}² are perfect squares. {odd} lies between {(k+3)**2} and {(k+4)**2}, so it is not a perfect square."
        choices=[(str(odd),"Correct. "+exp)]+[(str(s),f"Incorrect. {s} is a perfect square ({k+j}²), so it shares the stated property of the other square numbers.") for j,s in enumerate(squares)]
        shown=sorted(squares+[odd])
        return make(t,v,"Classification","Perfect-square classification",f"Among {', '.join(map(str,shown))}, which number is NOT a perfect square?",choices,0,exp,difficulty="Foundation")
    if t == 43:
        a,b=4+n,10+n
        offset=3+v%7
        ans=b*b+offset
        exp=f"The stated rule maps x to x²+{offset}. For {b}, the result is {b}²+{offset} = {ans}."
        return numeric(t,v,"Analogy","Number mapping rule",f"Use the rule 'square the input, then add {offset}'. Thus {a} maps to {a*a+offset}. What does {b} map to?",ans,[(b*b-offset,"This subtracts the offset instead of adding it."),(2*b+offset,"This doubles the input instead of squaring it."),((b+offset)**2,"This adds the offset before squaring, which reverses the stated order.")],exp,difficulty="Foundation")
    if t == 44:
        start=dt.date(2024+v%3,1+v%12,1+v%24)
        days=10+3*n
        end=start+dt.timedelta(days=days)
        names=list(calendar.day_name)
        ans=end.strftime("%A")
        weekday=start.weekday()
        exp=f"{days} days contains {days//7} full weeks and {days%7} extra day(s). Move {days%7} weekdays forward from {start.strftime('%A')} to {ans}. 'After' does not count the starting day as day 1."
        choices=[(ans,"Correct. "+exp)]
        for delta in (-1,1,2):
            w=names[(end.weekday()+delta)%7]
            choices.append((w,f"Incorrect. {w} is {abs(delta)} day(s) {'before' if delta<0 else 'after'} the required weekday. Reduce the elapsed days modulo seven. "+exp))
        return make(t,v,"Calendar reasoning","Weekday after elapsed days",f"{start.strftime('%d %B %Y')} is a {start.strftime('%A')}. What day of the week is it exactly {days} days after that date?",choices,0,exp)
    if t == 45:
        h=1+v%10
        m=5+5*(v//10)
        raw=abs(F(30*h)+F(m,2)-6*m)
        ans=min(raw,360-raw)
        exp=f"Minute hand angle from 12 = 6×{m} = {6*m}°. Hour hand angle = 30×{h} + 0.5×{m} = {fmt(F(30*h)+F(m,2))}°. Their difference is {fmt(raw)}°; choose the smaller of that and 360° minus that, giving {fmt(ans)}°."
        return numeric(t,v,"Clock reasoning","Angle between moving hands",f"What is the smaller angle between the hands of a correctly running analogue clock at {h}:{m:02d}?",ans,[(min(abs(30*h-6*m),360-abs(30*h-6*m)),"This incorrectly freezes the hour hand at the hour mark."),(360-ans,"This is the reflex angle, not the smaller angle."),(ans+5,"This does not match the continuously moving hour hand and minute hand positions.")],exp,unit="°")
    if t == 46:
        # Five objects in a row; each constraint supplies an unambiguous chain.
        names=[f"Card {letter}{1+v//5}" for letter in "ABCDE"]
        perm=list(range(5))
        random.Random(808+v).shuffle(perm)
        chain=[names[i] for i in perm]
        target=1+v%5
        ans=chain[target-1]
        statements=[f"{chain[i]} is immediately to the left of {chain[i+1]}" for i in range(4)]
        random.Random(909+v).shuffle(statements)
        exp=f"The immediate-left links form the complete order (left to right): {' → '.join(chain)}. Position {target} is {ans}."
        other=[x for x in chain if x!=ans][:3]
        choices=[(ans,"Correct. "+exp)]+[(x,f"Incorrect. {x} occupies position {chain.index(x)+1}, not position {target}. "+exp) for x in other]
        return make(t,v,"Arrangements","Linear order from adjacent links",f"Five distinct cards are arranged in a row. {'; '.join(statements)}. Which card is in position {target} from the left?",choices,0,exp)
    if t == 47:
        # Ordering is based on relations, independent of real-world assumptions.
        names=[f"Runner {c}{1+v//8}" for c in "PQRS"]
        random.Random(700+v).shuffle(names)
        a,b,c,d=names
        position=1+v%4
        ans=names[position-1]
        exp=f"From fastest to slowest the strict order is {a}, {b}, {c}, {d}. Therefore position {position} is {ans}. No ties are allowed."
        choices=[(x,('Correct. ' if x==ans else 'Incorrect. ')+f"{x} is {['first','second','third','fourth'][names.index(x)]} in the speed order. "+exp) for x in names]
        return make(t,v,"Ranking & order","Transitive ordering",f"Four runners have distinct speeds. {a} is faster than {b}; {b} is faster than {c}; {c} is faster than {d}. Who is {['fastest','second fastest','third fastest','slowest'][position-1]}?",choices,position-1,exp,difficulty="Foundation")
    if t == 48:
        k=5+n
        relations=[
            (f"P > Q > R and R = {k}",f"P > {k}",f"P and Q are both greater than R = {k}.",f"P = {k}",f"P < {k}",f"Q < {k}"),
            (f"P ≥ Q and Q > R = {k}",f"P > {k}",f"Q is strictly above {k}, and P is at least Q.",f"P = {k}",f"P < {k}",f"Q = {k}"),
            (f"P < Q ≤ R and R = {k}",f"P < {k}",f"P is strictly below Q, which cannot exceed {k}.",f"P = {k}",f"P > {k}",f"Q > {k}"),
            (f"P = Q and Q < R = {k}",f"P < {k}",f"P equals Q, and both are strictly below R = {k}.",f"P = {k}",f"P > {k}",f"Q > {k}"),
        ]
        premise,ans,reason,*wrong=relations[v%4]
        choices=[(ans,"Correct. "+reason)]+[(x,f"Incorrect. This contradicts the stated inequalities. {reason}") for x in wrong]
        return make(t,v,"Logical reasoning","Inequality chains",f"Given {premise}, which statement must be true?",choices,0,reason)
    if t == 49:
        a,b=6+n,3+v%7
        c=2+v%4
        ans=a*b+c
        exp=f"Apply the defined operation directly: {a} ⊙ {b} = ({a}×{b})+{c} = {ans}. This symbol has only the meaning specified in the question."
        return numeric(t,v,"Logical operations","A newly defined binary operation",f"For all numbers x and y, define x ⊙ y = xy + {c}, where xy means x multiplied by y. Find {a} ⊙ {b}.",ans,[(a+b+c,"This adds the two inputs instead of multiplying them."),(a*(b+c),"The constant is added after multiplying; it is not placed inside the second factor."),(a*b-c,"This subtracts the constant although the rule says to add it.")],exp,difficulty="Foundation")
    if t == 50:
        # Minimum counting from two overlapping finite sets.
        both=5+n
        onlya=12+v%8
        onlyb=18+v%9
        neither=3+v%6
        total=onlya+onlyb+both+neither
        a,b=onlya+both,onlyb+both
        ans=both
        exp=f"At least one subject = total − neither = {total}−{neither} = {total-neither}. Inclusion–exclusion gives both = {a}+{b}−{total-neither} = {both}."
        assert a+b-both==total-neither
        return numeric(t,v,"Sets & logical counting","Two-set inclusion–exclusion",f"Among {total} students, {a} study Telugu, {b} study English and {neither} study neither. How many study both languages?",ans,[(a+b-total,"This ignores the students who study neither."),(a+b,"This adds the two memberships and double-counts students in both."),(onlya+onlyb,"This counts students studying exactly one language, not both.")],exp)
    raise ValueError(t)


def build_quant_sets():
    """Return twenty balanced, deterministic lists of 100 question objects."""
    AUDIT.clear()
    sets=[]
    for s in range(20):
        items=[]
        for t in range(1,51):
            for j in range(2):
                v=2*s+j
                items.append(arithmetic(t,v) if t<=30 else reasoning(t,v))
        # Interleave the two variants while retaining a predictable section mix.
        random.Random(91000+s).shuffle(items)
        sets.append(items)
    validate(sets)
    return sets


def validate(sets):
    assert len(sets)==20
    ids=[]
    fingerprints=[]
    answers=Counter()
    for paper in sets:
        assert len(paper)==100
        assert sum(int(q['id'].split('-')[1])<=30 for q in paper)==60
        for q in paper:
            ids.append(q['id'])
            fingerprints.append((q['question'],tuple(sorted(o['text'] for o in q['options']))))
            assert len(q['options'])==4
            assert len({o['text'] for o in q['options']})==4
            assert 0<=q['answer']<4
            assert q['options'][q['answer']]['explanation'].startswith('Correct.')
            assert all(o['explanation'].startswith('Incorrect.') for j,o in enumerate(q['options']) if j!=q['answer'])
            assert q['explanation'] and q['source']['title']
            answers[q['answer']]+=1
    assert len(ids)==len(set(ids))==2000
    assert len({q['question'] for p in sets for q in p})==2000,'Duplicate stem'
    assert len(fingerprints)==len(set(fingerprints)), 'Duplicate complete question'
    assert all(400<count<600 for count in answers.values()), answers
    assert len(AUDIT)==2000
    return {"sets":20,"questions":2000,"templates":50,"arithmetic_per_set":60,"reasoning_per_set":40,
            "skills":len({q['skill'] for p in sets for q in p}),"answer_positions":dict(answers)}


if __name__ == '__main__':
    sets=build_quant_sets()
    path=Path(__file__).with_name('quant-sets.json')
    path.write_text(json.dumps(sets,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    print(json.dumps(validate(sets),indent=2))
    print(f'Wrote {path}')
