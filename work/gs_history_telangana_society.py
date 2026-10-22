"""Original mock-test content, separated by ownership to prevent cross-bank reuse.

Static concepts are original syllabus-based items. Consulted documentary
references are supplied only when actually inspected; no inferred page numbers.
"""
import random
from collections import Counter
from gs_content import build_gs_bank

ORIGINAL = {'title':'Original syllabus-based practice; not a past-paper quotation','page':None,'url':None}

def build_history_telangana_society():
    wanted = {'Indian History','Telangana','Environment & Social Awareness'}
    bank = [q.copy() for q in build_gs_bank() if q['topic'] in wanted]
    for i,q in enumerate(bank): q['id'] = f'HTS-{i+1:04d}'
    def add(topic, skill, rows, source=None, difficulty='Standard', take=4):
        """Each row is a distinct answerable fact, not a reverse of another row."""
        if isinstance(rows,str):
            rows=[tuple(x.strip() for x in line.split('|')) for line in rows.strip().splitlines() if line.strip()]
        assert len(rows)==4, (skill,len(rows))
        assert all(len(r)==3 for r in rows), skill
        for a,(term,stem,reason) in enumerate(rows):
            if a >= take: break
            order=list(range(4)); random.Random(8100+len(bank)).shuffle(order)
            options=[]
            for j in order:
                label,_,fact=rows[j]
                text=('Correct. '+fact) if j==a else f'Incorrect. {fact} Here the question describes {term}, not {label}.'
                options.append({'text':label,'explanation':text})
            bank.append({'id':f'HTS-{len(bank)+1:04d}','section':'General Studies','topic':topic,'skill':skill,
                'question':stem,'options':options,'answer':order.index(a),'explanation':reason,
                'source':dict(source[a] if isinstance(source,list) else (source or ORIGINAL)),
                'difficulty':difficulty,'origin':'Original practice'})
    def h(skill,rows,source=None): add('Indian History',skill,rows,source)
    def t(skill,rows,source=None): add('Telangana',skill,rows,source)
    def s(skill,rows,source=None): add('Environment & Social Awareness',skill,rows,source)

    # 200 further Indian-history and culture facts, organised into comparisons.
    h('Prehistoric periods', '''
Palaeolithic | Which prehistoric phase is chiefly associated with early chipped-stone tools and hunting-gathering? | The Palaeolithic is the Old Stone Age, characterised by chipped tools and hunting-gathering lifeways.
Mesolithic | Which prehistoric phase is particularly associated with widespread use of microliths? | Mesolithic communities used small stone tools called microliths, often fitted into composite implements.
Neolithic | Which prehistoric phase is associated with polished stone tools and established farming communities? | Neolithic societies developed farming, animal husbandry and polished stone tools, though regional sequences varied.
Chalcolithic | Which archaeological term describes cultures using copper alongside stone tools? | Chalcolithic literally refers to the copper-and-stone phase, preceding widespread iron use in many regions.
''')
    h('Methods of studying the past', '''
Stratigraphy | Which archaeological method studies the sequence of layers at a site? | Stratigraphy interprets successive deposits; undisturbed lower layers are usually older than those above.
Radiocarbon dating | Which method estimates the age of suitable organic remains using the decay of carbon-14? | Radiocarbon dating estimates age from radioactive carbon in once-living material within its useful dating range.
Epigraphy | What is the study of inscriptions called? | Epigraphy studies inscriptions on durable surfaces, including their scripts, wording and historical setting.
Numismatics | What is the study of coins called? | Numismatics studies coins and related monetary objects, providing evidence about rulers, economies and iconography.
''')
    h('Harappan urban sites', '''
Mohenjo-daro | At which Harappan site was the structure called the Great Bath excavated? | The Great Bath is a major public structure excavated at Mohenjo-daro in Sindh.
Harappa | Which Punjab site gave its name to the Harappan civilisation? | Harappa, in present-day Pakistani Punjab, gave the civilisation its archaeological name.
Dholavira | Which Harappan site in Kachchh is especially noted for its elaborate water reservoirs? | Dholavira developed a distinctive system of reservoirs and water conservation suited to its environment.
Lothal | Which Gujarat Harappan site is associated with a basin traditionally interpreted as a dockyard? | Lothal contains a large basin commonly interpreted as a dockyard, although its precise function has been debated.
''')
    h('Early textual traditions', '''
Rigveda | Which Veda primarily contains hymns addressed to deities? | The Rigveda is a collection of hymns and is the earliest of the four Vedic collections.
Samaveda | Which Veda is especially associated with melodies used in ritual chanting? | The Samaveda arranges verses for melodic chanting in ritual performance.
Yajurveda | Which Veda principally supplies sacrificial formulae and ritual instructions? | The Yajurveda provides formulae and directions used in sacrificial ritual.
Atharvaveda | Which Veda includes charms, healing formulae and concerns of everyday life? | The Atharvaveda includes material on healing, protection and domestic concerns alongside other subjects.
''')
    h('Early political vocabulary', '''
Janapada | Which term refers to the territory where a jana, or people, had settled? | A janapada was the territorial settlement of a people and an early unit of political geography.
Mahajanapada | What term describes the larger territorial states prominent in northern India around the sixth century BCE? | Mahajanapadas were major territorial polities that developed with expanding settlements and political organisation.
Gana-sangha | Which term denotes an early polity governed through an assembly of ruling groups rather than a single hereditary monarch alone? | Gana-sanghas involved collective decision-making among elite groups; they were not universal adult democracies.
Rajan | Which early Indian political title is generally translated as king or chief? | Rajan denoted a ruler or chief, with powers that changed across periods and regions.
''')
    h('Buddhist institutions and monuments', '''
Sangha | What is the organised community of Buddhist monks and nuns called? | The Sangha is the monastic community, governed by disciplinary rules within Buddhist traditions.
Stupa | Which Buddhist monument is a mound-like structure often associated with relics? | A stupa is a commemorative or relic monument around which worshippers may circumambulate.
Chaitya hall | What is a Buddhist prayer hall, often containing a stupa, commonly called? | A chaitya hall is an assembly or worship space, distinct from residential monastic cells.
Vihara | Which term commonly denotes a Buddhist monastery or monastic residence? | A vihara provides accommodation and associated spaces for members of a monastic community.
''')
    h('Jain traditions', '''
Mahavira | Who is recognised in Jain tradition as the twenty-fourth Tirthankara? | Mahavira is the twenty-fourth Tirthankara and a major teacher of the Jain tradition.
Parshvanatha | Who is recognised as the twenty-third Jain Tirthankara? | Parshvanatha precedes Mahavira in the traditional sequence of twenty-four Tirthankaras.
Ahimsa | Which ethical principle emphasises avoiding harm to living beings? | Ahimsa means non-violence and has especially rigorous expression in Jain ethics.
Anekantavada | Which Jain doctrine emphasises that reality has many aspects and cannot be exhausted by one viewpoint? | Anekantavada teaches the many-sidedness of reality and cautions against treating one partial perspective as absolute.
''')
    h('Ancient literary evidence', '''
Upanishads | Which body of texts explores questions about brahman, atman and ultimate reality? | The Upanishads contain philosophical discussions associated with the later Vedic tradition.
Jatakas | Which stories narrate previous births of the Buddha? | Jataka narratives portray the Buddha in previous lives and provide evidence about moral ideals and social imagination.
Sangam literature | Which corpus is a major source for early Tamil society and poetry? | Sangam literature preserves early Tamil poetry concerning love, warfare, generosity and social life.
Indica | Which work associated with Megasthenes described India during the Mauryan period? | Megasthenes wrote Indica after his visit to the Mauryan court; it survives through later quotations.
''')
    h('Early Indian centres', '''
Magadha | Which ancient kingdom expanded from south Bihar to become the core of major early empires? | Magadha grew in south Bihar and became the political core of the Nanda and Mauryan empires.
Vajji | Which early confederacy had Vaishali as an important centre? | Vajji was a confederacy associated with Vaishali and traditions of collective elite governance.
Avanti | Which mahajanapada had Ujjayini as a major centre? | Avanti was an important western-central Indian polity with Ujjayini as a prominent centre.
Kosala | Which mahajanapada included the region associated with Shravasti? | Kosala was an important north Indian polity, with Shravasti as a major centre.
''')
    h('Early and early-medieval rulers', '''
Samudragupta | Which Gupta ruler’s conquests are praised in the Prayaga inscription composed by Harisena? | Harisena’s Prayaga prashasti celebrates Samudragupta’s military campaigns and political achievements.
Chandragupta II | Which Gupta ruler is associated with the title Vikramaditya and the defeat of the western Shakas? | Chandragupta II expanded Gupta power westward and is associated with the title Vikramaditya.
Harshavardhana | Which seventh-century ruler made Kannauj a major centre of his power? | Harshavardhana ruled much of northern India from a political centre at Kannauj in the seventh century.
Pulakeshin II | Which Chalukya ruler checked Harsha’s southward advance near the Narmada? | Pulakeshin II of the Badami Chalukyas resisted Harsha’s expansion into the Deccan.
''')
    h('Southern temple patronage', '''
Rajaraja I | Which Chola ruler commissioned the Brihadisvara Temple at Thanjavur? | Rajaraja I commissioned the great Brihadisvara Temple at Thanjavur, reflecting Chola power and temple patronage.
Rajendra I | Which Chola ruler founded Gangaikondacholapuram after northern campaigns? | Rajendra I established Gangaikondacholapuram and commemorated his northern campaign through its name and temple.
Narasimhavarman I | Which Pallava ruler is associated with the name Mamalla and the development of Mamallapuram? | Narasimhavarman I bore the title Mamalla, from which Mamallapuram derives its name.
Krishna I | Which Rashtrakuta ruler is associated with the rock-cut Kailasa temple at Ellora? | The Kailasa temple at Ellora is associated with Rashtrakuta patronage under Krishna I.
''')
    h('Temple architectural terms', '''
Shikhara | What is the rising tower above a sanctum commonly called in north Indian temple architecture? | Shikhara commonly denotes the superstructure above the sanctum in Nagara-style temples.
Gopuram | What is the monumental entrance tower characteristic of many south Indian temple complexes called? | A gopuram is a gateway tower, distinct from the sanctum’s superstructure.
Mandapa | What is a pillared hall within a temple complex called? | A mandapa is a hall used for assembly, ritual or approach to the sanctum.
Garbhagriha | What is the innermost sanctum housing the principal deity called? | The garbhagriha is the sacred inner chamber containing the principal image or emblem.
''')
    h('Early medieval sources', '''
Harshacharita | Which Sanskrit biography of Harsha was written by Banabhatta? | Banabhatta composed Harshacharita, a courtly biography whose praise must be read critically as historical evidence.
Rajatarangini | Which work by Kalhana narrates the history of Kashmir’s rulers? | Kalhana’s Rajatarangini is a twelfth-century Sanskrit narrative of Kashmir’s dynastic history.
Kitab-ul-Hind | Which work by Al-Biruni examined Indian society, learning and religious traditions? | Al-Biruni’s Kitab-ul-Hind records an analytical study of Indian knowledge and customs.
Rihla | Which travel account is associated with Ibn Battuta? | Ibn Battuta’s Rihla records his extensive travels, including time at the court of Muhammad bin Tughlaq.
''')
    h('Sultanate administration', '''
Iqta | What term described a revenue assignment used to support officials and soldiers under the Delhi Sultanate? | An iqta assigned revenue rights rather than private ownership of the land itself, subject to state control.
Muqti | What was the holder or administrator of an iqta commonly called? | A muqti administered an iqta, collected assigned revenues and met specified military or administrative obligations.
Diwan-i-arz | Which Sultanate department was associated with military administration? | The diwan-i-arz handled military organisation, including inspection and related administrative functions.
Diwan-i-wizarat | Which Sultanate department was principally concerned with finance? | The diwan-i-wizarat managed financial administration under the wazir.
''')
    h('Vijayanagara and Bahmani history', '''
Harihara and Bukka | Which brothers are traditionally associated with founding the Vijayanagara kingdom? | Harihara and Bukka established the Sangama dynasty at the beginning of Vijayanagara’s history.
Krishnadevaraya | Which Vijayanagara ruler composed the Telugu work Amuktamalyada? | Krishnadevaraya of the Tuluva dynasty is associated with Amuktamalyada and extensive literary patronage.
Talikota | At which battle in 1565 did a coalition of Deccan sultanates defeat the Vijayanagara army? | The battle of Talikota in 1565 severely weakened Vijayanagara and was followed by destruction at its capital.
Hasan Gangu | Which ruler, also known as Alauddin Bahman Shah, founded the Bahmani kingdom? | Hasan Gangu assumed the title Alauddin Bahman Shah when establishing Bahmani rule in 1347.
''')
    h('Mughal institutions', '''
Mansab | What Mughal term denoted an official’s graded rank? | A mansab expressed an official’s rank and associated service responsibilities in Mughal administration.
Jagir | What was a Mughal revenue assignment used to remunerate an officer called? | A jagir assigned revenues to an officer; it was generally transferable and did not automatically confer permanent ownership.
Zat | In the mansabdari system, which rank component indicated personal status? | Zat denoted a mansabdar’s personal rank and status within the hierarchy.
Sawar | Which mansab component related to the cavalry contingent an officer was expected to maintain? | Sawar specified the cavalry obligation or rank component associated with mounted service.
''')
    h('Mughal texts', '''
Baburnama | Which memoir was originally written by Babur in Chagatai Turkish? | Baburnama records Babur’s experiences and observations in Chagatai Turkish.
Akbarnama | Which work by Abul Fazl narrates Akbar’s reign? | Abul Fazl’s Akbarnama presents the history of Akbar’s reign within a courtly imperial perspective.
Ain-i-Akbari | Which part of Abul Fazl’s work describes Mughal administration, regulations and statistical information? | Ain-i-Akbari describes administrative arrangements, imperial regulations and aspects of social and economic life.
Tuzuk-i-Jahangiri | Which memoir is associated with the Mughal emperor Jahangir? | Tuzuk-i-Jahangiri records Jahangir’s reign and observations in autobiographical form.
''')
    h('Sufi vocabulary', '''
Khanqah | What was a Sufi residential and teaching centre called? | A khanqah provided a space for Sufi teaching, communal life and contact with followers.
Silsila | What term denotes a Sufi spiritual lineage? | A silsila traces a chain of spiritual transmission linking teachers and disciples.
Dargah | What term refers to the shrine or tomb of a Sufi saint? | A dargah is the shrine centred on a Sufi saint’s tomb and may attract devotional visitation.
Sama | What term is used for devotional listening, often involving music, in some Sufi traditions? | Sama is a devotional listening practice; its form and acceptance vary among Sufi traditions.
''')
    h('Regional devotional figures', '''
Basavanna | Which twelfth-century reformer is associated with the Lingayat movement and vachana literature? | Basavanna opposed caste hierarchy and promoted devotion expressed through Kannada vachanas.
Andal | Which woman Alvar poet is celebrated for Tamil devotional verses to Vishnu? | Andal is a woman Alvar saint associated with passionate Tamil devotion to Vishnu.
Tukaram | Which Marathi saint-poet is known for abhangas devoted to Vithoba? | Tukaram composed abhangas within Maharashtra’s Varkari devotional tradition.
Lal Ded | Which Kashmiri mystic is associated with poetic sayings called vakhs? | Lal Ded’s vakhs express spiritual reflection in the Kashmiri language.
''')
    h('Maratha institutions', '''
Shivaji | Which Maratha ruler was crowned at Raigad in 1674? | Shivaji’s coronation at Raigad in 1674 asserted an independent Maratha kingship.
Ashtapradhan | What was the council of eight principal ministers associated with Shivaji’s administration called? | The Ashtapradhan was the council of eight principal offices in Shivaji’s administrative system.
Chauth | What levy was conventionally assessed at one-fourth of revenue by the Marathas? | Chauth was a levy of one-fourth, associated with Maratha claims over territories beyond their direct core administration.
Sardeshmukhi | What additional Maratha claim was conventionally assessed at ten percent of revenue? | Sardeshmukhi was an additional ten-percent claim, justified through the status of superior revenue headship.
''')
    h('European entry and commerce', '''
Vasco da Gama | Which Portuguese navigator reached Calicut by sea in 1498? | Vasco da Gama reached Calicut in 1498, establishing a direct maritime route from Europe around Africa.
English East India Company | Which company received a royal charter from Elizabeth I in 1600? | The English East India Company received its charter in 1600 for trading in the East.
Dutch East India Company | Which company formed in 1602 is commonly known by the initials VOC? | The Dutch East India Company, or VOC, was established in 1602 as a major Asian trading corporation.
French East India Company | Which company was formed in 1664 under Colbert’s initiative? | The French East India Company was founded in 1664 during Louis XIV’s reign with Colbert’s support.
''')
    h('Company expansion', '''
Plassey | Which 1757 battle helped the East India Company establish political influence in Bengal? | At Plassey in 1757 the Company defeated Siraj-ud-Daulah, with defections and conspiracy playing a decisive role.
Buxar | Which 1764 battle strengthened the Company against the combined forces of Mir Qasim, Shuja-ud-Daulah and Shah Alam II? | The Company’s victory at Buxar strengthened its military and political position in eastern India.
Diwani grant | What right did the Company obtain over Bengal, Bihar and Orissa from Shah Alam II in 1765? | The Diwani grant authorised the Company to collect revenue in Bengal, Bihar and Orissa.
Doctrine of Lapse | Which annexation policy was associated with Dalhousie and succession disputes in princely states? | The Doctrine of Lapse denied recognition of some adopted successors and was used to annex states.
''')
    h('Resistance before 1857', '''
Santhal rebellion | Which 1855–56 uprising was led by Sidhu and Kanhu against exploitation in eastern India? | Sidhu and Kanhu led the Santhal rebellion against oppressive intermediaries and colonial arrangements.
Kol uprising | Which 1831–32 uprising occurred in the Chotanagpur region against outsiders and exploitative changes? | The Kol uprising challenged changes in land control and the influence of outsiders in Chotanagpur.
Paika rebellion | Which 1817 uprising in Odisha is associated with Bakshi Jagabandhu? | The Paika rebellion brought together traditional militia groups and others opposing colonial changes in Odisha.
Indigo revolt | Which 1859–60 movement in Bengal opposed coercive cultivation by European planters? | Indigo cultivators in Bengal resisted the coercive system that forced them to grow indigo on unfavourable terms.
''')
    h('1857 leaders and centres', '''
Bahadur Shah Zafar | Which Mughal emperor became the symbolic leader of the 1857 uprising in Delhi? | Rebels in Delhi proclaimed Bahadur Shah Zafar as their symbolic sovereign in 1857.
Rani Lakshmibai | Which leader is closely associated with the resistance at Jhansi in 1857–58? | Rani Lakshmibai led resistance linked to Jhansi and died fighting in 1858.
Begum Hazrat Mahal | Which leader resisted British rule in Awadh during the 1857 uprising? | Begum Hazrat Mahal helped lead the resistance in Awadh and supported her son’s claim in Lucknow.
Kunwar Singh | Which elderly landholder led the 1857 rebellion around Jagdishpur in Bihar? | Kunwar Singh of Jagdishpur became a major leader of the uprising in Bihar.
''')
    h('Nineteenth-century education and reform', '''
Ishwar Chandra Vidyasagar | Which reformer campaigned strongly for Hindu widow remarriage? | Vidyasagar advocated widow remarriage and women’s education, contributing to reform debates before the 1856 legislation.
Savitribai Phule | Which pioneer worked with Jyotirao Phule to expand girls’ education in Pune? | Savitribai Phule was a pioneering teacher and reformer who worked for girls’ education and against caste oppression.
Sir Syed Ahmad Khan | Which reformer founded the Muhammadan Anglo-Oriental College at Aligarh? | Sir Syed Ahmad Khan promoted modern education through the institution that later developed into Aligarh Muslim University.
Pandita Ramabai | Which reformer founded Sharada Sadan to support women’s education? | Pandita Ramabai worked for women’s education and established Sharada Sadan for women, including widows.
''')
    h('Reform organisations', '''
Prarthana Samaj | Which reform organisation was founded in Bombay in 1867 and associated with Atmaram Pandurang? | Prarthana Samaj promoted religious and social reform in western India, including reform of social customs.
Theosophical Society | Which organisation associated with Blavatsky and Olcott later established its headquarters at Adyar? | The Theosophical Society developed a major centre at Adyar and promoted study of spiritual and philosophical traditions.
Servants of India Society | Which organisation was founded by Gopal Krishna Gokhale in 1905? | Gokhale founded the Servants of India Society to train people for public service and national work.
SNDP Yogam | Which Kerala organisation is associated with the social reform ideals of Narayana Guru? | SNDP Yogam advanced education and social reform among disadvantaged communities, drawing on Narayana Guru’s ideals.
''')
    h('Early nationalism', '''
Dadabhai Naoroji | Which nationalist developed a prominent explanation of colonial poverty through the drain of wealth? | Dadabhai Naoroji argued that resources and income were drained from India without an equivalent return.
W.C. Bonnerjee | Who presided over the first session of the Indian National Congress in 1885? | W.C. Bonnerjee presided over the first Congress session held in Bombay in 1885.
A.O. Hume | Which retired civil servant helped organise the founding of the Indian National Congress? | A.O. Hume helped bring together the political leaders who founded the Congress in 1885.
Gopal Krishna Gokhale | Which Moderate leader stressed constitutional methods and became a political mentor to Gandhi? | Gokhale advocated constitutional reform and public service and influenced Gandhi’s understanding of Indian politics.
''')
    h('Nationalist newspapers', '''
Kesari | Which Marathi newspaper was associated with Bal Gangadhar Tilak? | Kesari was Tilak’s Marathi newspaper and a major vehicle of nationalist opinion.
Amrita Bazar Patrika | Which newspaper associated with the Ghosh brothers became a prominent nationalist publication? | Amrita Bazar Patrika became an influential nationalist newspaper under the Ghosh family’s leadership.
Young India | Which English-language journal did Gandhi use to communicate his political and ethical views? | Gandhi used Young India to explain his ideas about satyagraha, reform and national politics.
Al-Hilal | Which Urdu journal was launched by Abul Kalam Azad in 1912? | Abul Kalam Azad founded Al-Hilal to discuss political, religious and nationalist questions.
''')
    h('Constitutional legislation', '''
Pitt’s India Act, 1784 | Which Act created a Board of Control for the political affairs of the East India Company? | Pitt’s India Act established the Board of Control, increasing British government supervision over Company affairs.
Charter Act, 1813 | Which Act ended the Company’s trade monopoly in India while retaining specified exceptions for tea and China trade? | The Charter Act of 1813 opened much of Indian trade to other British merchants while retaining tea and China exceptions.
Charter Act, 1833 | Which Act ended the Company’s remaining commercial role and made it primarily an administrative body? | The Charter Act of 1833 ended the Company’s commercial functions and centralised legislative authority.
Government of India Act, 1935 | Which Act introduced provincial autonomy in British India? | The Government of India Act, 1935 provided provincial autonomy and a proposed federation that did not fully take effect.
''')
    h('Repression and resistance', '''
Vernacular Press Act | Which 1878 law sought to control critical writing in Indian-language newspapers? | The Vernacular Press Act targeted Indian-language publications and became a symbol of colonial restrictions on expression.
Ilbert Bill controversy | Which 1883 controversy concerned the authority of Indian judges to try European British subjects? | The Ilbert Bill controversy revealed racial opposition to giving Indian judges jurisdiction over European defendants.
Rowlatt Act | Which 1919 law extended exceptional powers of detention without ordinary trial? | The Rowlatt Act continued repressive wartime-style powers and provoked widespread protest in 1919.
Sedition | Which colonial legal category was used to prosecute speech alleged to generate disaffection toward the government? | Colonial sedition provisions were repeatedly used against nationalist expression; the historical category must be distinguished from current law.
''')
    h('Home Rule and revolutionary organisation', '''
Annie Besant | Which leader launched a Home Rule League in 1916 alongside Tilak’s separate league? | Annie Besant’s Home Rule League campaigned for self-government within the contemporary constitutional debate.
Ghadar Party | Which overseas revolutionary organisation was associated with Indian migrants on North America’s Pacific coast? | The Ghadar movement mobilised overseas Indians for an armed challenge to British colonial rule.
Hindustan Socialist Republican Association | Which revolutionary organisation was associated with Bhagat Singh and Chandrashekhar Azad in the late 1920s? | The HSRA combined revolutionary struggle against colonial rule with an increasingly socialist political outlook.
Anushilan Samiti | Which revolutionary network emerged in Bengal and combined physical training with anti-colonial activity? | Anushilan Samiti was a Bengal revolutionary network associated with organisation, training and anti-colonial action.
''')
    h('Gandhian methods', '''
Satyagraha | Which method seeks to resist injustice through adherence to truth and non-violent pressure? | Satyagraha combines truth-seeking, non-violence and willingness to bear suffering in resisting injustice.
Swadeshi | What principle encourages the use and development of locally produced goods? | Swadeshi promotes indigenous production and consumption as a form of economic and political self-reliance.
Constructive programme | What term describes Gandhi’s work on activities such as village industries, sanitation and removal of untouchability? | The constructive programme sought social change and community capacity alongside direct political campaigns.
Trusteeship | Which Gandhian idea treats holders of wealth as responsible for using it for broader social welfare? | Trusteeship proposes moral responsibility in the use of wealth rather than unrestricted private entitlement.
''')
    h('Negotiations and commissions', '''
Simon Commission | Which constitutional commission appointed in 1927 had no Indian member? | The Simon Commission’s all-British composition led to widespread protests and boycott in India.
Nehru Report | Which 1928 constitutional proposal was prepared by a committee chaired by Motilal Nehru? | The Nehru Report proposed a constitutional framework, including dominion status, through an Indian-led committee.
Gandhi–Irwin Pact | Which 1931 agreement led Gandhi to attend the Second Round Table Conference? | The Gandhi–Irwin Pact suspended civil disobedience under agreed conditions and enabled Congress participation in the conference.
Poona Pact | Which 1932 agreement replaced separate electorates for the Depressed Classes with reserved seats in joint electorates? | The Poona Pact between Gandhi and Ambedkar’s representatives established reserved seats within joint electorates.
''')
    h('Final decade of colonial rule', '''
Cripps Mission | Which 1942 mission offered a post-war constitutional settlement but failed to secure agreement? | The Cripps Mission proposed post-war constitutional arrangements that major Indian political groups found unacceptable.
Cabinet Mission | Which 1946 mission proposed a constitutional framework with a union and provincial groupings? | The Cabinet Mission sought a constitutional settlement while attempting to preserve a united India.
Mountbatten Plan | Which June 1947 plan accepted partition as the basis of transfer of power? | The Mountbatten Plan of 3 June 1947 outlined partition and arrangements for transfer of power.
Indian Independence Act | Which British statute of 1947 provided for the creation of the two independent dominions? | The Indian Independence Act, 1947 provided for the dominions of India and Pakistan and the end of British rule.
''')
    h('Subhas Chandra Bose and wartime politics', '''
Forward Bloc | Which political organisation was founded by Subhas Chandra Bose in 1939? | Bose founded the Forward Bloc after differences within the Congress leadership.
Indian National Army | Which armed force sought Indian independence with support from Axis powers in Southeast Asia? | The Indian National Army sought to fight British rule from Southeast Asia and became strongly associated with Bose.
Rani of Jhansi Regiment | Which INA unit was an all-women regiment led by Lakshmi Sahgal? | The Rani of Jhansi Regiment was the INA’s women’s unit, commanded by Lakshmi Sahgal.
Royal Indian Navy revolt | Which 1946 protest began among naval ratings in Bombay and spread to other centres? | The Royal Indian Navy revolt expressed grievances among ratings and wider anti-colonial discontent in 1946.
''')
    h('Women in the national movement', '''
Sarojini Naidu | Who became the first Indian woman to preside over the Indian National Congress? | Sarojini Naidu presided over the Congress at Kanpur in 1925, becoming its first Indian woman president.
Aruna Asaf Ali | Which leader hoisted the Congress flag at Gowalia Tank during the launch of Quit India? | Aruna Asaf Ali became a prominent symbol of the Quit India Movement through her role at Gowalia Tank.
Usha Mehta | Which activist helped run the underground Congress Radio during Quit India? | Usha Mehta helped organise clandestine radio broadcasts during the 1942 movement.
Kasturba Gandhi | Which activist worked with Gandhi in South Africa and India and died in detention at the Aga Khan Palace? | Kasturba Gandhi participated in social and political campaigns and died while detained in 1944.
''')
    h('Agrarian movements of the twentieth century', '''
Bardoli satyagraha | Which 1928 movement against a revenue increase was led by Vallabhbhai Patel? | Bardoli cultivators resisted an increased revenue assessment under Patel’s leadership.
Tebhaga movement | Which Bengal sharecroppers’ movement demanded two-thirds of the crop for cultivators? | Tebhaga demanded that sharecroppers retain two-thirds of the produce instead of the customary smaller share.
Eka movement | Which early-1920s peasant movement in parts of Awadh stressed unity against high rents and oppression? | The Eka movement mobilised peasants in parts of Awadh against exploitative rents and related practices.
Moplah rebellion | Which 1921 uprising occurred in the Malabar region? | The Moplah rebellion occurred in Malabar amid agrarian grievances, religious mobilisation and anti-colonial tensions.
''')
    h('Labour and left organisations', '''
All India Trade Union Congress | Which national trade-union federation was founded in 1920? | The AITUC was founded in 1920 as an all-India organisation of trade unions.
Congress Socialist Party | Which socialist group formed within the Congress in 1934? | The Congress Socialist Party organised socialist currents within the Congress in 1934.
All India Kisan Sabha | Which national peasant organisation was formed in 1936? | The All India Kisan Sabha brought together peasant demands at a national level from 1936.
Meerut Conspiracy Case | Which colonial prosecution beginning in 1929 targeted trade-unionists and communist activists? | The Meerut Conspiracy Case prosecuted labour and communist activists and drew international attention.
''')
    h('Constituent Assembly beginnings', '''
9 December 1946 | On which date did the Constituent Assembly first meet? | The Constituent Assembly first met on 9 December 1946, before independence.
Sachchidananda Sinha | Who served as the temporary chairman at the Assembly’s first meeting? | Sachchidananda Sinha served as temporary chairman before the permanent president was elected.
Rajendra Prasad | Who was elected permanent President of the Constituent Assembly? | Rajendra Prasad presided over the Constituent Assembly during the framing of the Constitution.
Objectives Resolution | What resolution moved by Jawaharlal Nehru set out the Assembly’s broad constitutional goals? | The Objectives Resolution stated guiding aims and later influenced the Preamble’s principles.
''')
    h('Integration and social change after independence', '''
V.P. Menon | Which senior official worked closely with Patel on the integration of princely states? | V.P. Menon assisted Patel in negotiating and organising the accession and integration of princely states.
Bhoodan movement | Which movement initiated by Vinoba Bhave sought voluntary gifts of land for the landless? | Bhoodan encouraged landowners to donate land voluntarily for redistribution to landless people.
Community Development Programme | Which programme launched in 1952 sought broad rural development through coordinated local activities? | The Community Development Programme aimed to improve rural infrastructure, agriculture and social services.
Operation Flood | Which programme is associated with expanding India’s cooperative dairy network? | Operation Flood linked milk producers and markets through cooperatives and helped expand milk production and distribution.
''')
    h('Classical dance traditions', '''
Bharatanatyam | Which classical dance form is strongly associated with Tamil Nadu? | Bharatanatyam developed from dance traditions of Tamil Nadu and uses codified movement and expressive storytelling.
Kathak | Which classical dance form is associated with north Indian storytelling and intricate footwork? | Kathak combines narrative expression, spins and rhythmic footwork within north Indian traditions.
Kathakali | Which Kerala dance-drama is known for elaborate makeup and costume? | Kathakali presents dramatic stories through stylised movement, facial expression and striking costumes.
Odissi | Which classical dance form is associated with Odisha and the tribhanga posture? | Odissi is rooted in Odisha’s performance traditions and uses characteristic curved postures including tribhanga.
''')
    h('Music traditions', '''
Hindustani music | What is the principal classical music tradition of northern India called? | Hindustani classical music developed in northern India through diverse regional and courtly influences.
Carnatic music | What is the principal classical music tradition of southern India called? | Carnatic music is the major southern classical tradition, with strong emphasis on composed works and improvisation.
Raga | What melodic framework organises notes and characteristic phrases in Indian classical music? | A raga provides a melodic framework with characteristic note relationships, phrases and expressive possibilities.
Tala | What cyclical rhythmic framework structures time in Indian classical music? | Tala organises rhythm into repeating cycles with subdivisions and accented positions.
''')
    h('Traditional painting', '''
Madhubani | Which painting tradition is associated with the Mithila region? | Madhubani painting is associated with Mithila and uses strong patterns and themes drawn from life and belief.
Warli | Which western Indian painting tradition is known for simple geometric human and animal figures? | Warli painting uses stylised geometric forms to depict community life, ritual and nature.
Pattachitra | Which Odisha painting tradition is associated with detailed cloth-based narrative images? | Odisha Pattachitra uses prepared cloth surfaces and detailed narrative or devotional imagery.
Kalamkari | Which textile art uses hand-drawn or block-printed designs, traditionally with natural dyes? | Kalamkari decorates textiles through drawing or printing and elaborate dyeing processes.
''')
    h('Heritage monuments beyond Telangana', '''
Sanchi | Which Buddhist site in Madhya Pradesh is famous for its stupas and carved gateways? | Sanchi preserves stupas and richly carved gateways illustrating Buddhist themes.
Ajanta | Which Maharashtra cave complex is especially celebrated for ancient Buddhist mural paintings? | Ajanta contains Buddhist rock-cut caves with important murals and sculptures.
Konark | Which Odisha temple is conceived as a monumental chariot of the Sun God? | Konark’s Sun Temple uses a chariot form with carved wheels and horses.
Mahabalipuram | Which Pallava coastal site is noted for monolithic rathas and the Shore Temple? | Mahabalipuram preserves Pallava rock-cut and structural monuments on the Tamil coast.
''')
    h('Historical languages and scripts', '''
Brahmi | Which script was used for most Ashokan inscriptions in the Indian subcontinent? | Brahmi was used in most Ashokan inscriptions and became an ancestor of many later Indian scripts.
Kharosthi | Which ancient script, used in the northwest, was generally written from right to left? | Kharosthi was used in the northwest and was written from right to left, unlike Brahmi’s usual direction.
Prakrit | What broad label covers several Middle Indo-Aryan languages used in early inscriptions and literature? | Prakrit refers to a group of Middle Indo-Aryan languages distinct from classical Sanskrit.
Persian | Which language became prominent in administration and high literary culture under many medieval Indian courts? | Persian served as an important language of administration and courtly culture under the Sultanates and Mughals.
''')
    h('Trade and urban vocabulary', '''
Shreni | What term commonly denotes a guild of merchants or artisans in early Indian history? | Shrenis were associations of people engaged in particular trades or crafts.
Hundi | What instrument enabled credit and transfer of funds through merchant networks? | A hundi was a negotiable financial instrument used in trade and remittance networks.
Caravanserai | What was a lodging and service station for travelling merchants and caravans called? | A caravanserai provided shelter and facilities along trade routes.
Entrepot | What term describes a trading centre where goods are received and redistributed? | An entrepot concentrates trade by receiving goods for storage, exchange or onward shipment.
''')
    h('Historical interpretation', '''
Primary source | A letter written by a participant at the time of an event is ordinarily classified as what? | A primary source provides evidence originating in the period or from direct participation, though it still requires criticism.
Secondary source | A modern historian’s analysis synthesising earlier records is ordinarily classified as what? | A secondary source interprets evidence from other sources to explain the past.
Anachronism | What error occurs when a historian imposes an institution or idea from a later age onto an earlier period? | Anachronism places something outside its proper historical context and can distort interpretation.
Corroboration | What method compares independent sources to check a historical claim? | Corroboration tests a claim by comparing evidence from different, preferably independent, sources.
''')
    h('Cultural terms and forms', '''
Yakshagana | Which traditional dance-drama form is strongly associated with coastal Karnataka? | Yakshagana combines music, dialogue, costume and dance in a dramatic performance tradition.
Chhau | Which eastern Indian dance tradition includes masked forms in Purulia and Seraikella? | Chhau has regional styles in eastern India, with masks used in some but not all forms.
Koodiyattam | Which Kerala tradition performs Sanskrit theatre through highly codified expression? | Koodiyattam is a Sanskrit theatre tradition of Kerala with detailed expressive techniques.
Puppetry | What performance form animates figures controlled by strings, rods, shadows or hands? | Puppetry uses manipulated figures to narrate stories through several regional techniques.
''')
    h('Historical science and knowledge', '''
Charaka Samhita | Which medical text is strongly associated with the Ayurvedic tradition of internal medicine? | Charaka Samhita discusses health, disease and treatment within the Ayurvedic tradition.
Sushruta Samhita | Which medical text is particularly noted for discussions of surgery? | Sushruta Samhita includes descriptions of surgical procedures and instruments.
Brahmagupta | Which mathematician authored Brahmasphutasiddhanta and discussed arithmetic involving zero? | Brahmagupta’s mathematical and astronomical work includes rules for operations with zero and negative numbers.
Bhaskara II | Which mathematician wrote Lilavati and Bijaganita as parts of his mathematical work? | Bhaskara II’s works include Lilavati on arithmetic and Bijaganita on algebra.
''')

    h('Women and literary nationalism', '''
Vande Mataram | Which song from Bankim Chandra Chattopadhyay’s Anandamath became a major nationalist symbol? | Vande Mataram appears in Anandamath and became an influential expression of nationalist feeling.
Jana Gana Mana | Which composition by Rabindranath Tagore was adopted as India’s National Anthem? | Jana Gana Mana was composed by Tagore and adopted as the National Anthem in 1950.
Hind Swaraj | In which 1909 work did Gandhi criticise modern civilisation and discuss self-rule? | Hind Swaraj presents Gandhi’s ideas about civilisation, non-violence and the meaning of self-rule.
The Discovery of India | Which book did Jawaharlal Nehru write during imprisonment at Ahmednagar Fort? | Nehru wrote The Discovery of India while imprisoned during the 1940s, reflecting on India’s history and culture.
''')
    add('Indian History','Historical civic milestones','''
National Planning Committee | Which planning body was established by the Congress in 1938 under Jawaharlal Nehru’s chairmanship? | The National Planning Committee began organised discussion of India’s future economic development before independence.
Vaikom satyagraha | Which 1924–25 struggle in Travancore challenged caste restrictions on access to roads near a temple? | Vaikom satyagraha challenged exclusion from public approach roads and became an important anti-caste campaign.
Salt Satyagraha | Which 1930 campaign challenged the colonial monopoly on salt? | Salt Satyagraha used defiance of the salt law as a mass campaign against colonial rule.
Swadeshi boycott | Which method urged rejection of imported goods in favour of indigenous products? | Swadeshi boycott linked consumer choices to national economic self-reliance.
''',take=2)

    # 68 further society/environment applications; all scenarios are distinct.
    s('Social resources', '''
Human capital | A community improves literacy, health and job skills. Which form of productive capacity is it strengthening? | Human capital consists of people’s knowledge, skills and health that enable productive and social participation.
Social capital | Neighbours build trusted networks that help them coordinate during emergencies. What resource is strengthened? | Social capital consists of networks, trust and norms that support cooperation and collective action.
Upward social mobility | A person moves from a disadvantaged occupational position to one with greater status and opportunity. What change is illustrated? | Upward social mobility is movement to a higher social or economic position, within or across generations.
Intergenerational mobility | A study compares parents’ occupations with those of their adult children. Which type of mobility is being studied? | Intergenerational mobility compares social or economic positions between parents and children.
''')
    s('Understanding deprivation', '''
Absolute poverty | A household cannot meet a defined minimum standard of basic needs. Which poverty concept best fits? | Absolute poverty is deprivation relative to a specified basic-needs threshold.
Relative poverty | A household has far fewer resources than the typical household in its society. Which poverty concept best fits? | Relative poverty concerns disadvantage compared with the living standards of a particular society.
Multidimensional poverty | A survey combines deprivation in schooling, health and living conditions rather than income alone. What approach is used? | Multidimensional poverty measures several overlapping forms of deprivation.
Poverty vulnerability | A household is above a poverty threshold but a small health or crop shock could push it below. What condition is highlighted? | Vulnerability to poverty concerns the risk of falling into deprivation when adverse events occur.
''')
    s('Gender and work', '''
Gender stereotyping | A teacher says that mechanical work is naturally suitable only for boys. Which barrier is illustrated? | Gender stereotyping assigns abilities or roles on the basis of gender rather than individual capability.
Glass ceiling | Qualified women enter an organisation but face an invisible barrier to its highest leadership roles. What is this called? | A glass ceiling is an informal barrier preventing advancement to senior positions despite qualifications.
Unpaid care work | Time spent caring for children and dependent adults without wages belongs to which category? | Unpaid care work sustains households and society even when it is not remunerated.
Gender-responsive budgeting | A government reviews how spending affects women and men differently. What budgeting approach is it using? | Gender-responsive budgeting examines the gender effects of revenues and expenditure to improve fairness and outcomes.
''')
    s('Education inclusion scenarios', '''
Language support | A child understands mathematics but cannot yet follow the classroom’s unfamiliar language. Which intervention most directly addresses the barrier? | Language support connects learning to a language the child understands while building proficiency in the classroom language.
Bridge learning | A child returns to school after a long interruption and receives targeted instruction to fill learning gaps. What is this support called? | Bridge learning helps a returning learner regain foundational knowledge needed to rejoin regular instruction.
Accessible learning material | A learner with low vision receives large-print and screen-reader-compatible books. Which intervention is illustrated? | Accessible material presents the same learning content in formats a learner can perceive and use.
Retention support | A school follows up repeated absence and works with families to keep children enrolled. What outcome is it primarily supporting? | Retention support reduces the barriers that lead students to leave school before completing their education.
''')
    s('Disability and design', '''
Reasonable accommodation | A qualified applicant is given an appropriate individual adjustment to participate in an assessment. Which principle is illustrated? | Reasonable accommodation makes suitable adjustments for a person’s needs without imposing a disproportionate burden.
Universal design | A new public building is planned from the beginning for use by people with varied abilities. Which approach is this? | Universal design aims to make environments usable by as many people as possible without later specialised adaptation.
Assistive technology | A person uses a hearing aid or screen reader to perform everyday tasks. What category do these devices belong to? | Assistive technology supports functioning and participation by compensating for specific barriers or impairments.
Environmental barrier | A wheelchair user can perform a job but cannot enter the office because the entrance has only stairs. What is the immediate obstacle? | The obstacle is in the built environment, rather than an inability to perform the work itself.
''')
    s('Community decision-making', '''
Participation | Residents help identify priorities before a village project is selected. Which governance principle is illustrated? | Participation gives affected people a meaningful role in decisions that shape their lives.
Transparency | A local body publishes its project costs and procurement decisions in an understandable format. Which principle is strengthened? | Transparency makes relevant information visible and understandable so decisions can be scrutinised.
Accountability | Officials must explain a project’s failure and face a defined corrective process. Which principle is being applied? | Accountability requires decision-makers to justify actions and accept appropriate consequences or correction.
Social audit | Community members compare public-work records with actual work and publicly discuss discrepancies. What process is this? | A social audit uses public participation to examine implementation, records and outcomes of a programme.
''')
    s('Interpreting social statistics', '''
Selection bias | An unemployment survey interviews only people attending a job fair and generalises to all adults. What is the main problem? | Job-fair attendees are not a representative sample of all adults, creating selection bias.
Confounding | A study links umbrella use with illness without considering that rainy weather affects both. What problem is illustrated? | A confounding factor can influence both measured variables and create a misleading apparent relationship.
Denominator mismatch | One report counts accidents per vehicle while another counts them per resident. Why are their rates not directly comparable? | Rates based on different denominators measure different risks and need a common base for comparison.
Survivorship bias | A study of business success examines only firms still operating and ignores those that closed. What bias may result? | Survivorship bias omits failed or missing cases, potentially overstating the factors associated with success.
''')
    s('Migration and settlement', '''
Push factor | Repeated crop failure encourages a household to leave its village. What type of migration influence is this? | A push factor is an adverse condition at the place of origin that encourages departure.
Pull factor | Better educational opportunities attract a family to a city. What type of migration influence is this? | A pull factor is an appealing condition at the destination that attracts migrants.
Remittance | A worker living elsewhere sends part of their earnings to family in the home village. What is this transfer called? | Remittances are transfers sent by migrants to people in their place of origin.
Circular migration | A worker repeatedly moves between a home village and a city for temporary employment. What pattern is this? | Circular migration involves repeated movement between places rather than a single permanent relocation.
''')
    s('Information integrity', '''
Phishing | A message impersonates a bank and asks a student to enter a password on a lookalike website. What technique is being used? | Phishing deceives people into disclosing sensitive information by impersonating a trusted source.
Deepfake | A fabricated video makes a public figure appear to say words they never spoke. What technology-related manipulation is illustrated? | A deepfake synthetically alters or generates audiovisual content to imitate a person or event.
Lateral reading | A student leaves an unfamiliar website to examine what independent reliable sources say about it. What verification technique is this? | Lateral reading checks a source through independent sources rather than relying only on its own claims.
Context manipulation | An authentic photograph of an old flood is falsely labelled as today’s event. What is misleading about the post? | The image may be authentic, but the false time or place changes its meaning and misleads the audience.
''')
    s('Personal-data protection', '''
Data minimisation | A service collects only the information needed to provide its stated function. Which privacy practice is illustrated? | Data minimisation limits collection to information necessary for a defined purpose.
Informed consent | A participant receives a clear explanation of data use and voluntarily agrees before collection. Which practice is illustrated? | Informed consent requires understandable information and a genuine voluntary choice about participation.
Two-factor authentication | A login requires a password and a separate verification factor. Which security measure is being used? | Two-factor authentication combines independent categories of proof to reduce reliance on a password alone.
Least privilege | A volunteer receives access only to the records required for their assigned task. Which access-control principle is used? | Least privilege restricts access to the minimum permissions needed for a legitimate task.
''')
    s('Public integrity', '''
Conflict of interest | An official evaluates a contract bid from a company owned by a close relative. What concern should be disclosed? | A conflict of interest arises when private interests could improperly influence an official responsibility.
Nepotism | A manager appoints an unqualified relative over better-qualified applicants because of family ties. What practice is illustrated? | Nepotism gives preference to relatives on the basis of relationship rather than merit or fair procedure.
Bribery | A person offers an official money to obtain an improper favour. What misconduct is illustrated? | Bribery offers or accepts an improper benefit to influence a decision or action.
Whistleblowing | An employee reports credible evidence of serious organisational wrongdoing through an appropriate channel. What action is this? | Whistleblowing exposes wrongdoing to a person or body able to address it, ideally with protection against retaliation.
''')
    s('Air and noise pollution applications', '''
Fine particulate exposure | A roadside air monitor records high PM2.5 during combustion-heavy traffic. Which health-related environmental exposure is it tracking? | PM2.5 consists of fine particles small enough to penetrate deeply into the respiratory system.
Ground-level ozone formation | A hot sunny city has nitrogen oxides and volatile organic compounds reacting in the air. Which secondary pollutant can result? | Ground-level ozone can form through sunlight-driven reactions involving nitrogen oxides and volatile organic compounds.
Acid deposition | Sulfur dioxide and nitrogen oxides form acids that reach land and water. Which environmental process is this? | Acid deposition transfers acidic compounds from the atmosphere through wet or dry deposition.
Noise pollution | Persistent excessive sound from machinery disrupts sleep and communication. What environmental problem is illustrated? | Noise pollution is unwanted or harmful sound that can affect well-being, communication and hearing.
''')
    s('Climate responses', '''
Mitigation | A city replaces high-emission electricity generation with low-emission sources. Which climate response is it pursuing? | Mitigation reduces greenhouse-gas emissions or enhances their removal to limit climate change.
Adaptation | A coastal community raises critical equipment above expected flood levels. Which climate response is it pursuing? | Adaptation adjusts systems to actual or expected climate effects to reduce harm.
Carbon sink | A growing forest absorbs more carbon dioxide than it releases over a defined period. What role does it play? | A carbon sink has a net uptake of carbon over the period considered.
Maladaptation | A flood barrier protects one neighbourhood but substantially increases flood risk for a poorer neighbouring area. What problem can this represent? | Maladaptation is an intervention that unintentionally increases vulnerability or shifts risk onto others.
''')
    s('Managing shared resources', '''
Common-pool resource | A village groundwater aquifer is difficult to exclude users from, but one user’s extraction reduces water available to others. What resource type is it? | Common-pool resources combine difficulty of exclusion with subtractable use.
Overharvesting | Fish are removed faster than the population can replenish itself. What pressure is illustrated? | Overharvesting exceeds the regenerative capacity of a biological resource.
Sustainable yield | A forest plan limits extraction to a level consistent with long-term regeneration. What target is it pursuing? | Sustainable yield aims to maintain resource productivity over time rather than exhaust the stock.
Collective management | Water users agree on shared extraction rules and monitoring to protect their aquifer. What management approach is illustrated? | Collective management creates agreed rules and responsibilities among users of a shared resource.
''')
    s('Disaster action scenarios', '''
Early warning | Authorities detect a dangerous storm and communicate a timely, understandable alert to exposed communities. What capacity is demonstrated? | Early warning links risk detection, communication and readiness so people can act before harm occurs.
Evacuation | Residents are moved from an unsafe floodplain to a designated safer location before inundation. What action is this? | Evacuation temporarily relocates people from danger to a safer area using planned routes and arrangements.
Recovery | After a disaster, a community restores livelihoods, housing and essential services. Which phase is illustrated? | Recovery restores and improves affected systems after an emergency, ideally reducing future vulnerability.
Risk mitigation | A school strengthens its building before any earthquake occurs. What kind of disaster-risk action is this? | Risk mitigation reduces the potential severity of future hazard impacts through preventive measures.
''')
    s('Environment and land-use decisions', '''
Habitat fragmentation | A new road splits continuous forest into small isolated patches. Which ecological pressure does this create? | Habitat fragmentation breaks connected habitat into separated patches, restricting movement and ecological processes.
Invasive alien species | A species introduced outside its natural range spreads and harms native biodiversity. What category does it fit? | An invasive alien species spreads after introduction and causes ecological or other harm.
Edge effect | Conditions near a forest boundary differ from those in the interior after clearing. What phenomenon is illustrated? | Edge effects are ecological changes at habitat boundaries, including altered light, temperature and species interactions.
Environmental impact assessment | Before a major project, likely effects on air, water, biodiversity and communities are systematically examined. What process is this? | Environmental impact assessment evaluates likely environmental consequences to inform planning and decisions.
''')
    s('Public-service ethics scenarios', '''
Procedural fairness | Applicants receive the same published criteria, reasons for decisions and an opportunity to correct errors. What principle is illustrated? | Procedural fairness concerns consistent, impartial processes and a meaningful chance to be heard.
Empathy | A service worker listens carefully to understand the difficulties faced by a distressed applicant. What interpersonal quality is shown? | Empathy seeks to understand another person’s experience while maintaining appropriate professional judgment.
Confidentiality | A counsellor protects personal information from unnecessary disclosure. What professional obligation is being observed? | Confidentiality restricts disclosure of entrusted information, subject to legitimate duties and applicable rules.
Proportionality | An authority selects an effective response that imposes no greater restriction than needed for its legitimate objective. What principle is used? | Proportionality matches the intensity of an action to its objective and weighs avoidable burdens.
''')

    def ref(title,url=None,page=None): return {'title':title,'url':url,'page':page}
    def private(name,page=None): return ref(name+' — supplied private reference',page=page)
    culture=ref('Government of Telangana — Language & Culture','https://www.telangana.gov.in/about/language-culture/')
    scert7=ref('SCERT Telangana — Class 7 Social Studies','https://scert.telangana.gov.in/pdf/publication/ebooks2019/7%20social%20em-21.pdf')
    scert8=ref('SCERT Telangana — Class 8 Social Studies','https://scert.telangana.gov.in/pdf/publication/ebooks2019/8%20social%20em%202020-21.pdf')
    archaeo=ref('Original Telangana archaeology practice; regional scope follows supplied history resources')
    # Regional history and cultural interpretation.
    t('Ancient Deccan rulers','''
Simuka | Who is conventionally identified as the founder of the Satavahana dynasty? | Simuka is conventionally placed at the beginning of the Satavahana royal line.
Gautamiputra Satakarni | Which Satavahana ruler is noted for defeating the western Kshatrapa Nahapana? | Gautamiputra Satakarni restored Satavahana power and defeated Nahapana’s western Kshatrapa forces.
Hala | Which Satavahana ruler is traditionally associated with the Gathasaptashati? | Hala is traditionally credited with the Gathasaptashati, an anthology of Prakrit verses.
Vashishthiputra Pulumavi | Which Satavahana ruler was the son and successor of Gautamiputra Satakarni? | Vashishthiputra Pulumavi succeeded Gautamiputra Satakarni in the Satavahana royal succession.
''',archaeo)
    t('Ancient Telangana archaeological sites','''
Kotilingala | Which Telangana site is especially important for coins of early Satavahana and pre-Satavahana rulers? | Kotilingala has yielded coins important for understanding early political history in the Telangana region.
Dhulikatta | Which Peddapalli-region site preserves an early Buddhist stupa and settlement remains? | Dhulikatta is an early historic Buddhist and settlement site in the Peddapalli region.
Phanigiri | Which Suryapet-region hill site is known for a substantial Buddhist monastic complex? | Phanigiri preserves Buddhist stupas, monastic remains and sculptural evidence in the Suryapet region.
Kondapur | Which archaeological site near Sangareddy is known for an early historic urban settlement and museum? | Kondapur preserves early historic settlement evidence, including craft and trade material displayed in its archaeological museum.
''',archaeo)
    t('Reading early Deccan evidence','''
Matronymic | In a name such as Gautamiputra, what naming feature identifies descent through the mother’s name? | A matronymic incorporates a mother’s name; it does not by itself prove that the entire society was matriarchal.
Overstruck coin | A ruler stamps a new design over an older ruler’s coin. What type of coin evidence can indicate a political transition? | An overstruck coin retains traces of an earlier issue beneath a later stamp, providing evidence of monetary reuse and political change.
Donative inscription | A record states that a merchant paid for a monastery’s structure. What kind of inscription is it? | A donative inscription records a gift and can identify donors, beneficiaries and patronage networks.
Punch-marked coin | A coin bears several separate symbols impressed by punches rather than one complete die design. What type is it? | Punch-marked coins carry individually impressed symbols and are important evidence of early monetary circulation.
''',archaeo)
    t('Kakatiya political history','''
Ganapati Deva | Which Kakatiya ruler issued the Motupalli charter to encourage maritime trade? | Ganapati Deva’s Motupalli charter offered assurances intended to encourage merchants and sea trade.
Rudrama Devi | Which Kakatiya sovereign was a woman who ruled using royal titles also associated with male kingship? | Rudrama Devi ruled the Kakatiya kingdom and exercised sovereign authority despite opposition to female succession.
Prataparudra | Which Kakatiya ruler faced the final Tughlaq conquest of Warangal in 1323? | Prataparudra was the Kakatiya ruler when the Tughlaq army captured Warangal in 1323.
Prola II | Which Kakatiya ruler preceded Rudradeva and strengthened the dynasty’s position during Chalukya decline? | Prola II expanded Kakatiya authority during the weakening of Western Chalukya power.
''',scert7)
    t('Kakatiya-era literary works','''
Nritta Ratnavali | Which Sanskrit treatise by Jayapa Senani discusses dance? | Jayapa Senani’s Nritta Ratnavali is an important treatise on dance associated with the Kakatiya period.
Basava Puranamu | Which Telugu work by Palkuriki Somanatha narrates the life and teachings of Basava? | Palkuriki Somanatha wrote Basava Puranamu in Telugu using the dvipada form.
Prataparudra Yashobhushanam | Which work by Vidyanatha is associated with the praise of Prataparudra and literary theory? | Vidyanatha’s Prataparudra Yashobhushanam combines poetic illustration with discussion of literary ornamentation.
Ranganatha Ramayanamu | Which Telugu Ramayana is traditionally associated with Gona Budda Reddy? | Ranganatha Ramayanamu is traditionally attributed to Gona Budda Reddy and uses the dvipada form.
''',scert7)
    t('Kakatiya administration and economy','''
Nayankara | What system linked military chiefs to territorial revenue and service obligations under the Kakatiyas? | Nayankara arrangements connected chiefs’ control over revenues with military and administrative service.
Ayagar services | What term is associated with hereditary village-service roles in medieval Deccan rural organisation? | Ayagar services involved specialised village functions, supported through customary arrangements and land or revenue rights.
Tank cascade | What irrigation arrangement links a sequence of tanks so that overflow from one can feed another? | A tank cascade connects storage structures within a drainage system, spreading water retention across a landscape.
Merchant guild | What collective institution could organise traders, protect commercial interests and make temple donations? | Merchant guilds coordinated commercial activity and could act as collective patrons in medieval society.
''',scert7)
    t('Ramappa architectural understanding','''
Lightweight porous bricks | Which building material helped reduce the load of the Ramappa temple’s superstructure? | Porous lightweight bricks reduced the weight carried by the temple’s supporting structures.
Sandbox foundation | Which foundation technique is associated with Kakatiya engineering at Ramappa? | A sandbox foundation uses a prepared sand-based layer as part of the structural support system.
Dolerite carving | Which hard dark stone is especially associated with finely carved bracket figures at Ramappa? | Dolerite was worked into finely finished sculptural elements, demonstrating advanced stone-carving skill.
Integrated temple landscape | A temple is planned together with a nearby reservoir and agricultural setting. Which planning idea does Ramappa’s setting illustrate? | Ramappa’s setting connects sacred architecture with water management, terrain and agricultural life.
''',ref('UNESCO — Ramappa nomination dossier, architectural description','https://whc.unesco.org/document/172291'))
    t('Qutb Shahi state formation','''
Sultan Quli Qutb-ul-Mulk | Who founded the Qutb Shahi dynasty at Golconda? | Sultan Quli Qutb-ul-Mulk established independent Qutb Shahi rule after serving under the Bahmani administration.
Ibrahim Quli Qutb Shah | Which Qutb Shahi ruler is known for patronising Telugu culture and for a period of exile at Vijayanagara? | Ibrahim Quli Qutb Shah spent time in Vijayanagara and later patronised diverse literary traditions at Golconda.
Abul Hasan Tana Shah | Who was the last ruler of the Qutb Shahi kingdom? | Abul Hasan, known as Tana Shah, ruled when the Mughal conquest ended Qutb Shahi sovereignty.
Bahmani fragmentation | Which broad political process created the setting for independent Deccan sultanates such as Golconda? | Weakening and fragmentation of Bahmani authority enabled provincial rulers to establish independent sultanates.
''',scert7)
    t('Historic Hyderabad institutions','''
Salar Jung I | Which nineteenth-century minister is associated with major administrative and revenue reforms in Hyderabad State? | Salar Jung I reorganised administration, revenue collection and public institutions in nineteenth-century Hyderabad.
Mir Mahbub Ali Khan | Which sixth Nizam was ruling Hyderabad during the devastating Musi flood of 1908? | Mir Mahbub Ali Khan was the sixth Nizam and ruled during the 1908 Musi flood.
Mir Osman Ali Khan | Which seventh Nizam was the last ruler of princely Hyderabad? | Mir Osman Ali Khan ruled Hyderabad from 1911 until the end of princely sovereignty in 1948.
Nizam-ul-Mulk Asaf Jah I | Which Deccan governor established Asaf Jahi rule in 1724? | Nizam-ul-Mulk established the Asaf Jahi dynasty as Mughal central power weakened.
''',scert7)
    t('Hyderabad administrative vocabulary','''
Khalsa or Diwani land | What category of land revenue was administered directly by the Hyderabad State rather than assigned as jagir? | Khalsa or Diwani areas were under direct state revenue administration.
Jagirdari | What arrangement assigned revenue rights over a territory to a jagirdar? | Jagirdari assigned revenues and associated privileges to holders rather than collecting all revenues directly through state officials.
Sarf-e-khas | What term denoted the Nizam’s private estate revenues? | Sarf-e-khas referred to estates and revenues reserved for the Nizam’s private establishment.
Taluqdar | Which official title was associated with district-level revenue administration in Salar Jung’s reforms? | Paid taluqdar officials became important in reorganised district revenue administration.
''',ref('Telangana Socio Economic Outlook 2017 — administrative reforms','https://www.ecostat.telangana.gov.in/PDF/PUBLICATIONS/Socio_Economic_Outlook_2017.pdf'))
    t('Industrial Hyderabad','''
Singareni coal mining | Which historic industry supplied mineral fuel for industrial development in the Godavari valley? | Singareni coal mining developed around the Godavari valley coalfields and supplied industrial fuel.
Nizam Sugar Factory | Which historic enterprise at Bodhan was associated with sugar processing? | The Nizam Sugar Factory at Bodhan processed sugarcane and was a major industrial enterprise of Hyderabad State.
Azam Jahi Mills | Which historic Warangal enterprise was associated with cotton textiles? | Azam Jahi Mills was a major textile enterprise in Warangal during the Nizam period.
Sirpur Paper Mills | Which industrial enterprise at Kagaznagar was associated with paper production? | Sirpur Paper Mills developed paper manufacturing at Kagaznagar.
''',scert8)
    t('Museum and archive distinctions','''
Salar Jung III | Whose personal art collection formed the central basis of the Salar Jung Museum? | Mir Yousuf Ali Khan, Salar Jung III, assembled the collection that became the museum’s principal foundation.
Veiled Rebecca | Which celebrated marble sculpture at Salar Jung Museum depicts a veiled woman? | Veiled Rebecca is a marble sculpture renowned for creating the appearance of translucent fabric in stone.
Musical clock | Which Salar Jung Museum exhibit attracts visitors through an automated hourly display? | The museum’s musical clock features a mechanical hourly display and complex clockwork.
Provenance record | What museum documentation traces an object’s ownership and acquisition history? | Provenance records help establish an object’s history, authenticity and the circumstances of its collection.
''',ref('Telangana Tourism — Salar Jung Museum','https://tourism.telangana.gov.in/attractions/salar-jung-museum'))
    t('Telangana literary voices','''
Bammera Pothana | Which poet rendered the Bhagavata into Telugu in the work commonly called Andhra Mahabhagavatam? | Bammera Pothana is celebrated for the Telugu Andhra Mahabhagavatam.
Kaloji Narayana Rao | Which Telangana poet is associated with the collection Naa Godava? | Kaloji’s Naa Godava reflects a public, critical and humanistic poetic voice.
Dasarathi Krishnamacharyulu | Which Telangana poet wrote Agnidhara and Rudraveena? | Dasarathi Krishnamacharyulu wrote poetry expressing resistance, social concern and regional aspiration.
Suravaram Pratap Reddy | Which scholar wrote Andhrula Sanghika Charitra? | Suravaram Pratap Reddy’s Andhrula Sanghika Charitra studies the social history of Telugu-speaking people.
''')
    t('Modern regional writing','''
Vattikota Alwar Swamy | Who wrote the Telugu novel Prajala Manishi? | Vattikota Alwar Swamy’s Prajala Manishi depicts social and political life in the Telangana region.
Dasarathi Rangacharya | Which writer authored the novel Chillara Devullu? | Dasarathi Rangacharya’s Chillara Devullu portrays Telangana’s social conditions and feudal relations.
C. Narayana Reddy | Which Telugu poet wrote the long poem Viswambhara? | C. Narayana Reddy’s Viswambhara explores humanity and civilisation in poetic form.
Makhdoom Mohiuddin | Which Urdu poet from Telangana combined literary work with trade-union and political activism? | Makhdoom Mohiuddin was an Urdu poet and activist closely connected with Hyderabad’s labour and political movements.
''',[ORIGINAL,ORIGINAL,ORIGINAL,private('Telangana Armed Struggle.pdf',29)])
    t('Performance traditions','''
Perini Shivatandavam | Which Telangana performance tradition is popularly described as the dance of warriors? | Perini Shivatandavam is associated with vigorous movement and the Kakatiya-era warrior tradition.
Oggu Katha | Which narrative performance tradition tells stories of deities such as Mallanna using music and oral narration? | Oggu Katha combines oral narration and music in the devotional traditions of Telangana communities.
Chindu Bhagavatam | Which Telangana theatre form combines music, dialogue and energetic leaps in a regional Yakshagana tradition? | Chindu Bhagavatam is a theatrical form whose name is associated with its energetic jumping movements.
Dhoom Dham | Which composite cultural form became associated with songs and performances of Telangana social and political mobilisation? | Dhoom Dham combines performance traditions to express social grievances and political aspirations.
''',culture)
    t('Shared cultural expressions','''
Ganga-Jamuna Tehzeeb | What expression describes the composite cultural traditions associated with Hyderabad? | Ganga-Jamuna Tehzeeb refers to shared cultural practices and interaction among diverse communities.
Mushaira | What is a gathering at which poets recite Urdu poetry called? | A mushaira is a poetic gathering centred on recitation and literary exchange.
Ghazal | Which poetic form consists of couplets linked by a formal rhyme and refrain pattern? | The ghazal is a lyric form composed of autonomous couplets within a shared formal pattern.
Qawwali | Which musical form is associated with Sufi devotional performance? | Qawwali presents devotional poetry through ensemble singing and rhythmic musical performance.
''',culture)
    t('Festival practices','''
Saddula Bathukamma | What name is associated with the concluding major day of Bathukamma festivities? | Saddula Bathukamma marks the culminating celebration, including the immersion of flower arrangements.
Rangam | Which Bonalu-associated ritual involves an oracle delivering a prophecy? | Rangam is the oracle or prophecy ritual within Bonalu festivities.
Pothuraju | Which figure in Bonalu processions is traditionally regarded as the goddess’s brother? | Pothuraju is represented as a vigorous protective male figure in Bonalu processions.
Peerla Panduga | By what popular name is Muharram observance known in Telangana? | Muharram is widely known as Peerla Panduga in Telangana and has traditions of participation across communities.
''',culture)
    t('Handicraft materials','''
Silver filigree | Which Karimnagar craft makes intricate objects from fine silver wires? | Silver filigree forms delicate patterns by shaping and joining fine silver wires.
Poniki wood | Which soft wood is traditionally used for Nirmal toys? | Poniki wood is valued for its lightness and workability in the traditional Nirmal toy craft.
Mirror embroidery | What decorative technique is characteristic of Banjara needlework? | Banjara needlework combines embroidery with small mirrors and colourful decorative elements.
Bidri inlay | Which craft places contrasting metal inlay into a darkened metal surface? | Bidri work uses inlay, commonly silver, against a dark metal background; its name derives from Bidar.
''',[private('GI Tags of Telangana.pdf',4),private('GI Tags of Telangana.pdf',5),culture,culture])
    t('Regional textiles','''
Siddipet Gollabhama | Which sari tradition is identified by a milkmaid motif? | Siddipet Gollabhama saris use the distinctive milkmaid figure as a decorative motif.
Narayanpet handloom sari | Which Telangana sari tradition is noted for a checked body and contrasting borders with temple-related patterns? | Narayanpet saris are known for checked fields and characteristic borders reflecting regional weaving traditions.
Telia Rumal | Which textile tradition uses an oil-treatment process before dyeing and is associated with Puttapaka? | Telia Rumal is an oil-treated ikat textile tradition associated with Puttapaka.
Warangal durrie | Which Telangana textile product is a durable flat-woven floor covering? | Warangal durries are woven floor coverings, distinct from saris or painted narrative cloths.
''',[private('GI Tags of Telangana.pdf',8),private('GI Tags of Telangana.pdf',8),private('GI Tags of Telangana.pdf',9),private('GI Tags of Telangana.pdf',10)])
    t('Craft-process literacy','''
Warp | In a Pochampally loom, what are the lengthwise threads held under tension called? | Warp threads run lengthwise on a loom and are interlaced by the weft.
Weft | What are the threads passed across the warp during weaving called? | Weft threads cross the warp and build the woven fabric row by row.
Resist | In patterned dyeing, what term describes a method that prevents dye reaching selected parts? | A resist blocks dye in selected areas so that a planned pattern remains after colouring.
Zari | What term refers to decorative metallic thread used in borders of many ceremonial saris? | Zari is metallic or metal-effect thread used to create decorative woven or embroidered patterns.
''')
    t('Food and cultural knowledge','''
Hyderabad Haleem | Which slow-cooked Hyderabad dish combines meat, grain and pulses into a thick preparation? | Hyderabad Haleem is a slow-cooked preparation combining meat with grain and pulses.
Sakinalu | Which Telangana festive snack is made as concentric rice-flour rings before frying? | Sakinalu are crisp ring-shaped snacks traditionally prepared during festive occasions.
Jonna rotte | What is the common Telangana name for a flatbread made with sorghum flour? | Jonna rotte is a sorghum-based flatbread, associated with regional dryland food traditions.
Sarva pindi | Which Telangana preparation is a savoury rice-flour pancake commonly cooked in a pan with seasonings? | Sarva pindi is a seasoned rice-flour pancake prepared with ingredients such as pulses and spices.
''')
    t('Fort architecture and interpretation','''
Monolithic hill fort | Bhongir’s fort occupies a large single rock mass. Which physical description best fits its setting? | Bhongir is a hill fort built on a prominent monolithic rock, using elevation for defence.
Bastion | What projecting part of a fort wall improves observation and allows defence along adjacent wall faces? | A bastion projects from the wall and improves defensive coverage and observation.
Granary | What fort building stores grain to sustain inhabitants during a siege? | A granary stores food supplies, helping a fort withstand interruptions to outside provisioning.
Gateway deflection | Why might a fort entrance force attackers to turn rather than proceed straight through? | A deflected approach slows entry and exposes attackers to defenders while limiting a direct rush.
''',private('Forts in Telangana.pdf'))
    t('Fort locations and associations','''
Devarakonda | Which Telangana fort is associated with the Recherla Velama rulers and a setting enclosed by hills in Nalgonda? | Devarakonda was an important fortified centre of Recherla Velama power in the Nalgonda region.
Nagunur | Which fort complex in the Karimnagar region contains important Kakatiya-period temples? | Nagunur preserves a fort and temple complex with notable medieval temple remains.
Khammam | Which Telangana town has a prominent fort rising on Stambhadri hill? | Khammam Fort occupies Stambhadri hill and overlooks the town.
Medak | Which fort includes gateways known as Simha Dwaram and Gaja Dwaram? | Medak Fort has gateways identified by lion and elephant imagery, including Simha and Gaja Dwaram.
''',[private('Forts in Telangana.pdf',5),private('Forts in Telangana.pdf',2),private('Forts in Telangana.pdf',9),private('Forts in Telangana.pdf',10)])
    t('Early twentieth-century Hyderabad','''
Hyderabad State Bank | Which institution founded in 1941 managed the Hyderabad State’s currency and banking functions? | Hyderabad State Bank was established in 1941 and later developed into State Bank of Hyderabad.
Osmania Sikka | What name was used for the currency of Hyderabad State? | Osmania Sikka referred to Hyderabad State’s currency, distinct from the currency circulating in British India.
Industrial Trust Fund | What state-backed financing mechanism was established to support industrial development in Hyderabad? | The Industrial Trust Fund provided support for industrial enterprises in Hyderabad State.
Asafia Library | What was the earlier name associated with Hyderabad’s State Central Library? | The State Central Library developed from the Asafia Library, an important public institution in Hyderabad.
''',scert8)

    t('Employee mobilisation before 1969','''
Mahadev Singh | Which Socialist leader called for Telangana Safeguards Day in July 1968? | Mahadev Singh called for observance of Telangana Safeguards Day to press implementation of regional protections.
K.R. Amos | Which employee leader was closely associated with TNGO mobilisation in the 1960s? | K.R. Amos led the Telangana Non-Gazetted Officers organisation and supported agitation over safeguards.
HNGO | Which earlier Hyderabad employee association preceded the TNGO organisational identity? | The Hyderabad Non-Gazetted Officers association formed the earlier organisational background of TNGO.
L.N. Chary | Which employee leader served as associate president with K.R. Amos in the early TNGO organisation? | L.N. Chary was associated with the early leadership of TNGO as associate president.
''',private('Telangana Movement (Part 1).pdf',6))
    t('January 1969 mobilisation','''
Annabattula Ravindranath | Which student began a major hunger strike at Khammam in January 1969? | Annabattula Ravindranath’s Khammam hunger strike helped galvanise the early 1969 agitation.
Potu Krishnamurthy | Which activist undertook a hunger strike at Palvancha over local employment in KTPS? | Potu Krishnamurthy’s protest focused on local employment at the Kothagudem Thermal Power Station.
Kolishetty Ramadasu | Which activist was associated with the Telangana Regional Samiti formed in 1968? | Kolishetty Ramadasu organised the Telangana Regional Samiti and supported early mobilisation around KTPS grievances.
K. Rama Sudhakar Raju | Which teachers’ association leader supported the early Khammam–Palvancha agitation? | K. Rama Sudhakar Raju helped mobilise support among teachers and for the early hunger-strike campaign.
''',[private('Telangana Movement 1969 part 2.pdf',4),private('Telangana Movement 1969 part 2.pdf',5),private('Telangana Movement (Part 1).pdf',8),private('Telangana Movement 1969 part 2.pdf',4)])
    t('Student platforms in 1969','''
Implementation of safeguards | What was the principal early demand of the student Telangana Parirakshana Samiti? | The student Telangana Parirakshana Samiti initially emphasised implementation of assurances and safeguards.
Separate statehood | What was the principal demand of the Telangana Action Committee formed by student leaders in January 1969? | The Telangana Action Committee pressed for a separate Telangana state rather than relying only on safeguards.
Mallikarjun | Which medical student was among the prominent founders of the Telangana Action Committee? | Mallikarjun was a prominent student leader associated with the Telangana Action Committee.
D.S. Reddy | Who was Osmania University’s Vice-Chancellor during the late-1960s autonomy dispute and early 1969 agitation? | D.S. Reddy was the Vice-Chancellor whose tenure became linked to the dispute over university autonomy.
''',private('Telangana Movement 1969 part 2.pdf'))
    t('Political organisation in 1969','''
Madan Mohan | Which Siddipet lawyer was the founder-convenor of the Telangana People’s Convention? | Madan Mohan helped establish the Telangana People’s Convention before its reorganisation as Telangana Praja Samiti.
Reddy Hostel | Where was the major Telangana conference of 8–9 March 1969 held in Hyderabad? | The March 1969 conference was held at Reddy Hostel, a significant public gathering place in Hyderabad.
Sada Lakshmi | Which leader presided over the March 1969 Telangana conference at Reddy Hostel? | Sada Lakshmi presided over the conference and played a visible role in the movement.
T. Purushottama Rao | Who unveiled the Telangana map at the March 1969 Reddy Hostel conference? | T. Purushottama Rao unveiled the map used to express the movement’s territorial claim.
''',private('Telangana Movement 1969 Part 3.pdf'))
    t('Committees and response measures','''
Kumar Lalit committee | Which committee was appointed in January 1969 to examine Telangana’s surplus revenues? | The Kumar Lalit committee examined calculations of Telangana surplus funds in response to the safeguards controversy.
Vashishta Bhargava committee | Which committee was constituted after the Eight-Point Formula to assess Telangana surplus funds? | The Vashishta Bhargava committee was a later inquiry into the calculation of regional surplus funds.
Wanchoo committee | Which committee examined possible responses after the 1969 Supreme Court ruling on public-employment residence requirements? | The Wanchoo committee considered legal and administrative options following the court ruling.
Eight-Point Formula | What response package did Prime Minister Indira Gandhi announce in April 1969? | The Eight-Point Formula proposed measures concerning finances, development and safeguards in response to the agitation.
''',[private('Telangana Movement 1969 part 2.pdf',10),private('Telangana Movement Part 4.pdf',6),private('Telangana Movement 1969 Part 3.pdf',11),private('Telangana Movement Part 4.pdf',6)])
    t('Public figures and acts of protest','''
Konda Laxman Bapuji | Which minister resigned from the Andhra Pradesh cabinet in support of the 1969 Telangana cause? | Konda Laxman Bapuji resigned his ministerial position during the 1969 agitation.
Korapati Pattabhi Ramayya | Which former legislator from the Andhra region undertook a hunger strike supporting Telangana in March 1969? | Korapati Pattabhi Ramayya publicly supported the Telangana demand through a hunger strike and a pamphlet.
M. Narayana Reddy | Which Nizamabad parliamentarian pressed for discussion of Telangana in the Lok Sabha in April 1969? | M. Narayana Reddy raised the Telangana issue in Parliament and sought a dedicated debate.
K. Ramachandra Reddy | Which Assembly Chief Whip resigned his post in May 1969 in support of the Telangana movement? | K. Ramachandra Reddy resigned as Chief Whip as an act of support for the movement.
''',[private('Telangana Movement 1969 Part 3.pdf',10),private('Telangana Movement 1969 Part 3.pdf',7),private('Telangana Movement Part 4.pdf',3),private('Telangana Movement Part 4.pdf',15)])
    t('Publications and intellectual intervention','''
The Telangana Movement—An Investigative Focus | What compilation emerged from the May 1969 intellectuals’ conference at Osmania University? | The compilation brought together analyses of regional grievances discussed at the conference.
K. Jayashankar | Which scholar contributed an analysis concerning Nagarjunasagar to the 1969 intellectual debate? | K. Jayashankar developed an influential scholarly case on regional disparities, including irrigation questions.
Telangana Rashtram Endukoraku | What pamphlet title means Why Telangana State and is associated with Korapati Pattabhi Ramayya? | The pamphlet explained arguments for Telangana statehood to a wider public.
Conference of Intellectuals | What type of gathering at Osmania University in May 1969 brought together papers on regional disparities? | The Conference of Intellectuals brought scholarly arguments into the public debate over Telangana.
''',[private('Telangana Movement Part 4.pdf',12),private('Telangana Movement Part 4.pdf',12),private('Telangana Movement 1969 Part 3.pdf',7),private('Telangana Movement Part 4.pdf',12)])
    t('Employee action and representation','''
Indefinite strike | What form of action did Telangana employee associations begin on 10 June 1969? | Employee associations began an indefinite strike to press their demands during the agitation.
Women’s satyagraha | What form of collective protest did Telangana Praja Samiti organise on 17 June 1969? | The women’s satyagraha brought women’s organised participation visibly into the movement.
Cabinet resignation | What institutional action did eight Telangana ministers take in late June 1969? | The ministers resigned their cabinet posts as pressure grew during the regional agitation.
Parliamentary representation | Raising grievances through MPs in the national legislature uses which political channel? | Parliamentary representation brings regional claims into national legislative debate and scrutiny.
''',private('Telangana Movement Part 5.pdf'))
    t('Electoral phase after 1969','''
Shovel | With which election symbol did Telangana Praja Samiti contest the 1971 Lok Sabha election? | Telangana Praja Samiti contested the election with the shovel symbol.
Ten seats | How many Lok Sabha seats did Telangana Praja Samiti win in the 1971 general election? | Telangana Praja Samiti won ten Lok Sabha seats, demonstrating substantial regional electoral support.
P.V. Narasimha Rao | Who became Chief Minister of Andhra Pradesh in September 1971 after Kasu Brahmananda Reddy? | P.V. Narasimha Rao succeeded Kasu Brahmananda Reddy as Chief Minister in 1971.
Telangana Praja Parishad | Which organisation formed in 1970 criticised the transformation of the movement into conventional party politics? | Telangana Praja Parishad represented a strand critical of the direction taken by Telangana Praja Samiti.
''',private('Telangana Movement Part 6.pdf'))
    t('Regional Committee leadership','''
K. Achyuta Reddy | Who was the first chairman of the Telangana Regional Committee? | K. Achyuta Reddy became the first chairman of the Telangana Regional Committee.
Masuma Begum | Who was the first deputy chairperson of the Telangana Regional Committee? | Masuma Begum served as the committee’s first deputy chairperson.
T. Hayagrivachari | Who succeeded K. Achyuta Reddy as chairman of the Telangana Regional Committee in 1962? | T. Hayagrivachari chaired the committee during the period beginning in 1962.
J. Chokka Rao | Who chaired the Telangana Regional Committee during the period beginning in 1967? | J. Chokka Rao chaired the committee during the later 1960s, including the period of growing regional agitation.
''',private('Telangana Regional Committee.pdf',11))
    t('Regional Committee procedure','''
One-third | According to the supplied committee reference, what fraction of members formed the quorum for Telangana Regional Committee meetings? | The supplied reference states that one-third of members constituted the quorum.
Chairman | Who ordinarily convened meetings of the Telangana Regional Committee? | The chairman convened meetings, with the deputy chairperson acting in the chairman’s absence.
Standing subcommittee | What type of Telangana Regional Committee subcommittee had an ongoing remit? | Standing subcommittees addressed continuing subject areas rather than a single temporary inquiry.
Ad hoc subcommittee | What type of subcommittee was formed temporarily for a specified matter? | An ad hoc subcommittee was constituted for a particular issue and was temporary in character.
''',private('Telangana Regional Committee.pdf'))
    t('Regional Committee policy fields','''
School education | Which field was the focus of a dedicated Telangana Regional Committee standing subcommittee concerned with learning institutions? | Education was one of the committee’s continuing policy areas, including regional educational interests.
Local bodies and public health | Which combined field formed another standing subcommittee’s remit? | The committee maintained a standing focus on local bodies and public-health matters.
Development | Which broad field formed the third standing subcommittee described in the supplied reference? | A development subcommittee examined measures intended to improve the region’s economic and social conditions.
Agricultural land transfers | Which land-related matter fell within the regional safeguard discussions reviewed by the committee? | The sale or transfer of agricultural land in Telangana was among the matters considered in regional safeguard arrangements.
''',private('Telangana Regional Committee.pdf'))

    t('Armed struggle leadership and public life','''
Ravi Narayana Reddy | Which peasant leader won the Nalgonda Lok Sabha seat in the first general election? | Ravi Narayana Reddy moved from peasant mobilisation into parliamentary representation from Nalgonda.
Baddam Yella Reddy | Which armed-struggle leader was elected to the Lok Sabha from Karimnagar in 1952? | Baddam Yella Reddy represented Karimnagar in the first Lok Sabha after the armed struggle.
Mallu Swarajyam | Which woman armed-struggle leader later represented Thungathurthy in the Legislative Assembly? | Mallu Swarajyam participated in the armed struggle and later served as a legislator from Thungathurthy.
Arutla Kamala Devi | Which woman activist represented Alair in the Legislative Assembly after the armed struggle? | Arutla Kamala Devi combined participation in the struggle with later legislative service from Alair.
''',[private('Telangana Armed Struggle.pdf',25),private('Telangana Armed Struggle.pdf',26),private('Telangana Armed Struggle.pdf',32),private('Telangana Armed Struggle.pdf',28)])
    t('Peasant cultural mobilisation','''
Maa Bhoomi | Which play by Sunkara Satyanarayana and Vasireddy Bhaskara Rao was used in peasant mobilisation? | Maa Bhoomi dramatised agrarian oppression and resistance for audiences during the Telangana struggle.
Gollasuddulu | Which oral performance form could combine narration, song and social commentary in peasant mobilisation? | Gollasuddulu adapted familiar oral-performance techniques to communicate social and political messages.
Village library | Which institution gave rural residents shared access to books and discussion during mobilisation? | Village libraries broadened access to reading and created spaces for discussion of social conditions.
Political song | Which cultural medium could convey a movement’s message to listeners who could not read a printed pamphlet? | Political songs used memorable language and performance to communicate grievances and aspirations orally.
''',private('Telangana Armed Struggle.pdf'))
    t('Agrarian conflict sites','''
Palakurthi | Which place was associated with the conspiracy case involving Chakali Ailamma’s family and village activists? | Palakurthi was the setting of a confrontation and prosecution linked to village mobilisation and landlord conflict.
Kadavendi | Which village developed a committee opposing Visunur Deshmukh’s authority before the 1946 confrontation? | Kadavendi’s village organisation became a focal point of resistance to the local landlord’s authority.
Kamareddy Gudem | Which place is associated with the killing of peasant litigant Shaik Bandagi? | Shaik Bandagi’s killing at Kamareddy Gudem became an important remembered episode in agrarian resistance.
Dharmapuram | Which place is associated in the supplied reference with Lambadi resistance and Jatoth Thanu Nayak? | Dharmapuram’s struggle involved Lambadi cultivators resisting landlord claims and coercion.
''',private('Telangana Armed Struggle.pdf'))
    t('Peasant resistance concepts','''
Land redistribution | Transferring large landholdings to landless or small cultivators addresses which demand of the armed struggle? | Land redistribution sought to alter concentrated ownership and improve cultivators’ access to land.
Tenancy protection | Preventing arbitrary eviction of cultivators addresses which agrarian concern? | Tenancy protection secures cultivators’ occupation against arbitrary removal under specified arrangements.
Debt relief | Reducing oppressive accumulated obligations to moneylenders addresses which agrarian concern? | Debt relief addresses burdens of rural indebtedness and the power created by coercive credit relations.
Collective bargaining | Cultivators present demands together rather than negotiating separately with a landlord. What strategy is used? | Collective bargaining pools the negotiating strength of cultivators facing a more powerful counterparty.
''',private('Telangana Armed Struggle.pdf',10))
    t('Organisation during the armed struggle','''
Village committee | What local organisational unit coordinated collective decisions and mobilisation in many participating villages? | Village committees created local structures for collective decision-making and movement activity.
Guerrilla unit | What form of armed organisation relies on small mobile groups rather than a large conventional front? | Guerrilla units use mobility, local knowledge and dispersed action against stronger conventional forces.
Village defence group | What local group focused on protecting residents against raids or attacks? | Village defence groups organised immediate local protection within the movement’s wider structure.
Parallel administration | When a movement establishes local decision-making bodies outside the recognised state hierarchy, what arrangement results? | Parallel administration creates alternative institutions that exercise authority alongside or against official government.
''',private('Telangana Armed Struggle.pdf',11))
    t('Chronology of the armed struggle','''
1946–1951 | Which broad period is conventionally used for the Telangana peasant armed struggle? | The armed struggle is generally dated from 1946 to its withdrawal in 1951.
1951 withdrawal | Which development ended the organised armed phase and opened the way to wider electoral participation? | The withdrawal of the armed struggle in 1951 shifted the movement away from its armed phase.
Post-1948 continuation | What distinguishes the later phase of the Telangana armed struggle from the earlier anti-Nizam phase? | The struggle continued after Hyderabad’s integration, now confronting the new Indian administration over agrarian and political issues.
Communist leadership | Which political current provided the central organised leadership of the armed struggle? | Communist organisations played the central organised leadership role in the peasant armed struggle.
''',private('Telangana Armed Struggle.pdf'))
    t('Memoirs and movement evidence','''
Telangana Porata Smrithulu | Which memoir is associated with Arutla Ramachandra Reddy? | Arutla Ramachandra Reddy recorded memories of the struggle in Telangana Porata Smrithulu.
Veera Telangana—Naa Anubhavalu | Which recollective work is associated with Ravi Narayana Reddy? | Ravi Narayana Reddy wrote about his experience of the Telangana movement in this memoir tradition.
Jailu Lopala | Which work by Vattikota Alwar Swamy draws on prison experience? | Jailu Lopala presents stories shaped by imprisonment and the social conditions encountered there.
Telangana Sayudha Poratam—Na Anubhavalu | Which autobiographical account is associated with Nalla Narsimhulu? | Nalla Narsimhulu recorded his experiences of the armed struggle in this account.
''',private('Telangana Armed Struggle.pdf'))
    t('Tribal resistance and rights','''
Komaram Bheem | Which Gond leader is closely associated with the slogan Jal, Jangal, Jameen? | Komaram Bheem’s resistance is associated with the defence of water, forest and land rights.
Jodeghat | Which place is associated with Komaram Bheem’s final resistance and memorial? | Jodeghat is associated with Bheem’s death and the memorialisation of his struggle.
Gond | Komaram Bheem belonged to which Adivasi community? | Komaram Bheem was a Gond leader whose struggle became an important symbol of Adivasi rights.
Water, forest and land | What does Jal, Jangal, Jameen express in English? | The slogan links water, forest and land as the material basis of community life and rights.
''',ref('Ministry of Tourism — Kumaram Bheem festival','https://www.utsav.gov.in/view-event/kumaram-bheem-festival'))

    # Added regional geography, public institutions and state-formation concepts.
    geo = ref('Original Telangana geography practice; regional context checked against GSI Geology and Mineral Resources of Telangana','https://mines.telangana.gov.in/MinesAndGeology/Documents/RTI%20Circulars/Geology_Telangana_GSI%20%281%29.pdf')
    t('Regional geology','''
Gondwana sedimentary succession | Which geological succession contains the principal coal-bearing strata of the Godavari valley? | The Godavari valley coal measures occur in the Gondwana sedimentary succession, deposited in an ancient continental basin.
Peninsular Gneissic Complex | Which ancient crystalline complex forms a major part of Telangana’s basement geology? | Granite and gneiss of the Peninsular Gneissic Complex underlie extensive parts of Telangana.
Deccan basalt | Which volcanic rock forms part of the western Telangana landscape associated with the Deccan Traps? | Deccan basalt formed from ancient lava flows and occurs toward the western margin of the state.
Eastern Dharwar Craton | Much of Telangana’s ancient crystalline terrain belongs to which cratonic region? | Much of Telangana’s old granite-gneiss terrain forms part of the Eastern Dharwar Craton.
''',geo)
    t('Reading the Telangana landscape','''
Inselberg | A resistant isolated rock hill rises abruptly above the surrounding Telangana plain. What landform is described? | An inselberg is an isolated residual hill left standing above a more extensively eroded surface.
Tor | A hilltop near Hyderabad has exposed piles of rounded granite blocks. Which landform term best describes them? | A tor is an exposed rock outcrop commonly composed of blocks shaped by jointing and weathering.
Pediment | A gently sloping rock surface extends outward from the foot of a Telangana hill. What is this erosion surface called? | A pediment is a gently inclined erosional rock surface at the base of a retreating hill or escarpment.
Graben | The Godavari geological basin includes a down-dropped block bounded by faults. What is such a structure called? | A graben is a block that has subsided relative to neighbouring blocks along faults.
''',geo)
    t('Physiographic map reading','''
West-to-east regional slope | Which broad slope direction helps explain the eastward drainage of much of the Telangana plateau? | Much of the plateau slopes generally eastward, although local valleys and streams can have other directions.
Krishna Piedmont | Which named physiographic division occupies the southern Telangana belt associated with the Krishna valley? | The Krishna Piedmont is the southern physiographic belt distinguished from the Telangana Plateau and Godavari Basin.
Mean sea level | Telangana elevation figures on a conventional physical map are normally measured relative to what datum? | Mean sea level provides the reference surface for expressing land elevation on conventional maps.
Contour interval | The height difference between two successive contour lines on a Telangana topographic map is called what? | The contour interval is the constant vertical difference between adjacent contour lines on a given map.
''',private('2. Physiographic Divisions Of Telangana.pdf'))
    t('Rivers and source regions','''
Ananthagiri Hills | In which hills near Vikarabad does the Musi originate? | The Musi originates in the Ananthagiri Hills near Vikarabad before flowing through Hyderabad.
Pranahita | Which major tributary meets the Godavari at Kaleshwaram? | The Pranahita joins the Godavari at Kaleshwaram, creating a major confluence in the region.
Tungabhadra | Which Krishna tributary forms part of Telangana’s southern boundary near Alampur? | The Tungabhadra flows past the Alampur region before joining the Krishna system.
Maner | Which Godavari tributary gives its name to the Lower Manair reservoir near Karimnagar? | The Maner, also spelled Manair, is a Godavari tributary carrying the Lower Manair reservoir.
''',[ref('Vikarabad district — Ananthagiri Hills','https://vikarabad.telangana.gov.in/gallery/ananthagiri-hills/'),ref('Telangana Tourism — Kaleshwaram','https://tourism.telangana.gov.in/page/kaleshwaram'),ORIGINAL,ORIGINAL])
    t('Distinct reservoir associations','''
Singur | Which reservoir on the Manjira is associated with drinking-water supply to Hyderabad? | Singur is a reservoir on the Manjira and has supplied drinking water to Hyderabad.
Jurala | Which Krishna project near the Gadwal region is also called Priyadarshini Jurala? | Priyadarshini Jurala is a Krishna River project associated with the Gadwal region.
Kinnerasani | Which reservoir near Palvancha shares its name with a wildlife sanctuary? | Kinnerasani reservoir and the adjoining sanctuary occupy the landscape near Palvancha.
Dindi | Which project shares its name with a tributary joining the Krishna in the Nalgonda region? | The Dindi project is built on the Dindi tributary of the Krishna system.
''')
    t('Water structures in practice','''
Spillway | At a Telangana dam, which structure releases excess floodwater safely past the barrier? | A spillway provides a controlled route for excess water, helping prevent overtopping of the dam.
Sluice | Which gated opening in a village tank bund regulates water released into an irrigation channel? | A sluice controls the outflow from a tank or reservoir into a channel.
Ayacut | In Telangana irrigation records, what term means the area served or intended to be served by an irrigation system? | Ayacut refers to the command area associated with an irrigation project or water source.
Balancing reservoir | What storage structure evens out differences between incoming water and a downstream supply schedule? | A balancing reservoir temporarily stores water to reconcile variations in inflow and demand.
''')
    t('Soil-management decisions','''
Black cotton soil | A Telangana field has clay-rich soil that swells when wet and develops deep cracks when dry. Which soil is indicated? | Black cotton soils commonly contain expansive clay, producing swelling and shrinkage with changes in moisture.
Red soil | A Telangana soil derives a reddish colour from iron oxides. Which broad soil group is indicated? | Red soils owe much of their colour to iron oxides; colour alone does not establish their fertility.
Lateritic soil | Which soil group forms under strong weathering and leaching, leaving concentrations of iron and aluminium compounds? | Lateritic soils develop under intense weathering and leaching rather than by simple deposition of fresh river silt.
Alluvial soil | Newly deposited sediment along a Telangana river’s floodplain belongs to which broad soil group? | Alluvial soils develop from sediments transported and deposited by flowing water.
''',ref('Original soil-identification practice; Telangana soil occurrence checked against CGWB Ground Water Year Book 2023–24','https://gwdata.cgwb.gov.in/download/Yearbook/Telangana_GWYB_23-24.pdf'))
    t('Dryland agriculture decisions','''
Contour bunding | A farmer builds earthen barriers along equal-elevation lines across a Telangana slope. Which practice is used? | Contour bunding slows runoff along a slope and helps retain soil and moisture within the field.
Mulching | Crop residues are spread over the soil between plants to limit moisture loss. Which practice is used? | Mulching covers the soil surface, moderating evaporation, temperature and weed growth.
Intercropping | A Telangana farmer grows two crops in arranged rows on the same field during the same season. What is the system? | Intercropping grows more than one crop together in a planned spatial arrangement.
Crop rotation | A field is planted with cereals one season and pulses in a later season in a planned sequence. What is the practice? | Crop rotation changes crops over time on the same land to manage nutrients, pests and production risk.
''')
    t('Farm-production processes','''
Ginning | Which processing step separates cotton fibre from seeds before textile manufacture? | Ginning separates lint from cotton seeds; spinning subsequently converts the fibre into yarn.
Parboiling | Rice mills soak and heat paddy before drying and milling. What is this preliminary treatment called? | Parboiling is a hydrothermal treatment of paddy before milling, affecting grain strength and nutrient distribution.
Turmeric curing | A turmeric grower boils or steams harvested rhizomes before drying them. What processing stage is involved? | Curing prepares turmeric rhizomes for drying and commercial handling after harvest.
Sericulture | Raising silkworms to obtain silk cocoons is known by which term? | Sericulture combines silkworm rearing with the associated production of cocoons for silk.
''')
    t('Regional mining and materials','''
Limestone | Which abundant sedimentary raw material supports cement production in the Nalgonda–Suryapet belt? | Limestone supplies calcium carbonate used in cement manufacture and occurs in the regional sedimentary formations.
Granite | Which hard crystalline dimension stone is quarried for polished building slabs in Telangana? | Granite is quarried and cut into dimension stone for buildings and decorative surfaces.
Quartz | Which silica-rich mineral can provide a raw material for glass and related industries? | Quartz is crystalline silica and is used as a raw material in several silica-based industries.
Feldspar | Which mineral group is an important flux in ceramic and glass manufacture? | Feldspar helps lower the melting temperature of mixtures in ceramic and glass production.
''',ORIGINAL)
    t('Regional forest settings','''
Dry deciduous forest | Which forest type sheds much of its foliage during the dry season and is widespread in Telangana? | Dry deciduous vegetation reduces water loss by shedding leaves during the pronounced dry season.
Riparian vegetation | Plants growing along Telangana riverbanks belong to which location-based vegetation category? | Riparian vegetation occupies the transition between a river and surrounding land.
Scrub vegetation | A heavily degraded dry landscape supports scattered thorny shrubs rather than a closed tree canopy. Which description fits? | Scrub vegetation has low, often thorny woody plants and open cover characteristic of dry or disturbed settings.
Sacred grove | A village protects a patch of woodland because of shared religious or cultural traditions. What is such a patch called? | Sacred groves are woodland patches conserved through community beliefs and customary protection.
''')
    t('Northern Telangana hill locations','''
Kerimeri Ghats | Which hill tract is associated with Kumuram Bheem Asifabad district? | Kerimeri Ghats form a prominent hill landscape in the Kumuram Bheem Asifabad region.
Nirmal hills | Which northern Telangana hill group shares its name with the town known for painted wooden crafts? | The Nirmal hills are associated with the Nirmal region in northern Telangana.
Ramagiri hills | Which hill tract in the Peddapalli region is associated with Ramagiri Khilla? | Ramagiri hills contain the hill-fort landscape known as Ramagiri Khilla in the Peddapalli region.
Pandavula Gutta | Which Jayashankar Bhupalpally rock landscape is known for prehistoric paintings? | Pandavula Gutta preserves rock-art evidence in the Jayashankar Bhupalpally region.
''',private('2. Physiographic Divisions Of Telangana.pdf'))
    t('Waterfalls and lake landscapes','''
Kuntala | Which Telangana waterfall is formed on the Kadem River near Neredigonda? | Kuntala waterfall occurs on the Kadem River near Neredigonda in the Adilabad region.
Bogatha | Which waterfall in the Wazeedu area is popularly promoted as Telangana’s Niagara? | Bogatha waterfall is associated with Wazeedu in the Mulugu region and is known for its broad cascade.
Laknavaram | Which Mulugu lake is particularly associated with a suspension footbridge connecting wooded islands? | Laknavaram is a lake landscape known for its islands and suspension-bridge visitor facilities.
Mallela Theertham | Which waterfall lies within the Nallamala forest landscape of Telangana? | Mallela Theertham is a waterfall in the Nallamala forest region, reached through a wooded landscape.
''',[ref('Adilabad district — Kuntala Water Falls','https://adilabad.telangana.gov.in/tourist-place/kuntala-water-falls/'),ref('Mulugu district — Bogatha Waterfall','https://mulugu.telangana.gov.in/tourist-place/bogatha-waterfall/'),ORIGINAL,ORIGINAL])
    t('Urban nature and public recreation','''
Kasu Brahmananda Reddy National Park | Which national park preserves a green enclave in Hyderabad’s Jubilee Hills? | Kasu Brahmananda Reddy National Park occupies a protected green enclave in Jubilee Hills.
Mrugavani National Park | Which national park is associated with the Chilkur area on the Hyderabad–Vikarabad route? | Mrugavani National Park is located in the Chilkur area near the Hyderabad–Vikarabad route.
Mahavir Harina Vanasthali National Park | Which national park is located at Vanasthalipuram on Hyderabad’s eastern side? | Mahavir Harina Vanasthali National Park protects an area at Vanasthalipuram.
Nehru Zoological Park | Which Hyderabad institution near Mir Alam Tank primarily maintains animals in managed enclosures for conservation and education? | Nehru Zoological Park is a zoological institution near Mir Alam Tank, distinct from a national park protecting an in-situ landscape.
''',[ORIGINAL,ref('Ranga Reddy district — Mrugavani National Park','https://rangareddy.telangana.gov.in/tourist-place/mrugavani-national-park/'),ref('Telangana Forest Department — Annual Administration Report 2009–10','https://forests.telangana.gov.in/Documents/AAR/AAR9-10.pdf'),ORIGINAL])
    t('Hyderabad urban heritage','''
Hussain Sagar | Which historic lake separates parts of Hyderabad and Secunderabad and contains a large Buddha statue on an island platform? | Hussain Sagar is the historic lake between the twin-city areas with the well-known Buddha statue.
Purana Pul | Which bridge is widely known as Hyderabad’s old bridge across the Musi? | Purana Pul is an early bridge across the Musi, predating the foundation of Hyderabad city.
Chowmahalla Palace | Which palace complex was an important ceremonial seat of the Hyderabad Nizams? | Chowmahalla Palace served as a major ceremonial palace complex of the Asaf Jahi rulers.
Falaknuma Palace | Which Hyderabad palace has a name commonly translated as Mirror of the Sky? | Falaknuma means Mirror of the Sky and is the name of a prominent Hyderabad palace.
''')
    t('Telangana pilgrimage geography','''
Basara | Which town on the Godavari is known for its Gnana Saraswati temple? | Basara is associated with the Gnana Saraswati temple and a riverside setting on the Godavari.
Yadagirigutta | Which Telangana temple town is associated with Lakshmi Narasimha worship? | Yadagirigutta is a major Lakshmi Narasimha pilgrimage centre in Telangana.
Vemulawada | Which Telangana town is especially associated with the Raja Rajeshwara temple? | Vemulawada is an important Shaiva pilgrimage centre associated with Raja Rajeshwara.
Alampur | Which Telangana temple town contains the Navabrahma group near the Tungabhadra? | Alampur preserves the early Chalukyan Navabrahma temple group near the Tungabhadra.
''')
    t('Regional religious architecture','''
Medak Cathedral | Which major Telangana church is associated with Gothic Revival architecture in Medak town? | Medak Cathedral is a prominent Gothic Revival church in the town of Medak.
Mecca Masjid | Which large historic mosque stands close to Charminar in Hyderabad? | Mecca Masjid is a major historic mosque adjoining the Charminar area.
Kolanupaka | Which Telangana village is known for an important Jain temple dedicated to Rishabhanatha? | Kolanupaka has a prominent Jain temple with long-standing religious importance.
Keesaragutta | Which hill temple near Hyderabad is associated with Ramalingeswara worship? | Keesaragutta is a hilltop Shaiva pilgrimage site near Hyderabad.
''')
    t('Telangana public research institutions','''
CCMB | Which Hyderabad research centre is especially associated with cellular and molecular biology? | The Centre for Cellular and Molecular Biology conducts research in modern biological sciences.
IICT | Which Hyderabad CSIR laboratory is especially associated with chemical technology? | The Indian Institute of Chemical Technology conducts research in chemistry and chemical technologies.
NGRI | Which Hyderabad institute specialises in geophysical research on the Earth? | The National Geophysical Research Institute studies the Earth using geophysical methods.
National Institute of Nutrition | Which Hyderabad institution is especially associated with nutrition research? | The National Institute of Nutrition studies nutrition and its relationship to health.
''')
    t('Education and knowledge centres','''
ICRISAT | Which international research institution at Patancheru is associated with crops of the semi-arid tropics? | ICRISAT conducts agricultural research focused on semi-arid tropical farming systems and crops.
NALSAR | Which Hyderabad university is especially associated with legal education and research? | NALSAR is a university specialising in law and related research.
English and Foreign Languages University | Which Hyderabad central university specialises in English and foreign-language education? | The English and Foreign Languages University focuses on language study, teaching and research.
Maulana Azad National Urdu University | Which Hyderabad central university is named after Maulana Abul Kalam Azad and promotes Urdu-medium education? | Maulana Azad National Urdu University promotes Urdu-medium higher education alongside related academic work.
''')
    t('Regional economic clusters','''
Genome Valley | Which Hyderabad-region cluster is associated with biotechnology and life-sciences enterprises? | Genome Valley is a life-sciences cluster that brings research and biotechnology-related businesses together.
HITEC City | Which Hyderabad business district is especially associated with information-technology offices? | HITEC City is a major concentration of information-technology and related service-sector offices.
Sircilla | Which Telangana town is especially associated with powerloom textile production? | Sircilla has a major powerloom weaving cluster, distinct from purely manual handloom production.
Shamshabad | At which locality is Hyderabad’s Rajiv Gandhi International Airport situated? | Rajiv Gandhi International Airport is located at Shamshabad south of central Hyderabad.
''')
    t('State-profile historical statistics','''
988 | According to the Telangana State Profile’s 2011 Census data, how many females were there per 1,000 males? | The published 2011 sex ratio for Telangana is 988 females per 1,000 males; this is a dated census measure.
66.54 percent | What literacy rate does the Telangana State Profile report for the 2011 Census? | The profile reports a 2011 literacy rate of 66.54 percent for Telangana.
312 persons per square kilometre | What population density does the Telangana State Profile report from the 2011 Census? | The reported 2011 population density is 312 persons per square kilometre.
38.88 percent | What share of Telangana’s population was urban according to the State Profile’s 2011 Census figures? | The state profile reports an urban population share of 38.88 percent in 2011.
''',ref('Government of Telangana — State Profile, 2011 Census figures','https://www.telangana.gov.in/About/State-Profile/'))
    t('State formation institutions','''
Appointed day | In the Andhra Pradesh Reorganisation Act, what term identifies the date notified for the reorganisation to take effect? | The appointed day is the date notified by the Central Government for the statutory reorganisation to take effect.
Parliament | Which legislature enacted the Andhra Pradesh Reorganisation Act, 2014? | Parliament enacted the law reorganising the former state and forming Telangana.
Successor States | What collective legal term does the Reorganisation Act use for Andhra Pradesh and Telangana after division? | Successor States are the two states that emerged from the reorganisation of the former Andhra Pradesh.
First Schedule | Which Schedule of the Constitution lists states and territories and required consequential amendment for Telangana’s formation? | The First Schedule records the states and their territories, so reorganisation required corresponding changes.
''',ref('India Code — Andhra Pradesh Reorganisation Act, 2014','https://www.indiacode.nic.in/bitstream/123456789/2123/1/A2014-6.pdf'))
    t('Understanding post-bifurcation arrangements','''
119 | How many Assembly seats were allocated to Telangana at its formation under the 2014 Reorganisation Act? | Telangana was allocated 119 seats in the Legislative Assembly at formation.
17 | How many Lok Sabha seats were allocated to Telangana in the 2014 reorganisation? | Telangana was allocated 17 seats in the House of the People.
Common High Court pending separation | What transitional judicial arrangement did the 2014 Act provide before a separate High Court for Andhra Pradesh was established? | The Act continued a common High Court at Hyderabad until a separate Andhra Pradesh High Court was established.
Limited common-capital period | Did the 2014 Act make Hyderabad a permanent common capital or provide a limited common-capital period? | The Act provided a common-capital period of up to ten years, not a permanent joint-capital arrangement.
''',ref('India Code — Andhra Pradesh Reorganisation Act, 2014','https://www.indiacode.nic.in/bitstream/123456789/2123/1/A2014-6.pdf'))
    t('Late statehood movement landmarks','''
9 December 2009 | On which date did the Union Government announce that the process of forming Telangana would be initiated? | The Union Government made the announcement about initiating Telangana’s formation on 9 December 2009.
Srikrishna Committee | Which committee headed by a former Supreme Court judge examined the Andhra Pradesh situation in 2010? | The committee chaired by Justice B.N. Srikrishna examined the situation in Andhra Pradesh and submitted its report in 2010.
Telangana Joint Action Committee | Which umbrella platform coordinated several political and social organisations during the later statehood movement? | The Telangana Joint Action Committee brought multiple organisations into coordinated statehood mobilisation.
Telangana Rashtra Samithi | Which political party was founded in 2001 with a central demand for separate Telangana statehood? | Telangana Rashtra Samithi was founded in 2001 with separate Telangana statehood as its central objective.
''',[ref('Telangana State Portal — account of 9 December 2009 announcement','https://www.telangana.gov.in/news/press-releases/2024/08/telangana-talli-statue-will-be-installed-on-the-lines-of-million-march-on-december-9/'),ref('Centre for Good Governance — Telangana: Ushering in the New Era','https://cgg.gov.in/wp-content/uploads/2019/06/Telangana-Ushering-in-the-New-Era_MRK-Murthy-4.pdf'),ORIGINAL,ORIGINAL])
    t('Forms of statehood mobilisation','''
Sakala Janula Samme | Which 2011 mobilisation is commonly translated as the strike of all sections of people? | Sakala Janula Samme was a broad strike involving multiple social and occupational groups demanding Telangana statehood.
Million March | Which 2011 Telangana mobilisation brought large numbers of protesters toward Hyderabad’s Tank Bund? | The Million March was a major public mobilisation at Tank Bund during the statehood movement.
Vanta Varpu | Which protest form involved collective cooking in public spaces during the Telangana movement? | Vanta Varpu used public cooking and shared meals as a collective form of political demonstration.
Rail Roko | Which protest form sought to block railway movement to draw attention to the statehood demand? | Rail Roko literally refers to stopping trains and was used as a disruptive protest tactic.
''')
    t('Administrative and regional planning terms','''
Revenue mandal | In Telangana’s revenue administration, which territorial unit groups villages below a revenue division? | A revenue mandal is an administrative unit composed of villages and lies below the revenue-division level.
District Collector | Which district officer heads the general revenue administration and coordinates many district functions? | The District Collector leads district revenue administration and coordinates a broad range of district responsibilities.
Gram Sabha | Which village-level body comprises registered voters and can discuss local public issues directly? | The Gram Sabha comprises the registered voters in a village area and supports direct local participation.
Municipal ward | Into what territorial electoral units is a municipality ordinarily divided for councillor representation? | Municipal wards are the territorial units through which residents elect local representatives.
''')
    t('Interpreting regional development evidence','''
Constant-price GSDP | Which measure helps compare Telangana’s production across years after adjusting for price changes? | Constant-price GSDP uses a fixed price basis to separate changes in output from changes in prices.
Per-capita state income | A state-income total is divided by the population. Which average indicator results? | Per-capita state income is an average per resident; it does not show how evenly that income is distributed.
District disaggregation | Statewide averages are split into separate district figures. What statistical step can reveal regional disparities? | District disaggregation reveals differences hidden when all districts are combined into one statewide total.
Time-series comparison | A researcher compares the same Telangana indicator using consistent definitions across several years. What type of comparison is this? | A time-series comparison follows an indicator over time; definitions and boundaries must remain comparable.
''')
    add('Telangana','Boundary and location literacy','''
Landlocked state | Telangana has no coastline. Which geographic classification follows from this? | Telangana is landlocked: it is surrounded by land rather than having a direct sea coast.
Four neighbouring states | Telangana shares land boundaries with Maharashtra, Chhattisgarh, Karnataka and Andhra Pradesh. How many neighbouring states does this list contain? | Telangana borders four states: Maharashtra, Chhattisgarh, Karnataka and Andhra Pradesh.
Island state | Which description would require the state’s territory to be surrounded by water? | An island is surrounded by water; that description does not apply to Telangana.
Coastal state | Which description would require a direct boundary with the sea? | A coastal state has a shoreline on the sea; Telangana does not have one.
''',ref('Government of Telangana — State Profile','https://www.telangana.gov.in/About/State-Profile/'),take=2)

    # Review replacements keep the subject quotas while eliminating repeated
    # tested facts within this bank and across the science/geography bank.
    def replace(qid, skill, question, rows, source=None):
        q = next(q for q in bank if q['id'] == qid)
        correct, reason = rows[0]
        order = list(range(4))
        random.Random(91000 + int(qid.split('-')[1])).shuffle(order)
        q.update(skill=skill, question=question, answer=order.index(0),
                 explanation=reason, source=dict(source or ORIGINAL),
                 options=[{'text': rows[j][0], 'explanation':
                           ('Correct. ' if j == 0 else 'Incorrect. ') + rows[j][1]}
                          for j in order])

    replace('HTS-0049','Biodiversity conservation','A small predator population has a disproportionately large effect on maintaining community structure. Which ecological description applies?',[
        ('Keystone species','A keystone species has an ecological influence that is large relative to its abundance.'),
        ('Dominant species','A dominant species is abundant or contributes much biomass; abundance alone does not establish a disproportionate influence.'),
        ('Vagrant species','A vagrant occurs outside its usual range; that term does not describe community influence.'),
        ('Captive species','Captivity concerns management outside free-ranging conditions, not the magnitude of an ecological role.')])
    replace('HTS-0050','Ecological transitions','A survey records the transition zone between grassland and forest, containing characteristics of both communities. What is this zone called?',[
        ('Ecotone','An ecotone is a transition zone between neighbouring ecological communities.'),
        ('Biome','A biome is a broad ecological region, not specifically the transition between two communities.'),
        ('Territory','A territory is an area defended by an organism or group; the question concerns vegetation communities.'),
        ('Home range','A home range is the area normally used by an individual animal, not a community transition zone.')])
    replace('HTS-0051','Species distributions','A plant naturally occurs only in one restricted geographic region. Which term describes its distribution?',[
        ('Endemic','An endemic species is naturally restricted to a particular geographical area.'),
        ('Cosmopolitan','A cosmopolitan species has a very wide global distribution, the opposite geographic pattern.'),
        ('Migratory','Migration is regular movement between locations, not restriction to one region.'),
        ('Domesticated','Domestication concerns human-directed breeding and management, not a naturally restricted range.')])
    replace('HTS-0052','Ecosystem services','A mangrove belt reduces wave energy before it reaches settlements. In ecosystem-service classifications, which category best fits this benefit?',[
        ('Regulating service','Reducing wave energy and moderating natural hazards are regulating functions of ecosystems.'),
        ('Provisioning service','Provisioning services supply material products such as food or timber; the benefit described is hazard moderation.'),
        ('Cultural service','Cultural services concern recreation, spiritual value or aesthetic benefits rather than wave reduction.'),
        ('A harvested commodity','No material product is harvested in this example; protection results from the standing ecosystem.')])
    replace('HTS-0069','Education indicators','A school tracks the share of enrolled pupils who leave before completing a specified stage. Which indicator is being measured?',[
        ('Dropout rate','A dropout rate records discontinuation before completion within a defined student cohort or period.'),
        ('Attendance rate','Attendance measures presence during scheduled classes and does not by itself establish permanent discontinuation.'),
        ('Pass percentage','Pass percentage measures success among examinees, not departure before completing a stage.'),
        ('Pupil–teacher ratio','This ratio compares student numbers with teacher numbers and does not track pupil departures.')])
    replace('HTS-0071','Maternal-health indicators','Which indicator expresses maternal deaths per 100,000 live births in a defined period?',[
        ('Maternal mortality ratio','The maternal mortality ratio relates maternal deaths to live births, conventionally per 100,000.'),
        ('Crude death rate','The crude death rate relates all deaths to the population, normally per 1,000 persons.'),
        ('Stillbirth rate','Stillbirth statistics concern babies born without signs of life, not deaths of mothers.'),
        ('Total fertility rate','Total fertility rate estimates births per woman under prevailing age-specific fertility rates.')])
    replace('HTS-0074','Community disease monitoring','Health facilities regularly report unusual clusters of fever so authorities can detect outbreaks early. What public-health function is this?',[
        ('Disease surveillance','Surveillance systematically collects, analyses and interprets health information for public-health action.'),
        ('Clinical treatment','Treatment aims to manage an individual patient’s illness; the question describes population monitoring.'),
        ('Rehabilitation','Rehabilitation helps restore functioning after illness or injury, rather than detecting outbreaks.'),
        ('Nutritional supplementation','Supplementation supplies nutrients and is not the systematic reporting of disease patterns.')])
    replace('HTS-0150','Historical research methods','What is the study of old handwriting and historical letter forms called?',[
        ('Palaeography','Palaeography studies historical handwriting and letter forms, helping scholars read and date documents.'),
        ('Genealogy','Genealogy reconstructs family descent rather than studying the shapes of historical writing.'),
        ('Heraldry','Heraldry studies coats of arms and related emblems rather than handwriting.'),
        ('Ethnography','Ethnography investigates living social and cultural practices through descriptive research.')])
    replace('HTS-0347','Social learning','A child learns everyday social norms through family interaction, schooling and peer groups. What process is illustrated?',[
        ('Socialisation','Socialisation is the process through which people learn norms, roles and expectations of social life.'),
        ('Biological inheritance','Biological inheritance transmits genetic material; the question concerns learned social behaviour.'),
        ('Population ageing','Population ageing is a shift in age structure and does not describe learning norms.'),
        ('Occupational displacement','Occupational displacement concerns loss or replacement of employment, not social learning.')])
    replace('HTS-0127','Tank engineering','A village tank bund has an uncontrolled breach during a flood. Which immediate structural problem most directly distinguishes this from normal sluice operation?',[
        ('Loss of containment','A breach is a failure of the embankment to retain water; a sluice is a designed controlled outlet.'),
        ('Planned crop rotation','Changing crops has no direct relationship to structural failure of a tank bund.'),
        ('Routine reservoir evaporation','Evaporation removes water as vapour and does not create a physical gap in the bund.'),
        ('Normal channel lining','Channel lining strengthens conveyance channels and is not an uncontrolled embankment break.')])
    replace('HTS-0141','Telangana sacred geography','At which Nizamabad-region place do the Manjira and Haridra meet the Godavari?',[
        ('Kandakurthi','Kandakurthi is associated with the confluence of the Godavari, Manjira and Haridra.'),
        ('Alampur','Alampur is associated with the Tungabhadra region and the Navabrahma temples, not this confluence.'),
        ('Bhadrachalam','Bhadrachalam stands on the Godavari downstream and is not the Manjira–Haridra confluence.'),
        ('Vemulawada','Vemulawada is a temple town in the Rajanna Sircilla region, not this river confluence.')],ref('Original regional river-confluence practice; Manjira course checked against University of Hyderabad thesis','https://igmlnet.uohyd.ac.in/docs/hi-res/hcu_images/TH12592.pdf'))
    replace('HTS-0142','Telangana geographic position','On a map of Telangana, which neighbouring state lies principally to its west?',[
        ('Karnataka','Karnataka adjoins Telangana on the western side.'),
        ('Odisha','Odisha does not share a land boundary with Telangana.'),
        ('Tamil Nadu','Tamil Nadu lies farther south and does not share a boundary with Telangana.'),
        ('Kerala','Kerala is on India’s southwestern coast and does not border Telangana.')],ref('Government of Telangana — State Profile','https://www.telangana.gov.in/About/State-Profile/'))
    replace('HTS-0538','Twentieth-century regional public life','Who was the first elected Chief Minister of Hyderabad State after the 1952 election?',[
        ('Burgula Ramakrishna Rao','Burgula Ramakrishna Rao headed the elected government of Hyderabad State after the 1952 election.'),
        ('Tanguturi Prakasam','Tanguturi Prakasam became Chief Minister of Andhra State, a different state.'),
        ('D. Sanjivayya','D. Sanjivayya served as Chief Minister of Andhra Pradesh after its formation, not of Hyderabad in 1952.'),
        ('Kasu Brahmananda Reddy','Kasu Brahmananda Reddy was a later Chief Minister of Andhra Pradesh.')])
    replace('HTS-0565','Oral cultural forms','Which narrative form typically uses a principal storyteller with supporting performers and the burra instrument?',[
        ('Burrakatha','Burrakatha combines narration, music and supporting commentary, traditionally with a burra instrument.'),
        ('Kuchipudi','Kuchipudi is a classical dance-drama tradition, not this distinctive storytelling ensemble.'),
        ('Harikatha','Harikatha usually centres on a principal religious storyteller with musical accompaniment, without the defining Burrakatha trio format.'),
        ('Dappu performance','Dappu performance centres on the frame drum; it is not the named burra storytelling form.')])
    replace('HTS-0580','Hyderabad labour organisation','Which doctor and labour leader helped establish Hyderabad Trade Union Congress in 1946 alongside Makhdoom Mohiuddin?',[
        ('Raj Bahadur Gaur','Raj Bahadur Gaur helped establish Hyderabad Trade Union Congress in 1946 alongside Makhdoom Mohiuddin.'),
        ('Suravaram Pratap Reddy','Suravaram Pratap Reddy is known chiefly as a scholar, journalist and social historian, rather than as the doctor and labour organiser described.'),
        ('Burgula Ramakrishna Rao','Burgula Ramakrishna Rao led the elected Hyderabad government; the labour organiser described is Raj Bahadur Gaur.'),
        ('Kaloji Narayana Rao','Kaloji is celebrated as a poet and public intellectual; the labour organiser described is Raj Bahadur Gaur.')],private('Telangana Armed Struggle.pdf',30))
    replace('HTS-0589','Tribal festival customs','At Nagoba Jatara, what ceremony introduces newly married women into the Mesram clan?',[
        ('Bheting','Bheting introduces new brides to the clan during Nagoba Jatara.'),
        ('Rangam','Rangam is the oracle ritual associated with Bonalu, not the Nagoba bride-introduction ceremony.'),
        ('Saddula Bathukamma','Saddula Bathukamma is the concluding major celebration of Bathukamma.'),
        ('Peerla Panduga','Peerla Panduga is the local name associated with Muharram observance.')],ref('Ministry of Tourism — Nagobha Jatara','https://utsav.gov.in/view-event/nagobha-jatara-1'))
    replace('HTS-0590','Northern Telangana traditions','Which Gond dance is associated with elaborate peacock-feather headgear?',[
        ('Gussadi','Gussadi dancers are known for elaborate peacock-feather headgear and distinctive performance attire.'),
        ('Kathak','Kathak is a North Indian classical dance tradition and is not the Gond form described.'),
        ('Garba','Garba is associated with Gujarat and does not identify this Gond dance.'),
        ('Bihu','Bihu is associated with Assam and does not identify the Telangana Gond dance.')],ref('SCERT Telangana — Class 5 EVS, forest communities','https://scert.telangana.gov.in/pdf/publication/ebooks2019/5%20evs%20em%202021.pdf'))
    replace('HTS-0615','Tribal community geography','Which Adivasi community is especially associated with the Nallamala forests of Telangana?',[
        ('Chenchu','Chenchu communities have long-standing connections with the Nallamala forest landscape.'),
        ('Toda','Toda communities are associated with the Nilgiri region, not principally the Nallamala forests.'),
        ('Khasi','Khasi communities are associated with Meghalaya in northeastern India.'),
        ('Jarawa','Jarawa communities are associated with the Andaman Islands.')],ref('SCERT Telangana — Class 5 EVS, life of the Chenchus','https://scert.telangana.gov.in/pdf/publication/ebooks2019/5%20evs%20em%202021.pdf'))
    replace('HTS-0616','Tribal festival geography','Which Telangana tribal festival is held at Keslapur and is associated particularly with the Mesram clan?',[
        ('Nagoba Jatara','Nagoba Jatara at Keslapur is particularly associated with the Mesram clan and Nagoba worship.'),
        ('Medaram Jatara','Medaram Jatara is associated with Sammakka and Saralamma at Medaram, not Keslapur.'),
        ('Edupayala Jatara','Edupayala Jatara is associated with a temple site in the Medak region, not Keslapur.'),
        ('Kurumurthy Jatara','Kurumurthy Jatara is associated with the southern Telangana temple of Kurumurthy.')],ref('Telangana Tourism — Festivals and Fairs','https://www.tourism.telangana.gov.in/page/festivals-and-fairs'))
    replace('HTS-0617','Telangana textiles','Which Telangana sari tradition is especially associated with a cotton body joined to a silk border and pallu?',[
        ('Gadwal sari','Gadwal saris are traditionally associated with a cotton body combined with silk borders and pallu.'),
        ('Kanchipuram sari','Kanchipuram saris are associated with Tamil Nadu and traditionally use a silk body as well as silk borders.'),
        ('Baluchari sari','Baluchari saris are associated with West Bengal and narrative motifs woven into the fabric.'),
        ('Muga silk sari','Muga silk is associated with Assam’s golden-coloured silk rather than the Gadwal cotton-silk combination.')],ref('Government of Telangana — Gadwal history and textiles','https://gadwal.telangana.gov.in/history/'))
    replace('HTS-0618','Telangana literary heritage','Which work of Gunadhya is traditionally described as having been composed in the Paisachi language?',[
        ('Brihatkatha','The lost Brihatkatha is traditionally attributed to Gunadhya and associated with Paisachi; later versions preserve parts of its narrative tradition.'),
        ('Rajatarangini','Kalhana’s Rajatarangini is a Sanskrit chronicle of Kashmir.'),
        ('Buddhacharita','Ashvaghosha’s Buddhacharita is a Sanskrit poetic account of the Buddha’s life.'),
        ('Harshacharita','Banabhatta’s Harshacharita is a Sanskrit prose work associated with King Harsha.')])
    replace('HTS-0622','Telangana heritage engineering','Which reservoir was built across the Musi near Gandipet as part of Hyderabad’s response to flood and water-supply needs?',[
        ('Osman Sagar','Osman Sagar, also called Gandipet, was constructed across the Musi to support flood moderation and water supply.'),
        ('Himayat Sagar','Himayat Sagar was constructed across the Esi tributary rather than directly across the Musi at Gandipet.'),
        ('Hussain Sagar','Hussain Sagar is the older urban lake between Hyderabad and Secunderabad, not the Gandipet reservoir.'),
        ('Mir Alam Tank','Mir Alam Tank is another historic Hyderabad water body with a multiple-arch dam, not Osman Sagar.')])
    replace('HTS-0631','Regional conservation sites','Which Telangana sanctuary is associated with marsh crocodile habitat along the Godavari near Mancherial?',[
        ('Shivaram Wildlife Sanctuary','Shivaram Wildlife Sanctuary is associated with riverine habitat and marsh crocodiles along the Godavari.'),
        ('Manjira Wildlife Sanctuary','Manjira sanctuary occupies the Manjira reservoir landscape, a different river system locality.'),
        ('Pocharam Wildlife Sanctuary','Pocharam sanctuary is associated with the Pocharam reservoir landscape, not the Godavari near Mancherial.'),
        ('Kinnerasani Wildlife Sanctuary','Kinnerasani sanctuary surrounds the Kinnerasani reservoir near Palvancha, not the specified Godavari stretch.')])
    replace('HTS-0633','Regional archaeology','Which traditional Telugu term refers to megalithic tombs as graves of rakshasas?',[
        ('Rakshasa Gullu','Rakshasa Gullu is a traditional Telugu name associated with megalithic graves, recorded in archaeological descriptions.'),
        ('Char Kaman','Char Kaman names the four historic arches near Charminar in Hyderabad, not megalithic graves.'),
        ('Purani Haveli','Purani Haveli is an Asaf Jahi palace complex in Hyderabad.'),
        ('Badshahi Ashurkhana','Badshahi Ashurkhana is a historic Muharram ceremonial building in Hyderabad.')],ref('Archaeological Survey of India — Ancient India 9, megalithic terminology','https://nmma.nic.in/nmma/NAS1/nmma_doc/AI/Ancient%20India%209.pdf'))
    replace('HTS-0678','The 2014 reorganisation law','Which section of the Andhra Pradesh Reorganisation Act, 2014 expressly provides for formation of Telangana State?',[
        ('Section 3','Section 3 of the Act provides for the formation of Telangana State.'),
        ('Section 5','Section 5 concerns Hyderabad’s transitional common-capital arrangement.'),
        ('Section 30','Section 30 concerns the transitional common High Court arrangement.'),
        ('Section 89','Section 89 concerns the Krishna Water Disputes Tribunal, not the section forming the state.')],ref('India Code — Andhra Pradesh Reorganisation Act, 2014','https://www.indiacode.nic.in/bitstream/123456789/2123/1/A2014-6.pdf'))
    replace('HTS-0072','Population-data quality','A census age table has unusually large totals at ages ending in 0 and 5. Which reporting problem is suggested?',[
        ('Age heaping','Age heaping occurs when reported ages cluster at preferred digits, often because respondents round uncertain ages.'),
        ('Seasonal migration','Seasonal migration concerns movement over the year and does not by itself explain preferred age digits.'),
        ('Natural increase','Natural increase is births minus deaths; it does not describe rounding of reported ages.'),
        ('Household overcrowding','Overcrowding relates occupants to available living space, not preferred final digits in ages.')])
    replace('HTS-0297','Bengal intellectual history','Which teacher is associated with the Young Bengal movement and critical inquiry at Hindu College?',[
        ('Henry Louis Vivian Derozio','Derozio taught at Hindu College and inspired the Young Bengal circle to question received social and religious practices.'),
        ('Ishwar Chandra Vidyasagar','Vidyasagar is especially associated with education and widow-remarriage reform; he did not lead the Derozian Young Bengal circle.'),
        ('Keshab Chandra Sen','Keshab Chandra Sen was a later Brahmo reformer, not the Hindu College teacher described.'),
        ('Bankim Chandra Chattopadhyay','Bankim Chandra was a novelist and civil servant, not the teacher associated with Young Bengal.')])
    replace('HTS-0298','Revolutionary nationalist actions','Which 1925 revolutionary action involved taking government money from a train near Lucknow?',[
        ('Kakori train action','Revolutionaries carried out the Kakori train action in 1925 to obtain government funds for their movement.'),
        ('Chittagong armoury raid','The Chittagong armoury raid targeted armouries in 1930, not a train near Lucknow in 1925.'),
        ('Alipore conspiracy case','The Alipore case followed revolutionary activities in Bengal in 1908, a different episode.'),
        ('Delhi conspiracy case','The Delhi conspiracy case concerned the 1912 attack on Viceroy Hardinge, not the Kakori train action.')])
    replace('HTS-0299','Resistance to Company expansion','Which ruler of Kittur resisted East India Company intervention in 1824?',[
        ('Rani Chennamma','Rani Chennamma of Kittur resisted Company intervention in 1824.'),
        ('Rani Lakshmibai','Lakshmibai ruled Jhansi and fought in the uprising of 1857, a later and different resistance.'),
        ('Begum Hazrat Mahal','Begum Hazrat Mahal led resistance in Awadh during 1857, not Kittur in 1824.'),
        ('Rani Durgavati','Rani Durgavati resisted Mughal expansion in Gondwana in the sixteenth century.')])
    replace('HTS-0399','River ecosystem management','A dam operating plan reserves a flow downstream to sustain river habitats and ecological processes. What is this provision called?',[
        ('Environmental flow','Environmental flow is water of an appropriate quantity, timing and quality retained for river ecosystems and their dependent functions.'),
        ('Dead storage','Dead storage is reservoir water below the normally usable outlet level; it is not a downstream ecological release.'),
        ('Canal duty','Canal duty relates irrigation discharge to the area served, rather than the ecological flow requirement.'),
        ('Navigation lockage','Lockage uses water to move boats through a navigation lock and does not define ecological flow provision.')])
    replace('HTS-0693','Early Andhra Mahasabha conferences','Where was the first Andhra Mahasabha conference in Hyderabad State held in 1930?',[
        ('Jogipet','The first Andhra Mahasabha conference in Hyderabad State was held at Jogipet in 1930.'),
        ('Bhuvanagiri','Bhuvanagiri hosted the important 1944 conference associated with the organisation’s political division, not the first conference.'),
        ('Khammam','Khammam hosted a later Andhra Mahasabha conference, rather than the first meeting in 1930.'),
        ('Sircilla','Sircilla hosted a later Andhra Mahasabha conference; Jogipet was the first conference venue.')])
    replace('HTS-0579','Armed-struggle chronology','Which broad period is conventionally used for the Telangana peasant armed struggle?',[
        ('1946–1951','The organised Telangana peasant armed struggle is conventionally dated from 1946 to its withdrawal in 1951.'),
        ('1919–1922','These dates correspond to the broader period of the Rowlatt and Non-Cooperation movements, not the Telangana armed struggle.'),
        ('1930–1934','These dates are associated with the principal Civil Disobedience phase, not the Telangana armed struggle.'),
        ('1956–1969','These dates run from Andhra Pradesh’s formation to the 1969 agitation, after the armed struggle’s withdrawal.')],private('Telangana Armed Struggle.pdf'))
    replace('HTS-0581','Armed-struggle phases','What distinguishes the later phase of the Telangana armed struggle from its earlier anti-Nizam phase?',[
        ('It continued after Hyderabad’s integration under the new Indian administration.','The armed struggle continued after September 1948, with agrarian and political conflict now involving the new Indian administration.'),
        ('It ended immediately when the Nizam’s sovereignty ended in September 1948.','The struggle did not end immediately in September 1948; its organised armed phase continued until 1951.'),
        ('It became a campaign to restore the Nizam’s sovereignty.','Restoring Nizam sovereignty was not the objective of the later peasant armed struggle.'),
        ('It abandoned agrarian demands and focused solely on railway construction.','Land, tenancy and other agrarian demands remained central; railway construction was not its sole or defining purpose.')],private('Telangana Armed Struggle.pdf'))
    replace('HTS-0582','Armed-struggle political leadership','Which political current provided the central organised leadership of the Telangana peasant armed struggle?',[
        ('Communist organisations','Communist organisations supplied the principal organised leadership of the armed peasant struggle.'),
        ('Razakar organisations','Razakar organisations supported the Nizam’s order and opposed the peasant movement rather than leading it.'),
        ('The Nizam’s official administration','The Nizam’s administration was opposed by the struggle during its earlier phase and did not lead it.'),
        ('The East India Company','The East India Company belonged to an earlier period; its rule had ended long before the Telangana armed struggle.')],private('Telangana Armed Struggle.pdf'))
    # Give numerical items comparable distractors, rather than options whose
    # units or grammatical category reveal the answer without subject knowledge.
    for qid, values in {
        'HTS-0671': ('988','932','970','999'),
        'HTS-0672': ('66.54 percent','75.04 percent','57.99 percent','38.88 percent'),
        'HTS-0673': ('312 persons per square kilometre','213 persons per square kilometre','413 persons per square kilometre','512 persons per square kilometre'),
        'HTS-0674': ('38.88 percent','61.12 percent','11.14 percent','66.54 percent'),
        'HTS-0679': ('119','175','294','153'),
        'HTS-0680': ('17','25','42','12'),
    }.items():
        q = next(q for q in bank if q['id'] == qid)
        correct_reason = q['explanation']
        rows = [(values[0],correct_reason)]
        for value in values[1:]:
            rows.append((value, f'This is not the figure for the measure and reference period asked. {correct_reason}'))
        replace(qid, q['skill'], q['question'], rows, q['source'])
    replace('HTS-0700','Telangana boundaries','Which state does not share a land boundary with Telangana?',[
        ('Madhya Pradesh','Madhya Pradesh does not share a boundary with Telangana; Maharashtra and Chhattisgarh lie between relevant parts of the two states.'),
        ('Maharashtra','Maharashtra borders Telangana on the northern and northwestern side.'),
        ('Karnataka','Karnataka borders Telangana on the western side.'),
        ('Andhra Pradesh','Andhra Pradesh borders Telangana on its southern and eastern sides.')],ref('Government of Telangana — State Profile','https://www.telangana.gov.in/About/State-Profile/'))
    return bank

if __name__=='__main__':
    import json
    import re
    from pathlib import Path
    b=build_history_telangana_society()
    counts=dict(Counter(q['topic'] for q in b))
    assert counts == {'Indian History':250,'Environment & Social Awareness':100,'Telangana':350},counts
    norm=lambda s:re.sub(r'[^a-z0-9]+',' ',s.casefold()).strip()
    stems=[norm(q['question']) for q in b]
    assert len(set(stems))==700
    assert len({q['id'] for q in b})==700
    for q in b:
        assert len(q['options'])==4 and 0 <= q['answer'] < 4,q['id']
        assert len({norm(o['text']) for o in q['options']})==4,q['id']
        assert q['explanation'] and all(o['explanation'] for o in q['options']),q['id']
        assert q['source']['title'],q['id']
    cross=[]
    cross_path=Path(__file__).with_name('gs-science-geo.json')
    if cross_path.exists():
        sg=json.loads(cross_path.read_text(encoding='utf-8'))
        d={norm(q['question']):q['id'] for q in sg}
        cross=[{'id':q['id'],'other':d[norm(q['question'])]} for q in b if norm(q['question']) in d]
    assert not cross,cross
    changed=sorted(set(re.findall(r"replace\('(HTS-\d{4})'",Path(__file__).read_text(encoding='utf-8'))))
    out=Path(__file__).with_name('gs-history-telangana-society.json')
    out.write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8')
    audit={
        'count':len(b),'topics':counts,'unique_ids':700,'unique_normalized_stems':700,
        'options_and_explanations_complete':True,
        'exact_stem_duplicates_with_science_geography':cross,
        'review_replacement_ids':changed,
        'numeric_distractors_rebuilt':['HTS-0671','HTS-0672','HTS-0673','HTS-0674','HTS-0679','HTS-0680'],
        'review_summary':[
            'Replaced science/geography overlap: food-chain roles, literacy and sex-ratio definitions, vaccination, radiocarbon dating, soil definitions, crop rotation, seasonal monsoon and plateau identification.',
            'Replaced polity/economy overlap: dependency ratio, first Constituent Assembly meeting, temporary chair, permanent president, common-pool resource, Gram Sabha, First Schedule and human capital.',
            'Replaced internal overlap: library function, 1951 withdrawal, repeated Bheem community/slogan clues, and repeated 1969 conference description.',
            'Improved numerical distractors and armed-struggle phase/chronology/leadership distractors to use parallel answer categories.',
            'Retained Godavari and Krishna as answers where the tested facts are specific reservoir-river associations, distinct from their headwaters or basin identity in the geography module.'
        ],
        'scope_note':'Structural checks and targeted conceptual review completed. This is original practice content with supplied/primary references where identified; this audit is not a claim that every item has received independent subject-expert verification.'
    }
    Path(__file__).with_name('gs-history-telangana-society-audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf-8')
    print(len(b),counts,'exported',out.name)
