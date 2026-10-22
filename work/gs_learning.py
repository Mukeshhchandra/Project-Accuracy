"""Original, concise General Studies learning methods for Accuracy.

These are learning examples, not additional mock-test questions. They teach
reasoning and evidence checks; no option-letter, guessing or score guarantees.
"""
from copy import deepcopy


def _source(title="Original learning method and worked example", url=None):
    return {"title": title, "url": url}


def _method(title, steps, question, solution, trap, source=None):
    return {
        "title": title,
        "steps": steps,
        "example": {"question": question, "solution": solution},
        "trap": trap,
        "source": source or _source(),
    }


LESSONS = [
    {
        "topic": "General Science",
        "summary": "Use units, causal chains and controlled comparisons to explain an answer before selecting it.",
        "methods": [
            _method(
                "Let the units check the equation",
                [
                    "Write the required quantity and its unit before substituting numbers.",
                    "Convert all measurements to a consistent system, especially minutes, centimetres and milliamperes.",
                    "Check that the equation produces the required unit.",
                    "Estimate the order of magnitude, then calculate and attach the unit.",
                ],
                "A small pump transfers 840 joules in 14 seconds. Is its power 60 W or 11,760 W?",
                "Power is energy divided by time. The unit J/s is W, so 840 ÷ 14 = 60 W. Multiplying gives J·s, which cannot be a unit of power.",
                "Dimensional consistency can reject a wrong formula, but it cannot prove that every dimensionally valid formula fits the situation.",
            ),
            _method(
                "Identify what remains constant",
                [
                    "Underline the condition that is held fixed: voltage, resistance, temperature or mass.",
                    "Write the relevant relationship using symbols before numbers.",
                    "Change only the stated variable and compare the new expression with the old one.",
                    "Check that the assumed relationship remains valid under the stated conditions.",
                ],
                "An ideal 15 V supply is connected to a resistor. Its resistance rises from 5 Ω to 10 Ω while the supply stays fixed. What happens to current?",
                "Use I = V/R. Initially I = 15/5 = 3 A; afterwards I = 15/10 = 1.5 A. Current halves because voltage stays fixed and resistance doubles.",
                "A memorised statement such as 'doubling resistance doubles something' is incomplete. First identify what is fixed and what is being asked.",
                _source("NCERT Science, Electricity; original numerical example", "https://ncert.nic.in/textbook/pdf/jesc111.pdf"),
            ),
            _method(
                "Separate observation from explanation",
                [
                    "State what was actually measured without adding a cause.",
                    "List the variables that differ between the compared groups.",
                    "Choose a comparison that changes the proposed cause while keeping other conditions similar.",
                    "Check for an alternative explanation before claiming causation.",
                ],
                "Seedlings beside a window grow faster than seedlings in a cupboard. Does this alone prove that light caused the difference?",
                "No. Light is a plausible cause, but temperature, water and seed quality may also differ. Compare similar seedlings with matched soil, watering and temperature while changing light exposure.",
                "A correct observation can support several explanations. Correlation alone does not identify which explanation is responsible.",
            ),
        ],
    },
    {
        "topic": "Geography",
        "summary": "Convert descriptions into simple spatial sketches, and trace how terrain affects water and weather.",
        "methods": [
            _method(
                "Turn map scale into one clean conversion",
                [
                    "Read the scale as a ratio in the same units on both sides.",
                    "Convert one map centimetre into ground metres or kilometres.",
                    "Multiply the measured map length by that converted value.",
                    "Check whether the question wants straight-line distance or an actual winding route.",
                ],
                "On a 1:75,000 map, a straight route measures 6.4 cm. What ground distance does it represent?",
                "One centimetre represents 75,000 cm = 750 m = 0.75 km. Therefore 6.4 × 0.75 = 4.8 km. This is the mapped route length, not a travel-time estimate.",
                "The 75,000 is initially in centimetres, not kilometres. Skipping this conversion changes the answer by several orders of magnitude.",
            ),
            _method(
                "Trace drainage as a directed network",
                [
                    "Draw each stream as an arrow pointing downstream.",
                    "Mark each confluence and label the receiving river.",
                    "Keep a tributary, a distributary and the main channel conceptually separate.",
                    "Trace a drop of water to its final outlet before choosing a basin.",
                ],
                "In a schematic map, stream P joins river Q, and Q joins river R before R reaches the sea. Which channel determines P's ultimate drainage basin?",
                "Follow P → Q → R → sea. P lies in R's drainage basin. P is a tributary of Q and belongs to the wider network drained by R.",
                "A nearby river is not necessarily the receiving river. Basin membership follows drainage connections and divides, not simple proximity.",
            ),
            _method(
                "Explain rainfall with a process chain",
                [
                    "Identify the source and direction of moist air.",
                    "Check whether terrain or heating forces the air upward.",
                    "Connect rising air with cooling, condensation and possible rainfall.",
                    "For the other side of a barrier, consider descent and loss of moisture rather than copying the same rainfall amount.",
                ],
                "Moist winds approach a ridge from the west. Town A is on its western slope and town B lies just east of the ridge. Which is more likely to receive orographic rain?",
                "A is on the windward slope: the air is forced upward there, cools and can condense. Air reaching B may have lost moisture and descend. A is therefore more likely to receive this type of rain, with actual amounts depending on conditions.",
                "Do not label east or west as permanently wetter. Windward and leeward depend on the wind direction specified.",
            ),
        ],
    },
    {
        "topic": "Indian Polity",
        "summary": "Identify the institution, the kind of power and the relevant condition instead of matching a familiar name.",
        "methods": [
            _method(
                "Match the task to the institution",
                [
                    "Restate the action in the question: appoint, advise, legislate, audit, adjudicate or conduct an election.",
                    "Separate who formally acts from who advises or administers the process.",
                    "Check the constitutional provision or governing law for that particular action.",
                    "Reject institutions with related but different responsibilities.",
                ],
                "A revision note says that because Parliament chooses the President, Parliament itself administers the presidential poll. What is wrong?",
                "The note confuses the electoral college with election administration. The presidential electoral college includes specified elected MPs and MLAs. The Election Commission conducts the election under Article 324.",
                "Participation in an election is different from conducting it. Also, not every member of Parliament or a state legislature belongs to the presidential electoral college.",
                _source("Election Commission of India, presidential election FAQs", "https://www.eci.gov.in/faq/1/2"),
            ),
            _method(
                "Test qualifiers one at a time",
                [
                    "Circle words such as all, only, every, ordinarily and subject to.",
                    "Break a long statement into separate legal propositions.",
                    "Check each proposition against its own rule and any stated exception.",
                    "Reject the statement only when a substantive claim is wrong, not merely because it uses an absolute word.",
                ],
                "A practice statement claims: 'Every public decision is automatically invalid unless every affected person agrees.' Is the claim supported merely by the principle of participation?",
                "No. Participation gives people opportunities to be heard or represented; it does not establish a universal unanimity requirement. The governing procedure must determine who decides and what consent, if any, is required.",
                "Words such as 'always' are signals to check carefully, not automatic proof that an option is false.",
            ),
            _method(
                "Sort a constitutional scenario by the question asked",
                [
                    "Separate the policy's objective from the authority to make it.",
                    "Identify whether the question concerns legislative competence, individual rights, procedure or implementation.",
                    "List the exact facts needed to decide that issue.",
                    "Avoid answering an authority question with a personal judgment about whether the policy is desirable.",
                ],
                "A state proposes a useful welfare programme. Does its usefulness alone settle whether the state can enact every provision in it?",
                "No. Desirability and legal competence are separate. The relevant legislative field, constitutional limits and any applicable law must also be examined. A beneficial objective does not answer those questions by itself.",
                "A morally attractive option may still fail to address the legal issue the question actually asks.",
            ),
        ],
    },
    {
        "topic": "Indian Economy",
        "summary": "Track the time period, price basis and transaction boundary before interpreting economic numbers.",
        "methods": [
            _method(
                "Use the date test for stocks and flows",
                [
                    "Ask whether the quantity is measured at a moment or over an interval.",
                    "Classify a balance on a date as a stock and an amount per period as a flow.",
                    "Check the units: rupees differs from rupees per month.",
                    "Use opening stock + inflows − outflows = closing stock when the quantities describe the same account.",
                ],
                "A savings account has ₹18,500 on 1 May. During May, ₹6,200 is deposited and ₹3,700 withdrawn. Identify the stock and calculate the closing balance.",
                "₹18,500 is the opening stock. Deposits and withdrawals are flows during May. The closing stock is 18,500 + 6,200 − 3,700 = ₹21,000, ignoring interest and fees.",
                "A large stock does not imply a large current flow. Do not compare wealth with monthly income as though they use the same time basis.",
                _source("NCERT National Income Accounting; original account example", "https://ncert.nic.in/textbook/pdf/leec102.pdf"),
            ),
            _method(
                "Remove the price change before judging output",
                [
                    "Determine whether the figure uses current prices or a fixed base-year price.",
                    "For a stated index with base 100, divide nominal value by index/100.",
                    "Compare real values on the same price basis.",
                    "Keep an exact calculation separate from a small-change approximation.",
                ],
                "An illustrative economy's nominal output is ₹242 crore and its price index is 110, with the base year equal to 100. What is output at base-year prices?",
                "Real output = 242 ÷ 1.10 = ₹220 crore. Dividing removes the 10% price-level increase represented by the index.",
                "Subtracting 10% of ₹242 gives ₹217.8 crore, not ₹220 crore. Reversing a percentage rise requires division by 1.10.",
                _source("NCERT National Income Accounting; original price-index example", "https://ncert.nic.in/textbook/pdf/leec102.pdf"),
            ),
            _method(
                "Draw the transaction chain to avoid double counting",
                [
                    "List each production stage and its sale value.",
                    "Identify intermediate purchases that are already embodied in a later sale.",
                    "Either add value added at every stage or count the final product once.",
                    "Check that both methods give the same total for the simplified chain.",
                ],
                "In a simplified chain, a grower sells fibre for ₹70, a spinner sells the resulting yarn for ₹110, and a weaver sells the finished cloth to a consumer for ₹190. What total should be counted?",
                "Assuming no other intermediate inputs, value added is 70 + (110 − 70) + (190 − 110) = ₹190. The final-sale method also gives ₹190. Adding all three sales would count earlier stages again.",
                "The same physical item may be intermediate or final depending on its use. A business purchase is not automatically an intermediate input if it is a capital asset.",
                _source("NCERT National Income Accounting; original production-chain example", "https://ncert.nic.in/textbook/pdf/leec102.pdf"),
            ),
        ],
    },
    {
        "topic": "Indian History",
        "summary": "Build chronology from anchor events, distinguish evidence from claims, and compare movements by their objectives and methods.",
        "methods": [
            _method(
                "Create a partial timeline before guessing a year",
                [
                    "Write the events you can date confidently.",
                    "Place uncertain events between the nearest known anchors.",
                    "Use explicit before/after clues to establish relative order.",
                    "Check whether an option reverses a known relationship before trying to recall every date.",
                ],
                "An original chronology exercise states: a petition preceded a strike; a settlement followed the strike; a commission reported after the settlement. What order is certain?",
                "Petition → strike → settlement → commission report. The relative order follows from the clues even though no exact year is supplied.",
                "A later account can describe an earlier event. The date of the document and the date of the event need separate positions.",
            ),
            _method(
                "Ask what a source can actually establish",
                [
                    "Identify who created the source, when, for whom and for what purpose.",
                    "Separate a direct observation from praise, accusation or later interpretation.",
                    "Ask whether independent evidence supports the specific claim.",
                    "Keep the conclusion narrower than the evidence when necessary.",
                ],
                "A ruler's inscription calls the ruler victorious everywhere. Does this by itself prove direct administration over every named region?",
                "No. A royal inscription can establish that the court made the claim, but praise may exaggerate conquest. Coins, local inscriptions and administrative evidence can help distinguish direct rule from tribute, raids or rhetoric.",
                "A contemporary source can be valuable and still be selective or biased. Primary does not mean automatically impartial.",
            ),
            _method(
                "Compare movements with a four-column grid",
                [
                    "Record the immediate grievance, wider objective, participants and principal method.",
                    "Use the clue that is most specific to the question, not a leader shared by several events.",
                    "Distinguish a local struggle from a nationwide campaign.",
                    "Check whether the options describe an objective, a method or a consequence.",
                ],
                "A hypothetical local protest asks landlords to reduce rent, while another campaign demands an end to colonial rule. Both use boycotts. What best distinguishes their stated objectives?",
                "The first concerns an immediate agrarian demand; the second concerns national political independence. A shared method, boycott, does not make their objectives identical.",
                "One movement can combine several objectives, and methods can change. A comparison grid should record the period described in the question.",
            ),
        ],
    },
    {
        "topic": "Telangana",
        "summary": "Link regional facts through river networks, period-specific maps and craft processes so similar names remain distinct.",
        "methods": [
            _method(
                "Learn projects as a river network",
                [
                    "Make a card with project, river, wider basin and location.",
                    "Draw the tributary joining its main river.",
                    "Keep the dam site separate from the region supplied by its canals.",
                    "Test yourself from the river toward the project and from the location toward the basin.",
                ],
                "A draft revision card places both Nizamsagar and Nagarjuna Sagar directly on the Krishna. Which part needs correction?",
                "Nagarjuna Sagar is on the Krishna. Nizamsagar is on the Manjira, which belongs to the Godavari system. Similar project-name endings do not indicate a shared river.",
                "A project's command area can extend beyond its dam site. Do not infer the dam's river solely from the districts receiving water.",
                _source("Supplied Telangana geography resources; original comparison exercise", None),
            ),
            _method(
                "Keep historical dates and present boundaries separate",
                [
                    "Write the date attached to the event or dataset.",
                    "Identify whether the named district is the district at that time or a present-day location.",
                    "Use a consistent boundary system when comparing statistics.",
                    "Preserve both historical and current labels in revision notes when reorganisation has changed the name or area.",
                ],
                "A heritage note uses an undivided district name, while a newer government page assigns the same monument to a newly formed district. Must one be false?",
                "Not necessarily. The monument can remain in the same physical place while the administrative boundary changes. Check both documents' dates and boundary conventions before treating the labels as contradictory.",
                "Do not compare district population totals across a boundary change as if the geographical area stayed fixed.",
            ),
            _method(
                "Recognise crafts through their production process",
                [
                    "Record the material, preparation step, technique and resulting product.",
                    "Distinguish work done before weaving from decoration added to finished cloth.",
                    "Associate the process with the place only after understanding the process.",
                    "Use the material or sequence clue to separate plausible regional craft options.",
                ],
                "A workshop dyes tied sections of yarn before placing it on a loom. Another joins fine metal wires into decorative patterns. Should both be classified as embroidery?",
                "No. Patterned resist-dyeing of yarn before weaving is the key process used in ikat. Shaping and joining fine metal wires is filigree. Embroidery decorates a base fabric with stitches.",
                "A shared decorative purpose does not imply a shared technique. Separate yarn treatment, weaving, painting, stitching and metalwork.",
                _source("Telangana Tourism, Arts and Crafts; original process comparison", "https://www.tourism.telangana.gov.in/page/arts-crafts"),
            ),
        ],
    },
    {
        "topic": "Environment & Social Awareness",
        "summary": "Follow the mechanism, use the right denominator and identify the barrier that an intervention actually addresses.",
        "methods": [
            _method(
                "Trace an environmental cause through its intermediate steps",
                [
                    "Identify the initial pressure: nutrient input, habitat loss, extraction or another disturbance.",
                    "Write at least one intermediate ecological change.",
                    "Connect that change to the observed consequence.",
                    "Check whether a proposed remedy acts on the cause or only on a visible symptom.",
                ],
                "After fertiliser runoff, a pond develops abundant algae and fish later die. Why is 'the fertiliser physically blocked the fish's gills' an inadequate explanation?",
                "The likely chain is nutrient enrichment → algal growth → decomposition that consumes dissolved oxygen → oxygen stress for fish. Evidence is still needed for the particular pond, but this mechanism explains the delayed effect better than the unsupported gill-blockage claim.",
                "An algal bloom and an oxygen shortage are connected through biological processes; they are not interchangeable names for the same event.",
            ),
            _method(
                "Put the denominator beside every social statistic",
                [
                    "Write who or what is counted in the numerator.",
                    "Write the population at risk or relevant total in the denominator.",
                    "Check the time period and multiplier, such as per 1,000 or percent.",
                    "Compare like rates rather than raw totals from differently sized populations.",
                ],
                "During the same year, 12 of village A's 600 households report an incident, compared with 15 of village B's 1,500 households. Which village has the higher proportion of affected households?",
                "A: 12/600 × 100 = 2%. B: 15/1,500 × 100 = 1%. A has the higher proportion despite having fewer affected households. The calculation assumes comparable definitions and recording.",
                "A larger affected-household count can reflect a larger population. Count each affected household once when calculating this proportion; counting repeated incidents answers a different question.",
            ),
            _method(
                "Match support to the actual barrier",
                [
                    "Describe the task the person needs to perform.",
                    "Identify the obstacle rather than assuming a lack of ability.",
                    "Choose a support that directly removes or reduces that obstacle.",
                    "Check that the support preserves the purpose of the activity and the person's agency.",
                ],
                "A student understands a lesson but cannot read the tiny text on its digital handout. Would repeating the same small-text explanation solve the main barrier?",
                "No. The immediate barrier is the format. Resizable text, suitable contrast and an accessible digital version address access while preserving the learning objective.",
                "Giving everyone an identical format is not the same as giving everyone an effective opportunity to use it.",
            ),
        ],
    },
    {
        "topic": "Current affairs",
        "summary": "Make dated, source-linked notes and distinguish announcements, legal commencement and completed outcomes.",
        "methods": [
            _method(
                "Build a dated event card",
                [
                    "Record what happened, the responsible institution and the relevant place.",
                    "Write the event date separately from the article's publication date.",
                    "Save the primary announcement or official record.",
                    "Add the status: proposed, approved, commenced, launched or completed.",
                ],
                "Illustrative example: a release published on 18 August says a facility was inaugurated on 16 August. Which date belongs in an 'inauguration date' answer?",
                "16 August is the event date. 18 August is the publication date. Keep both on the card so a later question about the release date can also be answered correctly.",
                "A recent article may describe an old event. Publication recency alone does not make the event new.",
            ),
            _method(
                "Check status before memorising a headline",
                [
                    "Locate the document that controls the claim, such as a notification, official result or organiser's announcement.",
                    "Read its scope, effective date and any qualifying conditions.",
                    "Separate a proposal or approval from implementation.",
                    "If official records conflict, record the uncertainty and look for the later correction rather than forcing a conclusion.",
                ],
                "Illustrative example: a policy is announced on 4 April, notified on 22 April and says it takes effect on 1 June. When does the notification say it becomes effective?",
                "1 June. Announcement, notification and commencement are three distinct stages. The example provides an explicit effective date, which controls this question.",
                "A minister's announcement, a news summary and a legal commencement date may refer to different stages of the same development.",
            ),
            _method(
                "Link one event to a small static-concept map",
                [
                    "Write the verified event as a single dated statement.",
                    "Add the institution, geographical location and one underlying syllabus concept.",
                    "Form a short 'why' question about that concept.",
                    "Keep speculative outcomes separate from established facts and refresh time-sensitive notes before using them.",
                ],
                "Illustrative example: a report announces restoration of a wetland. What useful static links should a revision note add without predicting success?",
                "Add the wetland's location and drainage basin, the implementing authority, and concepts such as habitat, water storage and ecological restoration. Whether the work achieves its targets requires later evidence.",
                "A project's stated target is not a measured outcome. Record the target and eventual result in separate fields.",
            ),
        ],
    },
]


def build_gs_lessons():
    """Return fresh lesson objects; callers may enrich them without shared mutation."""
    return deepcopy(LESSONS)


if __name__ == "__main__":
    lessons = build_gs_lessons()
    expected = {
        "General Science", "Geography", "Indian Polity", "Indian Economy",
        "Indian History", "Telangana", "Environment & Social Awareness",
        "Current affairs",
    }
    assert len(lessons) == 8 and {x["topic"] for x in lessons} == expected
    examples = []
    for lesson in lessons:
        assert lesson["summary"] and len(lesson["methods"]) == 3
        for method in lesson["methods"]:
            assert 3 <= len(method["steps"]) <= 5
            assert all(method["steps"]) and method["title"] and method["trap"]
            assert method["example"]["question"] and method["example"]["solution"]
            assert method["source"]["title"]
            examples.append(method["example"]["question"].casefold())
    assert len(examples) == len(set(examples)) == 24
    print("Validated 8 GS topics, 24 methods and 24 distinct worked examples.")
