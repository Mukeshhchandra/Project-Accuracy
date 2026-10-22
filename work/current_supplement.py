"""100 additional original, dated current-affairs questions.
Primary pages consulted 2026-10-19. No copied past-paper questions.
"""
import random

SOURCES = {
 'xposat': ('ISRO: PSLV-C58/XPoSat, 1 January 2024','https://www.isro.gov.in/ISRO_EN/PSLV_C58_XPoSat_Mission.html'),
 'aditya': ('ISRO: Aditya-L1 halo insertion, 6 January 2024','https://www.isro.gov.in/halo-orbit-insertion-adtya-l1.html'),
 'rlv': ('ISRO: RLV LEX-03, 23 June 2024','https://www.isro.gov.in/ISRO_EN/ISRO_Completes_RLV_Technology_Demonstrations_RLV-LEX3.html?timeline=timeline'),
 'eos': ('ISRO: EOS-08 mission overview, August 2024','https://www.isro.gov.in/EOS-08_Mission.html'),
 'sslv': ('ISRO: SSLV-D3, 16 August 2024','https://www.isro.gov.in/Mission_SSLV_D3.html'),
 'solar': ('PIB: PM-Surya Ghar approval, 29 February 2024','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2010133&lang=2&reg=3'),
 'ups': ('PIB: UPS approval, 24 August 2024','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2048607&lang=2&reg=3'),
 'bio': ('PIB: BioE3 approval, 24 August 2024','https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2048569&lang=1&reg=3'),
 'mausam': ('PIB: Mission Mausam approval, 11 September 2024','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2053896&lang=2&reg=48'),
 'sports': ('PIB: Sports year-end review, 20 December 2024','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2086403&lang=2&reg=48'),
 'khel': ('PIB: National Sports Awards 2024, announced 2 January 2025','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2089557&lang=2&reg=3'),
 'games': ('PIB: 38th National Games closing, 14 February 2025','https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2103368&lang=1&reg=46'),
 'games_open': ('PIB: 38th National Games opening, 28 January 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2097172&lang=2&reg=48'),
 'whc': ('UNESCO: 46th World Heritage Committee session, 2024','https://whc.unesco.org/en/sessions/46com'),
 'classical': ('PIB: five classical languages approved, 3 October 2024','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2061660&lang=45&reg=46'),
 'bharat': ('President Secretariat: Bharat Ratna communique, 9 February 2024','https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2004408&lang=1&reg=3'),
 'nobel_lit': ('Nobel Prize: Han Kang, Literature 2024','https://www.nobelprize.org/laureate/1042'),
 'nobel_peace': ('Nobel Prize: Peace award 2024','https://www.nobelprize.org/press-release-peace-2024?trk=public_post_comment-text'),
 'nobel_med': ('Nobel Prize: Medicine 2024 press release','https://www.nobelprize.org/prizes/medicine/2024/press-release/?os=__'),
 'nobel_chem': ('Nobel Prize: Chemistry 2024 press release','https://www.nobelprize.org/prizes/chemistry/2024/press-release/?trk=news_storyline_guest-text'),
 'nobel_econ': ('Nobel Prize: Economic Sciences 2024 press release','https://www.nobelprize.org/prizes/economic-sciences/2024/press-release/?trk=public_post_comment-text'),
 'wetland': ('PIB: Indore and Udaipur wetland accreditation, 25 January 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2096165&lang=2&reg=48'),
 'wed24': ('UNEP: World Environment Day 2024 report','https://wedocs.unep.org/items/f3dac7f1-e186-4845-9707-4824213ec68f/full'),
 'wed25': ('UNEP: World Environment Day, 5 June 2025','https://www.unep.org/en/news-and-stories/press-release/world-environment-day-2025-mobilizes-commitment-action-end-plastic'),
 'years': ('UN: International Years official list','https://www.un.org/en/node/116796'),
 'quantum': ('UNESCO: International Year of Quantum Science and Technology 2025','https://www.unesco.org/en/years/quantum-science-technology?hub=180536'),
 'glacier': ('UNRIC: 2025 observances and first World Day for Glaciers','https://unric.org/en/2025-year-of-glaciers-peace-quantum-science-cooperatives/'),
 'ax4': ('PIB: Axiom-4 science experiments, 26 June 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2139954'),
 'chenab': ('PIB: Chenab and Anji inauguration, 6 June 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2134513&lang=1&reg=3'),
 'chenab_specs': ('PIB: Chenab and Anji bridge features, 4 June 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2133723&lang=1&reg=44'),
 'pamban': ('PIB: New Pamban Bridge, 7 April 2025','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2119836&lang=2&reg=48'),
 'vadhvan': ('PIB: Vadhavan port approval, 19 June 2024','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2026695&lang=2&reg=48'),
 'coop': ('UN: International Year of Cooperatives 2025 announcement','https://www.un.org/sustainabledevelopment/blog/2024/06/press-release-iyc2025/'),
 'ax4_crew': ('ISRO: Axiom-4 launch and crew, 2025','https://www.isro.gov.in/ISRO_EN/Successful_Launch_of_Axiom_Mission.html'),
 'ax4_return': ('ISRO: Axiom-4 completed, July 2025','https://www.isro.gov.in/Axiom04_mission_successfully_concluded_return_ISRO_Gaganyatri_ShubhanshuShukla.html'),
 'g20': ('MEA: Annual Report 2024, G20 activities','https://www.mea.gov.in/Images/CPV/140725MEAAnnualReport2024English.pdf'),
 'brics': ('BRICS Science Ministers: Brasilia Declaration, 25 June 2025','https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/noticias/2025/06/brics-celebra-10-anos-de-cooperacao-em-cti-com-expansao-historica-e-proposta-de-rede-submarina-para-o-sul-global/FINALBRICSSTIMinisterialDeclarationBrasilia25June2025.pdf'),
 'space_approval': ('PIB: Space-sector projects, 12 December 2024','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2083766&lang=2&reg=3'),
 'physics24': ('Nobel Prize: Physics 2024 press release','https://www.nobelprize.org/prizes/physics/2024/press-release/?gsid=dfe62181-4b48-468e-ad50-e69ebe9cd2be'),
 'literature25': ('Nobel Prize: Literature 2025 press release','https://www.nobelprize.org/uploads/2025/10/Enpress25.pdf'),
 'peace25': ('Norwegian Nobel Committee: 2025 laureate','https://www.nobelpeaceprize.org/laureates/2025'),
 'chemistry25': ('Nobel Prize: Chemistry 2025 press release','https://www.nobelprize.org/prizes/chemistry/2025/press-release/?gsid=9a869906-891e-4357-91eb-742a8c64dc42'),
 'kho': ('PIB: Kho Kho World Cup winners felicitated, 22 January 2025','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2095089&lang=2&reg=48'),
 'cricket25': ('ICC: 2025 Women World Cup final and awards, 2 November 2025','https://www.icc-cricket.com/media-releases/shafali-verma-i-cannot-express-this-feeling-in-words'),
 'indiaai': ('PIB: IndiaAI Mission approval, 7 March 2024','https://www.pib.gov.in/pressreleaseiframepage.aspx?lang=2&prid=2012355&reg=3'),
 'onos': ('PIB: One Nation One Subscription approval, 25 November 2024','https://www.pib.gov.in/PressReleasePage.aspx?PRID=2077097&lang=2&reg=48&s=35'),
 'edrive': ('PIB: PM E-DRIVE approval, 11 September 2024','https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2053889&lang=2&reg=48'),
}

def add_current_supplement(bank):
    start = len(bank)
    def rows(source, skill, text):
        for line in text.strip().splitlines():
            v=line.split('|')
            assert len(v)==9,(len(v),line)
            question=v[0]; pairs=list(zip(v[1::2],v[2::2]))
            order=list(range(4));random.Random(99300+len(bank)).shuffle(order)
            title,url=SOURCES[source]
            bank.append({'id':f'CAS-{len(bank)-start+1:03d}','section':'General Studies','topic':'Current affairs','skill':skill,
                'question':question,'options':[{'text':pairs[j][0],'explanation':('Correct. ' if j==0 else 'Incorrect. ')+pairs[j][1]} for j in order],
                'answer':order.index(0),'explanation':pairs[0][1],'source':{'title':title,'url':url,'page':None},'difficulty':'Standard','origin':'Original practice'})

    # Space science: different mission capabilities and instruments, not inverse questions.
    rows('xposat','Space science: 2024','''
What new measurement capability was central to ISRO's XPoSat mission launched on 1 January 2024?|Polarisation of cosmic X-rays|XPoSat studies the polarisation of X-ray emissions from celestial sources.|Lunar soil sampling|XPoSat observes radiation; it does not collect lunar material.|Ocean salinity mapping|Ocean salinity is an Earth-observation variable, outside XPoSat's central objective.|GPS navigation timing|XPoSat is an astronomy mission, not a navigation constellation.
Which launcher carried XPoSat into orbit on 1 January 2024?|PSLV-C58|ISRO identifies PSLV-C58 as the XPoSat launch mission.|SSLV-D3|SSLV-D3 carried EOS-08 in August 2024.|GSLV-F16|GSLV-F16 carried NISAR in July 2025.|LVM3-M4|LVM3-M4 carried Chandrayaan-3 in 2023.
Which XPoSat payload, described by ISRO in January 2024, performs X-ray polarimetry?|POLIX|POLIX measures X-ray polarisation; Raman Research Institute developed it.|XSPECT|XSPECT supplies spectral and timing observations rather than POLIX polarimetry.|VELC|VELC is the coronagraph aboard the solar mission Aditya-L1.|GNSS-R|GNSS-R on EOS-08 measures reflected navigation signals.
In the January 2024 XPoSat mission description, what was POEM-3 designed to use as an orbital experiment platform?|The PSLV fourth stage|The PS4 stage was repositioned and stabilised for orbital experiments.|A lunar lander|POEM-3 experiments used an orbital rocket stage, not a lunar vehicle.|A discarded ocean buoy|The platform was in Earth orbit, not an ocean instrument.|The ISS crew cabin|POEM-3 was independent of the International Space Station.
''')
    rows('aditya','Solar observation: 2024','''
Aditya-L1 reached its designated halo orbit on 6 January 2024. Around which location does that orbit lie?|Sun-Earth L1|L1 provides a viewing location along the Sun-Earth line.|Earth-Moon L2|This is a different three-body system and point.|A point on the solar surface|Aditya-L1 is a distant observatory and does not land on the Sun.|Mars-Sun L1|The mission uses the Sun-Earth system, not Mars.
What observing advantage did ISRO give for Aditya-L1's January 2024 halo-orbit selection?|An unobstructed, continuous view of the Sun|The selected halo orbit supports sustained solar observations.|Permanent access to lunar soil|The observatory has no lunar sampling mission.|Continuous imaging of Earth's night side only|The scientific target is the Sun, not Earth's night side.|Removal of all need for station keeping|ISRO says the orbit minimises manoeuvres, not that none are required.
Approximately how far from Earth is the Aditya-L1 halo orbit reached in January 2024?|1.5 million kilometres|ISRO places the halo orbit roughly 1.5 million kilometres from Earth.|150 kilometres|This is far below the mission's L1 distance.|1,500 kilometres|This is a near-Earth scale, not the quoted L1 distance.|150 million kilometres|This approximates the Earth-Sun distance, not Earth to L1.
Which regions of the Sun are explicitly named in Aditya-L1's scientific objective in ISRO's January 2024 insertion report?|Chromosphere and corona|ISRO describes continuous study of chromospheric and coronal dynamics.|Mantle and core of Earth|These are terrestrial interior regions, not solar atmosphere layers.|Lunar maria and highlands|These are lunar surface features, outside this solar objective.|Martian polar caps|These belong to Mars, not the Sun.
''')
    rows('rlv','Reusable flight: 2024','''
What name did ISRO give the winged vehicle used in the RLV LEX-03 test on 23 June 2024?|Pushpak|Pushpak was the winged reusable-vehicle landing demonstrator.|Vikram|Vikram identifies India's lunar lander, not this winged demonstrator.|Pragyan|Pragyan is the Chandrayaan lunar rover name.|Aryabhata|Aryabhata was India's first satellite, not the 2024 landing vehicle.
Where did ISRO conduct RLV LEX-03 in June 2024?|Chitradurga, Karnataka|The Aeronautical Test Range at Chitradurga hosted the test.|Sriharikota, Andhra Pradesh|Sriharikota is a launch centre, not this test's runway site.|Thumba, Kerala|Thumba is associated with sounding rockets, not this landing test.|Chandipur, Odisha|Chandipur was not the location identified for LEX-03.
How was Pushpak brought to its release point for the June 2024 RLV LEX-03 experiment?|An Indian Air Force Chinook helicopter|The helicopter released the vehicle at about 4.5 kilometres altitude.|A geostationary satellite|A satellite did not lift the atmospheric test vehicle.|A submerged submarine launcher|This was a helicopter-drop runway experiment.|A lunar ascent rocket|The test took place in Earth's atmosphere, not on the Moon.
Which flight capability did RLV LEX-03 re-demonstrate in June 2024?|Autonomous horizontal runway landing|The uncrewed vehicle corrected its approach and landed on the runway.|Crewed lunar landing|The test carried no lunar-landing crew.|Powered Mars descent|Mars was not the test environment.|Underwater recovery of an orbital capsule|LEX-03 ended on a runway, not underwater.
''')
    rows('eos','Earth observation instruments: 2024','''
Which EOS-08 payload described in August 2024 uses reflected navigation-satellite signals?|GNSS-R|GNSS reflectometry analyses reflected Global Navigation Satellite System signals.|POLIX|POLIX measures cosmic X-ray polarisation on XPoSat.|XSPECT|XSPECT observes cosmic X-ray spectra and timing.|VELC|VELC observes the solar corona on Aditya-L1.
Which named EOS-08 payload, introduced in 2024, is designed for optical-infrared observation?|EOIR|EOIR expands to Electro Optical Infrared Payload.|GNSS-R|GNSS-R is a radio-signal reflectometry payload.|SiC UV Dosimeter|The dosimeter measures ultraviolet exposure rather than optical-infrared imaging.|POLIX|POLIX is an X-ray polarimeter on another mission.
Which EOS-08 instrument listed in August 2024 measures ultraviolet exposure?|SiC UV Dosimeter|The silicon-carbide ultraviolet dosimeter is the UV-monitoring payload.|EOIR|EOIR focuses on electro-optical infrared observations.|XSPECT|XSPECT is an X-ray instrument on XPoSat.|GNSS-R|GNSS-R receives reflected navigation signals.
''')
    rows('sslv','Launch development: 2024','''
What programme milestone did the successful SSLV-D3 flight of 16 August 2024 mark?|Completion of the SSLV Development Project|ISRO states that this third flight completed SSLV development.|India's first crewed orbital flight|SSLV-D3 carried satellites, not a crew.|Completion of a lunar sample return|The flight placed EOS-08 into Earth orbit.|The first launch of a geostationary crew station|The mission did not launch a crew station.
''')
    rows('solar','Renewable-energy policy: 2024','''
The February 2024 PM-Surya Ghar approval primarily supported which household installation?|Rooftop solar electricity systems|The programme supports residential rooftop solar generation.|Coal-fired domestic boilers|Coal boilers are not the renewable electricity installation supported.|Petrol generators only|The central installation is solar, not petrol generation.|New household LPG connections|LPG connections concern a separate policy instrument.
How many households were targeted in the February 2024 PM-Surya Ghar Cabinet approval?|One crore|The approval targeted rooftop solar for one crore households.|One lakh|This is one-hundredth of the stated household target.|Ten crore|This is ten times the approved target.|One thousand|This is far smaller than the national programme's target.
In the February 2024 PM-Surya Ghar design, the central subsidy was capped at what system capacity?|3 kW|The announced central financial assistance cap was at 3 kW.|30 kW|The household subsidy cap was one-tenth of this capacity.|300 kW|This is not the residential CFA cap in the approval.|0.3 kW|The announced cap was ten times this capacity.
Under the February 2024 PM-Surya Ghar benchmark, what subsidy was stated for a 3 kW or larger residential system?|Rs 78,000|The stated benchmark support for 3 kW or higher was Rs 78,000.|Rs 30,000|This was the stated amount for a 1 kW installation.|Rs 60,000|This was the stated amount for a 2 kW installation.|Rs 7,800|This is one-tenth of the stated 3 kW subsidy.
''')
    rows('ups','Pension policy: 2024','''
In the UPS Cabinet announcement of 24 August 2024, the full assured pension was what share of the preceding twelve months' average basic pay, with at least 25 qualifying years?|50%|The announcement specified half of that average basic pay.|60%|Sixty percent described family pension relative to the employee's pension.|100%|The announced assured pension was not the entire basic pay.|10%|Ten percent was not the full pension rate.
What minimum qualifying service was specified for the full UPS assured-pension rate in the August 2024 approval?|25 years|The full rate required at least 25 qualifying years.|10 years|Ten years was the minimum-service threshold for the minimum pension, not the full rate.|5 years|The announcement did not assign the full rate at five years.|40 years|The stated full-rate threshold was 25, not 40 years.
How was assured family pension expressed in the August 2024 UPS announcement?|60% of the employee's pension immediately before death|The base is the employee's pension, not the employee's full salary.|60% of the employee's last gross salary|The announcement used pension as the base, not gross salary.|100% of the employee's pension|The stated family-pension fraction was sixty percent.|A universal fixed Rs 1 lakh monthly|No such universal amount was specified.
What assured minimum monthly pension was stated in the August 2024 UPS announcement after at least ten qualifying years?|Rs 10,000|The Cabinet announcement specified this minimum monthly amount.|Rs 1,000|This is one-tenth of the announced minimum.|Rs 50,000|This was not the announced minimum pension.|Rs 1,00,000|This was not the scheme's stated minimum.
''')
    rows('bio','Biotechnology policy: 2024','''
What do the three E terms in the BioE3 policy approved in August 2024 stand for?|Economy, Environment and Employment|These three objectives explain the BioE3 name.|Education, Elections and Exports|These are not the three terms in the policy title.|Energy, Electronics and Entertainment|These substitute different sectors for the stated objectives.|Ecology, Ethics and Epidemiology|These do not reproduce the policy's named three E terms.
Which department proposed the BioE3 policy approved in August 2024?|Department of Biotechnology|The Cabinet approved the Department of Biotechnology's proposal.|Department of Posts|Postal administration was not the proposing department.|Department of Expenditure|It was not the department identified as the proposal's originator.|Department of School Education|The proposal concerned biotechnology and biomanufacturing.
What manufacturing approach was central to the BioE3 policy approved in August 2024?|High-performance biomanufacturing|The policy supports biological production technologies and commercialisation.|Exclusive expansion of coal extraction|Coal mining was not its central manufacturing approach.|Replacement of all science research with imports|The policy explicitly supports domestic research and entrepreneurship.|Banning biological research|The programme expands, rather than prohibits, biotechnology work.
Which support infrastructure was explicitly envisaged in the August 2024 BioE3 approval?|Biomanufacturing hubs, Bio-AI hubs and biofoundries|These facilities are named as support for technology development.|Only new customs checkpoints|Customs checkpoints are not the policy's research infrastructure.|Only district criminal courts|Courts are outside this biotechnology infrastructure provision.|Only highway toll plazas|Toll facilities are not the hubs specified in BioE3.
''')
    rows('mausam','Weather services: 2024','''
Which ministry was designated to chiefly implement Mission Mausam approved in September 2024?|Ministry of Earth Sciences|The mission strengthens weather and climate science under this ministry.|Ministry of Civil Aviation|Aviation benefits from forecasts but is not the chief implementing ministry.|Ministry of Coal|The mission was not assigned to coal administration.|Ministry of Culture|The policy concerns weather services rather than cultural administration.
What was the initial two-year outlay in the September 2024 Mission Mausam approval?|Rs 2,000 crore|The Cabinet approved a two-year outlay of Rs 2,000 crore.|Rs 200 crore|This is one-tenth of the approved amount.|Rs 20,000 crore|This is ten times the approved amount.|Rs 2 crore|This is one-thousandth of the approved amount.
Which set correctly identifies the three primary implementing institutes in Mission Mausam's 2024 approval?|IMD, IITM and NCMRWF|The weather department, tropical-meteorology institute and medium-range forecasting centre lead implementation.|RBI, SEBI and IRDAI|These are financial regulators, not the three weather institutes.|ASI, NMA and IGNCA|These concern archaeology and culture, not primary weather implementation.|NHAI, FCI and CCI|These bodies do not match the three named meteorological institutes.
What practical capability was Mission Mausam's 2024 approval designed to improve?|Weather and climate forecasts and related services|The mission develops observation, modelling and services for weather readiness.|Conducting parliamentary elections|That is an electoral administration function.|Issuing passports|Passport services are not the mission's purpose.|Regulating stock-exchange listings|Financial-market listing rules are outside this weather mission.
''')
    rows('sports','Sport developments: 2024','''
How many medals did India win at the Paris 2024 Paralympic Games?|29|The official review records 29 Paralympic medals.|6|Six was India's Olympic tally, not its Paralympic tally.|19|This was below the 2024 Paralympic total.|39|The official 2024 total was ten fewer.
Which city hosted the 45th Chess Olympiad in 2024?|Budapest|The official review places the 45th Olympiad in Budapest, Hungary.|Chennai|Chennai hosted the 44th edition in 2022.|Singapore|Singapore hosted the individual World Championship match in 2024.|Batumi|Batumi hosted an earlier Olympiad and the 2025 Women's World Cup, not this edition.
Which achievement did India's teams record at the 45th Chess Olympiad in 2024?|Gold in both the Open and Women's sections|Both Indian teams won their section's gold medal.|Gold only in the Women's section|The Open team also won gold.|Gold only in the Open section|The Women's team also won gold.|No team medal in either section|Both teams finished with gold medals.
What is the main target group of ASMITA Women's Leagues described in the December 2024 sports review?|Women athletes|ASMITA promotes women's participation in organised sport.|Only retired male coaches|The programme's participation focus is women athletes.|Only professional sports journalists|Journalism training is not the leagues' target.|Only stadium contractors|Construction contractors are not the athlete-participation target.
What was KIRTI designed to identify in the government's 2024 sports review?|Sporting talent among school-age children|Khelo India Rising Talent Identification assesses emerging sporting potential.|New coal deposits|KIRTI is a sports-talent programme, not geological exploration.|Income-tax evasion cases|Its assessment is sporting, not fiscal enforcement.|Candidates for judicial appointment|The programme does not recruit judges.
Who were the intended beneficiaries of RESET launched on 29 August 2024?|Retired sportspersons seeking skills and employability|RESET provides training for athletes' careers after sport.|Only preschool children|The intended beneficiaries are retired athletes.|Only active foreign diplomats|Diplomatic service is not the target group.|Only sports-equipment manufacturers|The programme trains people after sporting careers.
''')
    rows('khel','National sports honours: 2024 awards','''
Which para-athlete was among the four Major Dhyan Chand Khel Ratna 2024 recipients announced in January 2025?|Praveen Kumar|The official award list names Praveen Kumar for para-athletics.|Devendra Jhajharia|He was not among this four-person 2024 Khel Ratna list.|Sumit Antil|He was not among the four names in this announcement.|Mariyappan Thangavelu|He was not listed in this particular award year's quartet.
Which hockey player was named for the Major Dhyan Chand Khel Ratna 2024 in January 2025?|Harmanpreet Singh|The official list names Harmanpreet Singh in hockey.|P. R. Sreejesh|He was not the hockey recipient in this 2024 list.|Manpreet Singh|He was not the hockey recipient specified in this announcement.|Mandeep Singh|He was not named in this award's four-person list.
''')
    rows('games','National Games: 2025','''
Which State hosted the 38th National Games held in January-February 2025?|Uttarakhand|The Games were staged in Uttarakhand.|Goa|Goa hosted the preceding 37th edition in 2023.|Gujarat|Gujarat hosted the 36th edition in 2022.|Kerala|Kerala was not the host of the 38th edition.
Which contingent finished as overall champion of the 38th National Games in 2025?|Services Sports Control Board|Services led the final standings with 68 gold medals.|Maharashtra|Maharashtra did not lead the gold-based final standings.|Karnataka|Karnataka was not the overall champion at closing.|Uttarakhand|The host State was not the overall champion.
''')
    rows('games_open','Sustainable sports infrastructure: 2025','''
Which material-reuse feature was highlighted for the 38th National Games medals and trophies at the January 2025 opening?|Use of electronic waste|The opening address highlighted medals and trophies made using e-waste.|Use of newly mined ivory|Ivory was not the material-reuse feature described.|Use of untreated radioactive waste|This was not the Games' materials initiative.|Use of single-use plastic only|The highlighted feature was electronic-waste reuse.
''')
    rows('whc','International heritage governance: 2024','''
Which city hosted UNESCO's 46th World Heritage Committee session in July 2024?|New Delhi|UNESCO identifies the 46th session as New Delhi 2024.|Paris|Paris is UNESCO's headquarters city, not this session's host.|Rome|Rome was not the host named for the 46th session.|Kyoto|Kyoto was not the 2024 committee-session venue.
''')
    rows('classical','Language recognition: October 2024','''
Which group contains all five languages given Classical Language status in the October 2024 Cabinet decision?|Marathi, Pali, Prakrit, Assamese and Bengali|These are the five languages named in that approval.|Hindi, Urdu, Punjabi, Gujarati and Kashmiri|These were not the five languages named in the decision.|Tamil, Telugu, Kannada, Malayalam and Odia|These already had earlier recognition and are not the five new additions.|English, Sanskrit, Arabic, Persian and French|This group does not match the October 2024 additions.
The October 2024 Cabinet note on Classical Languages identified which language as the first recognised when the category began in 2004?|Tamil|The note records Tamil's recognition when the category was created in October 2004.|Sanskrit|Sanskrit received recognition later, in 2005.|Telugu|Telugu's recognition followed in 2008.|Odia|Odia received recognition in 2014, not at the category's creation.
''')
    rows('bharat','National civilian honours: 2024','''
Which agricultural scientist was named for the Bharat Ratna in the President's 9 February 2024 communique?|M. S. Swaminathan|The communique named Swaminathan posthumously.|Verghese Kurien|Kurien was not one of the three people in this communique.|Norman Borlaug|Borlaug was not a recipient named in this Indian award announcement.|C. V. Raman|Raman received the Bharat Ratna in an earlier year, not this announcement.
Which pair of former Prime Ministers was named alongside M. S. Swaminathan in the 9 February 2024 Bharat Ratna communique?|Chaudhary Charan Singh and P. V. Narasimha Rao|The communique lists these two former Prime Ministers.|Atal Bihari Vajpayee and Indira Gandhi|Both received the honour in earlier years, not this communique.|Morarji Desai and Rajiv Gandhi|These were earlier recipients and not the pair named here.|Lal Bahadur Shastri and V. P. Singh|This pair does not match the 9 February 2024 list.
''')
    rows('nobel_lit','Nobel awards: 2024','''
Who received the 2024 Nobel Prize in Literature?|Han Kang|The Korean author received the Literature award.|Jon Fosse|Fosse was the 2023 Literature laureate.|Annie Ernaux|Ernaux received the Literature prize in 2022.|Abdulrazak Gurnah|Gurnah received it in 2021.
''')
    rows('nobel_peace','Nobel awards: 2024','''
Which organisation received the 2024 Nobel Peace Prize for work toward a world without nuclear weapons?|Nihon Hidankyo|The Japanese movement represents atomic-bomb survivors and opposes nuclear weapons.|World Food Programme|It received the Peace Prize in 2020, not 2024.|International Campaign to Abolish Nuclear Weapons|ICAN received the prize in 2017, not 2024.|Doctors Without Borders|It received the Peace Prize in 1999, not 2024.
''')
    rows('nobel_med','Nobel science: 2024','''
The 2024 Nobel Prize in Physiology or Medicine recognised the discovery of which gene-regulating molecules?|microRNA|Ambros and Ruvkun's work revealed microRNA-based control of gene expression.|Haemoglobin|Haemoglobin transports oxygen; it was not this prize's discovery.|Insulin|Insulin is a hormone, not the newly identified regulatory RNA class.|Cellulose|Cellulose is a structural carbohydrate, not the awarded gene-regulation mechanism.
''')
    rows('nobel_chem','Nobel science: 2024','''
Which 2024 Chemistry Nobel laureate received half the prize for computational protein design?|David Baker|Baker's share recognised designing new proteins computationally.|Demis Hassabis|Hassabis shared the other half for protein-structure prediction.|John Jumper|Jumper shared the prediction half, not Baker's design half.|Geoffrey Hinton|Hinton was a 2024 Physics laureate, not this Chemistry recipient.
''')
    rows('nobel_econ','Nobel economic sciences: 2024','''
What central question was recognised by the 2024 Economic Sciences prize to Acemoglu, Johnson and Robinson?|How institutions arise and influence prosperity|Their work connects institutional differences to long-run economic outcomes.|How to identify cosmic X-ray sources|That concerns astronomy, not the awarded economics research.|How to design new protein molecules|Protein design was recognised in the 2024 Chemistry prize.|How to measure continental drift|This concerns geoscience rather than the awarded institutional economics.
''')
    rows('wetland','Wetland conservation: January 2025','''
Which two Indian cities received Wetland City Accreditation in January 2025?|Indore and Udaipur|The official January congratulatory release identifies this pair.|Hyderabad and Warangal|These were not the two cities recognised in this event.|Bhopal and Jaipur|Although Bhopal had been nominated, this was not the recognised pair.|Chennai and Kochi|These cities were not the pair announced in January 2025.
''')
    rows('wed24','Environment observances: 2024','''
Which country hosted the global World Environment Day observance in 2024?|Saudi Arabia|UNEP identifies Saudi Arabia as the 2024 host.|Republic of Korea|Korea hosted the 2025 observance, not 2024.|India|India was not the global host for 2024.|Brazil|Brazil was not the host identified in the 2024 report.
What environmental challenge was central to World Environment Day 2024?|Land restoration, desertification and drought resilience|The 2024 campaign focused on restoring land and resisting drought.|Only marine navigation safety|Navigation safety was not the campaign's environmental focus.|Only space debris removal|Space debris was not the 2024 central theme.|Only noise from aircraft|Aircraft noise was not the stated overarching focus.
''')
    rows('wed25','Environment observances: 2025','''
Which campaign theme guided World Environment Day on 5 June 2025?|Beat Plastic Pollution|UNEP's 2025 campaign called for action across plastics' life cycle.|Only One Earth|This was not the specific 2025 campaign theme.|Time for Nature|This was an earlier World Environment Day theme.|Ecosystem Restoration|This was not the named 2025 theme.
Where were the official World Environment Day 2025 celebrations held?|Jeju, Republic of Korea|UNEP identifies Jeju as the 2025 official celebration venue.|Riyadh, Saudi Arabia|Saudi Arabia hosted the previous year's observance.|Baku, Azerbaijan|Baku hosted COP29, a different event.|Belém, Brazil|Belém hosted COP30, not the official World Environment Day celebration.
''')
    rows('quantum','UN science observances: 2025','''
The UN designated 2025 as an International Year devoted to which field of science and technology?|Quantum science and technology|The designation promotes awareness and international cooperation in quantum science.|Classical mechanics only|The named international year concerns quantum science, not exclusively classical mechanics.|Astrology and divination|These are not the scientific field designated by the UN.|Marine cartography alone|Marine mapping was not the subject of this international year.
Which UN specialised agency led the International Year of Quantum Science and Technology 2025?|UNESCO|UNESCO leads the observance, consistent with its science and education remit.|International Maritime Organization|IMO's maritime remit does not make it the lead agency for this observance.|World Tourism Organization|Tourism was not the leading institutional remit for this quantum-science year.|International Civil Aviation Organization|ICAO was not named as the leading agency for the observance.
''')
    rows('glacier','Glacier preservation: 2025','''
On what date was the first World Day for Glaciers observed in 2025?|21 March|The UN designated 21 March annually, beginning in 2025.|5 June|This is World Environment Day, not the new glacier observance.|22 April|This is International Mother Earth Day, not World Day for Glaciers.|16 September|This is the ozone-layer observance, not the glacier date.
Which frozen-water resource was the specific focus of a UN International Year in 2025?|Glaciers|The International Year of Glaciers' Preservation highlights mountain ice and its significance.|Only sea-salt deposits|Salt deposits are not the frozen-water resource in this designation.|Only tropical coral reefs|Corals were not the resource named in this international year.|Only artificial ice rinks|The designation concerns glaciers, not sports facilities.
''')
    rows('coop','Cooperative development: 2025','''
What theme did the UN announce for the International Year of Cooperatives 2025?|Cooperatives Build a Better World|The theme highlights cooperatives' contribution to sustainable development.|Beat Plastic Pollution|This was the 2025 World Environment Day theme.|One Earth, One Family, One Future|This was India's G20 presidency theme, not this observance.|Our Land, Our Future|This belongs to the 2024 World Environment Day campaign.
Which Indian city was selected for the official launch of the International Year of Cooperatives 2025 during the November 2024 global cooperative conference?|New Delhi|The UN announcement placed the official launch at the New Delhi conference.|Hyderabad|Hyderabad was not the city named for this launch.|Ahmedabad|Ahmedabad was not the announced launch location.|Chennai|Chennai was not the host specified by the UN announcement.
''')
    rows('ax4_crew','Human spaceflight: 2025','''
Which Indian astronaut served as pilot on Axiom Mission 4 launched on 25 June 2025?|Shubhanshu Shukla|ISRO's crew announcement identifies Shukla as the Indian mission pilot.|Rakesh Sharma|Sharma flew in 1984 and was not Axiom-4's pilot.|Kalpana Chawla|Chawla flew on Space Shuttle missions, not Axiom-4.|Sunita Williams|Williams was not the Indian pilot named in the Axiom-4 crew.
Who commanded Axiom Mission 4 during its 2025 flight?|Peggy Whitson|ISRO lists Whitson as the mission commander.|Tibor Kapu|Kapu served as a mission specialist, not commander.|Shubhanshu Shukla|Shukla was the pilot, not the commander.|Sławosz Uznański|Uznański was a mission specialist, not commander.
Which two countries were represented by mission specialists Tibor Kapu and Sławosz Uznański on Axiom-4 in 2025?|Hungary and Poland, respectively|Kapu represented Hungary and Uznański represented Poland.|Poland and Hungary, respectively|This reverses the two astronauts' nationalities.|Romania and Serbia, respectively|Neither country matches the stated pair.|Japan and Canada, respectively|These were not the countries represented by the two specialists.
''')
    rows('ax4_return','Human spaceflight duration: 2025','''
How long did ISRO describe Shubhanshu Shukla's scientific stay aboard the ISS after Axiom-4 concluded in July 2025?|18 days|ISRO described an 18-day scientific mission aboard the ISS.|18 hours|The orbital stay lasted days, not hours.|180 days|This is ten times the reported stay.|18 months|The Axiom-4 stay was much shorter than eighteen months.
''')
    rows('ax4','Microgravity research: June 2025','''
Which organisms did an IISc Bengaluru experiment on Axiom-4 examine for survival, revival and reproduction in microgravity in 2025?|Tardigrades|The experiment studied these resilient microscopic animals.|Banyan trees|Large trees were not the organisms in this survival experiment.|Blue whales|The experiment did not involve large marine mammals.|House sparrows|Birds were not the organisms named for this experiment.
The UAS Dharwad and IIT Dharwad Axiom-4 experiment announced in June 2025 studied sprouts of which crops?|Moong and methi|The experiment examined their germination and nutritional properties in space.|Tea and coffee|These were not the named sprouting-seed crops.|Rubber and teak|These tree crops were not the seeds specified.|Cotton and jute|These fibre crops were not the announced sprout pair.
Which astronaut-health problem was targeted by BRIC-InStem's Axiom-4 experiment announced in June 2025?|Muscle loss and regeneration in microgravity|The experiment investigated mechanisms relevant to muscle deterioration in space.|Only tooth-whitening effectiveness|Cosmetic whitening was not the research objective.|Only seasonal skin tanning|The study focused on muscle biology, not tanning.|Only hearing of bird songs|The experiment did not investigate bird-song perception.
In the Axiom-4 cyanobacteria experiment announced in June 2025, which substance served as the nitrogen source?|Urea|The study examined cyanobacterial growth using urea in microgravity.|Helium|Helium contains no nitrogen and was not the stated source.|Pure oxygen|Oxygen does not supply nitrogen for this experiment.|Sodium chloride|Common salt contains no nitrogen and was not the source.
''')
    rows('chenab','Rail infrastructure: June 2025','''
Which bridge inaugurated on 6 June 2025 was identified as the world's highest railway arch bridge?|Chenab Rail Bridge|The Chenab crossing is the railway arch bridge highlighted at inauguration.|Anji Bridge|Anji is the cable-stayed rail bridge, not the arch bridge.|New Pamban Bridge|Pamban is a vertical-lift sea bridge in Tamil Nadu.|Bogibeel Bridge|Bogibeel is not the railway arch bridge inaugurated in this event.
What engineering distinction was given to Anji Bridge at its June 2025 inauguration?|India's first cable-stayed rail bridge|Anji uses cable-stayed construction for rail connectivity in difficult terrain.|India's first underwater railway tunnel|Anji is a bridge, not an underwater tunnel.|The world's longest suspension road bridge|That is not Anji's announced classification or record.|A floating pontoon bridge|Anji is a permanent cable-stayed structure, not pontoons.
''')
    rows('chenab_specs','Railway engineering: 2025','''
Approximately how high above the river was the Chenab railway arch bridge described in the June 2025 government release?|359 metres|The release gives a height of 359 metres above the river.|35.9 metres|This is one-tenth of the stated height.|3,590 metres|This is ten times the stated height.|59 metres|The published height was substantially greater.
''')
    rows('pamban','Coastal rail infrastructure: 2025','''
What type of movable span distinguishes the New Pamban railway sea bridge opened in April 2025?|Vertical-lift span|The central span rises vertically to provide marine clearance.|A permanent earth embankment|An embankment cannot lift for ship passage.|A retractable undersea tunnel|Pamban is a sea bridge, not a tunnel.|A ropeway cabin|Its transport structure is a railway bridge, not a cable car.
The New Pamban Bridge opened in 2025 links the Indian mainland with which island?|Rameswaram Island|The bridge crosses Pamban Strait to connect Rameswaram with the mainland.|Majuli|Majuli is a river island in Assam, not this sea crossing.|Sagar Island|Sagar is in West Bengal, not the Pamban connection.|Minicoy|Minicoy in Lakshadweep is not connected by Pamban Bridge.
''')
    rows('vadhvan','Port development: June 2024','''
In which State is the Vadhavan greenfield major-port project approved by the Cabinet in June 2024?|Maharashtra|The approved site is in Palghar district near Dahanu.|Telangana|Telangana is landlocked and is not the approved port location.|Odisha|Odisha has ports, but Vadhavan is not in that State.|Gujarat|Vadhavan's approved site lies in Maharashtra, not Gujarat.
Which bodies formed the special-purpose vehicle for Vadhavan Port in the June 2024 approval?|JNPA and Maharashtra Maritime Board|The approval names these as the project company's shareholders.|RBI and SEBI|Financial regulators were not the project company's founders.|ISRO and DRDO|Space and defence research bodies were not the named shareholders.|NHAI and FCI|These were not the two maritime bodies named in the approval.
What was JNPA's equity share in the Vadhavan Port project company under the June 2024 approval?|74%|JNPA held 74%; Maharashtra Maritime Board held 26%.|26%|This was the Maharashtra Maritime Board share, not JNPA's.|50%|The approved company was not an equal-share partnership.|100%|The Maharashtra Maritime Board also held equity.
''')
    rows('g20','Multilateral diplomacy: 2024','''
Which city hosted the G20 leaders' summit on 18-19 November 2024?|Rio de Janeiro|Brazil's presidency concluded with the Rio summit.|New Delhi|New Delhi hosted the 2023 leaders' summit.|Bali|Bali hosted the 2022 leaders' summit.|Osaka|Osaka hosted the 2019 leaders' summit.
Which initiative launched at the opening of the Rio G20 Summit in 2024 included India as a founding member?|Global Alliance against Hunger and Poverty|The alliance was a principal Brazilian-presidency initiative.|International Solar Alliance|ISA originated in 2015 and was not this new Rio alliance.|Coalition for Disaster Resilient Infrastructure|CDRI was launched in 2019, not at Rio 2024.|World Trade Organization|The WTO began in 1995, not at the Rio summit.
Which regional organisation participated in the 2024 Rio G20 Summit as a permanent member following its admission during India's presidency?|African Union|The African Union's inclusion was agreed during India's 2023 presidency.|ASEAN|ASEAN was not the newly admitted permanent member described.|SAARC|SAARC did not receive the permanent membership described here.|Gulf Cooperation Council|The GCC was not the organisation admitted during India's presidency.
''')
    rows('brics','International groupings: 2025','''
Which country did the June 2025 BRICS science-ministers' declaration welcome as a new BRICS member, distinct from partner countries?|Indonesia|The declaration names Indonesia as a member and lists partners separately.|Malaysia|The declaration lists Malaysia among partners rather than the new full member.|Thailand|Thailand is identified among partners in the declaration.|Vietnam|Vietnam is listed as a partner, not the new member named in this clause.
''')
    rows('space_approval','Space project approvals: 2024','''
What new lunar capability was central to Chandrayaan-4 as approved and described by the government in 2024?|Returning lunar samples to Earth|The planned mission combines landing, sample collection and safe return.|Only mapping Earth's oceans|The mission concerns the Moon, not ocean mapping.|Landing a rover on Venus|Venus is a separate planetary target.|Launching a commercial television satellite|The approved mission is lunar exploration, not broadcasting.
Which planet was the target of the new orbiter project described in the government's December 2024 space roadmap?|Venus|The Venus Orbiter Mission targets Venus's surface, atmosphere and solar interaction.|Saturn|Saturn was not the destination of this approved orbiter.|Neptune|Neptune was not the target named in the roadmap.|Mercury|The approved project was for Venus, not Mercury.
What did BAS denote in the government's 2024 space-development roadmap?|Bharatiya Antariksh Station|BAS is India's proposed space-station programme.|Bharat Agricultural Survey|This is not the expansion used in the space roadmap.|Ballistic Aeronautical Shield|The roadmap did not use BAS for a missile defence system.|Bureau of Astronomical Standards|BAS named a station project, not a standards bureau.
Which feature of the NGLV project approved in 2024 is intended to reduce the cost of repeated space launches?|Reusability|Reusing launch hardware is a central low-cost design objective.|Discarding every component after every launch|This is the opposite of the highlighted reusable approach.|Eliminating payload capacity|The project aims to increase payload capability, not eliminate it.|Avoiding all launch-vehicle development|NGLV is explicitly a new launch-vehicle development project.
''')
    rows('physics24','Nobel physics: 2024','''
The 2024 Physics Nobel to John Hopfield and Geoffrey Hinton recognised foundational work in which field?|Machine learning with artificial neural networks|Their physics-based methods helped establish artificial-neural-network learning.|Discovery of microRNA|That was the subject of the 2024 Medicine award.|Computational protein design alone|That was part of the 2024 Chemistry award.|Nuclear disarmament activism|That was the subject of the 2024 Peace award.
''')
    rows('literature25','Nobel literature: 2025','''
Which Hungarian author received the 2025 Nobel Prize in Literature?|László Krasznahorkai|The Swedish Academy's 2025 release names Krasznahorkai.|Han Kang|Han Kang received the 2024 prize and is Korean.|Jon Fosse|Fosse received the 2023 prize and is Norwegian.|Annie Ernaux|Ernaux received the 2022 prize and is French.
''')
    rows('peace25','Nobel peace: 2025','''
Which Venezuelan democracy advocate received the 2025 Nobel Peace Prize?|Maria Corina Machado|The Norwegian Nobel Committee recognised Machado's work for democracy.|Narges Mohammadi|Mohammadi was the 2023 Peace laureate, not the 2025 recipient.|Malala Yousafzai|Yousafzai shared the 2014 Peace Prize.|Ellen Johnson Sirleaf|Sirleaf shared the 2011 Peace Prize.
''')
    rows('chemistry25','Nobel chemistry: 2025','''
Which materials were central to the 2025 Chemistry Nobel awarded to Kitagawa, Robson and Yaghi?|Metal-organic frameworks|MOFs are porous structures assembled from metal and organic building blocks.|microRNAs|These are regulatory RNA molecules, central to the 2024 Medicine award.|Artificial neural networks|These were central to the 2024 Physics award.|Ordinary table salt alone|The prize concerned designed porous frameworks, not salt discovery.
''')
    rows('kho','Indian sport: January 2025','''
What result did India's teams achieve at the inaugural Kho Kho World Cup in January 2025?|Both men's and women's titles|The government felicitated both Indian title-winning teams.|Only the men's title|The women's team also won its competition.|Only the women's title|The men's team also won its competition.|Neither title|Both teams won, so this contradicts the recorded result.
Which venue hosted the title victories in the inaugural Kho Kho World Cup on 19 January 2025?|Indira Gandhi Indoor Stadium, New Delhi|The government release names this indoor stadium.|Eden Gardens, Kolkata|Eden Gardens is a cricket ground, not the named final venue.|Wankhede Stadium, Mumbai|This cricket stadium was not the Kho Kho title venue.|Gachibowli Stadium, Hyderabad|The January 2025 title victories took place in New Delhi.
''')
    rows('cricket25','Women cricket awards: November 2025','''
Who was Player of the Match in the ICC Women's Cricket World Cup final on 2 November 2025?|Shafali Verma|The ICC awarded her final performance with bat and ball.|Deepti Sharma|Sharma was Player of the Tournament, a different award.|Laura Wolvaardt|Wolvaardt scored a century but was not final Player of the Match.|Smriti Mandhana|Mandhana was not the recipient of the final match award.
Who was named Player of the Tournament at the ICC Women's Cricket World Cup in November 2025?|Deepti Sharma|The ICC named Sharma after her all-round tournament performance.|Shafali Verma|Verma won the final's Player of the Match, not the tournament award.|Annabel Sutherland|Sutherland was not the named tournament award recipient.|Harmanpreet Kaur|India's captain was not the recipient of this individual tournament award.
''')
    rows('indiaai','Artificial-intelligence policy: March 2024','''
What minimum scale of GPU infrastructure was envisaged in the March 2024 IndiaAI Mission approval?|10,000 or more GPUs|The original compute pillar specified at least 10,000 graphics processors.|Only 100 GPUs|This is far below the initial approved scale.|Exactly 10 GPUs|The mission was designed as national infrastructure, not ten processors.|No computing infrastructure|Compute capacity was an explicit mission pillar.
Which organisation's independent business division was designated to implement the IndiaAI Mission in March 2024?|Digital India Corporation|The IndiaAI division under DIC was named as implementer.|Food Corporation of India|Foodgrain management was not the organisational home of IndiaAI.|National Highways Authority of India|Road infrastructure was not the mission's implementing organisation.|Sports Authority of India|Sports administration did not house the IndiaAI division.
''')
    rows('onos','Research access policy: November 2024','''
What access problem did One Nation One Subscription, approved in November 2024, primarily address?|Access to scholarly journals for eligible government institutions|The scheme centrally supports research-journal access for government higher education and R&D institutions.|Universal free cinema subscriptions|Commercial entertainment access is not the scheme's purpose.|Compulsory mobile-phone ownership|The scheme concerns research publications, not phone ownership.|Replacement of all university examinations|It expands information access and does not replace examinations.
''')
    rows('edrive','Electric mobility policy: September 2024','''
Which ministry's proposal led to the PM E-DRIVE electric-mobility scheme approved in September 2024?|Ministry of Heavy Industries|The Cabinet approved MHI's scheme to support electric mobility.|Ministry of External Affairs|Foreign affairs was not the proposing ministry.|Ministry of Tribal Affairs|The proposal was not attributed to tribal-affairs administration.|Ministry of Panchayati Raj|Local-government administration was not the scheme's proposing ministry.
''')
    assert len(bank)-start==100,len(bank)-start
