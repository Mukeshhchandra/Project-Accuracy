"""Short, original solving guides for every quantitative/reasoning skill."""
from collections import defaultdict

# Skill | first step | efficient method | trap. Worked examples come from the
# independently checked practice bank, so each lesson links directly to practice.
GUIDES = """
Percentage of a quantity|Identify the whole that represents 100%.|Use p% of N = N × p/100; cancel common factors before multiplying.|A percentage is not an absolute count; changing the base changes the answer.
Successive percentage changes|Write each increase as 1+p/100 and each decrease as 1−p/100.|Multiply the factors, subtract 1, then multiply by 100 to get the signed net percentage.|Adding or subtracting the rates ignores the changed base.
Profit on cost price|Identify cost price and confirm the profit is measured on cost.|Selling price = cost × (1+profit%/100); find profit separately only if asked.|Profit on selling price requires a different equation.
Recovering cost before repricing|Recover cost from the old selling price: cost = sale/(1−loss%/100).|Apply the required profit factor to the recovered cost.|Applying profit to the old selling price uses the wrong base.
Successive discounts|Keep the marked price as the original base.|Multiply the marked price by each remaining-price factor: (1−d1/100)(1−d2/100).|Two discounts of 10% do not equal a single 20% discount.
Simple interest|Keep principal, annual percentage rate and time in years separate.|Interest = PRT/100; amount = P+interest.|Do not report the amount when the question asks only for interest.
Finding time from simple interest|Check that the given value is interest, not the final balance.|Rearrange I=PRT/100 to T=100I/(PR).|Convert months to years when the rate is annual.
Annual compound interest|Count the number of complete annual compounding periods.|Amount = P(1+r/100)^n; subtract P to get compound interest.|Interest compounds on the growing balance, not repeatedly on P alone.
Compound versus simple interest|Check that the period is exactly two years with annual compounding.|For that case, CI−SI = P(r/100)^2; it is the interest earned on first-year interest.|This two-year shortcut cannot be used unchanged for three years or half-yearly compounding.
Sharing in a three-part ratio|Add all parts of the stated ratio.|One part = total/sum of parts; multiply by the requested person's parts.|Equal division is valid only when all ratio parts are equal.
Partnership capital and time|Calculate capital × time for each partner using the same time unit.|Divide profit in the resulting capital-time ratio.|A partner investing more money for less time need not get the larger share.
Present and future ages|Assign present ages before writing a future ratio.|After t years, add t to EACH person's age; combine the ratio equation with the present total.|A future ratio is generally not the ratio of present ages.
Replacing one observation|Convert the average change into a change in the total: n × (new average−old average).|New item = removed item + change in total.|Adding the average change alone omits the group size.
Adding two observations|Find the old total and the new total using their different group sizes.|The difference is the sum of the two newcomers; subtract the known newcomer.|The two new observations need not average the new group mean.
Weighted average|Multiply each group mean by its number of observations.|Add group totals and divide by the combined number of observations.|The ordinary mean of two group means works only for equal group sizes.
Combined work rates|Represent the job as one whole or use an LCM-sized job.|Add rates 1/a+1/b; take the reciprocal for the completion time.|Adding completion times does not add simultaneous productivity.
A worker leaves before completion|Calculate the fraction completed in the first stage.|Apply the remaining worker's rate to the unfinished fraction; then add both elapsed times.|The time spent finishing the remainder is not the total elapsed time.
Inlet and outlet pipes|Treat filling as positive work and draining as negative work.|Net filling rate = 1/fill time−1/empty time; reciprocal gives time only if this is positive.|Subtract rates, not the stated completion times.
An outlet opens after a delay|Find the fraction filled while only the inlet runs.|Divide the remaining fraction by the later net rate; add the initial delay.|Using the net rate for the whole tank incorrectly assumes the outlet ran from the start.
Average speed over equal distances|Confirm the outward and return distances are equal.|Average speed = 2uv/(u+v), derived from total distance divided by total time.|The arithmetic mean of speeds applies to equal times, not equal distances.
Train passing a platform|Add the train length and platform length for complete clearance.|Convert km/h to m/s with ×5/18; divide the total length by speed.|Passing a pole uses only train length; a platform has additional length.
Two trains crossing in opposite directions|Add both train lengths and, for opposite motion, both speeds.|Convert combined speed to m/s, then divide combined length by it.|For same-direction overtaking, relative speed is the difference.
Boats upstream|Separate still-water boat speed from the stream speed.|Upstream speed = boat−stream; time = distance/upstream speed.|Downstream uses a sum. Upstream progress requires boat speed greater than current.
Diluting a mixture|Identify which component is unchanged when pure water is added.|Keep milk fixed, find water required by the target ratio, then subtract water already present.|The amount of water finally present is not the amount added.
Removing and replacing a mixture|Find each component's fraction before removing any well-mixed liquid.|A removed fraction removes the same fraction of each component; add the replacement component afterward.|Removing mixture is not equivalent to removing that volume of pure milk.
Least common multiple|Look for repeated events that must coincide again.|Use LCM(a,b)=a×b/HCF(a,b), or prime factors with their largest powers.|HCF finds a common divisor, not the first simultaneous recurrence.
Factoring a quadratic|Move all terms to one side and identify the coefficients.|For a monic quadratic, find two numbers whose sum is the linear coefficient and product is the constant; then solve each factor.|The factor constants have opposite signs to the corresponding roots.
Solving a linear equation|Expand brackets and collect variable terms on one side.|Collect constants on the other side; divide by the variable's coefficient.|Changing sides changes signs; preserve the order when subtracting brackets.
Two prices and total receipts|Write one equation for total units and one for total money.|Eliminate one unknown by substitution or by multiplying and subtracting equations.|Adding unit counts to rupee amounts mixes unlike quantities.
Rectangle from perimeter|Convert perimeter to length+width by dividing by 2.|Use the stated side relation to solve for dimensions, then multiply them for area.|Perimeter and area have different units; do not multiply perimeter by a side.
Area of a right triangle|Identify the two perpendicular legs.|Area = half × perpendicular leg 1 × perpendicular leg 2.|The hypotenuse is not a perpendicular height to either leg.
Cylinder volume|Check whether the measurement given is radius or diameter.|Volume = πr²h; halve a diameter before squaring.|Using diameter as radius makes the volume four times too large.
Area of a circular sector|Find the sector's fraction of a complete turn.|Area = (angle/360) × πr² for an angle in degrees.|Arc length uses 2πr; it is not sector area.
Square pyramid volume|Find the area of the square base and identify the perpendicular height.|Volume = base area × vertical height/3.|Slant height is not the vertical height used in volume.
Two-set inclusion–exclusion|Identify the two set totals and their overlap.|Union = A+B−both; neither = total−union.|Subtract the overlap once because adding A and B counted it twice.
Selecting an unordered pair|Decide whether choosing AB differs from choosing BA.|For distinct objects without replacement, unordered pairs = n(n−1)/2.|Use n(n−1) when the two positions are ordered and distinct.
Two draws without replacement|Track favourable and total objects on the first draw.|After drawing without replacement, reduce both relevant counts for the second draw; multiply the probabilities.|Using the original denominator twice assumes replacement.
Share from quarterly data|Identify the specific part and add all relevant quarters for the whole.|Share percentage = requested amount/whole ×100.|The largest quarter is not the denominator unless explicitly stated.
Growth with a specified base|Read carefully which earlier or reference value is the base.|Growth percentage = (new−base)/base ×100.|Dividing by the new value answers a different percentage question.
Finding a whole from the remainder|Write the remaining fraction after the used fraction is removed.|Whole = remaining amount/remaining fraction.|Dividing by the used fraction treats the remainder as the amount used.
Metres per minute to kilometres per hour|Attach units to the value before converting.|Multiply m/min by 60/1000 = 0.06 to obtain km/h.|The factor 3.6 converts m/s, not m/min.
Constant-difference series|Calculate successive differences.|If one constant difference fits every shown transition, apply it once more.|Check the entire sequence; the first gap alone does not establish a rule.
Constant-ratio series|Compare successive nonzero terms by division.|If one ratio fits every transition, multiply the last term by that ratio.|A constant difference and a constant ratio are different patterns.
Increasing differences|Write a separate row of consecutive differences.|Inspect how those differences change, continue that pattern, and add the next difference.|Adding the last observed difference assumes it stays constant.
Interleaved sequences|Separate odd-position terms from even-position terms.|Solve the progression within the required subsequence and then return to the original positions.|Adjacent terms may belong to different rules.
Cyclic alphabet progression|Convert A–Z to positions 1–26 and identify the shift.|Wrap around after 26: new position = ((position−1+shift) mod 26)+1.|Treating Z as a stopping point breaks a cyclic rule.
Uniform alphabet shift|Determine both the shift size and its direction from the stated rule.|Apply the same modular shift to every letter while preserving letter order.|Reversing the word is different from shifting its letters.
Alphabet-value sum|Confirm the index convention, such as A=1 rather than A=0.|Convert every letter and add all values, including repeated letters.|Counting only the first and last letters omits the middle of the word.
Straight-line displacement|Cancel opposing directions to find net horizontal and vertical movement.|Use √(horizontal²+vertical²) for the straight-line distance.|Total distance walked is usually greater than displacement.
Shortest route on a street grid|Find net horizontal and vertical displacement.|For unrestricted perpendicular streets, shortest grid distance = absolute horizontal + absolute vertical displacement.|Pythagoras would cut diagonally off the permitted street route.
Rank from the opposite end|Check that all ranks refer to the same list without ties.|Opposite rank = total−given rank+1.|The +1 keeps the person's own position from being omitted.
Total from two ranks|Confirm both ranks describe the same person in the same row.|Total = rank from left + rank from right−1.|Without subtracting 1, the person is counted twice.
Transitive ordering|Translate every comparison into a consistent arrow direction.|Chain the comparisons; only report relations forced by the chain.|An unspecified comparison between two branches is not automatically known.
Tracing explicit family links|Draw generations vertically and record only explicitly stated relationships.|Trace the path from the person being described to the reference person, noting maternal or paternal side.|Do not infer a person's gender from a name.
Syllogisms with explicit existence|Draw containment, overlap and exclusion separately.|Test whether a conclusion holds in every arrangement satisfying the premises; a single valid counterexample disproves necessity.|All A are B does not imply all B are A, or even that A exists without an existence premise.
Perfect-square classification|Compare each option with nearby integer squares.|An integer is a perfect square only if its integer square root squared equals it.|Ending digits can rule out some squares but cannot alone prove a number is square.
Number mapping rule|Translate the stated mapping into a formula before substitution.|Apply operations in the given order; use all supplied examples to check the rule.|Squaring then adding is different from adding then squaring.
Weekday after elapsed days|Identify the starting weekday and whether the problem says after n days.|Discard full weeks and move forward by n mod 7 days.|Counting the starting day as day 1 causes an off-by-one error for elapsed days.
Angle between moving hands|Minute hand = 6m degrees; hour hand = 30h+0.5m degrees from 12.|Take the absolute difference; for the smaller angle use min(d,360−d).|The hour hand continues moving between the hour marks.
Linear order from adjacent links|Write immediately-before links as adjacent blocks.|Merge compatible blocks, preserving every immediate neighbour relation.|Somewhere before is weaker than immediately before.
Inequality chains|Write comparisons in one consistent direction.|Combine only compatible directions; one strict link in a valid chain makes the end-to-end comparison strict.|From A>B and C>B, A versus C is undetermined.
A newly defined binary operation|Read the custom operation as a substitution rule, not as ordinary addition or multiplication.|Replace operands in the definition and respect any brackets before simplifying.|A custom operator need not be commutative: swapping operands can change the value.
"""

def build_quant_lessons(sets):
    guides={}
    for line in GUIDES.strip().splitlines():
        name,first,method,trap=line.split('|')
        assert name not in guides
        guides[name]=(first,method,trap)
    examples={}
    for paper in sets:
        for q in paper:
            examples.setdefault(q['skill'],q)
    assert set(examples)==set(guides), (set(examples)-set(guides),set(guides)-set(examples))
    grouped=defaultdict(list)
    for name,q in sorted(examples.items()):
        first,method,trap=guides[name]
        grouped[q['topic']].append({
            'title':name,
            'steps':[first,method,'Check the requested unit, sign and magnitude; substitute the result back where possible.'],
            'example':{'question':q['question'],'solution':q['explanation'],'questionId':q['id']},
            'trap':trap,
            'source':{'title':'Original worked example · calculation checked','url':None}})
    return [{'topic':topic,'summary':'Choose a method below. Read when the shortcut applies, work through the example, and check the common mistake before practising.',
             'methods':methods} for topic,methods in sorted(grouped.items())]
