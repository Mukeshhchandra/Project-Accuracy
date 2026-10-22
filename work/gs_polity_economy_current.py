"""650 distinct practice questions: 300 polity, 200 economy, 150 dated events.
Original question writing, checked against named primary educational references.
"""
import random
from gs_content import build_gs_bank
from current_content import build_current_bank

COI = {"title":"Constitution of India, Legislative Department (2024 text); provision identified in explanation", "url":"https://lddashboard.legislative.gov.in/sites/default/files/coi/COI_2024.pdf", "page":None}
POLITY_TEXT = {"title":"Indian Polity, 6th edition — supplied reference; original practice, not an extracted question", "url":None,"page":None}
NCERT = {"title":"NCERT Introductory Microeconomics — original application of standard concepts", "url":"https://ncert.nic.in/textbook.php?leec2=3-6", "page":None}
MACRO = {"title":"NCERT Introductory Macroeconomics — original application of standard concepts", "url":"https://ncert.nic.in/textbook.php?leec1=0-6", "page":None}
DEV = {"title":"NCERT Indian Economic Development — original practice on standard concepts", "url":"https://ncert.nic.in/textbook.php?keec1=0-8", "page":None}
RBI = {"title":"Reserve Bank of India: Functions and Working", "url":"https://rbi.org.in/scripts/PublicationsView.aspx?Id=18086", "page":None}

def build_polity_economy_current():
    bank=[]
    for q in build_gs_bank():
        if q['topic'] in ('Indian Polity','Indian Economy'):
            q=dict(q)
            if q['topic']=='Indian Polity' and q['source'].get('url') and 'constitution' in q['source']['url']:
                q['source']=dict(COI)
            bank.append(q)
    bank.extend(build_current_bank())

    def g(topic,skill,rows,source=None):
        entries=[line.split('|') for line in rows.strip().splitlines()]
        assert len(entries)==4,(skill,len(entries))
        assert all(len(e)==3 for e in entries),skill
        for k,(term,prompt,fact) in enumerate(entries):
            order=list(range(4));random.Random(87123+len(bank)).shuffle(order)
            options=[]
            for j in order:
                t,_,f=entries[j]
                options.append({'text':t,'explanation':('Correct. '+fact) if j==k else ('Incorrect. '+f+' This question concerns '+term+'.')})
            bank.append({'id':f'PEC-{len(bank)+1:04d}','section':'General Studies','topic':topic,'skill':skill,'question':prompt,'options':options,'answer':order.index(k),'explanation':fact,'source':dict(source or (COI if topic=='Indian Polity' else NCERT)),'difficulty':'Standard','origin':'Original practice'})
    def p(skill,rows,source=None):g('Indian Polity',skill,rows,source)
    def e(skill,rows,source=None):g('Indian Economy',skill,rows,source)

    # P01–P31: 124 new polity questions. Each row tests its own proposition.
    p('Constitution-making dates', '''
26 November 1949|When did the Constituent Assembly adopt the Constitution of India?|The Assembly adopted the Constitution on 26 November 1949; most provisions commenced later.
26 January 1950|When did most provisions of the Indian Constitution commence?|Article 394 sets 26 January 1950 as the general commencement date, with specified provisions commencing earlier.
9 December 1946|On which date did the Constituent Assembly first meet?|The Constituent Assembly held its first meeting on 9 December 1946.
24 January 1950|On which date did members sign the final Constitution before its general commencement?|Members signed the Constitution on 24 January 1950, shortly before Republic Day.
''',POLITY_TEXT)
    p('Constituent Assembly responsibilities', '''
B. R. Ambedkar|Who chaired the Drafting Committee of the Constituent Assembly?|Ambedkar chaired the Drafting Committee responsible for preparing the constitutional draft.
Rajendra Prasad|Who was the permanent President of the Constituent Assembly?|Rajendra Prasad presided over the Constituent Assembly as its elected President.
Sachchidananda Sinha|Who served as temporary chairman at the Constituent Assembly's first meeting?|Sachchidananda Sinha initially chaired the Assembly before the election of its permanent President.
B. N. Rau|Who served as Constitutional Adviser to the Constituent Assembly?|B. N. Rau was the Constitutional Adviser, contributing comparative research and an initial draft.
''',POLITY_TEXT)
    p('Preamble ideals', '''
Republic|Which Preamble ideal is inconsistent with a hereditary head of state?|A republic has a non-hereditary head of state; in India the President is elected indirectly.
Sovereign|Which Preamble term describes India's independent authority in internal and external affairs?|Sovereignty signifies independence from an external authority, subject to voluntarily undertaken international obligations.
Secular|Which Preamble ideal rejects the identification of the Indian State with a single official religion?|Secularism requires religious freedom and a constitutional relationship with religions rather than one state religion.
Fraternity|Which Preamble ideal links individual dignity with the unity and integrity of the nation?|Fraternity expresses common citizenship and mutual respect, supporting dignity and national unity.
''')
    p('Constitutional architecture', '''
Parliamentary government|Which system makes the political executive collectively accountable to the popularly elected legislative chamber?|Parliamentary government links executive tenure to legislative confidence; Article 75 makes the Union ministry responsible to Lok Sabha.
Federal distribution of powers|What feature divides legislative authority between Union and State governments under a supreme Constitution?|Federalism distributes authority constitutionally, although India's framework contains significant Union powers.
Judicial review|What allows a court to examine whether legislation conflicts with the Constitution?|Judicial review tests legal action against superior constitutional requirements and can invalidate unconstitutional provisions.
Single citizenship|What feature means an Indian is constitutionally a citizen of India rather than separately a citizen of a State?|India has a single constitutional citizenship; moving between States does not create a new State citizenship.
''',POLITY_TEXT)
    p('Territory and citizenship powers', '''
Article 1|Which Article describes India as a Union of States?|Article 1 names India, that is Bharat, a Union of States and specifies its territory.
Article 2|Which Article empowers Parliament to admit or establish new States on terms it thinks fit?|Article 2 addresses admission or establishment of new States.
Article 3|Which Article provides for formation of new States and alteration of existing States' areas, boundaries or names?|Article 3 governs internal territorial reorganisation, subject to its presidential recommendation and consultation procedure.
Article 11|Which Article preserves Parliament's power to regulate citizenship by law?|Article 11 permits parliamentary legislation on acquisition, termination and other citizenship matters.
''')
    p('Citizenship Act concepts', '''
Naturalisation|A foreign applicant seeks citizenship after meeting the prescribed residence and other statutory conditions. What is this route called?|Naturalisation is a statutory method of acquiring citizenship; meeting relevant legal requirements is essential.
Renunciation|An adult citizen voluntarily makes the prescribed declaration giving up Indian citizenship. Which concept applies?|Renunciation is a voluntary relinquishment under the Citizenship Act's procedure.
Termination|An Indian citizen voluntarily acquires citizenship of another country, attracting the statutory cessation rule. Which concept applies?|Termination concerns cessation consequent on voluntary acquisition of foreign citizenship under the Act.
Deprivation|The government withdraws citizenship acquired in a specified manner on statutory grounds such as fraud, following the required process. Which concept applies?|Deprivation is an involuntary statutory withdrawal and differs from voluntary renunciation.
''',POLITY_TEXT)
    p('Equality and exploitation provisions', '''
Article 15|Which Article prohibits specified forms of discrimination on grounds including religion, race, caste, sex and place of birth?|Article 15 contains discrimination prohibitions and also permits specified affirmative-action provisions.
Article 16|Which Article principally concerns equality of opportunity in public employment?|Article 16 governs equality in State employment, alongside its constitutional exceptions and reservation provisions.
Article 18|Which Article abolishes State-conferred titles, except military or academic distinctions?|Article 18 addresses titles; academic degrees and military distinctions are expressly excepted.
Article 23|Which Article prohibits trafficking in human beings, begar and similar forms of forced labour?|Article 23 prohibits these exploitative practices; its protection is not confined to State action.
''')
    p('Individual-right safeguards', '''
Article 24|Which Article prohibits employing children below fourteen in factories, mines or other hazardous employment?|Article 24 establishes this constitutional child-labour prohibition.
Article 21A|Which Article provides free and compulsory education for children aged six to fourteen as determined by law?|Article 21A establishes this age-specific education right.
Article 20(1)|Which clause protects against conviction for an act that was not an offence when committed?|Article 20(1) bars retrospective criminal conviction and a greater penalty than applicable when the offence occurred.
Article 20(3)|Which clause protects an accused person against being compelled to be a witness against himself or herself?|Article 20(3) protects against compelled self-incrimination by an accused person.
''')
    p('Article 19 freedoms', '''
Speech and expression|A citizen publishes criticism of public policy, subject to constitutionally permissible restrictions. Which Article 19 freedom is directly involved?|Article 19(1)(a) protects speech and expression, subject to reasonable restrictions under Article 19(2).
Peaceful assembly without arms|Citizens hold an unarmed peaceful demonstration. Which distinct Article 19 freedom is involved?|Article 19(1)(b) protects peaceful assembly without arms, subject to Article 19(3).
Formation of associations or unions|Citizens establish an organisation to pursue shared interests. Which Article 19 freedom is directly involved?|Article 19(1)(c) protects forming associations, unions and cooperative societies, subject to its restrictions.
Practising a profession|A citizen seeks to carry on a lawful occupation, trade or business. Which Article 19 freedom is involved?|Article 19(1)(g) covers professions, occupations, trades and businesses, subject to Article 19(6).
''')
    p('Rights and restrictions', '''
Reasonable restriction by law|What constitutional form is generally required to limit an Article 19 freedom on an authorised ground?|Restrictions must have legal authority and satisfy the Constitution's grounds and reasonableness requirements.
Public order|Which Article 19(2) ground relates to preventing disruption of community peace rather than merely protecting a minister from criticism?|Public order is an enumerated ground for restricting speech; disagreement with government alone is not equivalent to disorder.
Defamation|Which Article 19(2) ground concerns unlawful injury to another person's reputation?|Defamation is expressly included among the constitutional grounds for reasonable speech restrictions.
Sovereignty and integrity of India|Which restriction ground expressly protects the nation's territorial and sovereign unity?|The sovereignty and integrity of India is an express restriction ground in specified Article 19 clauses.
''')
    p('Scope of constitutional protections', '''
Citizens only|Who can claim the freedoms expressly enumerated in Article 19?|Article 19 is worded as a guarantee to citizens, unlike several protections available to all persons.
All persons|To whom does Article 14's general equality protection extend?|Article 14 protects any person within India's territory, not solely Indian citizens.
State and private conduct|Does the constitutional prohibition of untouchability apply only when a government officer practises it?|Article 17's prohibition is not confined to State action and is implemented through penal legislation.
Constitutional authority of law|Under Article 300A, what is required before a person may be deprived of property?|Property cannot be taken merely by executive wish; Article 300A requires authority of law.
''')
    p('Criminal and arrest protections', '''
Double jeopardy protection|Which Article 20 safeguard bars being prosecuted and punished for the same offence more than once?|Article 20(2) protects against a second prosecution and punishment for the same offence in its constitutional scope.
Information about grounds of arrest|Under Article 22(1), what must an ordinarily arrested person be informed of as soon as possible?|An arrested person must be informed of the grounds of arrest; Article 22 also contains specified exceptions.
Consultation with a legal practitioner|Which assistance does Article 22(1) protect for an ordinarily arrested person?|Article 22(1) protects the right to consult and be defended by a legal practitioner of choice.
Production before a magistrate within twenty-four hours|What is Article 22(2)'s general time safeguard, excluding necessary journey time?|The arrested person must be brought before the nearest magistrate within twenty-four hours, subject to constitutional exceptions.
''')
    p('Religious freedoms', '''
Article 25|Which Article protects freedom of conscience and the profession, practice and propagation of religion?|Article 25 protects these freedoms subject to public order, morality, health and other constitutional provisions.
Article 26|Which Article protects religious denominations' management of religious affairs within its limits?|Article 26 addresses denominational institutions, religious affairs and property, subject to public order, morality and health.
Article 27|Which Article protects against compelled taxation specifically appropriated to promote or maintain a particular religion?|Article 27 limits compulsion to pay taxes specifically devoted to promoting or maintaining a particular religion or denomination.
Article 28|Which Article deals with religious instruction and worship in educational institutions of specified kinds?|Article 28 distinguishes institutions wholly State-funded from other specified categories and protects against compelled participation in relevant cases.
''')
    p('Cultural and educational protections', '''
Article 29(1)|Which provision protects a section of citizens' right to conserve its distinct language, script or culture?|Article 29(1) safeguards conservation by any section of citizens having a distinct language, script or culture.
Article 29(2)|Which provision bars specified discriminatory denial of admission to State-maintained or State-aided educational institutions?|Article 29(2) prohibits denial solely on religion, race, caste, language or any of them.
Article 30(1)|Which provision protects religious and linguistic minorities' right to establish and administer educational institutions?|Article 30(1) gives this educational-institution right to minorities based on religion or language.
Article 30(2)|Which provision bars discrimination in educational aid because an institution is managed by a religious or linguistic minority?|Article 30(2) prevents that ground of discrimination in granting State aid.
''')
    p('Directive Principle articles', '''
Article 38|Which Directive Principle asks the State to promote welfare through a social order informed by justice and reduce inequalities?|Article 38 addresses a just social order and reduction of inequalities in income, status, facilities and opportunities.
Article 41|Which Directive Principle concerns work, education and public assistance within the State's economic capacity and development?|Article 41 states these welfare objectives subject to economic capacity and development.
Article 42|Which Directive Principle calls for just and humane working conditions and maternity relief?|Article 42 combines humane work conditions with maternity relief.
Article 43|Which Directive Principle refers to a living wage and a decent standard of life for workers?|Article 43 seeks a living wage, decent life and related opportunities; it also addresses cottage industries.
''')
    p('Additional Directive Principles', '''
Article 43A|Which Directive Principle calls for workers' participation in management of industries?|Article 43A directs the State to secure worker participation in industrial management through suitable measures.
Article 45|Which provision directs early childhood care and education for children below six years?|Article 45's current wording concerns children under six, distinct from the six-to-fourteen right in Article 21A.
Article 47|Which Directive Principle treats nutrition, living standards and public health as primary State duties?|Article 47 addresses these public-health and welfare responsibilities, including specified intoxicating substances.
Article 50|Which Directive Principle asks the State to separate the judiciary from the executive in public services?|Article 50 concerns separation of judicial and executive functions in State public services.
''')
    p('Article 39 objectives', '''
Adequate means of livelihood|What does Article 39(a) seek equally for men and women?|Article 39(a) concerns citizens' equal right to adequate means of livelihood.
Distribution for the common good|What objective does Article 39(b) prescribe for ownership and control of material resources of the community?|Article 39(b) calls for distribution that best serves the common good.
Avoiding concentration of wealth|What does Article 39(c) seek to prevent to the common detriment?|Article 39(c) addresses economic arrangements that concentrate wealth and means of production harmfully.
Equal pay for equal work|What employment-related principle is stated in Article 39(d)?|Article 39(d) calls for equal pay for equal work for both men and women.
''')
    p('International-policy directives', '''
International peace and security|What broad international objective is stated in Article 51(a)?|Article 51(a) directs the State to promote international peace and security.
Just and honourable relations between nations|What relationship standard does Article 51(b) encourage?|Article 51(b) calls for maintaining just and honourable relations between nations.
Respect for international law and treaty obligations|What legal orientation does Article 51(c) promote in dealings among organised peoples?|Article 51(c) fosters respect for international law and treaty obligations.
Settlement of disputes by arbitration|Which method of international dispute settlement is encouraged by Article 51(d)?|Article 51(d) encourages arbitration of international disputes.
''')
    p('Fundamental Duties: public life', '''
Respect for constitutional institutions and national symbols|Which duty includes abiding by the Constitution and respecting the National Flag and National Anthem?|Article 51A(a) links constitutional allegiance with respect for constitutional institutions and national symbols.
Cherishing freedom-struggle ideals|Which duty asks citizens to follow the noble ideals that inspired the national struggle for freedom?|Article 51A(b) concerns the ideals of the freedom struggle.
Defending the country when called upon|Which duty includes rendering national service when called upon?|Article 51A(d) concerns defence of the country and national service.
Safeguarding public property and abjuring violence|Which duty is most directly relevant to refusing to destroy buses during a protest?|Article 51A(i) addresses protection of public property and rejection of violence.
''')
    p('Fundamental Duties: knowledge and society', '''
Scientific temper, humanism and inquiry|Which duty encourages a citizen to question superstition through evidence and reform?|Article 51A(h) encourages scientific temper, humanism and the spirit of inquiry and reform.
Preserving composite cultural heritage|Which duty concerns valuing and preserving the rich heritage of India's composite culture?|Article 51A(f) addresses the country's composite cultural inheritance.
Striving for excellence|Which duty calls for excellence in individual and collective activity?|Article 51A(j) links excellence to the nation's continuing advancement.
Education opportunities for children aged six to fourteen|Which duty applies to a parent or guardian concerning a child or ward's education?|Article 51A(k) requires the parent or guardian to provide educational opportunities in that age band.
''')
    p('Presidential electoral college', '''
Elected members of both Houses of Parliament|Which parliamentary members participate in the President's electoral college?|Article 54 includes elected members of both parliamentary Houses; nominated members are excluded.
Elected State Legislative Assembly members|Which members of a State legislature vote in the presidential election?|The electoral college includes elected Assembly members, not Legislative Council members.
Delhi and Puducherry elected Assembly members|Which Union Territory Assembly members are specifically included by Article 54's explanation?|For Articles 54 and 55, the explanation includes the National Capital Territory of Delhi and Puducherry.
Proportional representation by single transferable vote|What voting system is constitutionally prescribed for the presidential election?|Article 55 provides proportional representation by single transferable vote with secret ballot.
''')
    p('Qualifications for the Presidency', '''
Thirty-five years|What is the minimum age for election as President of India?|Article 58 requires completion of thirty-five years.
Indian citizenship|What citizenship qualification must a presidential candidate satisfy?|Article 58 requires the candidate to be a citizen of India.
Qualification for election to Lok Sabha|For which parliamentary House must a presidential candidate be qualified for election?|Article 58 links presidential eligibility to qualification for election as a member of the House of the People.
No disqualifying office of profit|Which employment-related condition generally limits eligibility for the Presidency?|Article 58 disallows specified offices of profit, with stated exceptions for certain constitutional offices.
''')
    p('Presidential tenure and vacancies', '''
Five-year term|What is the normal constitutional term of the President from entering office?|Article 56 provides five years, subject to resignation, removal and holding office until a successor enters.
Resignation to the Vice-President|To whom does the President address a resignation in writing?|Article 56 requires a resignation addressed to the Vice-President.
Eligibility for re-election|Can a person who has served as President be elected again under Article 57?|Article 57 permits re-election, subject to the Constitution's eligibility provisions.
Election within six months of a casual vacancy|What is the constitutional outer period for filling a presidential vacancy caused by death, resignation or removal?|Article 62 requires the election as soon as possible and within six months of such vacancy.
''')
    p('Presidential impeachment', '''
Violation of the Constitution|What is the constitutional ground for impeachment of the President?|Article 61 provides impeachment for violation of the Constitution.
Either House of Parliament|Where can a charge for presidential impeachment originate?|Either parliamentary House can prefer the charge under Article 61.
Fourteen days' written notice|What minimum notice must precede the originating resolution for presidential impeachment?|Article 61 requires at least fourteen days' written notice signed by the prescribed proportion of members.
Two-thirds of the total membership|What voting threshold does Article 61 prescribe for the House's impeachment resolution?|The threshold is at least two-thirds of the House's total membership, not merely members present and voting.
''')
    p('President: constitutional functions', '''
Returning a non-Money Bill once|What reconsideration action can the President take under Article 111 on an ordinary Bill?|The President may return a non-Money Bill for reconsideration; after it is passed again, assent cannot be withheld.
Seeking Supreme Court advice|What power does Article 143 provide on a question of public importance?|The President may refer specified questions to the Supreme Court for its advisory opinion.
Appointing the Prime Minister|Which formal appointment is expressly made by the President under Article 75(1)?|The President appoints the Prime Minister; other ministers are appointed on the Prime Minister's advice.
Pardoning a death sentence|Which clemency power is expressly within Article 72's scope regardless of whether the relevant law is Union or State?|Article 72 expressly includes all cases involving a sentence of death.
''')
    p('Vice-President: election and removal', '''
Members of both Houses of Parliament|Who constitute the electoral college for electing the Vice-President?|Article 66 includes parliamentary members, including nominated members; State legislators do not vote.
Qualification for Rajya Sabha membership|For which House must a vice-presidential candidate be qualified for election?|Article 66 requires qualification for election to the Council of States.
Removal resolution originating in Rajya Sabha|Which House initiates the constitutional resolution to remove the Vice-President?|Article 67 requires a Rajya Sabha resolution passed by a majority of all its then members and agreed to by Lok Sabha.
Acting as President during a presidential vacancy|What role does Article 65 assign the Vice-President when the Presidency becomes vacant?|The Vice-President acts as President until an elected successor enters office.
''')
    p('Council of Ministers accountability', '''
Collective responsibility to Lok Sabha|To which House is the Union Council of Ministers collectively responsible?|Article 75(3) expressly makes the Council collectively responsible to the House of the People.
Presidential reconsideration followed by binding advice|Under Article 74, what happens if ministerial advice is reconsidered and then submitted again?|The President may require reconsideration but must act on the advice tendered after reconsideration.
Ministerial advice protected from judicial inquiry|What does Article 74(2) say about a court inquiring into advice tendered to the President?|The question whether any advice was tendered, and its contents, is not to be inquired into by a court.
Prime Minister's communication duty|Who must communicate Council decisions and provide requested administrative information to the President under Article 78?|Article 78 assigns these communication duties to the Prime Minister.
''')
    p('Union ministers: constitutional limits', '''
Six months|How long may a Union minister ordinarily remain continuously outside both Houses before ceasing to be a minister?|Article 75(5) sets a six-consecutive-month limit for a minister who is not a member of either House.
Fifteen per cent of Lok Sabha strength|What is the constitutional ceiling on the total Union ministry including the Prime Minister?|Article 75(1A) caps the number at fifteen per cent of the total number of Lok Sabha members.
Oaths of office and secrecy|Which two oaths does the President administer to a Union minister before entry into office?|Article 75(4) requires the oaths of office and secrecy in the Third Schedule.
Presidential pleasure|Under Article 75(2), whose pleasure formally governs a Union minister's tenure?|Ministers hold office during the President's pleasure within the parliamentary constitutional framework.
''')
    p('Parliament: constitutional structure', '''
President and two Houses|What three components constitute Parliament under Article 79?|Parliament consists of the President, the Council of States and the House of the People.
Council of States|What is the constitutional English name of Rajya Sabha?|Article 79 names the upper House the Council of States.
House of the People|What is the constitutional English name of Lok Sabha?|Article 79 names the lower House the House of the People.
Six-month maximum gap between sessions|What maximum interval may ordinarily separate the last sitting of one parliamentary session and the first sitting of the next?|Article 85 prevents a six-month interval from intervening between those sittings.
''')
    p('Rajya Sabha membership', '''
Twelve presidential nominees|How many Rajya Sabha members may the President nominate under Article 80?|Article 80 provides twelve nominees with special knowledge or practical experience in specified fields.
One-third retiring every second year|What constitutional rotation principle applies to Rajya Sabha members?|Article 83 provides retirement of approximately one-third every second year; the House is not dissolved.
Elected Assembly members elect State representatives|Who choose a State's elected representatives in Rajya Sabha?|Article 80 prescribes election by elected members of the State Legislative Assembly using proportional representation.
Literature, science, art and social service|Which fields are specified for presidential nomination to Rajya Sabha?|Article 80(3) lists these four fields of special knowledge or practical experience.
''')
    p('Lok Sabha tenure and representation', '''
Five years from its first meeting|What is Lok Sabha's normal term unless dissolved earlier?|Article 83 sets five years from the date appointed for its first meeting, subject to the emergency extension provision.
Direct territorial-constituency elections|How are elected Lok Sabha members chosen?|Article 81 provides direct election from territorial constituencies, subject to constitutional representation rules.
Earlier dissolution permitted|Must every Lok Sabha necessarily complete its normal five-year term?|Article 83 allows earlier dissolution, so five years is a maximum normal term rather than a guaranteed duration.
Emergency extension by law for one year at a time|What limited term extension may Parliament provide for Lok Sabha while a national emergency operates?|Article 83 permits extensions by law of at most one year at a time, ending no later than six months after the emergency ceases.
''')

    # Additional rows are supplied below; quota assertions guard integration.
    _add_more_polity(p)
    _add_economy(e)
    from current_supplement import add_current_supplement
    add_current_supplement(bank)
    from collections import Counter
    counts=Counter(q['topic'] for q in bank)
    assert counts=={'Indian Polity':300,'Indian Economy':200,'Current affairs':150},counts
    assert len({q['question'] for q in bank})==650
    assert len({q['id'] for q in bank})==650
    return bank

def _add_more_polity(p):
    p('Parliament membership qualifications', '''
Twenty-five years|What is the minimum age for election to Lok Sabha?|Article 84 sets the minimum age for Lok Sabha membership at twenty-five.
Thirty years|What is the minimum age for Rajya Sabha membership?|Article 84 sets the Rajya Sabha minimum age at thirty.
Office of profit disqualification|An MP accepts a government office not exempted by Parliament from disqualification. Which Article 102 issue arises?|Article 102(1)(a) concerns holding an office of profit under government, subject to statutory exemptions.
President acting according to Election Commission opinion|Who decides an Article 103 question about an MP's Article 102(1) disqualification?|The President must obtain and act according to the Election Commission's opinion under Article 103.
''')
    p('Parliamentary sittings', '''
Adjournment|The presiding officer suspends a House sitting until tomorrow. What is this called?|Adjournment interrupts a sitting; it does not end the parliamentary session itself.
Prorogation|The President formally ends a parliamentary session. Which process is involved?|Prorogation under Article 85 ends a session, while the House itself continues to exist.
Dissolution|Which process ends the existing Lok Sabha so that a new House must be elected?|Dissolution terminates the life of Lok Sabha, unlike adjournment or prorogation.
One-tenth of total membership|What is the constitutional default quorum of either House of Parliament?|Article 100(3) sets quorum at one-tenth of total membership until Parliament otherwise provides by law.
''')
    p('Presiding officers', '''
Lok Sabha elects its Speaker|Who chooses the Speaker of Lok Sabha under Article 93?|Lok Sabha chooses its own Speaker and Deputy Speaker from among its members.
Deputy Speaker|When the Speaker's office is vacant, which officer ordinarily performs its duties under Article 95?|The Deputy Speaker ordinarily performs the Speaker's duties during a vacancy, subject to Article 95's further contingency rule.
Rajya Sabha elects its Deputy Chairman|Who chooses Rajya Sabha's Deputy Chairman under Article 89?|Rajya Sabha chooses a member of that House as Deputy Chairman.
Casting vote on equality|When an ordinary vote in a House is tied, what vote may its presiding officer exercise?|Article 100 gives the Chairman or Speaker a casting vote on equality, while ordinarily excluding a first-instance vote.
''')
    p('Bills and dissolution', '''
Ordinary bill may originate in either House|Where may an ordinary non-financial bill originate in Parliament?|Article 107 allows bills to originate in either House, subject to the special Money Bill and financial-bill rules.
Private member's bill|An MP who is not a minister introduces legislation. What is that bill called?|A private member's bill is introduced by a member acting outside the Council of Ministers.
Rajya Sabha bill pending without Lok Sabha passage does not lapse|Which pending bill survives dissolution of Lok Sabha under Article 107(4)?|A bill pending in Rajya Sabha that Lok Sabha has not passed does not lapse merely because Lok Sabha dissolves.
Constitution Amendment Bill|Which bill cannot be resolved by a joint sitting when the two Houses disagree?|Article 368 requires the necessary majority separately in each House and provides no joint-sitting route for constitutional amendments.
''')
    p('Money Bill procedure', '''
Lok Sabha only|In which House must a Money Bill originate?|Article 109 prohibits introduction of a Money Bill in Rajya Sabha.
Fourteen days|Within what period must Rajya Sabha return a Money Bill with any recommendations?|Article 109 allows fourteen days from receipt; failure to return it results in deemed passage as passed by Lok Sabha.
Recommendations that Lok Sabha may reject|What is Rajya Sabha's role in considering a Money Bill?|Rajya Sabha may recommend changes, but Lok Sabha may accept or reject any or all of them.
Speaker's certificate|Whose certificate must accompany a Money Bill when it is sent to Rajya Sabha and the President?|Article 110(4) requires the Lok Sabha Speaker's signed certificate that it is a Money Bill.
''')
    p('Budget authorisation', '''
Annual Financial Statement|What constitutional document presents the Union's estimated receipts and expenditure under Article 112?|The Annual Financial Statement contains the government's estimated receipts and expenditure for the financial year.
Appropriation Act|Which legislative authorisation permits withdrawal from the Consolidated Fund for voted grants and charged expenditure?|Article 114 requires an appropriation law before these withdrawals from the Consolidated Fund.
Vote on account|Which Article 116 device authorises spending for part of a year while the full budget process is completed?|A vote on account provides advance authorisation for a portion of the financial year's estimated expenditure.
Charged expenditure not submitted to vote|How does Parliament treat expenditure charged on the Consolidated Fund under Article 113?|Charged expenditure may be discussed but is not submitted to the vote of Parliament.
''')
    p('Constitutional majority calculations', '''
Majority of members present and voting|Ignoring abstentions, what majority normally decides an ordinary question under Article 100?|Ordinary House decisions use a majority of members actually present and voting, unless the Constitution provides otherwise.
Majority of total membership|A rule requires more than half of a House's full constitutional membership. Which majority does it describe?|A majority of total membership counts the full membership as the denominator rather than just those voting.
Majority of all the then members|Which phrase does Article 94 use for a resolution removing the Lok Sabha Speaker?|Article 94 requires a majority of all the then members of Lok Sabha, with advance notice.
Two-thirds present and voting plus majority of total membership|What combined parliamentary majority is required for the main Article 368 amendment procedure?|Article 368 requires both a majority of total membership and at least two-thirds of members present and voting in each House.
''')
    p('Parliamentary financial committees', '''
Public Accounts Committee|Which parliamentary committee principally examines government appropriation accounts and relevant CAG reports?|The Public Accounts Committee scrutinises accounts and audit findings to examine whether authorised public funds were properly spent.
Estimates Committee|Which parliamentary committee examines estimates and suggests economies and administrative improvements?|The Estimates Committee examines estimates to suggest economy, efficiency and improvements in organisation and presentation.
Committee on Public Undertakings|Which parliamentary committee focuses on accounts and performance of specified public enterprises?|The Committee on Public Undertakings examines public-enterprise accounts and relevant CAG reports within its remit.
Department-related Standing Committee|Which committee system examines ministry demands for grants and bills referred to it by the presiding officers?|Department-related Standing Committees provide detailed ministry-focused examination of demands, referred bills and policy documents.
''', POLITY_TEXT)
    p('Parliament questions and devices', '''
Starred question|Which parliamentary question requests an oral answer and permits supplementary questions?|A starred question is answered orally and can be followed by supplementaries under House rules.
Unstarred question|Which parliamentary question receives a written answer without supplementary questions?|An unstarred question receives a written response rather than oral questioning on the floor.
Short-notice question|Which question device can address an urgent matter of public importance with less than the usual notice?|A short-notice question is admitted on grounds of urgency under the applicable House rules.
Zero Hour|What informal parliamentary practice allows members to raise matters after Question Hour without being a Constitution-defined hour?|Zero Hour developed through parliamentary practice rather than a provision defining it in the Constitution.
''', POLITY_TEXT)
    p('Supreme Court qualifications', '''
Sixty-five years|At what age does a Supreme Court judge retire under Article 124?|Article 124(2) fixes the retirement age of a Supreme Court judge at sixty-five.
Five years as a High Court judge|Which judicial experience satisfies one Article 124 qualification route for appointment to the Supreme Court?|Service as a High Court judge for at least five years, including successive such courts, is one qualification route.
Ten years as a High Court advocate|Which advocacy experience satisfies one Article 124 qualification route for Supreme Court appointment?|Article 124 recognises at least ten years as an advocate of a High Court or successive High Courts.
Distinguished jurist in the President's opinion|Which Article 124 qualification route does not specify a minimum term as a judge or advocate?|A person considered a distinguished jurist by the President can qualify through the separate constitutional jurist route.
''')
    p('Supreme Court jurisdictions', '''
Original federal-dispute jurisdiction|A legal-right dispute arises between the Union and a State within Article 131's scope. Which jurisdiction applies?|Article 131 confers original jurisdiction for specified intergovernmental disputes involving a legal right.
Special leave to appeal|Which Article 136 power lets the Supreme Court grant discretionary leave against many court or tribunal decisions?|Special leave is a discretionary appellate gateway, subject to Article 136's exception concerning armed-forces courts and tribunals.
Review of its own judgments|What power does Article 137 expressly give the Supreme Court?|Article 137 permits review of the Supreme Court's own judgments or orders, subject to applicable law and rules.
Orders necessary for complete justice|What is the central purpose of the Supreme Court's Article 142(1) power?|Article 142 permits necessary decrees or orders to do complete justice in a cause or matter pending before it.
''')
    p('Judicial authority and removal', '''
Law declared by Supreme Court binds all Indian courts|What rule does Article 141 establish for the Supreme Court's declarations of law?|Article 141 makes law declared by the Supreme Court binding on all courts within India.
Supreme Court is a court of record|Which Article 129 status includes the Supreme Court's power to punish contempt of itself?|A court of record retains authoritative judicial records and has the expressly recognised contempt power.
Proved misbehaviour or incapacity|What are the constitutional grounds for removal of a Supreme Court judge?|Article 124(4) permits removal only for proved misbehaviour or incapacity through its prescribed parliamentary process.
Separate addresses by both Houses in the same session|What parliamentary step must precede a presidential order removing a Supreme Court judge?|Each House must adopt the Article 124(4) address in the same session with the specified dual special majority.
''')
    p('High Court structure', '''
Sixty-two years|At what age does a High Court judge retire under Article 217?|Article 217 fixes the retirement age of High Court judges at sixty-two.
President appoints High Court judges|Which constitutional authority formally appoints High Court judges under Article 217?|The President appoints High Court judges after the constitutional consultations and applicable appointment process.
Transfer under Article 222|Which provision permits presidential transfer of a High Court judge after consultation with the Chief Justice of India?|Article 222 specifically concerns transfer from one High Court to another.
Superintendence under Article 227|Which High Court power concerns supervision of courts and tribunals within its territorial jurisdiction, subject to the armed-forces exception?|Article 227 provides judicial superintendence over subordinate courts and tribunals in the territory concerned.
''')
    p('Subordinate judiciary', '''
Governor in consultation with High Court|Who makes appointments, postings and promotions of district judges under Article 233?|Article 233 assigns these decisions to the Governor in consultation with the relevant High Court.
Seven years as advocate or pleader|What minimum advocacy experience does Article 233 require for an eligible district-judge recruit not already in government service?|The person must have been an advocate or pleader for at least seven years and be recommended by the High Court.
State Public Service Commission and High Court consultation|Which consultation combination does Article 234 specify for rules governing recruitment below district-judge level?|The Governor makes the recruitment rules after consulting both the State Public Service Commission and High Court.
High Court control under Article 235|Which authority controls district courts and subordinate courts for Article 235 purposes?|Article 235 vests control in the High Court, including specified posting, promotion and leave matters for the judicial service.
''')
    p('Governor', '''
Presidential appointment|How is a State Governor appointed under Article 155?|The President appoints the Governor by warrant under the President's hand and seal.
Five years subject to presidential pleasure|What is the Governor's stated term under Article 156, subject to its qualifications?|The stated term is five years, but the Governor holds office during presidential pleasure and may continue until a successor enters office.
Minimum age thirty-five|What age qualification does Article 157 prescribe for a Governor?|A Governor must be an Indian citizen who has completed thirty-five years.
Resignation addressed to President|To whom does a Governor submit a written resignation?|Article 156 provides resignation by writing addressed to the President.
''')
    p('State Council of Ministers', '''
Governor appoints the Chief Minister|Who formally appoints a State's Chief Minister under Article 164?|The Governor appoints the Chief Minister; other ministers are appointed on the Chief Minister's advice.
Collective responsibility to Legislative Assembly|To which State House is the Council of Ministers collectively responsible?|Article 164(2) specifies collective responsibility to the State Legislative Assembly.
Fifteen-percent ceiling with twelve-member minimum|What numerical rule does Article 164(1A) provide for a State Council of Ministers including its Chief Minister?|The normal constitutional limit is fifteen percent of Assembly strength, with a minimum of twelve ministers.
Ministerial six-month legislative membership limit|A State minister remains outside the State Legislature continuously for six months. What does Article 164(4) require?|The minister ceases to hold office at the end of six consecutive months without legislative membership.
''')
    p('State legislatures', '''
Normally sixty to five hundred Assembly members|What general size range does Article 170 prescribe for a State Legislative Assembly, subject to constitutional exceptions?|Article 170 provides a general minimum of sixty and maximum of five hundred directly elected members.
Twenty-five-year minimum MLA age|What minimum age does Article 173 prescribe for membership of a Legislative Assembly?|A Legislative Assembly member must have completed twenty-five years.
Thirty-year minimum MLC age|What minimum age does Article 173 prescribe for membership of a Legislative Council?|A Legislative Council member must have completed thirty years.
Parliamentary law following a special Assembly resolution|How may a State Legislative Council be created or abolished under Article 169?|Parliament may legislate after the Assembly resolves by majority of total membership and two-thirds present and voting.
''')
    p('Legislative Council composition', '''
One-third elected by specified local authorities|Which Article 171 share of a Legislative Council is elected through municipal, district-board and other specified local-authority electorates?|As nearly as possible one-third is elected by members of specified local authorities.
One-twelfth elected by graduate electorates|Which Article 171 share of a Legislative Council is elected through qualifying graduate electorates?|As nearly as possible one-twelfth is elected by qualifying graduates resident in the State.
One-twelfth elected by teacher electorates|Which Article 171 share is elected through qualifying teachers in institutions not below secondary-school level?|As nearly as possible one-twelfth is elected by the constitutionally described teaching electorate.
One-third elected by MLAs from non-MLAs|Which Article 171 share is elected by Legislative Assembly members from persons outside that Assembly?|As nearly as possible one-third is elected by MLAs, from persons who are not members of the Assembly.
''')
    p('Parliament legislation on State subjects', '''
Article 249 national-interest resolution|Which provision allows Rajya Sabha, by the prescribed two-thirds vote, to enable Parliament to legislate on a State List matter in the national interest?|Article 249 gives this enabling role to Rajya Sabha for a resolution normally lasting at most one year at a time.
Article 250 during national emergency|Which provision empowers Parliament to legislate on State List matters while an Article 352 emergency operates?|Article 250 supplies this temporary emergency-related legislative power.
Article 252 consenting States|Two States want Parliament to regulate a State List subject for them. Which route begins with resolutions of their legislatures?|Article 252 lets Parliament legislate for consenting States, with later adoption possible by other States.
Article 253 treaty implementation|Which provision empowers Parliament to legislate throughout India to implement an international agreement, even on a State List subject?|Article 253 provides the treaty and international-decision implementation power.
''')
    p('Intergovernmental coordination', '''
Inter-State Council under Article 263|Which constitutional mechanism may be established to discuss common interests and recommend coordination among States and the Union?|Article 263 permits an Inter-State Council when the President considers that public interests would be served.
Inter-State river disputes under Article 262|Which provision permits Parliament to provide adjudication of disputes concerning inter-State river waters?|Article 262 addresses inter-State water disputes and permits statutory exclusion of court jurisdiction over them.
All-India services under Article 312|Which provision lets Parliament create a new all-India service after Rajya Sabha's prescribed national-interest resolution?|Article 312 requires the enabling Rajya Sabha resolution supported by two-thirds present and voting.
Full faith and credit under Article 261|Which provision concerns nationwide recognition of public acts, records and judicial proceedings of the Union and States?|Article 261 establishes full faith and credit, with proof and effect regulated as provided there.
''')
    p('Fiscal constitutional mechanisms', '''
GST Council under Article 279A|Which constitutional body makes recommendations on GST rates and related harmonisation matters?|Article 279A establishes the GST Council, chaired by the Union Finance Minister with specified Union and State representation.
Finance Commission ordinarily every fifth year|How frequently must the President constitute a Finance Commission under Article 280, unless an earlier time is necessary?|Article 280 requires constitution every fifth year or earlier if the President considers it necessary.
Union borrowing under Article 292|Which provision addresses Union borrowing on the security of the Consolidated Fund of India?|Article 292 provides Union borrowing powers subject to limits Parliament may fix by law.
State borrowing under Article 293|Which provision includes Union-consent conditions for specified borrowing by a State indebted to the Union?|Article 293 governs State borrowing and the relevant consent conditions.
''')
    p('National emergency safeguards', '''
War, external aggression or armed rebellion|Which grounds can support a national emergency under Article 352?|Article 352 lists war, external aggression and armed rebellion as the relevant security grounds.
Written decision of Union Cabinet|What executive decision must be communicated in writing before the President issues an Article 352 proclamation?|Article 352(3) requires the Union Cabinet's written decision, rather than an unsupported individual ministerial recommendation.
Parliamentary approval within one month|What is the ordinary initial parliamentary approval deadline for an Article 352 proclamation, subject to the Lok Sabha dissolution exception?|The proclamation ordinarily ceases after one month unless both Houses approve it by the required majority.
Articles 20 and 21 protected from Article 359 suspension|Which rights are expressly excluded from an Article 359 order suspending the right to move courts for enforcement?|Article 359 excludes the rights conferred by Articles 20 and 21 from that suspension mechanism.
''')
    p('President rule', '''
Failure of constitutional machinery in a State|What constitutional condition is addressed by Article 356?|Article 356 concerns a situation in which a State's government cannot be carried on according to the Constitution.
Initial approval within two months|What is the ordinary parliamentary approval deadline for an Article 356 proclamation, subject to its dissolution exception?|Article 356 ordinarily requires approval by both Houses before two months expire.
Six-month continuation periods|For how long can an approved Article 356 proclamation continue per parliamentary renewal, within constitutional limits?|Article 356 uses six-month continuation periods, with further conditions for extended operation.
High Court powers cannot be assumed|Which State institution's powers does Article 356 expressly prevent the President from assuming?|Article 356(1) prohibits assuming High Court powers or suspending constitutional provisions concerning High Courts.
''')
    p('Financial emergency', '''
Threat to financial stability or credit|What condition can justify an Article 360 financial-emergency proclamation?|Article 360 concerns a threat to the financial stability or credit of India or any part of its territory.
Both Houses approve within two months|What is the ordinary initial approval requirement for an Article 360 proclamation, subject to its Lok Sabha dissolution exception?|Approval of both Houses is ordinarily required before the two-month period expires.
Financial propriety directions to States|What type of direction may the Union issue during an Article 360 emergency?|The Union may direct States to observe specified canons of financial propriety and other necessary financial directions.
Reduction of specified public salaries|Which measure is expressly contemplated by Article 360 during a financial emergency?|Directions may include reductions of salaries and allowances of specified public servants, including Supreme Court and High Court judges.
''')
    p('Electoral principles', '''
Adult suffrage under Article 326|Which principle underlies elections to Lok Sabha and State Legislative Assemblies?|Article 326 bases these elections on adult suffrage, subject to citizenship, age and lawful disqualifications.
Single general electoral roll under Article 325|Which rule bars special electoral rolls based only on religion, race, caste or sex?|Article 325 provides one general roll for each territorial constituency and bars specified identity-based exclusion or special-roll claims.
Election petition under Article 329(b)|By what specified process may an election to Parliament or a State Legislature be called into question?|Article 329(b) directs election challenges to an election petition presented to the authority and in the manner provided by law.
Election Commission control includes presidential and vice-presidential elections|Besides parliamentary and State-legislature elections, which elections fall within Article 324's specified scope?|Article 324 includes elections to the offices of President and Vice-President of India.
''')
    p('Constitutional commissions', '''
National Commission for Scheduled Castes|Which commission is provided for by Article 338?|Article 338 establishes the National Commission for Scheduled Castes and specifies its safeguards-monitoring and advisory duties.
National Commission for Scheduled Tribes|Which commission is provided for by Article 338A?|Article 338A establishes the National Commission for Scheduled Tribes as a separate constitutional commission.
National Commission for Backward Classes|Which commission has constitutional status under Article 338B?|Article 338B establishes the National Commission for Backward Classes following the 102nd Amendment.
Special Officer for linguistic minorities|Which office does Article 350B provide to investigate linguistic-minority safeguards?|The Special Officer for linguistic minorities investigates constitutional safeguards and reports to the President.
''')
    p('Panchayat representation and continuity', '''
Five-year term from first meeting|What normal duration does Article 243E prescribe for a Panchayat unless dissolved earlier?|A Panchayat normally continues for five years from the date appointed for its first meeting.
Election within six months after dissolution|What is the ordinary Article 243E deadline for reconstituting a prematurely dissolved Panchayat?|Election should ordinarily be completed within six months, with an exception where the remaining term is less than six months.
Twenty-one years sufficient for age qualification|Which age threshold prevents disqualification solely for being under twenty-five for Panchayat membership?|Article 243F protects an otherwise eligible person who has attained twenty-one from disqualification only on that age ground.
At least one-third directly elected seats reserved for women|What minimum women's reservation does Article 243D prescribe among directly elected Panchayat seats?|At least one-third, including seats reserved for SC and ST women, must be reserved for women.
''')
    p('Local government institutions', '''
State Finance Commission under Article 243I|Which institution periodically reviews Panchayat finances and recommends fiscal arrangements?|The Governor constitutes a State Finance Commission every five years under Article 243I after the initial constitutional requirement.
State Election Commission under Article 243K|Which institution supervises electoral rolls and elections for Panchayats?|Article 243K vests this responsibility in the State Election Commission, whose Commissioner is appointed by the Governor.
District Planning Committee under Article 243ZD|Which committee consolidates Panchayat and municipal plans into a draft district development plan?|The District Planning Committee combines local plans and addresses matters of shared district interest.
Metropolitan Planning Committee under Article 243ZE|Which committee prepares a draft development plan for a metropolitan area?|The Metropolitan Planning Committee coordinates metropolitan planning using the relevant local plans and common interests.
''')
    p('Constitutional schedules beyond subject lists', '''
First Schedule|Which Schedule lists the States and Union territories with their territorial descriptions?|The First Schedule specifies States and Union territories and describes their territories.
Third Schedule|Which Schedule contains forms of constitutional oaths and affirmations?|The Third Schedule supplies oath and affirmation forms for specified ministers, legislators, judges and other officeholders.
Fourth Schedule|Which Schedule allocates seats in Rajya Sabha to States and Union territories?|The Fourth Schedule deals with allocation of Council of States seats.
Sixth Schedule|Which Schedule provides autonomous-district arrangements for specified tribal areas in Assam, Meghalaya, Tripura and Mizoram?|The Sixth Schedule establishes special administrative arrangements for the specified north-eastern tribal areas.
''')
    p('Selected constitutional amendments', '''
First Amendment, 1951|Which amendment inserted the Ninth Schedule and Articles 31A and 31B?|The First Amendment introduced these provisions, among other changes, in 1951.
Seventh Amendment, 1956|Which amendment accompanied States reorganisation and removed the earlier Part A, B and C State classification?|The Seventh Amendment reorganised constitutional arrangements for States and Union territories in 1956.
Sixty-first Amendment, 1988|Which amendment reduced the Article 326 voting-age threshold from twenty-one to eighteen?|The Sixty-first Amendment changed the constitutional voting age to eighteen.
Eighty-sixth Amendment, 2002|Which amendment inserted Article 21A and the parental duty in Article 51A(k)?|The Eighty-sixth Amendment introduced the education-right provision, revised Article 45 and added the related parental duty.
''')
    p('Constitutional language provisions', '''
Hindi in Devanagari script under Article 343|What official language and script does Article 343 specify for the Union, alongside its English-use arrangements?|Article 343 specifies Hindi in Devanagari script as the Union's official language, with constitutional and statutory provisions concerning English.
English judicial-language rule under Article 348|Which provision establishes the default language rule for Supreme Court and High Court proceedings, subject to its qualifications?|Article 348 provides the English-language rule and related constitutional qualifications; it does not declare a national language.
Representation in a language used in the Union or State|What linguistic right concerning grievance representations is provided by Article 350?|A person may submit a grievance representation to a Union or State officer in any language used in that Union or State.
Promotion of Hindi under Article 351|Which provision directs the Union to promote Hindi's spread and development while drawing on India's composite culture?|Article 351 contains this developmental directive and recognises enrichment from other Indian languages.
''')
    p('Statutory and executive institutions', '''
Central Information Commission under RTI Act|Which institution is established by the Right to Information Act, 2005 for central information-right appeals and complaints?|The Central Information Commission is a statutory body under the RTI Act, not a body created by a constitutional article.
National Human Rights Commission under 1993 Act|Which national institution is constituted under the Protection of Human Rights Act, 1993?|The NHRC has a statutory basis in the 1993 Act for its human-rights functions.
Lokpal under 2013 Act|Which Union-level anti-corruption institution derives its framework from the Lokpal and Lokayuktas Act, 2013?|The Lokpal is a statutory institution under the 2013 Act for the categories and procedures specified there.
NITI Aayog by executive resolution|Which policy institution was established through a Union Cabinet resolution rather than a constitutional amendment or founding statute?|NITI Aayog was constituted by executive resolution in January 2015 as the Union government's policy think tank.
''', POLITY_TEXT)

def _add_economy(e):
    e('Production possibilities', '''
Productively efficient point|An economy produces on its production-possibility frontier. What does this indicate about resource use?|A frontier point uses available resources and technology efficiently; increasing one output requires sacrificing another.
Underutilised resources|What does a point strictly inside an economy's production-possibility frontier generally represent?|An interior point indicates unemployment or inefficient use of resources, so both outputs may be increased.
Currently unattainable combination|What does a point outside the existing production-possibility frontier represent?|The combination exceeds current productive capacity with the existing resources and technology.
Outward frontier shift|What change can sustained improvements in productive technology cause to the production-possibility frontier?|Improved productive capacity can move the frontier outward, making more output combinations feasible.
''')
    e('Types of economic analysis', '''
Positive statement|Which type of economic statement asserts a testable relationship, such as that a price increase reduces quantity purchased under stated conditions?|Positive economics describes or predicts what occurs and can in principle be tested against evidence.
Normative statement|Which type of economic statement says that a particular tax policy ought to be adopted for fairness?|Normative economics contains a value judgment about what should be done.
Microeconomics|Which branch studies a single household's consumption or an individual firm's pricing decision?|Microeconomics studies the behaviour of individual economic units and particular markets.
Macroeconomics|Which branch studies aggregate output, nationwide unemployment and the general price level?|Macroeconomics analyses economy-wide aggregates and their interactions.
''')
    e('Utility and preference', '''
Total utility|What term describes the overall satisfaction from consuming a specified quantity of a good?|Total utility is the complete satisfaction attributed to all the units consumed.
Marginal utility|What term describes the change in satisfaction from consuming one additional unit?|Marginal utility measures the incremental satisfaction from an additional unit, holding relevant conditions constant.
Indifference curve|Which curve joins consumption bundles that a consumer regards as equally satisfactory?|An indifference curve represents combinations giving the same preference level to the consumer.
Budget line|Which line represents combinations that exactly exhaust a consumer's income at given prices?|The budget line describes the spending constraint using income and the prices of the two goods.
''')
    e('Related goods and income', '''
Normal good|A household buys more of a good when income rises, other things unchanged. How is the good classified?|Demand for a normal good rises with income, giving positive income elasticity over the relevant range.
Inferior good|A household switches away from a low-cost good as its income rises. How is that good classified over this range?|An inferior good has declining demand as income rises, holding prices and other relevant conditions constant.
Substitutes|A rise in tea's price raises demand for coffee, other things equal. What relationship does this suggest?|Substitutes can replace each other in use, so an increase in one good's price can raise demand for the other.
Complements|A rise in printer prices reduces demand for compatible ink, other things equal. What relationship does this suggest?|Complementary goods are used together, so a higher price for one can reduce demand for the other.
''')
    e('Demand elasticity', '''
Price-elastic demand|Quantity demanded changes by a larger percentage than price, in absolute terms. How is demand classified?|Price-elastic demand has absolute price elasticity greater than one.
Price-inelastic demand|Quantity demanded changes by a smaller percentage than price, in absolute terms. How is demand classified?|Price-inelastic demand has absolute price elasticity below one.
Unit-elastic demand|Quantity demanded and price change by equal percentages in opposite directions. How is demand classified?|Unit elasticity means absolute price elasticity equals one.
Perfectly inelastic demand|A consumer buys the same quantity despite a price change over the relevant range. What is the limiting elasticity case?|Perfectly inelastic demand has zero price elasticity and a vertical demand curve.
''')
    e('Demand-curve interpretation', '''
Movement along a demand curve|Only a good's own price changes while other demand factors remain fixed. How is the resulting quantity change shown?|An own-price change produces movement along the existing demand curve.
Rightward demand shift|A favourable change in consumer preferences raises purchases at every price. How is this represented?|A rightward shift shows greater demand at each given price, caused by a factor other than the good's own price.
Leftward demand shift|The number of buyers falls, reducing demand at each price. How is this represented?|A leftward shift indicates lower demand at every given price.
Ceteris paribus|Which analytical qualification means other relevant factors are held constant when examining a relationship?|Ceteris paribus isolates a particular relationship by holding other influences unchanged.
''')
    e('Production relationships', '''
Production function|What economic relationship maps quantities of inputs into the maximum feasible output?|A production function expresses the technological relationship between inputs and achievable output.
Short run|In production theory, what period has at least one input fixed?|The short run is defined by input constraints, not by a fixed number of calendar months.
Long run|In production theory, what period allows all inputs to be varied?|The long run is the planning horizon over which no input is fixed.
Diminishing marginal product|With one input fixed, successive units of another input eventually add less output. What principle describes this?|Diminishing marginal product concerns declining extra output from additional variable input, other conditions held constant.
''')
    e('Measures of product', '''
Total product|What measures the complete output produced using a specified amount of a variable input?|Total product is the total physical output associated with the input combination.
Average product|What is calculated by dividing total output by units of the variable input?|Average product measures output per unit of that input.
Marginal product|What measures the extra output generated by one additional unit of a variable input?|Marginal product is the change in total product per additional unit of the input.
Constant returns to scale|All inputs double and output also doubles. Which returns-to-scale case applies?|Constant returns to scale means proportionate increases in all inputs cause the same proportionate increase in output.
''')
    e('Costs of production', '''
Fixed cost|A shop pays the same lease rent even when producing nothing in the short run. What kind of cost is this?|A fixed cost does not vary with current output over the relevant short-run range.
Variable cost|A factory's raw-material spending rises as it produces more units. What kind of cost is this?|Variable cost changes with output because additional production uses more variable inputs.
Marginal cost|What measures the increase in total cost associated with producing one more unit?|Marginal cost is incremental total cost per additional unit of output.
Average total cost|A firm divides its total production cost by units produced. What measure results?|Average total cost is total cost per unit of output, combining fixed and variable components.
''')
    e('Revenue and profit', '''
Total revenue|Which measure equals selling price multiplied by quantity sold when all units sell at the same price?|Total revenue is the firm's sales receipts from its output.
Average revenue|Which measure divides total sales receipts by units sold?|Average revenue is revenue per unit; with a single selling price it equals that price.
Marginal revenue|Which measure captures the change in total revenue from selling one additional unit?|Marginal revenue is the incremental revenue generated by another unit sold.
Economic profit|Which measure subtracts both explicit and implicit opportunity costs from total revenue?|Economic profit recognises the opportunity cost of the owner's resources as well as cash expenses.
''')
    e('Market structures', '''
Perfect competition|Which benchmark market has many price-taking firms selling a homogeneous product with free entry and exit?|Perfect competition assumes that an individual firm cannot influence the market price.
Monopoly|Which market structure has one seller without close substitutes and substantial barriers to entry?|A monopoly is a single-seller market with market power protected by entry barriers.
Monopolistic competition|Many sellers offer differentiated products and can enter the market. Which structure fits?|Monopolistic competition combines numerous sellers with product differentiation and limited pricing power.
Oligopoly|A market is dominated by a small number of firms whose decisions affect one another. Which structure fits?|Oligopoly involves few major sellers and strategic interdependence.
''')
    e('External effects and shared goods', '''
Negative externality|A factory imposes uncompensated smoke damage on neighbouring households. What economic problem occurs?|A negative externality is a cost imposed on third parties that is not fully reflected in the private transaction.
Positive externality|A person's vaccination reduces infection risk for others. What economic effect occurs?|A positive externality provides a benefit to third parties beyond the decision-maker's own benefit.
Public good|Which type of good is both non-rival in consumption and difficult to exclude non-payers from using?|A public good combines non-rivalry and non-excludability, as in the standard national-defence example.
Common-pool resource|A fishery is difficult to exclude users from, but each fish caught reduces what remains. How is it classified?|A common-pool resource is non-excludable or hard to exclude from, but rival in use.
''')
    e('Price controls and market interventions', '''
Binding price ceiling|A legally enforced maximum price is below the competitive equilibrium price. Which control is binding?|A ceiling below equilibrium restrains price and can create excess demand if other conditions are unchanged.
Binding price floor|A legally enforced minimum price is above the competitive equilibrium price. Which control is binding?|A floor above equilibrium restrains downward adjustment and can create excess supply.
Per-unit production subsidy|Government pays producers an amount for each unit supplied. Which intervention directly lowers their net unit cost?|A production subsidy reduces the producer's effective cost and can encourage supply, depending on market conditions.
Per-unit excise tax|Government charges producers an amount for each unit sold. Which intervention creates a wedge between buyer and seller prices?|An excise tax creates a tax wedge; its economic incidence depends on supply and demand elasticities.
''')
    e('Stock and flow distinctions', '''
Stock variable|A household's wealth is measured on a specified date. What type of variable is wealth?|A stock is measured at a point in time rather than over a period.
Flow variable|A worker's earnings are measured over one month. What type of variable is income?|A flow is measured per time period, such as income earned during a month.
Depreciation|What is the allowance for wear, damage and obsolescence of fixed capital in national accounts?|Depreciation, or consumption of fixed capital, measures the reduction in capital value through use and obsolescence.
Net investment|Which measure subtracts depreciation from gross investment?|Net investment measures additions to capital after allowing for consumption of existing fixed capital.
''', MACRO)
    e('National-accounting boundaries', '''
Final good|A household buys bread for consumption. How is the bread classified for national-income accounting?|A final good is used for final consumption or investment rather than as an input into further production during the period.
Intermediate good|A bakery buys flour to make bread it will sell. How is the flour classified in that transaction?|An intermediate good is used up or transformed in producing another good; counting both at full value would double count.
Value-added method|Which accounting method sums each producer's output value minus intermediate input value?|The value-added method avoids counting the same intermediate production repeatedly.
Transfer payment|A pension transfer is paid without receiving a current good or service in exchange. How is the payment classified?|A transfer redistributes income without directly corresponding to current production, so it is not itself added to GDP.
''', MACRO)
    e('National income adjustments', '''
Gross national income|Which aggregate equals GDP plus net primary income received from the rest of the world?|Gross national income measures income accruing to residents, adjusting domestic production for cross-border primary income.
Net domestic product|Which aggregate equals gross domestic product minus consumption of fixed capital?|Net domestic product deducts depreciation from GDP.
GDP deflator|Which price index is calculated as nominal GDP divided by real GDP, multiplied by one hundred?|The GDP deflator reflects prices of domestically produced final goods and services represented in GDP.
Net exports|Which expenditure component equals exports of goods and services minus imports?|Net exports enter the GDP expenditure identity as X minus M, avoiding inclusion of foreign production in domestic output.
''', MACRO)
    e('Household income and saving', '''
Disposable income|What income remains available for household consumption and saving after personal direct taxes, including relevant transfers?|Disposable income measures what households can spend or save after the relevant tax and transfer adjustments.
Saving|What is the portion of disposable income not spent on consumption?|Saving is disposable income minus consumption over the accounting period.
Marginal propensity to consume|Which ratio measures the increase in consumption divided by the increase in disposable income?|The marginal propensity to consume describes consumption from an additional unit of disposable income.
Marginal propensity to save|Which ratio measures the increase in saving divided by the increase in disposable income?|The marginal propensity to save describes saving from additional disposable income; in the simple model it complements MPC to one.
''', MACRO)
    e('Simple income-determination model', '''
Investment multiplier|In the basic closed-economy model without taxes, what relates an initial autonomous-investment increase to the larger equilibrium-income change?|The simple investment multiplier equals one divided by one minus MPC, under the model's assumptions.
Autonomous consumption|What part of the simple consumption function does not vary with current income?|Autonomous consumption is the intercept component, distinguished from income-induced consumption.
Excess aggregate demand|Planned spending exceeds output at the current income level. Which disequilibrium is present?|Excess planned demand draws down unplanned inventories and can induce firms to expand output in the simple model.
Deficient aggregate demand|Planned spending is below output at the current income level. Which disequilibrium is present?|Deficient planned demand creates unintended inventory accumulation and can induce output reduction.
''', MACRO)
    e('Functions of money', '''
Medium of exchange|Money is accepted when goods are purchased, avoiding the need for a barter partner. Which function is illustrated?|As a medium of exchange, money intermediates purchases and sales.
Unit of account|Goods are priced in rupees so their values can be compared. Which function of money is illustrated?|A unit of account provides a common measure in which prices, debts and accounts are expressed.
Store of value|A household keeps purchasing power in a money balance for later use. Which function is intended?|Money can transfer purchasing power over time, although inflation can reduce its real value.
Standard of deferred payment|A contract specifies repayment of a fixed rupee debt next year. Which monetary function is illustrated?|Money serves as the agreed measure for payments due in the future.
''', MACRO)
    e('Money and banking concepts', '''
Double coincidence of wants|Which barter difficulty requires each trader to want exactly what the other offers?|Double coincidence of wants is the mutual matching requirement that money helps overcome.
Demand deposit|Which bank deposit can normally be withdrawn on demand and used through payment instructions?|Demand deposits are liquid bank liabilities available to depositors on demand, subject to account arrangements.
Time deposit|Which deposit is placed for an agreed period rather than being wholly payable on demand?|A time deposit has a maturity arrangement, although premature withdrawal may be allowed on stated terms.
Fiat money|Which form of money derives monetary acceptance from legal and institutional arrangements rather than its commodity value?|Fiat currency need not have intrinsic commodity value equal to its face value.
''', MACRO)
    e('Central banking functions', '''
Banker to government|The central bank manages government accounts and acts as its banking agent. Which role is illustrated?|As banker to government, the central bank provides banking and related debt-management services under its legal framework.
Banker to banks|Commercial banks hold settlement accounts and reserves with the central bank. Which role is illustrated?|The central bank provides the banking system with accounts and settlement facilities as banker to banks.
Lender of last resort|A central bank supplies emergency liquidity to address eligible banking-system liquidity stress. Which role is illustrated?|Lender-of-last-resort support addresses acute liquidity problems under applicable conditions; it is not an automatic guarantee of solvency.
Currency management|The central bank arranges distribution of banknotes and withdrawal of unfit notes. Which function is illustrated?|Currency management concerns supply, circulation quality and withdrawal of currency within the governing legal arrangements.
''', RBI)
    e('Bank credit concepts', '''
Collateral|A borrower pledges an asset that can secure repayment of a loan. What is this asset called?|Collateral is security offered against credit; it reduces a lender's potential loss but does not erase borrower obligations.
Credit appraisal|A lender assesses repayment capacity and risks before approving a loan. What process is occurring?|Credit appraisal evaluates the borrower's ability and willingness to repay and the proposed credit's risks.
Non-performing asset|Under applicable prudential norms, a loan stops meeting required servicing standards. What category may it enter?|A non-performing asset is a credit exposure classified under regulatory overdue or performance criteria, rather than simply a low-profit loan.
Financial intermediation|A bank channels funds from savers toward borrowers. What broad economic role does this illustrate?|Financial intermediation connects suppliers and users of funds while managing maturity, information and risk differences.
''', RBI)
    e('Financial-market instruments', '''
Equity share|Which security represents an ownership interest with a residual claim in a company?|An equity share represents ownership; dividends and capital value are not fixed or guaranteed.
Bond|Which instrument generally represents a debt claim requiring payments according to contractual terms?|A bond is debt financing, giving the holder a creditor claim rather than ordinary ownership.
Treasury bill|Which short-term government instrument is commonly issued at a discount and redeemed at face value?|Treasury bills are short-term government debt instruments without periodic coupon payments.
Commercial paper|Which instrument is an unsecured short-term money-market promissory note issued by eligible entities?|Commercial paper provides short-term financing to eligible issuers and carries issuer credit risk.
''', RBI)
    e('Financial-market organisation', '''
Primary market|A company issues new securities to raise funds. In which market does this transaction occur?|The primary market channels funds to issuers through new securities.
Secondary market|An investor sells an existing listed share to another investor. In which market does this occur?|The secondary market trades existing securities and provides liquidity without necessarily supplying new funds to the issuer.
Money market|Which market generally deals in short-term funds and instruments with maturities up to one year?|The money market serves short-term financing and liquidity management.
Capital market|Which market principally serves longer-term debt and equity financing?|The capital market connects longer-term fund users with investors through debt and equity instruments.
''', RBI)
    e('Indian financial institutions', '''
SEBI|Which Indian regulator's core remit concerns securities markets and investor protection in those markets?|SEBI regulates the securities market under its statutory framework and seeks to protect securities investors.
NABARD|Which apex development institution focuses on agriculture and rural development finance?|NABARD supports agriculture and rural development through refinance, development and supervisory functions within its remit.
SIDBI|Which development institution chiefly promotes, finances and develops the micro, small and medium enterprise sector?|SIDBI's principal development-finance mandate concerns the MSME sector.
IRDAI|Which Indian regulator supervises insurance businesses and policyholder interests within its statutory remit?|IRDAI regulates and develops the insurance sector and protects policyholder interests under the insurance framework.
''', RBI)
    e('Budget receipts and spending', '''
Revenue receipt|Which government receipt neither creates a liability nor reduces a government asset?|Revenue receipts include taxes and specified non-tax receipts without those capital effects.
Capital receipt|Borrowing creates a government liability, while a loan recovery reduces an asset. Which receipt category includes these cases?|Capital receipts either create liabilities or reduce government assets.
Capital expenditure|Government builds a new public bridge that creates an asset. What expenditure category best fits?|Capital expenditure generally creates assets or reduces liabilities, unlike routine current spending.
Revenue expenditure|Government pays salaries for current administrative services. What expenditure category best fits?|Revenue expenditure generally covers current operations without directly creating a capital asset or reducing a liability.
''', MACRO)
    e('Public funds and fiscal arrangements', '''
Consolidated Fund|Which constitutional fund receives ordinary Union revenues, borrowing proceeds and loan repayments?|Article 266 places these receipts in the Consolidated Fund of India, with withdrawals requiring legal authorisation.
Contingency Fund|Which fund enables advances for unforeseen expenditure pending subsequent authorisation?|Article 267 provides for a Contingency Fund held at the President's disposal under the governing law.
Public Account|Provident-fund and other specified monies held by government on behalf of others are credited to which constitutional account?|The Public Account contains other public monies under Article 266 rather than the government's ordinary Consolidated Fund revenues.
Disinvestment|Government sells part of its equity holding in a public enterprise. What process is this?|Disinvestment reduces government equity ownership; it need not always transfer management control.
''', MACRO)
    e('Tax design', '''
Specific tax|A tax is fixed at a stated amount per kilogram regardless of the product's price. What type is it?|A specific tax is levied per physical unit rather than as a percentage of value.
Ad valorem tax|A tax equals a percentage of the transaction value. What type is it?|An ad valorem tax changes with the taxable value because the rate is a percentage of that value.
Tax incidence|What concept identifies who ultimately bears a tax's economic burden after market adjustment?|Economic incidence can differ from the person legally responsible for remitting the tax.
Input tax credit|Under a value-added tax system, what mechanism offsets eligible tax paid on inputs against output-tax liability?|Input tax credit reduces cascading by allowing eligible input taxes to be credited, subject to the applicable conditions.
''', MACRO)
    e('Fiscal stabilisation', '''
Expansionary fiscal policy|During weak demand, government increases spending or reduces taxes to support aggregate demand. What broad stance is this?|Expansionary fiscal measures aim to raise demand, though effects depend on capacity, financing and economic conditions.
Contractionary fiscal policy|Government reduces demand by cutting spending or increasing taxes. What broad stance is this?|Contractionary fiscal policy withdraws demand relative to the alternative policy path.
Automatic stabiliser|Income-tax receipts fall automatically in a downturn without a new policy decision. What mechanism is operating?|Automatic stabilisers vary with economic activity and cushion fluctuations without fresh discretionary measures.
Crowding out|Higher public borrowing raises financing costs and discourages some private investment. What possible effect is this?|Crowding out is displacement of private activity through financing or resource pressures; it is not inevitable in every setting.
''', MACRO)
    e('Exchange-rate systems', '''
Floating exchange rate|Which exchange-rate arrangement primarily allows currency prices to respond to foreign-exchange supply and demand?|A floating rate adjusts through market forces, although actual systems may still involve intervention.
Fixed exchange rate|Authorities commit to a specified parity or narrow band and act to maintain it. Which arrangement is described?|A fixed exchange-rate arrangement uses an official parity supported by policy and reserve operations.
Currency depreciation|Under a market-determined system, a rupee buys less foreign currency than before. What change has occurred?|Depreciation is a fall in a currency's external value through exchange-market movements.
Currency devaluation|Authorities officially reduce the parity of a currency under a fixed-rate arrangement. What change is this?|Devaluation is an official downward change in the exchange-rate parity, distinguished from market depreciation.
''', MACRO)
    e('External accounts', '''
Current account|In balance-of-payments accounting, which account includes goods, services and primary and secondary income?|The current account records trade and income flows, including current transfers, between residents and non-residents.
Foreign direct investment|A cross-border investment establishes a lasting interest and significant influence in an enterprise. Which category fits?|Direct investment is associated with a lasting relationship and significant influence under the relevant statistical definitions.
Portfolio investment|A foreign investor purchases tradable securities without establishing a direct-investment relationship. Which category fits?|Portfolio investment covers eligible equity and debt securities outside direct investment and reserves.
Reserve assets|Which external assets are held and controlled by monetary authorities for external financing and intervention purposes?|Reserve assets are readily available external assets used to meet balance-of-payments financing needs and related purposes.
''', MACRO)
    e('International trade concepts', '''
Comparative advantage|A country can produce a good at a lower opportunity cost than another country. What advantage does it have?|Comparative advantage compares relative opportunity costs and can support gains from specialisation and trade.
Absolute advantage|A country produces a good using fewer inputs than another country. What advantage does this describe?|Absolute advantage compares productivity levels rather than opportunity costs.
Tariff|Government imposes a tax on an imported product. What trade-policy instrument is this?|A tariff taxes imports and can alter domestic prices, government revenue and trade volumes.
Import quota|Government caps the physical quantity of a product that can be imported. What instrument is this?|An import quota directly restricts the allowed import quantity rather than merely taxing it.
''', MACRO)
    e('Development indicators', '''
Human Development Index|Which UNDP composite combines health, education and standard-of-living dimensions?|HDI uses life expectancy, schooling measures and income per person to summarise selected human-development dimensions.
Gini coefficient|Which statistical measure summarises inequality in an income or consumption distribution?|The Gini coefficient measures inequality; its interpretation depends on the scale and distribution being measured.
Lorenz curve|Which graph relates cumulative population shares to cumulative income or consumption shares?|A Lorenz curve describes the distribution and is commonly compared with the line of equal distribution.
Poverty headcount ratio|Which indicator measures the share of people below a specified poverty threshold?|The headcount ratio measures poverty incidence but does not by itself measure how far below the threshold people are.
''', DEV)
    e('Population and labour indicators', '''
Labour-force participation rate|Which ratio measures people working or seeking or available for work as a share of the relevant population?|LFPR compares the labour force with the population specified by the survey's age and reference-period definitions.
Worker-population ratio|Which ratio measures employed persons as a share of the relevant population?|WPR measures employment relative to the specified population, rather than relative only to the labour force.
Unemployment rate|Which ratio divides unemployed labour-force participants by the labour force?|The unemployment rate excludes persons outside the labour force from its denominator.
Dependency ratio|Which demographic ratio compares dependent-age groups with the working-age group under stated age definitions?|The dependency ratio is an age-structure indicator; it does not mean every working-age person is employed.
''', DEV)
    e('Forms of employment', '''
Self-employment|A person operates an own-account enterprise and bears its business risk. Which employment form fits?|Self-employment involves working in one's own enterprise, with or without hired workers.
Regular salaried employment|A worker receives a regular wage or salary under an ongoing employment arrangement. Which form fits?|Regular salaried employment is distinguished from casual work and own-account work by the continuing employment relationship.
Casual wage labour|A worker is hired intermittently for daily or short-term wage work. Which form fits?|Casual labour typically lacks the continuing arrangement of regular salaried employment.
Informal employment|Which classification specifically describes a job's lack of formal employment protections or benefits, independently of whether wages are paid regularly or casually?|Informal employment is a job-based concept; it can exist within both informal and formal-sector enterprises.
''', DEV)
    e('Human and physical capital', '''
Human capital|Education, health and acquired skills improve a worker's productive capabilities. Which capital concept is illustrated?|Human capital refers to capabilities embodied in people through education, training, health and related investments.
Physical capital|A factory invests in machines and tools used repeatedly in production. Which capital concept is illustrated?|Physical capital consists of produced assets such as machinery and equipment used in production.
On-the-job training|A worker acquires productive skills through supervised practice at the workplace. Which investment method is illustrated?|On-the-job training builds human capital while the worker participates in workplace activities.
Brain drain|Skilled people emigrate, reducing the origin country's available skilled workforce. What phenomenon is described?|Brain drain refers to the outflow of skilled workers; its broader effects can also include remittances and knowledge links.
''', DEV)
    e('Agricultural development concepts', '''
Crop diversification|Farmers move from reliance on one crop toward several crops or higher-value activities. What strategy is this?|Crop diversification changes the production mix and can reduce dependence on a single crop's price and weather risks.
Agricultural marketing|Which system covers the movement and exchange of farm produce through aggregation, grading, storage, transport and sale?|Agricultural marketing links producers to buyers and affects prices received, wastage and market access.
Organic farming|Which production approach relies on ecological processes and restricts specified synthetic inputs under applicable standards?|Organic farming emphasises ecological management and compliance with organic production standards.
Land consolidation|Scattered small plots are reorganised into more compact holdings. What reform is described?|Consolidation reduces fragmentation and can make cultivation, irrigation and mechanisation more efficient.
''', DEV)
    e('Rural credit and inclusion', '''
Institutional rural credit|A farmer obtains a loan from a regulated bank or cooperative rather than an informal moneylender. What broad source category is this?|Institutional credit is supplied through formal financial institutions under applicable regulatory arrangements.
Self-help group|A small voluntary group pools savings and may lend internally or link to a bank. What institution is described?|A self-help group uses regular saving, group processes and often bank linkage to improve access to finance.
Financial inclusion|Which policy objective seeks affordable access to useful formal financial services for underserved people?|Financial inclusion covers appropriate payment, saving, credit, insurance and pension access, with responsible use.
Microfinance|Small-value financial services are offered to low-income clients often underserved by conventional banking. What approach is this?|Microfinance describes small-scale financial services; it is broader than a promise of free or interest-free credit.
''', DEV)
    e('Growth, sustainability and institutions', '''
Sustainable development|Which development principle seeks to meet present needs without compromising future generations' ability to meet theirs?|Sustainable development integrates present welfare with long-term environmental and social capacity.
Inclusive growth|Which growth objective emphasises broad participation and sharing of economic opportunities and benefits?|Inclusive growth asks who participates in growth and who receives its benefits, not just how fast aggregate output rises.
Social infrastructure|Schools, hospitals and sanitation systems fall primarily into which infrastructure category?|Social infrastructure supports human well-being and capabilities through education, health and related services.
Economic infrastructure|Transport networks, electricity supply and communication systems fall primarily into which infrastructure category?|Economic infrastructure provides foundational services that enable production, exchange and other economic activity.
''', DEV)
    e('Economic reform concepts', '''
Liberalisation|Government reduces selected licensing and administrative restrictions on economic activity. What reform process is described?|Liberalisation relaxes specified controls to allow greater market participation, while regulation may continue.
Privatisation|Ownership or control of a public enterprise is transferred to private actors. What reform process is described?|Privatisation concerns private ownership or control, rather than every sale of a small public shareholding.
Globalisation|Trade, capital, technology and production links increasingly connect national economies. What process is described?|Globalisation is growing international economic integration through several channels.
Competition policy|Which policy framework seeks to prevent anti-competitive agreements and abuse of market power while supporting market rivalry?|Competition policy promotes effective rivalry and addresses conduct that harms the competitive process.
''', DEV)
