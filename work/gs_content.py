"""Original, static-syllabus GS practice. Not an extracted official question bank.

Each concept group supplies four independently worded questions. Options are
related concepts; every explanation teaches the distinction. Source titles
explicitly distinguish syllabus-based authorship from consulted references.
"""
import random

CONCEPT = {'title': 'Original practice — standard General Studies concepts; not an official paper', 'page': None, 'url': None}
SCIENCE = {'title': 'Original practice — school-level General Science concepts', 'page': None, 'url': None}
CONSTITUTION = {'title': 'Constitution of India — relevant Article or Part stated in explanation', 'page': None, 'url': 'https://www.indiacode.nic.in/bitstream/123456789/15240/1/constitution_of_india.pdf'}
TS_PROFILE = {'title': 'Government of Telangana — State Profile', 'page': None, 'url': 'https://www.telangana.gov.in/about/state-profile/'}
TS_CULTURE = {'title': 'Telangana Tourism — History & Culture', 'page': None, 'url': 'https://tourism.telangana.gov.in/page/history-culture'}
TS_SYMBOLS = {'title': 'Government of Telangana — State Symbols', 'page': None, 'url': 'https://www.telangana.gov.in/about/state-symbols/'}

def build_gs_bank():
    bank = []
    def group(topic, skill, entries, source=None, difficulty='Standard'):
        assert len(entries) == 4
        for correct, (term, prompt, fact) in enumerate(entries):
            order = list(range(4))
            random.Random(9147 + len(bank)).shuffle(order)
            opts = []
            for j in order:
                other, _, distinction = entries[j]
                if j == correct:
                    explanation = 'Correct. ' + fact
                else:
                    explanation = f'Incorrect. {distinction} The clue in this question identifies {term}, rather than {other}.'
                opts.append({'text': other, 'explanation': explanation})
            bank.append({'id': f'GS-{len(bank)+1:04d}', 'section': 'General Studies',
                'topic': topic, 'skill': skill, 'question': prompt, 'options': opts,
                'answer': order.index(correct), 'explanation': fact,
                'source': dict(source[correct] if isinstance(source, list) else (source or CONCEPT)), 'difficulty': difficulty,
                'origin': 'Original practice'})

    # GENERAL SCIENCE — 80 questions.
    def science(skill, entries, difficulty='Standard'):
        group('General Science', skill, entries, SCIENCE, difficulty)
    science('SI units', [
        ('Newton', 'Which SI unit measures force?', 'A newton is the force that gives a 1 kg mass an acceleration of 1 m/s²: 1 N = 1 kg·m/s².'),
        ('Joule', 'Which SI unit measures work or energy?', 'A joule is the work done by a 1 newton force acting through 1 metre in its direction: 1 J = 1 N·m.'),
        ('Watt', 'A device transfers energy at a rate of one joule per second. Which SI unit describes that rate?', 'The watt measures power, the rate of energy transfer: 1 W = 1 J/s.'),
        ('Pascal', 'Which SI unit equals one newton per square metre?', 'The pascal measures pressure, defined as normal force per unit area: 1 Pa = 1 N/m².')
    ], 'Foundation')
    science('Electrical quantities', [
        ('Ampere', 'Which SI unit measures electric current?', 'The ampere measures electric current, the rate at which electric charge flows.'),
        ('Volt', 'Which unit measures electric potential difference between two points?', 'A volt is one joule of energy transferred per coulomb of charge; it measures potential difference.'),
        ('Ohm', 'A conductor allows one ampere to flow when one volt is applied. Its resistance is one of which unit?', 'The ohm measures resistance. Under Ohm’s law, R = V/I, so 1 Ω = 1 V/A.'),
        ('Coulomb', 'Which SI unit measures an amount of electric charge?', 'The coulomb measures electric charge; a current of one ampere transfers one coulomb per second.')
    ], 'Foundation')
    science('Heat transfer', [
        ('Conduction', 'A metal spoon becomes hot from its immersed end while the material itself does not flow. Which process dominates?', 'Conduction transfers energy through a material by microscopic interactions, without bulk movement of the material.'),
        ('Convection', 'Warm water rises and cooler water sinks in a heated vessel. What is this heat-transfer process?', 'Convection transfers heat through the bulk movement of a fluid; density differences can drive circulation.'),
        ('Radiation', 'How can energy from the Sun travel across the vacuum of space to Earth?', 'Thermal radiation transfers energy as electromagnetic waves and does not require a material medium.'),
        ('Evaporative cooling', 'A wet cloth cools as faster-moving water molecules leave its surface. Which process explains this?', 'Evaporation removes higher-energy molecules from a liquid surface, reducing the average energy of the remaining liquid.')
    ])
    science('Optical effects', [
        ('Reflection', 'A light ray strikes a plane mirror and returns into the same medium. Which process occurs?', 'Reflection returns light from a boundary into the original medium; the angle of reflection equals the angle of incidence.'),
        ('Refraction', 'A pencil appears bent where it enters water because light changes direction at the boundary. What causes this?', 'Refraction is the change in direction associated with light changing speed between media, except at normal incidence.'),
        ('Dispersion', 'White light passing through a prism separates into a spectrum because wavelengths bend by different amounts. Name the effect.', 'Dispersion separates wavelengths because the refractive index of a medium depends on wavelength.'),
        ('Scattering', 'Which interaction of sunlight with air molecules chiefly explains the blue daytime sky?', 'Scattering redirects light; small air molecules scatter shorter visible wavelengths more strongly than longer ones.')
    ])
    science('Lenses and mirrors', [
        ('Convex lens', 'Which optical element can converge parallel light rays to a real focus by refraction?', 'A convex lens is thicker at its centre and, in air, converges parallel light rays by refraction.'),
        ('Concave lens', 'Which lens diverges incoming parallel rays and is commonly used to correct myopia?', 'A concave lens is thinner at its centre and diverges rays, helping a myopic eye focus distant objects on the retina.'),
        ('Convex mirror', 'Which mirror usually gives drivers an upright, diminished image and a wider field of view?', 'A convex mirror curves outward and forms upright, diminished virtual images, giving a wide field of view.'),
        ('Plane mirror', 'Which mirror forms an upright virtual image of the same size as the object?', 'A plane mirror forms an image of equal size at an equal distance behind the mirror, with lateral inversion.')
    ])
    science('Motion and mechanics', [
        ('Inertia', 'A passenger tends to keep moving forward when a bus brakes suddenly. Which property explains this?', 'Inertia is the tendency of a body to resist a change in its state of rest or uniform straight-line motion.'),
        ('Momentum', 'Which physical quantity is the product of a body’s mass and velocity?', 'Linear momentum equals mass multiplied by velocity, p = mv, and is a vector quantity.'),
        ('Acceleration', 'Which quantity is the rate of change of velocity with time?', 'Acceleration measures change in velocity per unit time; a change in direction also counts as acceleration.'),
        ('Impulse', 'Which quantity equals force multiplied by the time interval for a constant force, and equals the change in momentum?', 'Impulse is the time integral of force; for constant force it is FΔt and equals the change in momentum.')
    ])
    science('Sound properties', [
        ('Frequency', 'Which wave property mainly determines the pitch of a sound?', 'Frequency is the number of oscillations per second. Higher frequency is normally perceived as higher pitch.'),
        ('Amplitude', 'For waves of the same frequency and medium, which property increases when a sound becomes more intense?', 'Greater displacement amplitude corresponds to greater sound intensity; intensity is proportional to amplitude squared.'),
        ('Wavelength', 'What is the spatial distance between two successive compressions in a sound wave called?', 'Wavelength is the distance between successive points in the same phase, such as two adjacent compressions.'),
        ('Period', 'What is the time taken for one complete oscillation of a vibrating source called?', 'The period is the time for one oscillation and is the reciprocal of frequency: T = 1/f.')
    ])
    science('Atomic structure', [
        ('Proton', 'Which positively charged particle in an atom’s nucleus determines the element’s atomic number?', 'Protons carry positive charge. The number of protons is the atomic number and identifies the element.'),
        ('Neutron', 'Which electrically neutral particle is found in the nucleus of most atoms?', 'A neutron has no net electric charge. Different neutron counts produce isotopes of the same element.'),
        ('Electron', 'Which negatively charged subatomic particle occupies states outside the nucleus?', 'Electrons carry negative charge and occupy atomic orbitals outside the nucleus; their arrangement shapes chemical behaviour.'),
        ('Nucleon', 'What collective term includes both protons and neutrons?', 'Nucleons are the particles of an atomic nucleus: protons and neutrons. Their total gives the mass number.')
    ], 'Foundation')
    science('Chemical processes', [
        ('Oxidation', 'In electron-transfer terms, what happens when a species loses electrons?', 'Oxidation is loss of electrons and an increase in oxidation state; it need not involve oxygen.'),
        ('Reduction', 'In electron-transfer terms, what happens when a species gains electrons?', 'Reduction is gain of electrons and a decrease in oxidation state; oxidation and reduction occur together.'),
        ('Neutralisation', 'What is the usual name for an acid–base reaction that produces salt and water?', 'Neutralisation is an acid–base reaction; in the familiar aqueous case, H⁺ and OH⁻ combine to form water.'),
        ('Precipitation', 'Mixing two solutions produces an insoluble solid that separates from the liquid. What process occurred?', 'Precipitation forms an insoluble solid from dissolved substances when their ions combine under suitable conditions.')
    ])
    science('Mixture separation', [
        ('Filtration', 'Which method is suitable for separating insoluble sand from water using a porous barrier?', 'Filtration retains insoluble particles on a filter while allowing the liquid and dissolved substances to pass.'),
        ('Distillation', 'Which separation method vaporises a liquid and then condenses its vapour to collect it?', 'Distillation separates substances using differences in volatility, involving vaporisation followed by condensation.'),
        ('Chromatography', 'Which method separates ink pigments because they travel at different rates between stationary and mobile phases?', 'Chromatography separates components through their differing affinities for a stationary phase and a moving phase.'),
        ('Sublimation', 'Which process can separate ammonium chloride from sand because it changes directly from solid to vapour on heating?', 'Sublimation is direct conversion of a solid into vapour without a liquid stage; the vapour can be redeposited as solid.')
    ])
    science('Common compounds', [
        ('Sodium chloride', 'Which compound is the main constituent of ordinary table salt?', 'Sodium chloride, NaCl, is common table salt and consists of sodium and chloride ions.'),
        ('Sodium hydrogen carbonate', 'What is the chemical name of baking soda?', 'Baking soda is sodium hydrogen carbonate, NaHCO₃; it releases carbon dioxide when it reacts with an acid.'),
        ('Calcium carbonate', 'Which compound is the main mineral constituent of limestone and marble?', 'Calcium carbonate, CaCO₃, is the main constituent of limestone and marble; it releases carbon dioxide with dilute acid.'),
        ('Calcium oxide', 'Which compound is commonly called quicklime?', 'Quicklime is calcium oxide, CaO. It reacts vigorously with water to form calcium hydroxide, called slaked lime.')
    ], 'Foundation')
    science('Cell organelles', [
        ('Mitochondrion', 'Which organelle is the main site of aerobic ATP production in a typical eukaryotic cell?', 'Mitochondria carry out major stages of aerobic respiration and generate much of the cell’s ATP.'),
        ('Ribosome', 'At which cellular structure are amino acids assembled into proteins using messenger RNA?', 'Ribosomes translate messenger RNA and join amino acids into polypeptides during protein synthesis.'),
        ('Chloroplast', 'Which organelle contains chlorophyll and performs photosynthesis in green plant cells?', 'Chloroplasts contain chlorophyll and convert light energy into chemical energy during photosynthesis.'),
        ('Golgi apparatus', 'Which organelle modifies, sorts and packages many proteins for transport or secretion?', 'The Golgi apparatus modifies and sorts proteins and lipids received from the endoplasmic reticulum, packaging them into vesicles.')
    ])
    science('Plant tissues', [
        ('Xylem', 'Which plant tissue primarily conducts water and dissolved minerals from the roots?', 'Xylem transports water and mineral nutrients, mainly upward from roots, and also provides mechanical support.'),
        ('Phloem', 'Which plant tissue transports sugars from sources such as leaves to growing or storage tissues?', 'Phloem translocates organic food, especially sugars, from sources to sinks; transport can occur in different directions.'),
        ('Meristem', 'Which plant tissue contains actively dividing cells responsible for growth?', 'Meristematic tissues contain cells that divide actively, producing new cells for plant growth.'),
        ('Epidermis', 'Which tissue forms the outer protective covering of a young plant organ?', 'The epidermis forms the outer protective layer; specialised epidermal structures include stomata and root hairs.')
    ])
    science('Human digestion', [
        ('Amylase', 'Which digestive enzyme begins starch digestion in the mouth?', 'Salivary amylase starts the breakdown of starch into smaller carbohydrates in the mouth.'),
        ('Pepsin', 'Which stomach enzyme begins protein digestion in an acidic environment?', 'Pepsin is a protein-digesting enzyme active in the acidic environment of the stomach.'),
        ('Lipase', 'Which class of digestive enzymes breaks down fats into fatty acids and related products?', 'Lipases catalyse fat digestion; pancreatic lipase acts in the small intestine after bile helps emulsify fats.'),
        ('Bile', 'Which liver secretion helps emulsify fats but is not itself a digestive enzyme?', 'Bile is made by the liver and helps disperse large fat globules into small droplets, increasing the area available to lipase.')
    ])
    science('Blood components', [
        ('Red blood cells', 'Which blood cells contain haemoglobin and carry most of the blood’s oxygen?', 'Red blood cells contain haemoglobin, which binds oxygen for transport from the lungs to body tissues.'),
        ('White blood cells', 'Which blood cells are mainly involved in immune defence?', 'White blood cells have immune roles such as destroying pathogens, producing antibodies and coordinating defence.'),
        ('Platelets', 'Which small blood fragments help form a plug at a damaged blood vessel?', 'Platelets are cell fragments that adhere at injury sites and help initiate blood clot formation.'),
        ('Plasma', 'What is the liquid component of blood that carries dissolved nutrients, hormones and wastes?', 'Plasma is the liquid matrix of blood, mostly water, containing proteins and dissolved substances.')
    ], 'Foundation')
    science('Hormones', [
        ('Insulin', 'Which pancreatic hormone lowers blood glucose by promoting glucose uptake and storage?', 'Insulin is secreted by pancreatic beta cells and helps lower blood glucose by promoting uptake and storage.'),
        ('Glucagon', 'Which pancreatic hormone raises blood glucose by promoting release of stored glucose?', 'Glucagon is secreted by pancreatic alpha cells and promotes processes such as liver glycogen breakdown.'),
        ('Thyroxine', 'Which iodine-containing thyroid hormone helps regulate metabolic rate?', 'Thyroxine is produced by the thyroid gland and helps regulate metabolism; iodine is needed for its synthesis.'),
        ('Adrenaline', 'Which hormone prepares the body for an immediate fight-or-flight response?', 'Adrenaline from the adrenal medulla increases readiness for acute stress, including faster heart rate and greater fuel availability.')
    ])
    science('Vitamins and deficiencies', [
        ('Vitamin A', 'Deficiency of which vitamin is classically associated with night blindness?', 'Vitamin A is important for normal vision; deficiency can impair dark adaptation and cause night blindness.'),
        ('Vitamin B1', 'Deficiency of which vitamin causes beriberi?', 'Vitamin B1, or thiamine, supports energy metabolism; severe deficiency can cause beriberi.'),
        ('Vitamin C', 'Deficiency of which vitamin causes scurvy, with impaired connective-tissue maintenance?', 'Vitamin C is required for normal collagen synthesis; deficiency causes scurvy, including bleeding gums and poor wound healing.'),
        ('Vitamin D', 'Deficiency of which vitamin can cause rickets in children by impairing bone mineralisation?', 'Vitamin D supports calcium absorption and bone mineralisation; deficiency in children can cause rickets.')
    ], 'Foundation')
    science('Pathogens and transmission', [
        ('Plasmodium', 'Which organism causes malaria?', 'Malaria is caused by Plasmodium parasites transmitted to humans through bites of infected female Anopheles mosquitoes.'),
        ('Mycobacterium tuberculosis', 'Which bacterium is the principal cause of human tuberculosis?', 'Mycobacterium tuberculosis causes tuberculosis, an infection that commonly affects the lungs and spreads through the air.'),
        ('Vibrio cholerae', 'Which bacterium causes cholera?', 'Vibrio cholerae causes cholera, an intestinal infection commonly transmitted through contaminated water or food.'),
        ('Dengue virus', 'Which pathogen causes dengue?', 'Dengue is caused by dengue viruses and is transmitted mainly by infected Aedes mosquitoes; it is not a bacterial disease.')
    ])
    science('Genetic concepts', [
        ('Gene', 'What is a functional hereditary unit consisting of a DNA sequence?', 'A gene is a DNA sequence with a functional product, such as an RNA or a protein through an RNA intermediate.'),
        ('Chromosome', 'What organised DNA–protein structure carries many genes in a cell?', 'A chromosome is an organised structure containing DNA and associated proteins, carrying many genetic loci.'),
        ('Allele', 'What is one of two or more alternative versions of a gene at a locus called?', 'Alleles are alternative versions at a genetic locus; differences between alleles can contribute to differences in traits.'),
        ('Mutation', 'What term describes a change in the DNA sequence?', 'A mutation is a change in genetic sequence. Its effect may be harmful, neutral or beneficial depending on context.')
    ])
    science('Reproduction and cell division', [
        ('Mitosis', 'Which cell-division process normally preserves chromosome number in the daughter nuclei?', 'Mitosis divides a eukaryotic nucleus into two with the same chromosome number, supporting growth and repair.'),
        ('Meiosis', 'Which process halves chromosome number to produce haploid cells in sexual reproduction?', 'Meiosis involves two divisions after one DNA replication, reducing chromosome number and generating genetic variation.'),
        ('Fertilisation', 'What process unites male and female gametes to form a zygote?', 'Fertilisation is fusion of gametes; in the usual diploid life cycle it restores the diploid chromosome number.'),
        ('Pollination', 'What is the transfer of pollen from an anther to a receptive stigma called?', 'Pollination is pollen transfer to the stigma. It precedes fertilisation but is not itself fusion of gametes.')
    ])

    # POLITY — 48 questions. Article references are supplied, not invented pages.
    def polity(skill, entries, difficulty='Standard'):
        group('Indian Polity', skill, entries, CONSTITUTION, difficulty)
    polity('Constitutional structure', [
        ('Part III', 'Which Part of the Indian Constitution contains Fundamental Rights?', 'Part III contains Fundamental Rights, including equality, freedoms and constitutional remedies.'),
        ('Part IV', 'Which Part contains the Directive Principles of State Policy?', 'Part IV contains the Directive Principles of State Policy, which guide governance and are not directly enforceable by courts.'),
        ('Part IVA', 'Which Part contains the Fundamental Duties of citizens?', 'Part IVA consists of Article 51A, listing Fundamental Duties of citizens.'),
        ('Part IX', 'Which Part of the Constitution concerns Panchayats?', 'Part IX deals with Panchayats and was inserted by the Constitution (73rd Amendment) Act, 1992.')
    ], 'Foundation')
    polity('Rights and Articles', [
        ('Article 14', 'Which Article guarantees equality before law and equal protection of the laws?', 'Article 14 guarantees equality before the law and equal protection of the laws to any person.'),
        ('Article 17', 'Which Article abolishes untouchability and forbids its practice in any form?', 'Article 17 abolishes untouchability and makes enforcement of a disability arising from it an offence punishable by law.'),
        ('Article 21', 'Which Article protects life and personal liberty against deprivation except according to procedure established by law?', 'Article 21 protects life and personal liberty; its text applies to every person, not only citizens.'),
        ('Article 32', 'Which Article guarantees the right to move the Supreme Court for enforcement of Fundamental Rights?', 'Article 32 provides constitutional remedies through the Supreme Court for enforcement of rights conferred by Part III.')
    ])
    polity('Constitutional writs', [
        ('Habeas corpus', 'Which writ is principally used to test the legality of a person’s detention?', 'Habeas corpus requires justification of detention and provides a remedy against unlawful restraint of personal liberty.'),
        ('Mandamus', 'Which writ can command a public authority to perform a legally required public duty?', 'Mandamus directs performance of a public or statutory duty when the legal conditions for the remedy are met.'),
        ('Quo warranto', 'Which writ questions the legal authority by which a person occupies a public office?', 'Quo warranto tests whether a person lawfully holds a public office; it concerns entitlement to that office.'),
        ('Certiorari', 'Which writ can quash an order of a lower court or tribunal for jurisdictional or other recognised legal defects?', 'Certiorari is a supervisory remedy used to quash decisions affected by recognised defects such as lack of jurisdiction or breach of natural justice.')
    ])
    polity('Constitutional bodies', [
        ('Election Commission of India', 'Which constitutional body supervises elections to Parliament and State Legislatures?', 'Article 324 vests supervision, direction and control of the specified elections in the Election Commission of India.'),
        ('Finance Commission', 'Which body is constituted under Article 280 to recommend distribution of tax revenues between the Union and States?', 'The Finance Commission under Article 280 recommends tax distribution and related fiscal arrangements.'),
        ('Comptroller and Auditor General', 'Which constitutional authority audits Union and State accounts under the constitutional and statutory framework?', 'The Comptroller and Auditor General, provided for in Article 148, performs public audit functions prescribed by law.'),
        ('Union Public Service Commission', 'Which body conducts examinations for appointment to Union services under Article 320?', 'The UPSC carries out recruitment-related constitutional functions, including examinations for Union services under Article 320.')
    ])
    polity('Union offices', [
        ('President', 'Under Article 53, in whom is the executive power of the Union vested?', 'Article 53 vests Union executive power in the President, exercised in accordance with the Constitution.'),
        ('Vice-President', 'Who is the ex officio Chairman of the Rajya Sabha?', 'Under Article 64, the Vice-President is ex officio Chairman of the Council of States, or Rajya Sabha.'),
        ('Prime Minister', 'Who heads the Council of Ministers that aids and advises the President?', 'Article 74 provides for a Council of Ministers headed by the Prime Minister to aid and advise the President.'),
        ('Attorney General for India', 'Which law officer is appointed under Article 76 to advise the Government of India on legal matters?', 'The Attorney General is the Union’s constitutional law officer under Article 76 and gives legal advice to the Government of India.')
    ])
    polity('Schedules', [
        ('Seventh Schedule', 'Which Schedule contains the Union, State and Concurrent Lists?', 'The Seventh Schedule distributes legislative subjects among the Union, State and Concurrent Lists.'),
        ('Eighth Schedule', 'Which Schedule lists the languages recognised in its constitutional framework?', 'The Eighth Schedule lists specified languages; inclusion does not make every listed language a Union official language.'),
        ('Tenth Schedule', 'Which Schedule contains provisions concerning disqualification on the ground of defection?', 'The Tenth Schedule contains the anti-defection framework for legislators, subject to its terms and judicial interpretation.'),
        ('Twelfth Schedule', 'Which Schedule lists functions that may be entrusted to Municipalities?', 'The Twelfth Schedule lists municipal matters such as urban planning, water supply and public health, linked to Article 243W.')
    ])
    polity('Constitutional amendments', [
        ('42nd Amendment', 'Which amendment added Fundamental Duties to the Constitution?', 'The 42nd Amendment Act, 1976 inserted Part IVA and Article 51A, creating the original set of Fundamental Duties.'),
        ('44th Amendment', 'Which amendment removed the right to property from the list of Fundamental Rights?', 'The 44th Amendment removed the right to property from Part III and placed constitutional protection in Article 300A.'),
        ('73rd Amendment', 'Which amendment gave constitutional status to the Panchayati Raj framework?', 'The 73rd Amendment Act, 1992 inserted Part IX and the Eleventh Schedule concerning Panchayats.'),
        ('74th Amendment', 'Which amendment introduced Part IXA concerning Municipalities?', 'The 74th Amendment Act, 1992 inserted Part IXA and the Twelfth Schedule concerning Municipalities.')
    ])
    polity('Federal subjects', [
        ('Defence', 'Which of these subjects belongs to the Union List?', 'Defence of India is a Union List subject, reflecting the national character of military security.'),
        ('Police', 'Which of these subjects is specifically a State List entry?', 'Police is a State List subject, subject to the qualifications and other constitutional provisions that apply.'),
        ('Education', 'Which of these subjects appears in the Concurrent List, subject to specified Union List entries?', 'Education is in the Concurrent List, subject to listed Union powers such as standards in higher education.'),
        ('Residuary subjects', 'Which term covers legislative matters not enumerated in the State or Concurrent Lists and assigned to Parliament under Article 248?', 'Parliament has residuary legislative power under Article 248 and Union List Entry 97, including residuary taxation.')
    ])
    polity('Parliamentary control', [
        ('Question Hour', 'Which parliamentary device ordinarily allows members to seek answers from ministers through listed questions?', 'Question Hour provides a formal opportunity for members to question ministers and seek accountability.'),
        ('No-confidence motion', 'Which motion tests whether the Council of Ministers retains the support of the Lok Sabha?', 'A no-confidence motion tests the ministry’s support in the Lok Sabha, consistent with collective responsibility under Article 75(3).'),
        ('Money Bill', 'What constitutional category under Article 110 covers a Bill containing only the specified financial matters?', 'Article 110 defines a Money Bill by specified matters such as taxation and appropriation; incidental provisions may also be included.'),
        ('Joint sitting', 'Which procedure under Article 108 may resolve certain deadlocks between the two Houses on an ordinary Bill?', 'Article 108 allows a joint sitting in specified cases of legislative deadlock; it does not apply to Money Bills or constitutional amendment Bills.')
    ])
    polity('Local government', [
        ('Gram Sabha', 'What body consists of persons registered in the electoral rolls of a village within the Panchayat area?', 'Article 243 defines the Gram Sabha as the body of registered voters of a village within the area of the Panchayat.'),
        ('Gram Panchayat', 'What is the commonly used name for the elected Panchayat at the village level?', 'A Gram Panchayat is the village-level elected local body; it is distinct from the assembly of all registered voters.'),
        ('Municipal Corporation', 'Which type of urban local body is constitutionally envisaged for a larger urban area?', 'Article 243Q provides for a Municipal Corporation for a larger urban area, subject to the constitutional framework.'),
        ('Nagar Panchayat', 'Which urban local body is envisaged for an area transitioning from rural to urban?', 'Article 243Q provides for a Nagar Panchayat for a transitional area moving from rural to urban character.')
    ])
    polity('Judicial and executive powers', [
        ('Article 226', 'Which Article empowers High Courts to issue writs for Fundamental Rights and for other purposes?', 'Article 226 gives High Courts writ jurisdiction for enforcement of Fundamental Rights and for other purposes.'),
        ('Article 123', 'Which Article provides the President’s power to promulgate ordinances when the constitutional conditions are met?', 'Article 123 allows Presidential ordinances when both Houses are not in session together and immediate action is considered necessary.'),
        ('Article 213', 'Which Article concerns a Governor’s power to promulgate ordinances?', 'Article 213 governs a Governor’s ordinance-making power during the specified legislative recess, subject to conditions and limitations.'),
        ('Article 368', 'Which Article lays down Parliament’s power and procedure for amendment of the Constitution?', 'Article 368 lays down the constituent power and principal amendment procedure, including State ratification for specified changes.')
    ])
    polity('Directive Principles', [
        ('Article 39A', 'Which Directive Principle calls for equal justice and free legal aid?', 'Article 39A directs the State to promote equal justice and provide free legal aid so economic or other disabilities do not deny access.'),
        ('Article 40', 'Which Directive Principle asks the State to organise village Panchayats?', 'Article 40 directs the State to organise village Panchayats and give them powers needed to function as units of self-government.'),
        ('Article 44', 'Which Directive Principle concerns a uniform civil code for citizens throughout India?', 'Article 44 directs the State to endeavour to secure a uniform civil code throughout India.'),
        ('Article 48A', 'Which Directive Principle specifically concerns protecting the environment, forests and wildlife?', 'Article 48A directs the State to protect and improve the environment and safeguard forests and wildlife.')
    ])

    # INDIAN HISTORY — 48 questions.
    def history(skill, entries, difficulty='Standard'):
        group('Indian History', skill, entries, CONCEPT, difficulty)
    history('Buddhist historical places', [
        ('Lumbini', 'Which place is associated with the birth of Gautama Buddha?', 'Lumbini, in present-day Nepal, is traditionally identified as the birthplace of Gautama Buddha.'),
        ('Bodh Gaya', 'At which place did Gautama Buddha attain enlightenment?', 'Bodh Gaya in present-day Bihar is associated with the Buddha’s enlightenment beneath the Bodhi tree.'),
        ('Sarnath', 'Which place near Varanasi is associated with the Buddha’s first sermon?', 'Sarnath is associated with the Buddha’s first sermon after enlightenment, often called the turning of the wheel of Dharma.'),
        ('Kushinagar', 'Which place is associated with the Buddha’s mahaparinirvana?', 'Kushinagar in present-day Uttar Pradesh is associated with the Buddha’s death and mahaparinirvana.')
    ], 'Foundation')
    history('Mauryan period', [
        ('Chandragupta Maurya', 'Who founded the Mauryan Empire?', 'Chandragupta Maurya established the Mauryan Empire in the late fourth century BCE after overthrowing the Nanda dynasty.'),
        ('Bindusara', 'Which Mauryan ruler was the son of Chandragupta Maurya and the father of Ashoka?', 'Bindusara ruled between Chandragupta Maurya and Ashoka in the Mauryan succession.'),
        ('Ashoka', 'Which Mauryan ruler recorded his remorse over the Kalinga war in his inscriptions?', 'Ashoka’s Major Rock Edict XIII discusses the suffering caused by the Kalinga war and his commitment to dhamma.'),
        ('Kautilya', 'Which thinker is traditionally associated with the Arthashastra and with advising Chandragupta Maurya?', 'Kautilya, also called Chanakya or Vishnugupta, is traditionally associated with the Arthashastra and Chandragupta Maurya.')
    ])
    history('Classical learning', [
        ('Aryabhata', 'Which scholar composed the Aryabhatiya, an important work on mathematics and astronomy?', 'Aryabhata composed the Aryabhatiya, addressing mathematics and astronomy, including a model of Earth’s rotation.'),
        ('Kalidasa', 'Who is associated with the Sanskrit play Abhijnanashakuntalam?', 'Kalidasa is the Sanskrit poet and dramatist associated with Abhijnanashakuntalam and works such as Meghaduta.'),
        ('Panini', 'Which grammarian composed the Ashtadhyayi?', 'Panini systematised Sanskrit grammar in the Ashtadhyayi, a highly structured collection of grammatical rules.'),
        ('Patanjali', 'Who is associated with the Mahabhashya commentary on grammatical tradition?', 'Patanjali is associated with the Mahabhashya, a major work in the Sanskrit grammatical tradition.')
    ])
    history('Delhi Sultanate', [
        ('Iltutmish', 'Which Delhi Sultan is associated with introducing the silver tanka and copper jital as important coin types?', 'Iltutmish consolidated the early Delhi Sultanate and introduced the silver tanka and copper jital coinage.'),
        ('Razia', 'Which ruler, a daughter of Iltutmish, became Sultan of Delhi?', 'Razia, daughter of Iltutmish, ruled Delhi in the thirteenth century and is known as Razia Sultan.'),
        ('Alauddin Khalji', 'Which Sultan is especially associated with an elaborate system of market and price controls?', 'Alauddin Khalji introduced extensive market regulations and price controls in Delhi as part of his administrative system.'),
        ('Muhammad bin Tughlaq', 'Which Sultan is associated with the experiments of token currency and transfer of the capital to Daulatabad?', 'Muhammad bin Tughlaq attempted token currency and a transfer of the capital from Delhi to Daulatabad.')
    ])
    history('Mughal rulers', [
        ('Babur', 'Which ruler defeated Ibrahim Lodi at the First Battle of Panipat in 1526?', 'Babur defeated Ibrahim Lodi at Panipat in 1526, establishing the foundation of Mughal rule in northern India.'),
        ('Akbar', 'Which Mughal emperor developed the policy of sulh-i kul, or universal peace?', 'Akbar’s governing ideal of sulh-i kul stressed peaceful relations and impartiality among religious communities.'),
        ('Shah Jahan', 'Which Mughal emperor commissioned the Taj Mahal?', 'Shah Jahan commissioned the Taj Mahal at Agra as a mausoleum for Mumtaz Mahal.'),
        ('Aurangzeb', 'Which Mughal emperor annexed the Qutb Shahi kingdom of Golconda in 1687?', 'Aurangzeb conquered Golconda in 1687, ending Qutb Shahi rule there during the Mughal expansion into the Deccan.')
    ])
    history('Bhakti and devotional traditions', [
        ('Kabir', 'Which poet-saint is known for dohas criticising empty ritual and emphasising devotion beyond religious divisions?', 'Kabir’s verses challenge ritualism and social divisions and emphasise a direct relationship with the divine.'),
        ('Guru Nanak', 'Who founded the Sikh religious tradition?', 'Guru Nanak founded the Sikh tradition, teaching devotion to one God, honest work and sharing with others.'),
        ('Mirabai', 'Which devotional poet is especially known for songs expressing devotion to Krishna?', 'Mirabai is associated with intensely personal devotional poetry addressed to Krishna.'),
        ('Chaitanya', 'Which Bengal-based devotional teacher is strongly associated with congregational Krishna sankirtana?', 'Chaitanya promoted Krishna devotion through collective singing, or sankirtana, particularly in Bengal and Odisha.')
    ])
    history('Colonial land revenue', [
        ('Permanent Settlement', 'Which revenue arrangement fixed the government’s land revenue demand on zamindars in perpetuity in Bengal?', 'The Permanent Settlement of 1793 fixed the revenue demand on zamindars in Bengal, with consequences for landlords and cultivators.'),
        ('Ryotwari system', 'In which colonial revenue system did the State generally settle revenue directly with individual cultivators?', 'The Ryotwari system treated individual cultivators, or ryots, as the parties responsible for paying assessed land revenue.'),
        ('Mahalwari system', 'Which colonial revenue system made a village estate or mahal the unit of revenue settlement?', 'The Mahalwari system assessed revenue on a mahal, commonly a village or estate, with collective responsibility arrangements.'),
        ('Subsidiary Alliance', 'Which British political arrangement required an Indian ruler to maintain a British force under treaty conditions?', 'A Subsidiary Alliance was a political and military treaty arrangement involving British troops, payment and restrictions on a ruler’s independence.')
    ])
    history('Social reformers', [
        ('Raja Rammohan Roy', 'Which reformer was closely associated with the founding of the Brahmo Sabha in 1828?', 'Raja Rammohan Roy founded the Brahmo Sabha in 1828, a precursor to the Brahmo Samaj, and advocated social and religious reform.'),
        ('Dayanand Saraswati', 'Who founded the Arya Samaj in 1875?', 'Dayanand Saraswati founded the Arya Samaj and advocated a return to the authority of the Vedas.'),
        ('Swami Vivekananda', 'Who founded the Ramakrishna Mission in 1897?', 'Swami Vivekananda founded the Ramakrishna Mission, combining spiritual teaching with organised service.'),
        ('Jyotirao Phule', 'Who founded the Satyashodhak Samaj in 1873?', 'Jyotirao Phule founded the Satyashodhak Samaj to challenge caste oppression and promote social equality and education.')
    ])
    history('Colonial constitutional changes', [
        ('Regulating Act, 1773', 'Which Act created the office of Governor-General of Bengal and began parliamentary regulation of Company rule?', 'The Regulating Act of 1773 created the Governor-General of Bengal with a council and increased parliamentary control over Company administration.'),
        ('Government of India Act, 1858', 'Which Act transferred the government of British India from the East India Company to the Crown?', 'The Government of India Act, 1858 ended Company government and transferred administration to the British Crown.'),
        ('Indian Councils Act, 1909', 'Which Act introduced separate electorates for Muslims in British India?', 'The Indian Councils Act, 1909, associated with the Morley–Minto reforms, introduced Muslim separate electorates.'),
        ('Government of India Act, 1919', 'Which Act introduced dyarchy in the provinces?', 'The Government of India Act, 1919 divided provincial subjects into transferred and reserved categories under dyarchy.')
    ])
    history('Mass movements', [
        ('Swadeshi movement', 'Which movement expanded after the partition of Bengal in 1905 and promoted indigenous goods and boycott?', 'The Swadeshi movement grew in response to the 1905 partition of Bengal, using boycott and promotion of indigenous production.'),
        ('Non-Cooperation Movement', 'Which movement begun in 1920 urged withdrawal from colonial institutions and was suspended after Chauri Chaura?', 'The Non-Cooperation Movement used withdrawal from colonial institutions; Gandhi suspended it in 1922 after the Chauri Chaura violence.'),
        ('Civil Disobedience Movement', 'Which movement began with Gandhi’s Salt March in 1930?', 'The Salt March launched the Civil Disobedience Movement, openly challenging colonial laws such as the salt monopoly.'),
        ('Quit India Movement', 'Which movement was launched in August 1942 with the demand for an immediate end to British rule?', 'The Quit India Movement was launched in August 1942 and demanded the immediate withdrawal of British rule.')
    ])
    history('Congress sessions and agreements', [
        ('Surat, 1907', 'At which Congress session did the split between Moderates and Extremists occur?', 'The Surat session of 1907 saw a split between the Moderate and Extremist groups within the Indian National Congress.'),
        ('Lucknow, 1916', 'Which session is associated with Congress–League cooperation through the Lucknow Pact?', 'The 1916 Lucknow session is associated with the Congress–Muslim League agreement and reunion of Congress factions.'),
        ('Lahore, 1929', 'Which Congress session adopted Purna Swaraj as its objective?', 'The Lahore session of December 1929 adopted complete independence, or Purna Swaraj, as the Congress objective.'),
        ('Karachi, 1931', 'Which Congress session adopted an important resolution on Fundamental Rights and a national economic programme?', 'The Karachi session of 1931 adopted resolutions addressing Fundamental Rights and economic policy goals.')
    ])
    history('Freedom struggle milestones', [
        ('Champaran, 1917', 'Which struggle concerned indigo cultivators and became Gandhi’s first major satyagraha in India?', 'The Champaran struggle of 1917 addressed the grievances of indigo cultivators in Bihar.'),
        ('Kheda, 1918', 'Which satyagraha in Gujarat concerned relief from land revenue after crop failure?', 'The Kheda satyagraha of 1918 sought revenue relief for cultivators affected by crop failure in Gujarat.'),
        ('Jallianwala Bagh, 1919', 'Which event involved British troops firing on a gathering in Amritsar on 13 April 1919?', 'The Jallianwala Bagh massacre occurred in Amritsar on 13 April 1919, when troops under Dyer fired on a gathering.'),
        ('Dandi, 1930', 'At which coastal village did Gandhi symbolically break the salt law at the end of his 1930 march?', 'Gandhi reached Dandi in April 1930 and broke the salt law, making salt a symbol of resistance to colonial rule.')
    ])

    # GEOGRAPHY — 48 questions.
    def geography(skill, entries, difficulty='Standard'):
        group('Geography', skill, entries, CONCEPT, difficulty)
    geography('Coordinates and reference lines', [
        ('Equator', 'Which imaginary circle divides Earth into the Northern and Southern Hemispheres?', 'The Equator is the 0° latitude circle, dividing the planet into Northern and Southern Hemispheres.'),
        ('Prime Meridian', 'Which reference meridian is assigned 0° longitude?', 'The Prime Meridian is the conventional 0° longitude reference passing through Greenwich.'),
        ('Tropic of Cancer', 'Which major latitude circle at about 23½° N passes through India?', 'The Tropic of Cancer lies at approximately 23½° N and marks the northern limit of the overhead midday Sun.'),
        ('Arctic Circle', 'Which major latitude circle lies at approximately 66½° N?', 'The Arctic Circle is near 66½° N, marking the approximate southern limit of at least one polar day and night each year.')
    ], 'Foundation')
    geography('Earth processes', [
        ('Rotation', 'Which motion of Earth chiefly produces the daily cycle of day and night?', 'Earth’s rotation about its axis brings different places into and out of sunlight each day.'),
        ('Revolution', 'Which motion is Earth’s annual journey around the Sun?', 'Revolution is Earth’s orbital movement around the Sun, completed in about one year.'),
        ('Axial tilt', 'Which feature, combined with Earth’s revolution, is the principal cause of the seasons?', 'Earth’s tilted axis changes the angle and duration of sunlight through the year; seasons are not caused mainly by Earth–Sun distance.'),
        ('Coriolis effect', 'Which apparent effect deflects large-scale moving air to the right in the Northern Hemisphere?', 'The Coriolis effect arises in Earth’s rotating frame and deflects large-scale motion rightward in the Northern Hemisphere and leftward in the Southern.')
    ])
    geography('Rock cycle', [
        ('Igneous rock', 'What type of rock forms when magma or lava cools and solidifies?', 'Igneous rocks form by the cooling and solidification of molten material; examples include granite and basalt.'),
        ('Sedimentary rock', 'What type of rock commonly forms through deposition, compaction and cementation of sediments?', 'Sedimentary rocks form from accumulated sediments or chemical and organic deposits; sandstone is a common example.'),
        ('Metamorphic rock', 'What type of rock forms when existing rock is changed by heat and pressure without complete melting?', 'Metamorphic rocks result from alteration under heat, pressure or reactive fluids; marble forms from limestone.'),
        ('Magma', 'What is molten rock beneath Earth’s surface called?', 'Magma is molten or partly molten rock below Earth’s surface; when erupted at the surface it is called lava.')
    ])
    geography('Weathering and erosion', [
        ('Weathering', 'What process breaks down rock in place without necessarily transporting it?', 'Weathering breaks down or chemically alters rock at its location through physical, chemical or biological processes.'),
        ('Erosion', 'What process removes and transports rock or soil by water, wind, ice or other agents?', 'Erosion involves removal and movement of material, distinguishing it from breakdown in place.'),
        ('Deposition', 'What occurs when a river or wind loses the capacity to carry sediment and leaves it behind?', 'Deposition is the laying down of transported material when the transporting agent loses energy or capacity.'),
        ('Mass movement', 'What term describes downslope movement of material primarily under gravity?', 'Mass movement moves soil or rock downslope under gravity, as in landslides, without requiring a flowing transport medium.')
    ])
    geography('Atmospheric layers', [
        ('Troposphere', 'In which atmospheric layer does most ordinary weather occur?', 'The troposphere is the lowest atmospheric layer and contains most water vapour and weather systems.'),
        ('Stratosphere', 'Which layer above the troposphere contains most of the atmosphere’s ozone layer?', 'The stratosphere contains the ozone-rich region that absorbs much of the Sun’s harmful ultraviolet radiation.'),
        ('Mesosphere', 'In which atmospheric layer do many meteors burn up?', 'Many meteors burn up in the mesosphere, which lies above the stratosphere and below the thermosphere.'),
        ('Thermosphere', 'Which atmospheric layer above the mesosphere has very high kinetic temperatures due to absorption of high-energy radiation?', 'The thermosphere absorbs high-energy solar radiation; despite high particle temperatures its air is extremely thin.')
    ])
    geography('Weather measurements', [
        ('Barometer', 'Which instrument measures atmospheric pressure?', 'A barometer measures atmospheric pressure, commonly expressed in hectopascals or millibars.'),
        ('Anemometer', 'Which instrument measures wind speed?', 'An anemometer measures wind speed; a wind vane indicates wind direction.'),
        ('Hygrometer', 'Which instrument measures humidity?', 'A hygrometer measures atmospheric moisture; relative humidity compares actual vapour with saturation at that temperature.'),
        ('Rain gauge', 'Which instrument measures precipitation collected over a specified area?', 'A rain gauge measures collected precipitation, usually reported as an equivalent depth in millimetres.')
    ], 'Foundation')
    geography('Rainfall mechanisms', [
        ('Convectional rainfall', 'Which rainfall type develops when strong surface heating causes moist air to rise?', 'Convectional rainfall follows the ascent, cooling and condensation of air heated near the surface.'),
        ('Orographic rainfall', 'Which rainfall type results when moist air is forced to rise over a mountain barrier?', 'Orographic rainfall occurs as moist air rises on a windward slope, cools and condenses.'),
        ('Frontal rainfall', 'Which rainfall type occurs when warm air is lifted over cooler air along a weather front?', 'Frontal rainfall develops where air masses meet and warmer air is forced upward over denser cooler air.'),
        ('Rain shadow', 'What term describes the relatively dry area on the leeward side of a mountain barrier?', 'A rain shadow forms where air descends after losing moisture on the windward side and becomes relatively warmer and drier.')
    ])
    geography('Indian soils', [
        ('Alluvial soil', 'Which widespread soil type is deposited by rivers and is prominent in the northern plains?', 'Alluvial soils develop from river-deposited sediments and cover extensive parts of the Indo-Gangetic plains.'),
        ('Black soil', 'Which clay-rich soil is noted for moisture retention and association with cotton cultivation?', 'Black soils have high clay content, retain moisture and often develop over basaltic parent material in the Deccan.'),
        ('Laterite soil', 'Which soil commonly develops under intense leaching in warm regions with heavy rainfall?', 'Laterite soils form under strong weathering and leaching; iron and aluminium compounds remain relatively concentrated.'),
        ('Red soil', 'Which soil group commonly gets its reddish colour from iron oxides in weathered parent material?', 'Red soils owe much of their colour to iron oxides and commonly develop from weathering of crystalline rocks.')
    ])
    geography('Indian river systems', [
        ('Narmada', 'Which river flows west through a rift valley between the Vindhya and Satpura ranges?', 'The Narmada flows westward through a rift valley between the Vindhya and Satpura ranges into the Arabian Sea.'),
        ('Godavari', 'Which river rises near Trimbakeshwar and is the largest Peninsular Indian river basin?', 'The Godavari rises near Trimbakeshwar in Maharashtra and drains the largest basin among Peninsular Indian rivers.'),
        ('Krishna', 'Which major river rises near Mahabaleshwar and has the Bhima and Tungabhadra as tributaries?', 'The Krishna rises near Mahabaleshwar; its important tributaries include the Bhima and Tungabhadra.'),
        ('Brahmaputra', 'Which river is known as the Yarlung Tsangpo in Tibet before entering India?', 'The Yarlung Tsangpo becomes the Siang or Dihang in Arunachal Pradesh and then the Brahmaputra in Assam.')
    ])
    geography('Coastal and river landforms', [
        ('Delta', 'Which depositional landform develops near a river mouth when sediment accumulates and channels may split into distributaries?', 'A delta forms where river sediment accumulates at a mouth faster than waves and currents can remove it.'),
        ('Estuary', 'What is a tidal river-mouth environment where freshwater mixes with seawater called?', 'An estuary is a partially enclosed coastal water body influenced by both river freshwater and marine tides.'),
        ('Meander', 'What is a broad winding bend in a river channel called?', 'A meander is a river bend shaped by erosion on the outer bank and deposition on the inner bank.'),
        ('Oxbow lake', 'What lake can form when a river cuts through the narrow neck of a meander?', 'An oxbow lake is an abandoned meander loop separated from the active river channel.')
    ])
    geography('Agricultural seasons', [
        ('Kharif', 'Which crop season is generally linked to sowing with the onset of the southwest monsoon?', 'Kharif crops are generally sown with the monsoon and harvested after the rainy season; paddy is an important example.'),
        ('Rabi', 'Which crop season generally involves winter sowing and spring harvesting in northern India?', 'Rabi crops are generally sown in the cooler season and harvested in spring; wheat is a major example.'),
        ('Zaid', 'What is the short agricultural season between the principal rabi and kharif seasons called?', 'Zaid is the short summer cropping season between rabi and kharif; irrigated vegetables and melons may be grown.'),
        ('Perennial cropping', 'Which term describes cultivation of plants that remain productive over more than two years?', 'Perennial crops live for several years, unlike annual crops restricted to one life cycle; plantation crops often fit this category.')
    ])
    geography('Natural vegetation', [
        ('Tropical evergreen forest', 'Which forest type is associated with persistently high rainfall and no marked collective leafless season?', 'Tropical evergreen forests occur in warm, wet regions; different species shed leaves at different times so the canopy remains green.'),
        ('Tropical deciduous forest', 'Which forest type commonly sheds leaves in the dry season to limit water loss?', 'Tropical deciduous forests occur in seasonal climates, with many trees shedding leaves during the dry period.'),
        ('Thorn scrub', 'Which vegetation type is adapted to low rainfall through features such as small leaves and thorns?', 'Thorn scrub contains drought-adapted plants suited to dry and semi-arid environments.'),
        ('Mangrove forest', 'Which coastal vegetation type tolerates saline, waterlogged intertidal conditions?', 'Mangroves are salt-tolerant plants of intertidal environments, often with specialised roots for aeration or support.')
    ])

    # ECONOMY — 40 questions, with no mutable rates or current rankings.
    def economy(skill, entries, source=None):
        group('Indian Economy', skill, entries, source or CONCEPT)
    economy('Sectors of production', [
        ('Primary sector', 'A farmer grows paddy and a fisher harvests fish. To which broad economic sector do these activities belong?', 'The primary sector directly uses natural resources through activities such as agriculture, fishing and mining.'),
        ('Secondary sector', 'A factory converts raw cotton into cloth. Which sector is primarily represented?', 'The secondary sector transforms raw materials into manufactured goods; construction is also included in this broad classification.'),
        ('Tertiary sector', 'A company transports goods and provides warehousing. Which sector does this service activity belong to?', 'The tertiary sector provides services, including transport, trade, education, banking and health services.'),
        ('Household own-use services outside the usual GDP production boundary', 'Unpaid cooking by a family member for that same household is generally placed in which category in national accounts?', 'Unpaid domestic services produced and consumed within the same household are generally excluded from the usual GDP production boundary; this does not mean they lack social value.')
    ])
    economy('Output measurement', [
        ('Nominal GDP', 'Which measure values current domestic production at current-year prices?', 'Nominal GDP values final domestic production at current prices, so it changes with both quantities and prices.'),
        ('Real GDP', 'Which GDP measure adjusts for price changes to track changes in production volume?', 'Real GDP measures output using constant-price or volume methods, allowing comparison of production apart from price changes.'),
        ('Gross value added', 'What measure equals the value of output minus the value of intermediate consumption?', 'Gross value added subtracts intermediate consumption from output, avoiding repeated counting of inputs across production stages.'),
        ('Per capita income', 'Which measure divides an aggregate income figure by population?', 'Per capita income is average income per person. It is useful for comparison but does not reveal how income is distributed.')
    ])
    economy('Price-level changes', [
        ('Inflation', 'What is a sustained increase in the general price level called?', 'Inflation is a sustained rise in the general price level, reducing the purchasing power of a unit of money.'),
        ('Disinflation', 'Prices are still rising, but their annual rate of increase falls from 8% to 5%. What is this called?', 'Disinflation is a reduction in the inflation rate; the overall price level may still be increasing.'),
        ('Deflation', 'What is a sustained decline in the general price level called?', 'Deflation means the general price level is falling, unlike disinflation, in which positive inflation merely slows.'),
        ('Stagflation', 'What term describes high inflation occurring alongside stagnant economic activity and weak employment?', 'Stagflation combines inflation with economic stagnation, posing difficulty because policies addressing one problem may worsen the other.')
    ])
    economy('Monetary tools', [
        ('Repo operation', 'Which RBI operation supplies liquidity to banks against eligible securities with an agreement to reverse the transaction?', 'A repo injects liquidity through a sale-and-repurchase arrangement involving eligible collateral; the policy repo rate is a key monetary signal.'),
        ('Cash Reserve Ratio', 'Which requirement concerns the specified cash balance that banks must maintain with the RBI against their relevant liabilities?', 'The Cash Reserve Ratio requires banks to maintain specified cash balances with the RBI; a higher requirement generally reduces lendable liquidity.'),
        ('Statutory Liquidity Ratio', 'Which requirement concerns the prescribed holding of specified liquid assets such as cash, gold and approved securities?', 'The Statutory Liquidity Ratio requires prescribed liquid assets against relevant liabilities; it differs from the cash balance held with RBI under CRR.'),
        ('Open market purchase', 'Which RBI action buys government securities outright to inject durable liquidity into the banking system?', 'An open market purchase injects liquidity by buying government securities outright; an open market sale absorbs liquidity.')
    ], {'title':'RBI — monetary policy and liquidity-management concepts (rates intentionally omitted)','page':None,'url':'https://rbi.org.in/scripts/PublicationsView.aspx?Id=18086'})
    economy('Budget deficits', [
        ('Revenue deficit', 'What is revenue expenditure minus revenue receipts called?', 'Revenue deficit is the excess of revenue expenditure over revenue receipts and indicates a shortfall on the revenue account.'),
        ('Fiscal deficit', 'What is total government expenditure minus total receipts excluding borrowings called?', 'Fiscal deficit is the gap between total expenditure and non-borrowing receipts, indicating the government’s overall borrowing requirement.'),
        ('Primary deficit', 'What is fiscal deficit minus interest payments called?', 'Primary deficit removes interest payments from the fiscal deficit, showing the gap apart from interest on past debt.'),
        ('Budget surplus', 'In a simplified budget comparison, what is the situation where receipts exceed expenditure called?', 'A budget surplus means receipts exceed the expenditure being compared; the exact account and receipt definition must be specified.')
    ])
    economy('Tax concepts', [
        ('Direct tax', 'A tax on an individual’s income is usually classified under which broad category?', 'A direct tax is imposed directly on income or wealth of the liable person; income tax is a standard example.'),
        ('Indirect tax', 'A tax charged on the supply of goods and services is usually classified under which broad category?', 'An indirect tax is imposed on transactions or supplies and may be passed through in prices; GST is a standard example.'),
        ('Progressive tax', 'What tax structure has an average tax rate that rises as taxable income rises?', 'A progressive tax takes a higher proportion of income as income increases, subject to the specific tax schedule.'),
        ('Regressive tax burden', 'What term describes a tax burden that takes a larger share of income from lower-income households?', 'A regressive burden falls proportionately more heavily on lower-income households, even if the nominal tax rate is identical.')
    ])
    economy('Unemployment concepts', [
        ('Seasonal unemployment', 'Farm workers have work during sowing and harvest but little work in the intervening months. What form of unemployment is illustrated?', 'Seasonal unemployment arises when work is available only during particular seasons of the year.'),
        ('Disguised unemployment', 'Six people work on a farm, but output would remain unchanged if two left. What concept does this illustrate?', 'Disguised unemployment occurs when additional workers contribute little or no additional output, though they appear employed.'),
        ('Frictional unemployment', 'A worker is briefly unemployed while moving voluntarily between suitable jobs. What concept best fits?', 'Frictional unemployment results from the time needed for workers and jobs to find an appropriate match.'),
        ('Structural unemployment', 'A worker’s skills no longer match the jobs available after a major technological change. What form of unemployment is this?', 'Structural unemployment arises from a mismatch between worker skills or locations and the structure of labour demand.')
    ])
    economy('International transactions', [
        ('Export', 'An Indian producer sells goods to a buyer abroad. What is this transaction called from India’s perspective?', 'An export supplies domestically produced goods or services to non-residents or foreign markets.'),
        ('Import', 'An Indian company buys a machine from a foreign supplier. What is this transaction called from India’s perspective?', 'An import acquires goods or services from foreign suppliers or non-residents.'),
        ('Balance of trade', 'Which balance is the value of merchandise exports minus merchandise imports?', 'The merchandise balance of trade compares goods exports with goods imports; it does not by itself cover all external transactions.'),
        ('Balance of payments', 'Which accounting statement records transactions between residents of an economy and the rest of the world over a period?', 'The balance of payments records current, capital and financial transactions with the rest of the world within its accounting framework.')
    ])
    economy('Choice and markets', [
        ('Opportunity cost', 'A student uses an hour for study instead of paid work. What is the value of the next-best forgone alternative called?', 'Opportunity cost is the value of the next-best alternative sacrificed when a choice is made.'),
        ('Demand', 'Which market concept describes quantities consumers are willing and able to buy at different prices?', 'Demand relates the quantity buyers are willing and able to purchase to price, with other determinants held constant.'),
        ('Supply', 'Which market concept describes quantities producers are willing and able to offer at different prices?', 'Supply relates the quantity sellers are willing and able to offer to price, with other determinants held constant.'),
        ('Market equilibrium', 'What situation occurs at a price where quantity demanded equals quantity supplied?', 'Market equilibrium occurs where planned purchases and planned sales match at a given price, absent other constraints.')
    ])
    economy('Food-security mechanisms', [
        ('Minimum support price', 'What announced agricultural price is intended to provide a price-support signal to farmers?', 'A minimum support price is an announced support price for specified crops; an announcement alone does not guarantee procurement of every farmer’s entire crop.'),
        ('Public procurement', 'What is the government’s actual purchase of agricultural produce under specified arrangements called?', 'Public procurement is the actual purchase of produce by public agencies; it is distinct from merely announcing a support price.'),
        ('Buffer stock', 'What is a reserve of food grains maintained to support supply management and food security called?', 'Buffer stocks are reserves used to manage supply, support distribution and respond to shortages within policy arrangements.'),
        ('Public Distribution System', 'What distribution mechanism supplies specified essential commodities through a network of fair-price shops?', 'The Public Distribution System distributes specified commodities through fair-price shops to eligible households under applicable arrangements.')
    ])

    # ENVIRONMENT & SOCIAL AWARENESS — 32 questions.
    def social(skill, entries, source=None):
        group('Environment & Social Awareness', skill, entries, source or CONCEPT)
    social('Ecosystem roles', [
        ('Producer', 'A green plant makes organic food from inorganic materials using sunlight. Which ecosystem role does it perform?', 'Producers, or autotrophs, build organic matter from inorganic sources and form the energy-entry base of most food webs.'),
        ('Primary consumer', 'A grasshopper eats grass. What is its feeding position in this simple food chain?', 'Primary consumers feed directly on producers and are generally herbivores in simple food-chain models.'),
        ('Secondary consumer', 'In the chain grass → grasshopper → frog, what is the frog’s trophic role?', 'A secondary consumer feeds on primary consumers; the frog eats the herbivorous grasshopper in the stated chain.'),
        ('Decomposer', 'Fungi break down dead organic material and release nutrients. What ecological role do they perform?', 'Decomposers break down dead material and recycle nutrients into forms that can be used again in ecosystems.')
    ])
    social('Environmental processes', [
        ('Eutrophication', 'A lake receives excess nutrients, develops an algal bloom and later loses dissolved oxygen. Which process is illustrated?', 'Eutrophication is nutrient enrichment that can stimulate algal growth; decomposition can deplete oxygen and damage aquatic life.'),
        ('Biomagnification', 'A persistent pollutant reaches higher concentrations at successive levels of a food chain. What is this process?', 'Biomagnification increases concentrations of persistent contaminants at higher trophic levels through feeding relationships.'),
        ('Bioaccumulation', 'A pollutant builds up within one organism because uptake exceeds removal. What is this called?', 'Bioaccumulation is contaminant buildup within an organism over time; it does not necessarily imply an increase across trophic levels.'),
        ('Ecological succession', 'A disturbed site is gradually colonised by changing communities of organisms. Which process is described?', 'Ecological succession is the change in community composition over time, often following disturbance or formation of a new habitat.')
    ])
    social('Conservation strategies', [
        ('In situ conservation', 'Protecting a wild species within its natural habitat is which form of conservation?', 'In situ conservation protects species in their natural habitats and maintains ecological interactions.'),
        ('Ex situ conservation', 'Preserving threatened plant seeds in a seed bank is which form of conservation?', 'Ex situ conservation maintains biological material outside its natural habitat, such as in seed banks or captive-breeding programmes.'),
        ('Habitat corridor', 'What conservation feature connects separated habitats to support movement and gene flow?', 'A habitat corridor links habitat patches so organisms can move between them, reducing the effects of fragmentation.'),
        ('Restoration ecology', 'Re-establishing native vegetation and ecological processes on a degraded site belongs to which field?', 'Ecological restoration seeks to assist recovery of degraded ecosystems, including their native communities and functions.')
    ])
    social('Waste hierarchy', [
        ('Reduce', 'Choosing to buy only what is needed so that less waste is produced illustrates which action?', 'Reducing waste prevents resource use and waste generation at the source, usually the preferred first step.'),
        ('Reuse', 'Refilling a durable water bottle many times illustrates which action?', 'Reuse extends the useful life of an item without necessarily reprocessing its material.'),
        ('Recycle', 'Processing used paper into material for new paper products illustrates which action?', 'Recycling reprocesses discarded materials into usable raw materials or new products.'),
        ('Composting', 'Controlled biological decomposition of segregated food scraps into soil amendment illustrates which process?', 'Composting uses biological decomposition of suitable organic waste to produce a stabilised soil amendment.')
    ])
    social('Social inclusion', [
        ('Equality', 'Giving every applicant the same formal eligibility rule illustrates which principle?', 'Equality concerns equal status or treatment; identical formal rules can still leave underlying disadvantages unaddressed.'),
        ('Equity', 'Providing additional support to learners who face greater barriers aims at which principle?', 'Equity addresses differing needs and barriers so people can have a fair opportunity to achieve outcomes.'),
        ('Accessibility', 'Installing ramps and providing screen-reader-compatible information primarily improve what?', 'Accessibility removes physical, communication and digital barriers so people with different abilities can use services.'),
        ('Social exclusion', 'Systematically preventing a community from participating in education, employment or civic life illustrates what?', 'Social exclusion is the process of denying people participation, opportunities or resources in social and economic life.')
    ])
    social('Population indicators', [
        ('Literacy rate', 'Which indicator measures the proportion of a defined population able to read and write with understanding?', 'A literacy rate measures literacy within a defined age group; comparisons require the same definition and population base.'),
        ('Infant mortality rate', 'Which indicator counts deaths before age one per 1,000 live births in a given period?', 'The infant mortality rate measures deaths of infants under one year per 1,000 live births.'),
        ('Sex ratio in the Indian census convention', 'Which indicator is traditionally expressed in India as the number of females per 1,000 males?', 'The Indian census sex-ratio convention reports females per 1,000 males; this differs from some international reporting conventions.'),
        ('Dependency ratio', 'Which indicator compares the population in conventionally dependent age groups with the working-age population?', 'A dependency ratio compares designated younger and older age groups with the working-age group; exact age boundaries must be specified.')
    ])
    social('Community health concepts', [
        ('Safe sanitation', 'Preventing human waste from contaminating drinking-water sources is mainly an example of what intervention?', 'Safe sanitation separates human waste from human contact and water supplies, interrupting transmission of many infections.'),
        ('Immunisation', 'Providing a vaccine to develop specific protection against a disease is what intervention?', 'Immunisation develops immune protection against specific pathogens; vaccines do not treat every cause of illness.'),
        ('Vector control', 'Removing stagnant-water breeding sites of mosquitoes primarily illustrates what measure?', 'Vector control reduces organisms that transmit pathogens, for example by limiting mosquito breeding sites.'),
        ('Health education', 'Teaching a community how infections spread and how to adopt preventive practices is an example of what?', 'Health education builds knowledge and practical skills for healthier behaviour; it complements services and environmental measures.')
    ])
    social('Disaster-risk concepts', [
        ('Hazard', 'A flood, earthquake or industrial chemical leak with the potential to cause harm is described as what?', 'A hazard is a potentially damaging event, process or condition; the resulting risk also depends on exposure and vulnerability.'),
        ('Exposure', 'The presence of people and buildings in a flood-prone area represents which component of disaster risk?', 'Exposure concerns people, property and other assets located where hazards may occur.'),
        ('Vulnerability', 'Poorly built housing and limited capacity to cope with a flood illustrate which risk component?', 'Vulnerability comprises conditions that make people or assets more susceptible to harm from a hazard.'),
        ('Preparedness', 'Practising evacuation and maintaining an emergency communication plan primarily illustrate which activity?', 'Preparedness builds the capabilities needed to anticipate, respond to and recover from likely emergencies.')
    ], {'title':'UNDRR — disaster-risk terminology','page':None,'url':'https://www.undrr.org/terminology'})

    # TELANGANA — 64 questions. Local sources stay private; no file URLs are published.
    def ref(title, url=None, page=None):
        return {'title': title, 'page': page, 'url': url}
    def telangana(skill, entries, source=None, difficulty='Standard'):
        group('Telangana', skill, entries, source or CONCEPT, difficulty)
    ts_arts = ref('Telangana Tourism — Arts & Crafts', 'https://www.tourism.telangana.gov.in/page/arts-crafts')
    ts_nature = ref('Telangana Tourism — Eco-Tourism', 'https://tourism.telangana.gov.in/experience/nature')
    ts_mha = ref('Ministry of Home Affairs — Committee for Consultations on the Situation in Andhra Pradesh, 2010', 'https://www.mha.gov.in/sites/default/files/CCSAP-REPORT-060111.pdf')
    struggle = 'Telangana Armed Struggle.pdf — supplied private reference'
    movement = 'Telangana Movement (Part 1).pdf — supplied private reference'
    telangana('State symbols', [
        ('Palapitta', 'What is Telangana’s state bird, commonly identified as the Indian roller?', 'Palapitta, the Indian roller, is Telangana’s state bird.'),
        ('Jinka', 'Which Telugu name identifies Telangana’s state animal, the deer?', 'Jinka, meaning deer, is designated as Telangana’s state animal.'),
        ('Jammi', 'Which tree is designated as Telangana’s state tree?', 'Jammi, Prosopis cineraria, is Telangana’s state tree and is associated with Dasara traditions.'),
        ('Tangedu', 'Which flower, used in Bathukamma arrangements, is Telangana’s state flower?', 'Tangedu, commonly known as Tanner’s cassia, is Telangana’s state flower.')
    ], TS_SYMBOLS, 'Foundation')
    telangana('Festivals', [
        ('Bathukamma', 'Which Telangana festival centres on seasonal flower arrangements and collective songs by women?', 'Bathukamma is the floral festival associated with arrangements of seasonal flowers and women’s collective singing.'),
        ('Bonalu', 'Which Telangana festival features offerings to Mahakali, traditionally carried in decorated pots?', 'Bonalu is a festival of offerings to Mahakali, including food carried in decorated pots.'),
        ('Sammakka–Saralamma Jatara', 'Which major tribal festival is associated with Medaram and the deities Sammakka and Saralamma?', 'The Sammakka–Saralamma Jatara at Medaram is a major tribal religious gathering in Telangana.'),
        ('Ugadi', 'Which festival marks the traditional Telugu New Year?', 'Ugadi marks the beginning of the Telugu calendar year and is celebrated in Telangana and neighbouring regions.')
    ], TS_CULTURE, 'Foundation')
    telangana('Craft traditions', [
        ('Pochampally Ikat', 'Which Telangana textile tradition creates patterns by resist-dyeing yarn before weaving?', 'Pochampally Ikat uses resist-dyed yarn arranged during weaving to create characteristic patterns.'),
        ('Cheriyal scroll painting', 'Which Telangana art form uses painted narrative scrolls to accompany storytelling?', 'Cheriyal scroll painting presents narrative scenes associated with local storytelling traditions.'),
        ('Pembarthi brassware', 'Which craft is especially associated with decorative brass metalwork in Telangana?', 'Pembarthi is known for brass metalwork, including elaborately worked decorative and ritual objects.'),
        ('Dokra', 'Which traditional metal craft uses the lost-wax casting technique?', 'Dokra metal craft uses lost-wax casting and is associated with tribal artistic traditions, including those of the Adilabad region.')
    ], ts_arts)
    telangana('Regional dynasties', [
        ('Kakatiyas', 'Which dynasty is particularly associated with Warangal and the Ramappa Temple?', 'The Kakatiyas ruled from the Warangal region and are associated with Ramappa Temple and extensive tank-building traditions.'),
        ('Qutb Shahis', 'Which dynasty ruled Golconda and founded Hyderabad in the late sixteenth century?', 'The Qutb Shahi dynasty ruled Golconda; Muhammad Quli Qutb Shah founded Hyderabad and built Charminar in 1591.'),
        ('Asaf Jahis', 'The Nizams of Hyderabad belonged to which ruling dynasty?', 'The Asaf Jahi dynasty ruled Hyderabad under the title of Nizam, beginning in the eighteenth century.'),
        ('Satavahanas', 'Which ancient Deccan dynasty preceded the Kakatiyas, Qutb Shahis and Asaf Jahis by many centuries?', 'The Satavahanas were an ancient Deccan ruling dynasty; the Kakatiya, Qutb Shahi and Asaf Jahi periods came much later.')
    ], TS_CULTURE)
    telangana('Modern regional chronology', [
        ('1948', 'In which year did Hyderabad State come under the Indian Union following military action?', 'Hyderabad State was integrated into the Indian Union in 1948 following the September military action.'),
        ('1956', 'In which year did the Telangana region of Hyderabad State merge with Andhra State to form Andhra Pradesh?', 'Andhra Pradesh was formed on 1 November 1956 by merging Andhra State with the Telangana region of Hyderabad State.'),
        ('1969', 'Which year is associated with the major first-phase Jai Telangana agitation after the formation of Andhra Pradesh?', 'The 1969 agitation pressed Telangana safeguards and the demand for a separate state, involving students and employees.'),
        ('2014', 'In which year was Telangana formed as a separate state on 2 June?', 'Telangana became a separate state on 2 June 2014 under the Andhra Pradesh Reorganisation Act, 2014.')
    ], [TS_PROFILE, TS_PROFILE, ref(movement, page=5), TS_PROFILE])
    telangana('Safeguards and arrangements', [
        ('Gentlemen’s Agreement', 'Which 1956 agreement set out safeguards for Telangana before the formation of Andhra Pradesh?', 'The Gentlemen’s Agreement of 1956 set out safeguards concerning Telangana’s finances, representation, education and employment.'),
        ('Six-Point Formula', 'Which 1973 political arrangement sought to address regional development and local opportunities after the Telangana and Jai Andhra agitations?', 'The Six-Point Formula of 1973 sought arrangements for regional development, education and local employment opportunities.'),
        ('Article 371D', 'Which constitutional Article is associated with special provisions concerning equitable opportunities in education and public employment in Andhra Pradesh and Telangana?', 'Article 371D provides special constitutional arrangements concerning equitable opportunities and facilities in public employment and education.'),
        ('G.O. 610', 'Which 1985 government order addressed repatriation of employees appointed in violation of local-cadre arrangements in Zones V and VI?', 'G.O. 610 of 1985 addressed identified violations of local-cadre arrangements, including repatriation to appropriate zones.')
    ], [ts_mha, ts_mha, CONSTITUTION, ref('Government of Telangana — Government Orders', 'https://www.telangana.gov.in/government-orders/')])
    telangana('People of the armed struggle', [
        ('Chakali Ailamma', 'Which woman associated with Palakurthi resisted an attempt to seize the produce from her cultivated land?', 'Chakali Ailamma, also called Chityala Ailamma, became a symbol of resistance to landlord oppression at Palakurthi.'),
        ('Doddi Komarayya', 'Whose death at Kadavendi on 4 July 1946 became a major turning point in the Telangana armed struggle?', 'Doddi Komarayya was killed during the Kadavendi incident on 4 July 1946, a major event in the growth of the armed struggle.'),
        ('Suddala Hanumanthu', 'Which Telangana poet is associated with the song Palleturi Pillagada?', 'Suddala Hanumanthu wrote revolutionary songs, including Palleturi Pillagada, associated with peasant mobilisation.'),
        ('Bandi Yadagiri', 'Which Telangana revolutionary songwriter is associated with Bandenaka Bandi Katti?', 'Bandi Yadagiri is associated with Bandenaka Bandi Katti, a song of resistance to landlord oppression.')
    ], [ref(struggle,page=15), ref(struggle,page=16), ref(struggle,page=31), ref(struggle,page=30)])
    telangana('Agrarian society', [
        ('Vetti', 'What term describes the forced unpaid labour opposed by peasants in the Telangana struggle?', 'Vetti was coercive labour extracted from subordinate groups, often without payment, and was a major target of peasant opposition.'),
        ('Tenant cultivation', 'A cultivator works land owned by another person in return for rent or a share of produce. Which relationship is described?', 'Tenant cultivation separates the cultivator from land ownership; rent or a share of produce is paid to the owner under the arrangement.'),
        ('Landlordism', 'What term describes a rural structure in which large landholders control land and extract rents from cultivators?', 'Landlordism centres on concentrated land ownership and the collection of rent or other claims from cultivators.'),
        ('Usurious lending', 'Charging severely exploitative interest that traps borrowers in escalating debt is described by which term?', 'Usurious lending involves exploitative interest demands; indebtedness was one mechanism of rural exploitation opposed in agrarian movements.')
    ], [ref(struggle,page=7), ref(struggle,page=15), ref(struggle,page=5), ref(struggle,page=7)])
    telangana('Safeguard concepts', [
        ('Regional revenue safeguards', 'A proposal says that surplus revenue from Telangana should be used for development within Telangana. Which issue does it principally address?', 'Regional revenue safeguards concern how revenue attributable to a region is used, including the allocation of its surplus for local development.'),
        ('Local employment safeguards', 'A proposal reserves specified public-employment opportunities for eligible local residents. Which issue does it principally address?', 'Local employment safeguards concern access to specified public jobs through applicable residence or local-cadre arrangements.'),
        ('Political representation', 'A proposal seeks participation of Telangana leaders in cabinet and other political decision-making. Which issue does it principally address?', 'Political representation concerns a region’s participation in institutions and decisions exercising public power.'),
        ('Regional development', 'A proposal seeks additional educational, irrigation and infrastructure facilities in a disadvantaged region. Which issue does it principally address?', 'Regional development concerns improving economic and social facilities across a region, including infrastructure and human development.')
    ], ref(movement,page=3))
    telangana('Institutions and movements', [
        ('Telangana Praja Samiti', 'Which organisation emerged as a major platform during the 1969 Telangana movement and later participated in elections?', 'Telangana Praja Samiti developed from a movement platform into an electoral political organisation during and after the 1969 agitation.'),
        ('Osmania University', 'Which Hyderabad university was initially known for using Urdu as the medium across branches of higher education?', 'Osmania University used Urdu as its initial medium of instruction across higher-education disciplines, including professional subjects.'),
        ('Kothagudem Thermal Power Station', 'Which power station at Palvancha is associated with early employment-related agitation in the 1969 Telangana movement?', 'Employment disputes at Kothagudem Thermal Power Station in Palvancha formed part of the background to the 1969 Telangana agitation.'),
        ('States Reorganisation Commission', 'Which commission headed by Fazl Ali examined the reorganisation of Indian states in the 1950s?', 'The States Reorganisation Commission, chaired by Fazl Ali, examined state boundaries and submitted its report in 1955.')
    ], [ref('Telangana Movement Part 6.pdf — supplied private reference',page=8),ref('Osmania University — Origin and History','https://www.osmania.ac.in/aboutus.php'),ref(movement,page=7),ts_mha])
    telangana('Water geography', [
        ('Musi', 'Which river flowing through Hyderabad is a tributary of the Krishna?', 'The Musi flows through Hyderabad and belongs to the Krishna river system.'),
        ('Manjira', 'On which Godavari tributary is the Nizamsagar project built?', 'The Manjira is a tributary of the Godavari and carries the Nizamsagar project.'),
        ('Godavari', 'Across which river was the Sriram Sagar project built near Pochampad?', 'The Sriram Sagar project, also called Pochampad, is built across the Godavari.'),
        ('Krishna', 'Across which major river is the Nagarjuna Sagar dam built?', 'Nagarjuna Sagar is a major dam across the Krishna River, supporting irrigation and hydropower.')
    ], [ref('Original basin-identification practice — Telangana geography', 'https://www.telangana.gov.in/departments/irrigation-and-cad/'),ref('Telangana Irrigation — Nizamsagar project','https://irrigation.telangana.gov.in/img/projectspdf/nizamsagar.pdf'),ref('Nizamabad district — Sriram Sagar','https://nizamabad.telangana.gov.in/about-district/'),ref('Telangana Irrigation — Nagarjuna Sagar','https://irrigation.telangana.gov.in/img/projectspdf/nsp.pdf')])
    telangana('Irrigation and water management', [
        ('Tank restoration', 'Desilting a village tank, repairing its bund and restoring feeder channels primarily exemplify which activity?', 'Tank restoration recovers storage and conveyance functions of existing small water bodies, a longstanding element of Telangana irrigation.'),
        ('Lift irrigation', 'A project uses pumps to raise river water to higher-elevation canals. What type of irrigation is this?', 'Lift irrigation supplies water by pumping it to a higher elevation, requiring energy as well as water availability.'),
        ('Drip irrigation', 'A farmer supplies small quantities of water near plant roots through emitters. What technique is used?', 'Drip irrigation delivers water through emitters near the root zone, reducing some conveyance and evaporation losses when well managed.'),
        ('Groundwater recharge', 'A percolation structure encourages rainwater to enter the soil and replenish an aquifer. What process is being promoted?', 'Groundwater recharge is the replenishment of an aquifer by infiltrating water; it differs from directly pumping groundwater out.')
    ], ref('Original Telangana water-management applications; Mission Kakatiya provides tank-restoration context','https://www.telangana.gov.in/mission-kakatiya/'))
    telangana('Protected landscapes', [
        ('Amrabad Tiger Reserve', 'Which Telangana tiger reserve lies in the Nallamala hill and forest landscape?', 'Amrabad Tiger Reserve occupies part of the Nallamala landscape, with rugged hills, forests and valleys.'),
        ('Kawal Tiger Reserve', 'Which Telangana tiger reserve is associated with the northern Deccan forest landscape and connectivity toward Maharashtra?', 'Kawal Tiger Reserve lies in northern Telangana and is important in the wider forest connectivity of the Deccan landscape.'),
        ('Eturnagaram Wildlife Sanctuary', 'Which Telangana sanctuary in the Mulugu region is associated with the Godavari river landscape?', 'Eturnagaram Wildlife Sanctuary is associated with the Godavari landscape in the Mulugu region.'),
        ('Pakhal Wildlife Sanctuary', 'Which Telangana sanctuary is associated with the lake of the same name near Warangal?', 'Pakhal Wildlife Sanctuary surrounds the Pakhal Lake landscape near Warangal.')
    ], ts_nature)
    telangana('Historic monuments', [
        ('Ramappa Temple', 'Which Kakatiya monument at Palampet is inscribed on the UNESCO World Heritage List?', 'The Kakatiya Rudreshwara Temple, popularly called Ramappa Temple, at Palampet is a UNESCO World Heritage Site.'),
        ('Charminar', 'Which Hyderabad monument with four minarets was built by Muhammad Quli Qutb Shah in 1591?', 'Charminar was built in Hyderabad in 1591 by Muhammad Quli Qutb Shah and is distinguished by its four minarets.'),
        ('Thousand Pillar Temple', 'Which Kakatiya temple at Hanumakonda is associated with Rudra Deva and shrines to Shiva, Vishnu and Surya?', 'The Thousand Pillar Temple at Hanumakonda was built under Rudra Deva and is a triple-shrine temple associated with Shiva, Vishnu and Surya.'),
        ('Golconda Fort', 'Which fortified complex near Hyderabad served as the centre of Qutb Shahi power before the foundation of Hyderabad?', 'Golconda was the fortified centre of the Qutb Shahi kingdom before Hyderabad was established as its capital city.')
    ], [ref('UNESCO — Kakatiya Rudreshwara (Ramappa) Temple','https://whc.unesco.org/en/list/1570/'),ref('Hyderabad district — Charminar','https://hyderabad.telangana.gov.in/tourist-place/charminar/'),ref('Hanumakonda district — Thousand Pillar Temple','https://hanumakonda.telangana.gov.in/tourist-place/thousand-pillar-temple/'),TS_CULTURE])
    telangana('Library movement and public knowledge', [
        ('Sri Krishnadevaraya Andhra Bhasha Nilayam', 'Which library established in Hyderabad in 1901 was an important centre for Telugu reading and cultural activity?', 'Sri Krishnadevaraya Andhra Bhasha Nilayam was established in Hyderabad in 1901 and helped expand access to Telugu literature.'),
        ('Library movement', 'What movement spread reading rooms and access to books and newspapers as part of Telangana’s public awakening?', 'The library movement expanded access to printed knowledge and provided spaces for reading, discussion and cultural awareness.'),
        ('Andhra Jana Sangham', 'Which organisation is associated with the early-1920s assertion of Telugu linguistic and cultural rights in Hyderabad State?', 'Andhra Jana Sangham emerged in the early 1920s as an organisation for Telugu linguistic and cultural interests in Hyderabad State.'),
        ('Print circulation', 'Books published outside a village are shared through its reading room. Which mechanism directly broadens access to those ideas?', 'Print circulation allows books, newspapers and pamphlets to reach new readers, supporting public discussion beyond their place of publication.')
    ], ref('SCERT Telangana — Class 8 Social Studies, Hyderabad State and the library movement','https://scert.telangana.gov.in/pdf/publication/ebooks2019/8%20social%20em%202020-21.pdf'))
    telangana('Regional geography applications', [
        ('Deccan Plateau', 'Which broad physiographic region contains most of Telangana?', 'Telangana lies mainly on the Deccan Plateau, an elevated peninsular landmass rather than a coastal plain.'),
        ('Southwest monsoon', 'Which seasonal circulation supplies the principal rainy-season inflows to Telangana’s river and tank systems?', 'The southwest monsoon supplies the principal rainy-season rainfall and river inflows in Telangana, usually concentrated in the June–September period.'),
        ('Watershed', 'A Telangana tank receives runoff from the surrounding land draining toward it. What is that contributing land area called?', 'A watershed or catchment is the area that drains toward a common outlet; protecting it helps maintain the receiving water body.'),
        ('Rainfed farming', 'A Telangana farmer grows a crop using rainfall without an assured irrigation supply. What farming category is this?', 'Rainfed farming relies mainly on rainfall, making soil moisture conservation and rainfall variability important management concerns.')
    ], ref('Original regional geography applications; Telangana Irrigation & CAD regional overview','https://www.telangana.gov.in/departments/irrigation-and-cad/'))
    return bank

if __name__ == '__main__':
    import json
    from collections import Counter
    bank = build_gs_bank()
    assert len({q['id'] for q in bank}) == len(bank)
    assert len({q['question'] for q in bank}) == len(bank)
    for q in bank:
        assert len(q['options']) == 4 and len({o['text'] for o in q['options']}) == 4
        assert 0 <= q['answer'] < 4
        assert all(len(o['explanation']) > 40 for o in q['options'])
    print(json.dumps({'count': len(bank), 'topics': dict(Counter(q['topic'] for q in bank))}, indent=2))
