"""Original school-syllabus science and geography questions.

Reference links identify authoritative subject references; textbook pages are
not fabricated. Questions are newly authored and are not NCERT past questions.
Each item has a distinct conceptKey. No parameter-only copies are generated.
"""
import copy
import hashlib
import json
import random
from collections import Counter
from pathlib import Path
from gs_content import build_gs_bank

NCERT_S={'title':'NCERT Science textbooks — subject reference; original practice question','url':'https://ncert.nic.in/textbook.php','page':None}
NCERT_G={'title':'NCERT Geography textbooks — subject reference; original practice question','url':'https://ncert.nic.in/textbook.php','page':None}
ISRO={'title':'ISRO — Chandrayaan-3 scientific payloads','url':'https://www.isro.gov.in/Chandrayaan3_Details.html','page':None}
IMD={'title':'India Meteorological Department — weather and climate educational references','url':'https://mausam.imd.gov.in/imd_latest/contents/faq.php','page':None}
USGS={'title':'US Geological Survey — This Dynamic Earth, plate motions','url':'https://pubs.usgs.gov/gip/dynamic/understanding.html','page':None}
NOAA={'title':'NOAA — ocean currents education reference','url':'https://www.noaa.gov/education/resource-collections/ocean-coasts/ocean-currents','page':None}
TIDES={'title':'NOAA — tides education reference','url':'https://www.noaa.gov/education/resource-collections/ocean-coasts/tides','page':None}
INDIA_PHYS={'title':'NCERT Contemporary India I — Physical Features of India','url':'https://www.ncert.nic.in/textbook/pdf/iess102.pdf','page':None}


def build_science_geo():
    bank=[]
    for q in build_gs_bank():
        if q['topic'] in ('General Science','Geography'):
            q=copy.deepcopy(q)
            q['source']=dict(NCERT_S if q['topic']=='General Science' else NCERT_G)
            q['conceptKey']=q['topic']+' / '+q['skill']+' / '+q['options'][q['answer']]['text']
            bank.append(q)
    def group(topic,skill,raw,source=None):
        entries=[tuple(x.strip() for x in line.split('|')) for line in raw.strip().splitlines() if line.strip()]
        assert len(entries)==4 and all(len(x)==3 for x in entries),(skill,entries)
        assert len({x[0] for x in entries})==4
        for k,(term,prompt,fact) in enumerate(entries):
            order=list(range(4));random.Random(48241+len(bank)*113).shuffle(order)
            opts=[]
            for j in order:
                other,_,definition=entries[j]
                reason=('Correct. '+fact) if j==k else ('Incorrect. '+definition+' The defining clue here identifies '+term+'.')
                opts.append({'text':other,'explanation':reason})
            bank.append({'id':'','section':'General Studies','topic':topic,'skill':skill,
                         'conceptKey':topic+' / '+skill+' / '+term,'question':prompt,'options':opts,
                         'answer':order.index(k),'explanation':fact,'source':dict(source or (NCERT_S if topic=='General Science' else NCERT_G)),
                         'difficulty':'Standard','origin':'Original practice'})
    def S(skill,raw,source=None):group('General Science',skill,raw,source)
    def G(skill,raw,source=None):group('Geography',skill,raw,source)

    # 01–20: Physical science, each row assesses a separate property/application.
    S('Types of energy', '''
Kinetic energy | Which energy is possessed by a moving cricket ball because of its motion? | Kinetic energy is energy of motion and equals one-half mass times speed squared in classical mechanics.
Gravitational potential energy | Which energy increases when a book is lifted slowly to a higher shelf? | Gravitational potential energy increases with height near Earth by mgh, relative to a chosen reference level.
Elastic potential energy | A compressed spring can launch a toy car. What stored energy drives the launch? | Deformation stores elastic potential energy in a spring; release can convert it into motion.
Chemical energy | Which stored energy in fuel is released through rearrangement of chemical bonds during combustion? | Chemical energy is associated with the arrangement of atoms and bonds and can change in a chemical reaction.
''')
    S('Energy conversion devices', '''
Electric motor | Which device converts electrical input chiefly into mechanical rotation? | An electric motor uses magnetic forces on current-carrying conductors to produce mechanical motion.
Electric generator | Which device converts mechanical rotation into electrical output by induction? | A generator changes magnetic flux through a circuit to induce an electromotive force.
Photovoltaic cell | Which device directly produces electric power from incident light without a moving turbine? | A photovoltaic cell converts light into electrical energy through charge separation in a semiconductor.
Loudspeaker | Which device uses electrical signals to move a diaphragm and produce sound? | A loudspeaker converts electrical signals into mechanical vibration and sound in the surrounding air.
''')
    S('Force and work applications', '''
Zero work by the supporting force | A person holds a stationary suitcase for ten seconds. What is the mechanical work done on it by the upward supporting force? | The suitcase has no displacement, so mechanical work on it is zero despite muscular energy expenditure.
Negative work by friction | A sliding box slows on a rough horizontal floor. How is the work done by kinetic friction classified? | Friction acts opposite the displacement, so its work on the sliding box is negative.
Positive work by gravity | A stone falls vertically downward. How is the work done by gravity during the fall classified? | Gravity and the downward displacement have the same direction, giving positive work.
Zero work by centripetal force | A body moves in a circle at constant speed under a radial force. How much work does that radial force do over a small displacement? | A radial centripetal force is perpendicular to the instantaneous tangential displacement and therefore does no work.
''')
    S('Conservation principles', '''
Conservation of energy | An ideal pendulum exchanges kinetic and potential energy while their sum remains fixed. Which principle describes this? | In an isolated ideal mechanical system without dissipative forces, total mechanical energy remains constant.
Conservation of linear momentum | Two trolleys collide with negligible external horizontal impulse. Which total vector quantity is unchanged? | The vector sum of linear momenta stays constant when net external impulse is zero.
Conservation of electric charge | Two initially neutral objects exchange electrons and acquire equal-magnitude, opposite net charges. Which conservation principle specifically explains their unchanged total charge? | Charge is transferred between objects, while the total electric charge of the isolated pair is conserved.
Conservation of mass in ordinary chemical reactions | Reactants are sealed in a container before a chemical reaction. Why is the measured total mass essentially unchanged afterward? | Ordinary chemistry rearranges atoms rather than creating or destroying them; mass is conserved to chemical measurement precision.
''')
    S('Simple machines', '''
Lever | A crowbar lifts a stone by turning about a fixed fulcrum. Which simple machine is being used? | A lever rotates around a fulcrum and can trade a larger effort distance for a greater load force.
Fixed pulley | Which simple machine can change the direction of a pull without providing an ideal force advantage when only one wheel is fixed overhead? | A single fixed pulley redirects the force; its ideal mechanical advantage is one.
Screw | Which simple machine is an inclined plane wrapped around a cylinder? | A screw converts rotation into axial motion through its helical inclined surface.
Wedge | Which simple machine has inclined surfaces that force material apart when pushed into it? | A wedge turns a forward applied force into separating forces along its sloping sides.
''')
    S('Fluid principles', '''
Archimedes principle | A submerged object experiences an upward force equal to the weight of displaced fluid. Which principle states this? | Archimedes principle equates buoyant force to the weight of fluid displaced by the object.
Pascal principle | A hydraulic lift transmits pressure through confined fluid to a larger piston. Which principle is applied? | A pressure change applied to an enclosed fluid is transmitted throughout it, enabling hydraulic force multiplication.
Bernoulli principle | In an ideal steady horizontal flow, a faster stream has lower static pressure. Which relationship explains this? | Bernoulli energy balance relates pressure, kinetic and gravitational terms along a streamline under its ideal assumptions.
Capillary action | Water rises in a thin glass tube above the surrounding level. Which phenomenon combines surface tension and wetting? | Capillary action arises from surface tension and adhesive interactions at the liquid-wall interface.
''')
    S('Material and flow properties', '''
Viscosity | Honey resists flowing much more than water at similar temperature. Which property describes this internal resistance? | Viscosity measures a fluid's resistance to relative motion between neighbouring layers.
Surface tension | A clean liquid surface tends to contract and can support a small carefully placed needle. Which property is responsible? | Surface tension is force per unit length at an interface and favours reducing surface area.
Density | Two samples have equal volume but different masses. Which property is larger for the heavier sample? | Density is mass divided by volume, so greater mass at the same volume means greater density.
Compressibility | A trapped gas shrinks greatly when pressure rises, whereas water changes volume little. Which property is greater for the gas? | Compressibility measures fractional volume change under pressure; gases are much more compressible than liquids.
''')
    S('Gravity applications', '''
Equal free-fall acceleration in vacuum | A feather and a stone are dropped together in an evacuated chamber. Which outcome is expected? | Without air resistance, both have the same gravitational acceleration at the same location and fall together.
Weight depends on local gravity | An astronaut moves from Earth to the Moon while retaining the same matter. Which property decreases? | Weight is gravitational force mg and decreases where gravitational acceleration is smaller; mass remains the same.
Orbital free fall | Why do astronauts in an orbiting spacecraft appear weightless? | Astronauts and spacecraft continuously fall together under gravity, so the usual supporting contact force is absent.
Inverse-square gravitational force | Two point masses are moved to twice their original separation. Which rule determines the new gravitational force? | Newtonian gravitational force varies inversely with the square of separation, so doubling separation reduces it to one quarter.
''')
    S('Thermal properties', '''
Specific heat capacity | Which property tells the heat needed to raise one kilogram of a substance by one kelvin without a phase change? | Specific heat capacity is heat supplied per unit mass per unit temperature rise.
Latent heat | Ice melts at its melting point while temperature remains nearly constant. What absorbs the supplied energy? | Latent heat supplies the energy required for a phase change without a temperature change at fixed pressure.
Thermal expansion | A metal lid becomes easier to loosen after warming. Which material response commonly helps? | Heating usually expands a metal lid, increasing its dimensions and loosening the fit.
Thermal equilibrium | Two bodies in thermal contact eventually have the same temperature and no net heat flow. What state have they reached? | Thermal equilibrium means equal temperature with no net transfer of heat between the bodies.
''')
    S('Thermodynamic processes', '''
Isothermal process | Which ideal gas process is carried out at constant temperature? | In an isothermal process temperature is constant; for a fixed amount of ideal gas, pressure times volume stays constant.
Isobaric process | Which gas process maintains constant pressure as volume and temperature can change? | An isobaric process occurs at constant pressure, such as idealised heating under a freely moving weighted piston.
Isochoric process | Gas is heated in an ideal rigid sealed container. What process keeps its volume fixed? | An isochoric process has constant volume, so the gas does no pressure-volume boundary work.
Adiabatic process | Which idealised process permits no heat exchange with the surroundings? | An adiabatic process has zero heat transfer, although work can still change the system's internal energy.
''')
    S('Domestic circuit principles', '''
Parallel connection | Which connection gives each household appliance the supply voltage and allows it to operate independently of the others? | Each parallel branch receives the supply voltage and can operate independently of other branches.
Series resistance addition | Two resistors are connected end-to-end with no branching. How is their equivalent resistance found? | In series the same current passes through both resistors and the equivalent resistance is their sum.
Fuse melting on excess current | What protective action does a correctly rated fuse perform during excessive current? | Excess current heats the fuse element until it melts, opening the circuit and interrupting current.
Protective earthing | Which protective measure connects an exposed metal appliance case to a low-resistance fault-current path? | Earthing provides a low-resistance fault-current path and helps protective devices disconnect a faulty supply.
''')
    S('Magnetic behaviour', '''
Closed magnetic field lines | Which statement describes magnetic field lines around and inside an ordinary bar magnet? | Magnetic field lines form closed loops, continuing through the magnet rather than starting or ending at isolated poles.
Electromagnet | Which device produces a controllable magnetic field when current passes through a coil, often around soft iron? | An electromagnet creates magnetism through electric current and its strength can be controlled by that current.
Ferromagnetism | Iron can retain strong alignment of magnetic domains. Which material behaviour does this illustrate? | Ferromagnetic materials contain domains that can align strongly and may retain magnetisation.
Electromagnetic induction | A voltage appears across a coil when its magnetic flux changes. What phenomenon is this? | Electromagnetic induction produces an emf when the magnetic flux linked with a circuit changes.
''')
    S('Electromagnetic spectrum uses', '''
Radio waves | Which broad electromagnetic band is used for conventional long-distance radio broadcasting? | Radio waves have long wavelengths and are used to carry modulated communication signals.
Microwaves | Which electromagnetic band heats water-containing food in a microwave oven? | Microwave electric fields interact with polar molecules and produce dielectric heating in food.
Infrared radiation | A thermal camera chiefly detects which band emitted strongly by ordinary warm objects? | Infrared radiation lies beyond visible red and is widely used to detect thermal emission.
Ultraviolet radiation | Which band beyond visible violet can cause sunburn and initiate vitamin D formation in skin? | Ultraviolet photons have more energy than visible photons and can cause photochemical changes in skin.
''')
    S('Wave phenomena', '''
Longitudinal wave | In ordinary sound travelling through air, particle vibrations run in which relation to propagation? | A longitudinal wave has particle oscillations parallel to its direction of travel, producing compressions and rarefactions.
Transverse wave | In a wave on a stretched string, the displacement is perpendicular to propagation. What type is this? | A transverse wave has oscillations perpendicular to its travel direction.
Echo | A distinct repetition of a sound is heard after reflection from a distant wall. What is it called? | An echo is reflected sound heard separately when its delay is sufficiently long.
Resonance | A swing responds strongly when pushes match its natural frequency. Which phenomenon amplifies the response? | Resonance occurs when periodic driving is near a system's natural frequency, producing a large response under suitable damping.
''')
    S('Optical instruments', '''
Compound microscope | Which instrument uses an objective and eyepiece to magnify a nearby tiny specimen? | A compound microscope forms an enlarged intermediate image with its objective and magnifies it with an eyepiece.
Astronomical telescope | Which instrument is designed to increase the apparent angular size of very distant celestial objects? | An astronomical telescope gathers light from distant objects and magnifies their apparent angular separation.
Periscope | Which instrument uses appropriately placed reflecting surfaces to view over an obstruction? | A periscope redirects light through mirrors or prisms so an observer can see from a displaced line of sight.
Slide projector | Which instrument forms a magnified real image of a small illuminated transparency on a screen? | A projector uses a converging lens to cast an enlarged real image onto a screen.
''')
    S('Human eye conditions', '''
Hypermetropia | A person has difficulty focusing nearby objects because the uncorrected focus would lie behind the retina. Which defect is this? | Hypermetropia is long-sightedness and is commonly corrected with a converging lens.
Presbyopia | Age-related loss of the eye's ability to accommodate makes near work difficult. What is this condition? | Presbyopia results mainly from reduced lens flexibility and accommodative ability with age.
Astigmatism | Unequal curvature in different directions of the cornea produces direction-dependent blur. What is this defect? | Astigmatism causes different meridians of the eye to focus differently and can be corrected with suitable cylindrical components.
Cataract | Clouding of the eye's normally transparent lens is called what? | A cataract is opacity of the natural lens, reducing the quality of light reaching the retina.
''')
    S('Nuclear radiation', '''
Alpha particle | Which emitted nuclear particle consists of two protons and two neutrons? | An alpha particle is a helium-4 nucleus carrying two positive elementary charges.
Beta-minus particle | In beta-minus decay, which light charged particle is emitted as a neutron changes into a proton? | A beta-minus particle is an electron created in the decay, accompanied by an antineutrino.
Gamma photon | Which radiation is an uncharged high-energy electromagnetic photon emitted in nuclear de-excitation? | Gamma radiation consists of photons and changes nuclear energy without itself carrying electric charge.
Neutrino | Which extremely weakly interacting, electrically neutral particle accompanies beta-plus decay or electron capture? | A neutrino carries away energy and momentum in these weak interactions and interacts very rarely with matter.
''')
    S('Nuclear processes', '''
Half-life | What is the time for the expected number of undecayed nuclei in a large radioactive sample to fall by half? | Radioactive half-life is a statistical decay timescale independent of the initial sample size.
Radiocarbon dating | Which technique estimates ages of once-living material from the decay of carbon-14? | Radiocarbon dating uses the changing carbon-14 abundance after an organism stops exchanging carbon with its environment.
Nuclear fission | A heavy nucleus divides into lighter nuclei with energy release. What process is this? | Fission splits a heavy nucleus and may release neutrons capable of sustaining a chain reaction.
Nuclear fusion | Light nuclei combine into a heavier nucleus in the Sun's energy-producing reactions. What process is this? | Fusion combines light nuclei; the Sun obtains energy mainly by converting hydrogen into helium.
''')
    S('Electronic components', '''
Light-emitting diode | Which semiconductor component emits light when current flows through its junction in the forward direction? | An LED emits photons when electrons and holes recombine across a suitably designed semiconductor junction.
Transistor | Which semiconductor component can amplify a signal or act as an electronic switch? | A transistor controls a larger current or voltage response using an input signal and is fundamental to switching and amplification.
Thermistor | Which resistive component is designed to change resistance strongly with temperature? | A thermistor is a temperature-sensitive resistor used for sensing or compensation.
Photodiode | Which semiconductor component is used primarily to detect incident light through a change in electric current? | A photodiode converts absorbed photons into charge carriers, allowing light to be measured electrically.
''')
    S('Additional SI base units', '''
Kelvin | What is the SI base unit of thermodynamic temperature? | The kelvin is the SI thermodynamic-temperature unit; temperature intervals of one kelvin and one degree Celsius have equal size.
Mole | What is the SI unit for amount of substance? | The mole counts a specified number of elementary entities, using the fixed Avogadro constant.
Candela | What is the SI base unit of luminous intensity in a given direction? | The candela measures luminous intensity weighted according to human visual sensitivity.
Metre | What is the SI base unit of length? | The metre is the SI base unit used for length and distance measurements.
''')

    # 21–46: Chemistry and materials.
    S('States of matter', '''
Solid | Which ordinary state retains both its own shape and nearly fixed volume? | A solid has particles constrained around relatively fixed positions, giving a definite shape and volume.
Liquid | Which state flows to take a container's shape but ordinarily retains nearly fixed volume? | A liquid has mobile neighbouring particles and a definite volume without a fixed shape.
Gas | A sample consists of widely separated, electrically neutral molecules and expands to fill its container. Which state describes this non-ionised sample? | An ordinary non-ionised gas consists of neutral particles moving throughout the available space, with no fixed shape or volume. Plasma contains a substantial population of free charged particles.
Plasma | Which state contains a substantial population of free charged particles and occurs in stars? | Plasma is an ionised state containing mobile electrons and ions that responds strongly to electromagnetic fields.
''')
    S('Changes of physical state', '''
Melting | What is the transition from solid to liquid called? | Melting turns a solid into liquid when supplied energy disrupts the rigid arrangement of particles.
Freezing | What is the transition from liquid to solid called? | Freezing forms a solid as liquid loses energy under suitable temperature and pressure conditions.
Condensation | Water droplets form when vapour meets a cool surface. What change occurs? | Condensation changes vapour into liquid and releases latent heat to the surroundings.
Boiling | Vapour bubbles form throughout a liquid when vapour pressure matches surrounding pressure. What process occurs? | Boiling is bulk vaporisation at the temperature where liquid vapour pressure equals external pressure.
''')
    S('Solution terminology', '''
Solute | Sugar dissolves in a large amount of water. What is the sugar called in this solution? | A solute is the component being dissolved, typically present in the smaller proportion in this example.
Solvent | In a dilute aqueous sugar solution, what role does water play? | The solvent is the dissolving medium; water is the solvent in an aqueous solution.
Saturated solution | At a fixed temperature, a solution is in equilibrium with undissolved solute and cannot dissolve more of it. What is it called? | A saturated solution contains the equilibrium maximum dissolved amount of that solute under the specified conditions.
Solubility | Which quantity expresses how much of a substance can dissolve in a given amount of solvent at a specified temperature? | Solubility specifies an equilibrium dissolution limit and depends on the substance, solvent and conditions.
''')
    S('Dispersed mixtures', '''
Suspension | Muddy water contains particles that can settle on standing and can be retained by ordinary filter paper. What mixture is this? | A suspension contains relatively large dispersed particles that may settle under gravity.
True solution | Salt water is homogeneous and dissolved particles do not scatter visible light into a visible beam. What mixture is this? | A true solution has molecular or ionic-scale solute dispersed uniformly in the solvent.
Colloid | A stable dispersion makes the path of a light beam visible through the Tyndall effect. What general class is this? | Colloidal particles are larger than molecules and can scatter light while remaining dispersed.
Emulsion | Tiny droplets of one liquid are dispersed in another immiscible liquid. What specific dispersion is this? | An emulsion is a liquid-in-liquid dispersion, such as fat droplets dispersed in the aqueous phase of milk.
''')
    S('Acid-base indicators', '''
Phenolphthalein | Which common indicator is colourless in acidic solution and pink in sufficiently basic solution? | Phenolphthalein changes from colourless to pink over its alkaline transition range.
Litmus | Which natural indicator turns red in acid and blue in base? | Litmus is a natural dye mixture showing characteristic red acidic and blue alkaline colours.
Turmeric | Which kitchen spice acts as an indicator that turns reddish-brown in a basic solution? | Turmeric contains curcumin, which changes from yellow toward reddish-brown in alkaline conditions.
Universal indicator | Which mixture of indicators gives a range of colours used to estimate pH over a broad range? | Universal indicator combines dyes whose transitions provide a multicolour scale across many pH values.
''')
    S('Interpreting pH', '''
Neutral at pH 7 | At 25°C, which description fits pure water with equal hydrogen-ion and hydroxide-ion concentrations? | Pure water is neutral at 25°C with pH 7; neutral pH can change with temperature.
Acidic below pH 7 | At 25°C, how is an aqueous solution with pH 3 classified? | A pH of 3 is acidic because hydrogen-ion activity exceeds that of neutral water at this temperature.
Basic above pH 7 | At 25°C, how is an aqueous solution with pH 11 classified? | A pH of 11 indicates a basic aqueous solution with hydroxide ions predominant over hydrogen ions.
Tenfold hydrogen-ion change per pH unit | What does a decrease of one pH unit indicate about hydrogen-ion activity? | pH is a negative base-ten logarithm, so decreasing pH by one corresponds to a tenfold increase in hydrogen-ion activity.
''')
    S('Food acids', '''
Acetic acid | Which organic acid is the characteristic acid in ordinary vinegar? | Vinegar contains acetic acid in water, giving its characteristic sourness.
Citric acid | Which organic acid is especially associated with citrus fruits such as lemons? | Citric acid is abundant in many citrus fruits and contributes to their sour taste.
Tartaric acid | Which acid is strongly associated with tamarind and is used in some baking powders? | Tartaric acid occurs in tamarind and can react with bicarbonate in leavening mixtures.
Lactic acid | Which acid forms during bacterial fermentation that sours milk? | Lactic acid bacteria ferment sugars to lactic acid, lowering pH and helping coagulate milk proteins.
''')
    S('Common inorganic acids', '''
Sulfuric acid | Which acid is used as the electrolyte in a conventional lead-acid car battery? | Lead-acid batteries use an aqueous sulfuric acid electrolyte involved in the electrode reactions.
Nitric acid | Which strong acid has formula HNO₃ and is used to manufacture nitrates? | Nitric acid contains nitrogen and is a strong acid as well as an oxidising reagent in many reactions.
Hydrochloric acid | Which acid is secreted into the human stomach to help provide its acidic environment? | Gastric cells secrete hydrochloric acid, supporting protein digestion and inhibiting many microbes.
Carbonic acid | Dissolved carbon dioxide reacts reversibly with water to form which weak acid? | Carbonic acid forms in the carbon-dioxide–water equilibrium and contributes to the acidity of carbonated water.
''')
    S('Common industrial compounds', '''
Washing soda | Which common name refers to sodium carbonate decahydrate, Na₂CO₃·10H₂O? | Washing soda is hydrated sodium carbonate and is used in cleaning and water-softening applications.
Plaster of Paris | Which material is calcium sulfate hemihydrate and sets when mixed with water? | Plaster of Paris is CaSO₄·½H₂O and hardens by rehydrating toward gypsum.
Gypsum | Which mineral is calcium sulfate dihydrate, CaSO₄·2H₂O? | Gypsum contains two water molecules per calcium sulfate formula unit and is a raw material for plaster.
Sodium hypochlorite | Which chemical is the active oxidising ingredient in many household chlorine-bleach solutions? | Sodium hypochlorite releases oxidising chlorine species in water and is used for bleaching and disinfection.
''')
    S('Organic functional groups', '''
Alcohol | Which functional class contains a hydroxyl group attached to a saturated carbon, as in ethanol? | Alcohols contain a carbon-bound hydroxyl group; ethanol has the group –OH attached to an ethyl group.
Aldehyde | Which class contains a terminal carbonyl group bonded to at least one hydrogen, as in ethanal? | Aldehydes have the –CHO functional group at the end of a carbon chain.
Ketone | Which class contains a carbonyl carbon bonded to two carbon groups, as in propanone? | Ketones have an internal carbonyl group of the form R–CO–R′.
Carboxylic acid | Which functional class contains the –COOH group? | Carboxylic acids contain both a carbonyl and hydroxyl joined at one carbon in a carboxyl group.
''')
    S('Hydrocarbon classes', '''
Alkane | Which class of open-chain hydrocarbons contains only single carbon–carbon bonds and has formula CₙH₂ₙ₊₂? | Acyclic alkanes are saturated hydrocarbons with only single bonds between carbon atoms.
Alkene | Which open-chain hydrocarbon class with one carbon–carbon double bond has formula CₙH₂ₙ? | Acyclic monoalkenes contain one carbon–carbon double bond and are unsaturated.
Alkyne | Which open-chain hydrocarbon class with one carbon–carbon triple bond has formula CₙH₂ₙ₋₂? | Acyclic monoalkynes contain a triple bond and have four fewer hydrogen atoms than the corresponding alkane.
Aromatic hydrocarbon | Benzene belongs to which class distinguished by a cyclic delocalised electron system? | Aromatic hydrocarbons include benzene, whose ring supports a stable delocalised π-electron system.
''')
    S('Carbon allotropes', '''
Diamond | Which carbon allotrope has a three-dimensional covalent network, very high hardness and low electrical conductivity when pure? | In diamond, each carbon bonds to four neighbours in a rigid tetrahedral network with no freely moving electrons.
Graphite | Which allotrope has stacked carbon sheets and conducts electricity along its layers? | Graphite has layered carbon networks with delocalised electrons and relatively weak forces between sheets.
Fullerene | Which carbon form includes closed cage-shaped molecules such as C₆₀? | Fullerenes are hollow carbon cages; C₆₀ has a roughly spherical cage of pentagonal and hexagonal rings.
Graphene | What is a single atomic layer of carbon arranged in a hexagonal lattice called? | Graphene is one carbon sheet, with exceptional in-plane bonding and mobile electronic charge carriers.
''')
    S('Element families', '''
Noble gases | Which periodic-table group contains helium and neon and has unusually low chemical reactivity? | Group 18 noble gases have filled outer electron shells and are relatively unreactive under ordinary conditions.
Halogens | Which group contains fluorine, chlorine, bromine and iodine? | Group 17 elements are halogens, reactive non-metals commonly forming singly charged negative ions.
Alkali metals | Which group includes lithium, sodium and potassium? | Group 1 alkali metals have one outer-shell electron and readily form singly charged positive ions.
Alkaline-earth metals | Which group includes magnesium and calcium? | Group 2 alkaline-earth metals have two outer-shell electrons and commonly form doubly charged positive ions.
''')
    S('Element identities', '''
Silicon | Which metalloid is the principal semiconductor used in conventional computer chips? | Silicon is a group 14 metalloid whose electronic properties can be controlled by doping.
Mercury | Which metallic element is liquid near ordinary room temperature? | Mercury is a metal with a melting point below ordinary room temperature, unlike most familiar metals.
Bromine | Which non-metallic element is a liquid near ordinary room temperature? | Bromine is a reddish-brown liquid halogen under ordinary room conditions.
Tungsten | Which high-melting-point metal is used in traditional incandescent bulb filaments? | Tungsten withstands high filament temperatures while emitting visible thermal radiation.
''')
    S('Chemical bonding', '''
Ionic bond | Which bond arises primarily from electrostatic attraction between oppositely charged ions? | Ionic bonding binds cations and anions, often after electron transfer between elements.
Covalent bond | Which bond involves atoms sharing one or more pairs of electrons? | Covalent bonds result from shared electron density between bonded atoms.
Metallic bond | Which bonding model describes positive metal ion cores surrounded by delocalised electrons? | Metallic bonding explains many metals' electrical conductivity, malleability and collective cohesion.
Hydrogen bond | Which attraction can occur between an O–H hydrogen and a nearby electronegative atom, as between water molecules? | Hydrogen bonding is a directional attraction involving hydrogen bonded to a strongly electronegative atom and a nearby acceptor.
''')
    S('Reaction patterns', '''
Combination reaction | Two reactants form one principal product, as calcium oxide and water form calcium hydroxide. What pattern is this? | A combination reaction joins reactant substances into a single principal product.
Decomposition reaction | Heating a compound causes it to break into two or more simpler substances. What pattern is this? | Decomposition splits one reactant compound into multiple products, often with heat, light or electricity.
Single displacement | Zinc added to copper sulfate solution releases copper metal. What reaction pattern occurs? | A more reactive element displaces a less reactive element from its compound.
Double displacement | Two ionic compounds exchange partner ions during a reaction. What pattern is this? | Double displacement exchanges ions between compounds, often forming a precipitate, gas or weakly ionised product.
''')
    S('Reaction energy and rates', '''
Exothermic reaction | A reaction transfers heat to its surroundings. How is it classified thermally? | An exothermic reaction releases energy as heat to the surroundings under the stated conditions.
Endothermic reaction | A reaction absorbs heat from its surroundings. How is it classified thermally? | An endothermic reaction requires net heat input from the surroundings.
Catalyst | Which substance accelerates a reaction through an alternative pathway without being consumed overall? | A catalyst changes the reaction pathway and lowers the kinetic barrier without changing the equilibrium position.
Inhibitor | Which substance slows a reaction by interfering with its mechanism? | An inhibitor decreases reaction rate, for example by blocking a reactive pathway or catalyst site.
''')
    S('Common gases and functions', '''
Oxygen | Which atmospheric gas supports ordinary burning and is consumed in aerobic respiration? | Oxygen acts as an oxidant in combustion and as the final electron acceptor in aerobic respiration.
Nitrogen | Which gas constitutes about four-fifths of dry air by volume? | Molecular nitrogen forms roughly 78% of dry air and is relatively unreactive because of its strong triple bond.
Carbon dioxide | Which gas turns limewater milky through calcium carbonate formation? | Carbon dioxide reacts with calcium hydroxide solution to form a white calcium carbonate precipitate under the usual test conditions.
Hydrogen | Which light gas gives a characteristic small pop when a suitable sample is ignited in air? | Hydrogen burns with oxygen to form water; a small laboratory sample can produce the characteristic pop test.
''')
    S('Water chemistry', '''
Temporary hardness | What type of water hardness caused mainly by calcium or magnesium bicarbonates can be reduced by boiling? | Boiling decomposes bicarbonates and can precipitate compounds responsible for temporary hardness.
Permanent hardness | What type of hardness from salts such as calcium sulfate is not removed simply by boiling? | Permanent hardness persists on boiling and requires processes such as ion exchange or chemical softening.
Ion exchange | Which treatment replaces hardness ions with other ions using a resin? | Ion-exchange resins bind calcium and magnesium ions and release replacement ions to soften water.
Reverse osmosis | Which membrane process uses pressure to drive water against its natural osmotic tendency? | Reverse osmosis pushes water through a selective membrane, leaving many dissolved solutes in a concentrated stream.
''')
    S('Metallurgy operations', '''
Roasting | A sulfide ore is strongly heated in excess air before reduction. What is this operation? | Roasting commonly converts sulfides into oxides while releasing sulfur dioxide.
Calcination | A carbonate ore is heated in limited or no air to remove carbon dioxide. What operation is this? | Calcination decomposes carbonate or hydrated ores by heat, often yielding an oxide.
Electrolytic refining | Impure metal at the anode dissolves while pure metal deposits at the cathode. What purification process is this? | Electrolytic refining transfers the desired metal through an electrolyte to a pure cathode deposit.
Gangue | What is the unwanted earthy or rocky material mixed with an ore called? | Gangue is the non-valuable mineral material associated with the desired ore mineral.
''')
    S('Protecting metals', '''
Rusting | Iron exposed to water and oxygen forms hydrated iron oxides. What corrosion process is this? | Rusting is iron corrosion requiring moisture and an oxidising environment, producing hydrated oxide products.
Galvanising | Steel is coated with zinc to protect it against corrosion. What process is this? | Galvanising adds a zinc layer that offers a barrier and sacrificial protection to the underlying iron.
Alloying for corrosion resistance | Chromium is added to steel so that a protective oxide film forms. What general method is being used? | Alloying modifies metal composition; chromium promotes the passive film responsible for stainless steel's corrosion resistance.
Anodising | An aluminium object is made the anode to thicken its protective oxide layer. What treatment is this? | Anodising grows a controlled oxide coating electrochemically on aluminium and certain other metals.
''')
    S('Synthetic polymers', '''
Polyethylene | Which common plastic is formed by polymerising ethene and is used in many bags and films? | Polyethylene consists of repeating ethene-derived units and is a widely used thermoplastic.
Polyvinyl chloride | Which chlorine-containing polymer is commonly used in pipes and cable insulation? | PVC is made from vinyl chloride monomers and can be formulated as rigid or flexible plastic.
Nylon | Which synthetic polymer family contains amide links and is used in strong fibres? | Nylons are synthetic polyamides whose chains can form strong fibres through orientation and intermolecular interactions.
Bakelite | Which early thermosetting phenol-formaldehyde plastic is used for heat-resistant electrical fittings? | Bakelite forms a cross-linked network that does not soften and remould like a thermoplastic on reheating.
''')
    S('Textile fibres', '''
Cotton | Which natural textile fibre is primarily cellulose from plant seed hairs? | Cotton fibres are cellulose-rich seed hairs of the cotton plant.
Wool | Which natural textile fibre consists mainly of keratin from animal hair? | Wool is a protein fibre, principally keratin, commonly obtained from sheep fleece.
Silk | Which protein fibre is obtained from the cocoon of the silkworm? | Silk is produced as long protein filaments by silkworms when spinning cocoons.
Polyester | Which common synthetic fibre family contains ester links and includes PET? | Polyester chains contain ester groups; PET is widely used for fibres as well as packaging.
''')
    S('Plant nutrient fertilisers', '''
Urea | Which widely used fertiliser supplies nitrogen and has formula CO(NH₂)₂? | Urea is a concentrated nitrogen fertiliser containing two nitrogen atoms per molecule.
Superphosphate | Which fertiliser name is associated chiefly with supplying phosphorus to crops? | Superphosphates contain soluble phosphate compounds made by treating phosphate rock with acid.
Potash fertiliser | Which fertiliser category principally supplies potassium? | Potash fertilisers contain potassium salts that provide the potassium nutrient required by plants.
Ammonium sulfate | Which fertiliser supplies both nitrogen and sulfur as ammonium and sulfate ions? | Ammonium sulfate contains ammonium nitrogen and sulfate sulfur, supplying both nutrients.
''')
    S('Environmental chemistry', '''
Chlorofluorocarbons | Which formerly common refrigerants release chlorine radicals that catalyse stratospheric ozone destruction? | CFCs can survive transport to the stratosphere, where ultraviolet light releases ozone-destroying chlorine radicals.
Carbon monoxide | Which combustion gas binds strongly to haemoglobin and reduces oxygen transport? | Carbon monoxide forms carboxyhaemoglobin, impairing the blood's ability to transport and release oxygen.
Sulfur dioxide | Which sulfur-containing gas from burning sulfur-rich fuels can contribute to acid deposition? | Sulfur dioxide can be oxidised and converted to acidic sulfate species in the atmosphere.
Methane | Which simple hydrocarbon is a greenhouse gas released by wetlands and anaerobic decomposition? | Methane is CH₄ and absorbs infrared radiation; anaerobic microbial processes are important sources.
''')
    S('Fuels and carbon materials', '''
Liquefied petroleum gas | Which domestic fuel is stored under pressure and consists mainly of propane and butane? | LPG contains easily liquefied light hydrocarbons, principally propane and butane, rather than pure methane.
Biogas | Which fuel mixture is produced by anaerobic digestion of organic waste and commonly contains methane and carbon dioxide? | Biogas is a microbial digestion product containing combustible methane mixed with carbon dioxide and smaller components.
Coke | Which carbon-rich solid fuel is obtained by destructive distillation of coal and used in iron smelting? | Coke is a porous carbon-rich residue formed when coal is heated with little air.
Charcoal | Which porous carbon-rich material is formed by heating wood with limited oxygen? | Charcoal is produced by pyrolysis of wood or other biomass and differs in origin from coal-derived coke.
''')

    # 47–80: Life science, physiology and ecology.
    S('Further cell structures', '''
Nucleus | Which membrane-enclosed compartment contains most DNA in a typical animal cell? | The nucleus houses most nuclear chromosomes and separates them from the cytoplasm in eukaryotes.
Endoplasmic reticulum | Which interconnected membrane network includes rough regions with ribosomes and smooth regions involved in lipid metabolism? | The endoplasmic reticulum is a membrane network involved in protein processing, lipid synthesis and intracellular transport.
Lysosome | Which acidic organelle contains enzymes that digest worn-out cell components and engulfed material? | Lysosomes contain hydrolytic enzymes active in an acidic interior and participate in cellular recycling.
Central vacuole | Which large plant-cell compartment stores cell sap and contributes to turgor pressure? | The central vacuole stores water and solutes and helps support plant cells through turgor.
''')
    S('Cell transport processes', '''
Diffusion | Molecules spread from a region of higher concentration to lower concentration without bulk fluid flow. What process is this? | Diffusion is net spreading down a concentration gradient due to random molecular motion.
Osmosis | Water passes through a selectively permeable membrane toward a solution of lower water potential. What process is this? | Osmosis is net water movement through a selectively permeable membrane driven by a water-potential difference.
Active transport | A membrane pump moves ions against their electrochemical gradient using metabolic energy. What process is this? | Active transport requires energy to move substances against the direction of passive equilibration.
Endocytosis | A cell membrane surrounds external material and forms an internal vesicle. What process occurs? | Endocytosis brings material into a cell by membrane invagination and vesicle formation.
''')
    S('Major biomolecule classes', '''
Proteins | Which biological macromolecules are polymers of amino acids joined by peptide bonds? | Proteins consist of amino-acid chains that fold into structures with enzymatic, structural and other functions.
Carbohydrates | Which biomolecule class includes starch, glycogen and cellulose? | These are carbohydrate polymers built from sugar units, serving energy-storage or structural roles.
Lipids | Which broad biomolecule group includes fats, oils and phospholipids and is largely water-insoluble? | Lipids include hydrophobic or amphipathic molecules important in energy storage and membranes.
Nucleic acids | Which macromolecule class includes DNA and RNA, made from nucleotide units? | Nucleic acids are nucleotide polymers central to storing, transmitting and expressing genetic information.
''')
    S('Enzyme terminology', '''
Substrate | What is the reactant molecule upon which an enzyme acts called? | An enzyme's substrate binds and is chemically transformed in the catalysed reaction.
Active site | Which region of an enzyme binds its substrate and performs catalysis? | The active site provides a specific three-dimensional chemical environment for binding and reaction.
Denaturation | Heating disrupts a protein's functional three-dimensional structure. What change is this? | Denaturation alters a protein's structure and commonly reduces function without necessarily breaking its peptide backbone.
Cofactor | What is a non-protein ion or molecule required for the activity of some enzymes called? | Cofactors assist enzyme function and include metal ions and organic coenzymes.
''')
    S('Modified plant organs', '''
Potato tuber | Which familiar food is a swollen underground stem with buds commonly called eyes? | A potato tuber is modified stem tissue; its eyes are buds capable of forming shoots.
Ginger rhizome | Which edible structure is a horizontally growing underground stem with nodes and internodes? | Ginger is a rhizome, an underground stem that stores food and supports vegetative growth.
Onion bulb | Which structure stores food chiefly in fleshy leaf bases around a shortened stem? | An onion bulb consists largely of swollen leaf bases attached to a short basal stem.
Carrot storage root | Which familiar food is an enlarged taproot used for food storage? | The carrot is principally a thickened storage taproot rather than a stem tuber.
''')
    S('Asexual reproduction examples', '''
Bryophyllum leaf buds | Which plant forms small plantlets from adventitious buds along leaf margins? | Bryophyllum can reproduce vegetatively when leaf-margin buds develop into new plants.
Yeast budding | Which process produces a new yeast cell as an outgrowth that later separates? | In budding, a small daughter outgrowth forms on the parent yeast cell and receives a nucleus.
Hydra budding | Which multicellular freshwater animal commonly reproduces by a body-wall bud? | Hydra forms multicellular buds that develop tentacles and separate as new individuals.
Planarian regeneration | Which flatworm can restore missing parts and, after suitable fragmentation, form complete individuals? | Planarians have extensive regenerative capacity supported by stem cells distributed through the body.
''')
    S('Flower structures', '''
Sepal | Which flower part typically protects the flower while it is a bud? | Sepals form the outer floral whorl and often enclose and protect a developing bud.
Petal | Which floral part is commonly coloured and helps attract animal pollinators? | Petals often provide visual or other signals to pollinators, though flowers vary in their pollination systems.
Anther | In which part of a typical flowering plant's stamen is pollen produced? | The anther contains pollen sacs in which pollen grains develop.
Ovary | Which basal part of the carpel contains ovules and commonly develops into a fruit after fertilisation? | The ovary encloses ovules; its wall commonly contributes to the developing fruit.
''')
    S('Seed structures', '''
Cotyledon | What is an embryonic seed leaf that may store food or absorb stored nutrients called? | Cotyledons are the embryo's seed leaves, with roles that differ among seed types.
Radicle | Which part of the seed embryo develops into the primary root? | The radicle is the embryonic root and usually emerges early in germination.
Plumule | Which embryonic seed structure develops into the shoot? | The plumule contains the developing shoot tip and young leaves of the embryo.
Testa | What is the protective outer seed coat commonly called? | The testa develops from an ovule integument and protects the enclosed embryo.
''')
    S('Plant growth regulators', '''
Auxin | Which plant hormone class is strongly associated with shoot cell elongation and phototropic curvature? | Auxins promote elongation in many shoot tissues and unequal distribution can produce bending responses.
Gibberellin | Which plant hormone class promotes stem elongation and can help break seed dormancy? | Gibberellins regulate growth and can stimulate processes involved in germination and stem extension.
Cytokinin | Which plant hormone class is especially associated with promoting cell division? | Cytokinins promote cell division and help regulate shoot development and leaf senescence.
Abscisic acid | Which plant hormone helps induce stomatal closure during water stress? | Abscisic acid coordinates drought responses and also promotes seed dormancy under many conditions.
''')
    S('Directional plant growth', '''
Phototropism | A shoot bends toward directional light. What growth response is this? | Phototropism is directional growth in response to light, commonly toward light in shoots.
Gravitropism | A root grows downward in response to gravity. What directional response is this? | Gravitropism is growth oriented by gravity; roots commonly show positive gravitropism.
Hydrotropism | A root bends toward a region with more available water. What response is this? | Hydrotropism is directional growth in response to a water or moisture gradient.
Thigmotropism | A climbing plant's tendril coils around a support after contact. What response is this? | Thigmotropism is directional growth in response to touch or mechanical contact.
''')
    S('Gas-exchange structures', '''
Stoma | Which adjustable pore in a leaf epidermis is flanked by guard cells? | A stoma regulates gas exchange and water-vapour loss through changes in guard-cell turgor.
Lenticel | Which porous region in woody bark permits gas exchange with underlying tissues? | Lenticels interrupt the protective bark with loosely arranged cells allowing gas diffusion.
Alveolus | Which tiny lung sac provides a large surface for gas exchange with blood? | Alveoli have thin walls and a rich capillary supply, enabling diffusion of respiratory gases.
Gill | Which aquatic respiratory structure exposes thin vascular surfaces to flowing water? | Gills exchange gases with water through a large, thin and well-supplied surface.
''')
    S('Human heart chambers', '''
Right atrium | Which human heart chamber receives most systemic venous blood through the venae cavae? | The right atrium receives oxygen-poor blood returning from the body and passes it to the right ventricle.
Right ventricle | Which chamber pumps blood toward the lungs through the pulmonary artery? | The right ventricle drives pulmonary circulation, sending blood to the lungs for gas exchange.
Left atrium | Which chamber receives oxygenated blood returning through the pulmonary veins? | The left atrium receives blood from the lungs and passes it to the left ventricle.
Left ventricle | Which chamber pumps blood into the aorta for systemic circulation? | The muscular left ventricle supplies the systemic circuit at relatively high pressure.
''')
    S('Circulatory vessels', '''
Artery | What is a blood vessel that carries blood away from the heart called, regardless of oxygen content? | Arteries are defined by outward flow from the heart; pulmonary arteries carry oxygen-poor blood.
Vein | What is a vessel that returns blood toward the heart called? | Veins carry blood toward the heart and often have valves, especially in the limbs.
Capillary | Which microscopic vessel type has a very thin wall suited to exchange with tissues? | Capillary walls consist chiefly of a single endothelial layer, supporting diffusion and fluid exchange.
Lymphatic vessel | Which vessel type returns excess tissue fluid to the bloodstream? | Lymphatic vessels collect tissue fluid as lymph and return it to venous circulation.
''')
    S('Urinary system structures', '''
Nephron | What is the microscopic functional unit of a kidney? | A nephron filters blood and modifies the filtrate through reabsorption and secretion to form urine.
Ureter | Which tube carries urine from a kidney to the urinary bladder? | Each ureter transports urine from the renal pelvis toward the bladder by muscular movement.
Urinary bladder | Which muscular organ temporarily stores urine before elimination? | The urinary bladder is a distensible reservoir for urine delivered by the ureters.
Urethra | Which passage carries urine from the bladder to the outside of the body? | The urethra provides the outlet through which urine leaves the bladder and body.
''')
    S('Central nervous system regions', '''
Cerebrum | Which major brain region supports conscious thought, sensory interpretation and voluntary motor planning? | The cerebrum includes cortical areas involved in perception, cognition and voluntary activity.
Cerebellum | Which brain region is especially important for coordination, balance and fine-tuning movement? | The cerebellum integrates sensory and motor information to improve movement timing and coordination.
Medulla oblongata | Which brainstem region contains centres important for breathing and cardiovascular regulation? | The medulla contains neural circuits controlling essential autonomic functions.
Spinal cord | Which long central nervous system structure conducts signals and mediates many simple reflexes? | The spinal cord connects peripheral nerves with the brain and contains reflex circuits.
''')
    S('Neuronal structures', '''
Dendrite | Which branching part of a typical neuron receives many incoming signals? | Dendrites provide receptive surfaces that carry local signals toward the neuronal cell body.
Axon | Which neuronal projection typically conducts action potentials away from the cell body? | The axon carries electrical signals toward synaptic terminals or other target regions.
Synapse | What is the specialised junction at which one neuron communicates with another cell? | A synapse transfers information chemically through neurotransmitters or, in some cases, electrically.
Myelin sheath | Which insulating covering helps action potentials travel rapidly along many vertebrate axons? | Myelin reduces current leakage and enables rapid saltatory conduction between exposed nodes.
''')
    S('Eye structures', '''
Retina | Which light-sensitive tissue at the back of the eye contains rods and cones? | The retina converts light into neural signals through photoreceptors and associated neural circuits.
Iris | Which coloured muscular structure adjusts the size of the pupil? | The iris controls pupil diameter and thereby regulates how much light enters the eye.
Pupil | What is the central opening in the iris through which light enters? | The pupil is an aperture rather than a tissue; its size changes under iris muscle control.
Cornea | Which transparent front surface of the eye provides much of its initial refraction? | The curved cornea is the major refracting surface at the eye's air-to-tissue boundary.
''')
    S('Ear structures', '''
Cochlea | Which spiral inner-ear structure contains sensory cells for hearing? | The cochlea converts sound-driven mechanical vibrations into auditory nerve signals.
Tympanic membrane | Which thin membrane vibrates when sound travels down the external ear canal? | The tympanic membrane, or eardrum, transmits vibrations to the middle-ear ossicles.
Semicircular canals | Which inner-ear structures detect rotational movements of the head? | The semicircular canals sense angular acceleration through fluid movement and hair-cell deflection.
Eustachian tube | Which passage helps equalise pressure between the middle ear and the throat region? | The Eustachian tube connects the middle ear with the nasopharynx and assists pressure equalisation.
''')
    S('Synovial joint types', '''
Hinge joint | Which joint type permits mainly bending and straightening, as at the elbow? | A hinge joint primarily allows movement about one axis, resembling a door hinge.
Ball-and-socket joint | Which joint type allows movement in many directions, as at the shoulder? | A spherical head fits into a cup-like socket, allowing movement about multiple axes.
Pivot joint | Which joint type permits rotation around a central axis, as in the upper neck? | A pivot joint allows one bone to rotate around another within a ring-like arrangement.
Gliding joint | Which joint type allows relatively flat surfaces to slide over one another, as among some wrist bones? | Gliding joints permit limited sliding movements between relatively flat articular surfaces.
''')
    S('Muscle and attachment tissues', '''
Skeletal muscle | Which striated muscle type is mainly responsible for voluntary movement of the skeleton? | Skeletal muscles attach to bones and are generally controlled by the somatic nervous system.
Smooth muscle | Which non-striated muscle type is present in intestinal and many blood-vessel walls? | Smooth muscle produces involuntary movements in hollow organs and vessel walls.
Cardiac muscle | Which branched striated muscle type forms the heart wall and contracts rhythmically? | Cardiac muscle is specialised involuntary tissue joined by intercalated discs for coordinated contraction.
Tendon | Which strong connective tissue structure attaches muscle to bone? | A tendon transmits a muscle's pulling force to bone and is composed mainly of aligned collagen fibres.
''')
    S('Human reproductive structures', '''
Ovary | Which female reproductive organ produces oocytes and secretes ovarian hormones? | Ovaries contain developing follicles and produce oocytes as well as hormones including oestrogens and progesterone.
Testis | Which male reproductive organ produces sperm and secretes testosterone? | Testes contain seminiferous tubules for sperm production and hormone-producing interstitial cells.
Uterus | In which muscular organ does a normal human pregnancy develop after implantation? | The uterus supports implantation and development of the embryo and fetus within its lining and cavity.
Placenta | Which temporary organ enables exchange between maternal and fetal systems without normally mixing their blood directly? | The placenta mediates gas, nutrient and waste exchange and produces hormones during pregnancy.
''')
    S('Additional human hormones', '''
Growth hormone | Which anterior pituitary hormone supports body growth through direct actions and growth-factor pathways? | Growth hormone influences metabolism and stimulates growth, partly through insulin-like growth factors.
Antidiuretic hormone | Which hormone increases water reabsorption in kidney collecting ducts? | Antidiuretic hormone, also called vasopressin, helps conserve water by increasing collecting-duct water permeability.
Oxytocin | Which hormone promotes uterine contractions and milk ejection? | Oxytocin stimulates uterine smooth muscle and the contractile cells involved in milk ejection.
Melatonin | Which pineal hormone helps signal biological night and regulate circadian timing? | Melatonin secretion is linked to the light-dark cycle and communicates night-time information to the body.
''')
    S('Additional vitamins', '''
Vitamin B12 | Which vitamin requires intrinsic factor for efficient intestinal absorption and supports normal nerve and blood-cell function? | Vitamin B12 absorption depends on intrinsic factor; deficiency can affect blood formation and the nervous system.
Vitamin K | Which vitamin is needed for activation of several blood-clotting proteins? | Vitamin K supports a chemical modification required for the function of several coagulation factors.
Vitamin E | Which fat-soluble vitamin is known chiefly for antioxidant protection of cell membranes? | Vitamin E includes compounds that help protect membrane lipids from oxidative damage.
Niacin | Deficiency of which B vitamin classically causes pellagra? | Niacin, vitamin B3, is a precursor of NAD and NADP; severe deficiency causes pellagra.
''')
    S('Mineral nutrition', '''
Iodine | Which mineral element is required to synthesise thyroid hormones? | Iodine is incorporated into thyroid hormones, making adequate intake important for normal thyroid function.
Iron | Which mineral element is located in the haem groups that bind oxygen in haemoglobin? | Iron in haem is essential for oxygen binding and transport in red blood cells.
Calcium | Which mineral is a major component of bone mineral and participates in muscle contraction and cellular signalling? | Calcium salts strengthen bones, while calcium ions also perform crucial signalling and contraction roles.
Zinc | Which trace element supports many enzymes and is important in wound healing and normal immune function? | Zinc is a catalytic or structural component of many proteins and contributes to growth and tissue maintenance.
''')
    S('Useful microorganisms', '''
Lactobacillus | Which bacterial group is commonly associated with converting milk into curd through fermentation? | Lactobacilli produce lactic acid from sugars, helping acidify and coagulate milk.
Rhizobium | Which bacterial genus forms nitrogen-fixing associations in many legume root nodules? | Rhizobium and related bacteria convert atmospheric nitrogen into biologically usable compounds in symbiosis with legumes.
Saccharomyces | Which yeast genus is widely used to leaven bread and ferment alcoholic beverages? | Saccharomyces yeasts ferment sugars, releasing carbon dioxide and ethanol under suitable conditions.
Penicillium | Which mould genus supplied the original source of the antibiotic penicillin? | Penicillin was discovered from antibacterial substances produced by Penicillium moulds.
''')
    S('Major microorganism groups', '''
Bacteria | Which group consists of prokaryotic organisms typically having peptidoglycan in their cell walls? | Bacteria lack a membrane-enclosed nucleus and most possess cell walls containing peptidoglycan.
Archaea | Which prokaryotic domain has distinctive membrane chemistry and lacks bacterial peptidoglycan? | Archaea are distinct from bacteria in molecular features including membrane lipids and cell-wall chemistry.
Protists | Amoeba and Paramecium are usually placed in which broad school-level grouping of mainly unicellular eukaryotes? | Protists are diverse eukaryotes that include many single-celled organisms with membrane-bound nuclei.
Fungi | Which eukaryotic group commonly absorbs nutrients and has chitin-containing cell walls? | Fungi absorb organic nutrients from their surroundings and typically possess chitin-rich cell walls.
''')
    S('Vertebrate groups', '''
Mammals | Which vertebrate group is characterised by mammary glands and hair at some life stage? | Mammals nourish young with milk from mammary glands and possess hair, even when sparse or temporary.
Birds | Which living vertebrate group is uniquely characterised by feathers? | Birds possess feathers and are endothermic vertebrates, with wings that need not support flight in every species.
Reptiles | Which traditional vertebrate group includes lizards, snakes and turtles with keratinised scales or scutes? | Reptiles possess protective keratinised coverings and are generally ectothermic.
Amphibians | Which vertebrate group includes frogs and salamanders and commonly has moist permeable skin? | Amphibians often combine aquatic early development with terrestrial or semi-aquatic adult life, though life cycles vary.
''')
    S('Invertebrate phyla', '''
Annelida | Earthworms belong to which phylum characterised by a segmented body plan? | Annelids are segmented worms with serially repeated body units.
Arthropoda | Insects, spiders and crabs belong to which phylum with jointed appendages and an exoskeleton? | Arthropods have segmented bodies, jointed limbs and a chitin-containing external skeleton.
Mollusca | Snails, clams and octopuses belong to which phylum with a mantle and typically a muscular foot? | Molluscs have a soft body with a mantle; the foot and shell are modified or reduced in some groups.
Echinodermata | Starfish and sea urchins belong to which marine phylum with a water-vascular system? | Echinoderms have a water-vascular system and often show fivefold symmetry as adults.
''')
    S('Viral disease agents', '''
Poliovirus | Which virus can infect motor neurons and cause paralytic poliomyelitis? | Poliovirus is an enterovirus; a small fraction of infections progress to nervous-system involvement and paralysis.
Influenza virus | Which virus group causes seasonal influenza through infection of the respiratory tract? | Influenza viruses infect the respiratory tract and undergo antigenic changes that affect circulating strains.
Human immunodeficiency virus | Which retrovirus attacks key immune cells and can lead to AIDS? | HIV progressively impairs immune function, especially through effects on CD4 T lymphocytes.
Measles virus | Which virus causes the highly contagious illness classically featuring fever and a spreading rash? | Measles is caused by measles virus and spreads efficiently through airborne transmission.
''')
    S('Disease vectors', '''
Female Anopheles mosquito | Which mosquito transmits human malaria parasites during blood feeding? | Female Anopheles mosquitoes can carry and transmit Plasmodium parasites responsible for malaria.
Aedes mosquito | Which mosquito genus is a major vector of dengue virus? | Aedes mosquitoes, especially Aedes aegypti, transmit dengue and several other viruses.
Sandfly | Which small biting insect transmits the parasites causing visceral leishmaniasis in the Indian subcontinent? | Infected female sandflies transmit Leishmania parasites that can cause visceral leishmaniasis.
Housefly as mechanical carrier | Which common insect can carry pathogens from contaminated material to food without being a biological mosquito vector? | Houseflies can mechanically transfer microbes on body surfaces and through feeding-related contamination.
''')
    S('Immune-system concepts', '''
Antigen | What is a substance containing sites that can be specifically recognised by antibodies or adaptive immune receptors called? | An antigen is a substance recognised by the adaptive immune system. The particular site recognised on an antigen is an epitope or antigenic determinant.
Antibody | Which immune protein binds specifically to an antigenic target? | Antibodies are immunoglobulins produced by differentiated B cells and bind particular antigenic structures.
Vaccination | Which preventive process presents antigenic information to establish immune protection without requiring the natural disease? | Vaccination stimulates protective immune responses and often establishes memory against a pathogen.
Immunological memory | Why can a later exposure to a previously encountered antigen trigger a faster, stronger response? | Long-lived memory lymphocytes allow adaptive immunity to respond more efficiently to a repeated antigen.
''')
    S('Ecological feeding roles', '''
Primary producer | Which ecological role converts inorganic carbon into organic biomass using light or chemical energy? | Primary producers synthesise organic matter and supply the initial energy-rich biomass for many food webs.
Primary consumer | What is an organism that feeds directly on primary producers called? | Primary consumers obtain energy by eating producers and commonly include herbivores.
Decomposer | Which role breaks down dead organic material externally and absorbs simpler products? | Decomposers such as many fungi and bacteria recycle nutrients through chemical breakdown of organic matter.
Detritivore | What is an animal that ingests fragments of dead organic material called? | Detritivores consume detritus physically, complementing the chemical decomposition performed by microbes.
''')
    S('Interactions between species', '''
Mutualism | Two interacting species each gain a benefit. What is the interaction called? | Mutualism benefits both partners, as in many pollinator-plant associations.
Commensalism | One species benefits while the other is neither significantly helped nor harmed. What is this interaction? | Commensalism gives one partner a benefit with no appreciable effect on the other under the described conditions.
Parasitism | One organism obtains resources from a host while harming it. What interaction is this? | Parasitism benefits the parasite at the host's expense, usually without immediate host death.
Competition | Two organisms depend on the same limited resource and each reduces the other's access. What interaction is this? | Competition occurs when shared limited resources constrain the success of interacting organisms.
''')

    S('Genetic description', '''
Genotype | What term describes an organism's genetic constitution at one or more specified loci? | Genotype refers to genetic makeup, such as the allele combination at a particular gene locus.
Phenotype | What term describes observable characteristics arising from genotype and environmental influences? | Phenotype includes observable traits and reflects both genetic and environmental contributions.
Homozygous | A diploid organism carries two identical alleles at a locus. How is it described at that locus? | Homozygosity means that the two homologous copies carry the same allele at the specified locus.
Heterozygous | A diploid organism carries two different alleles at a locus. How is it described at that locus? | Heterozygosity means that the homologous copies carry different alleles at that locus.
''')

    # Geography: 50 groups plus two individually authored application questions.
    G('Earth interior', '''
Crust | Which compositional layer forms Earth's thin outermost rocky shell? | The crust is Earth's outer rocky layer and is generally thinner beneath oceans than beneath continents.
Mantle | Which thick silicate-rich layer lies between Earth's crust and core? | The mantle extends below the crust to the core and is mostly solid rock capable of slow deformation.
Outer core | Which major internal layer is liquid and helps generate Earth's magnetic field? | The outer core is a liquid iron-rich layer whose moving conductive fluid supports the geodynamo.
Inner core | Which central iron-rich layer remains solid despite very high temperatures because of immense pressure? | Earth's inner core is solid, with pressure strongly affecting the melting conditions of its material.
''')
    G('Earthquake waves and origin', '''
P wave | Which seismic body wave is compressional and can pass through both solids and liquids? | Primary waves compress and expand material in the travel direction and propagate through solids and fluids.
S wave | Which seismic body wave is a shear wave and cannot travel through a liquid? | Secondary waves require shear rigidity, which liquids lack, so they do not pass through the liquid outer core.
Surface wave | Which seismic wave category travels along Earth's surface and can cause strong ground motion? | Surface waves are concentrated near Earth's surface and often have large damaging amplitudes.
Hypocentre | What is the underground point where an earthquake rupture begins called? | The hypocentre, or focus, is the earthquake's initiation point below the surface; the epicentre is directly above it.
''')
    G('Plate-boundary processes', '''
Divergent boundary | At which boundary do plates move apart and new oceanic crust commonly forms? | Divergent boundaries separate plates; rising magma can solidify to form new crust at spreading centres.
Convergent boundary | At which boundary do plates move toward one another, producing collision or subduction? | Convergent motion brings plates together and can build mountains or consume lithosphere by subduction.
Transform boundary | At which boundary do plates slide mainly horizontally past one another? | Transform boundaries accommodate lateral motion without systematic creation or destruction of crust.
Subduction | What is the process in which one lithospheric plate descends beneath another called? | Subduction carries one plate downward into the mantle at a convergent margin and commonly forms a trench.
''',USGS)
    G('Mountain-building forms', '''
Fold mountain | Which mountain type is produced chiefly by compression and folding of rock layers? | Fold mountains develop where compressional tectonics shorten and thicken the crust, as in major collision belts.
Fault-block mountain | Which mountain type forms when blocks of crust move vertically along faults? | Fault-block mountains are elevated crustal blocks bounded by significant faults.
Volcanic mountain | Which mountain type is built by accumulated lava and other erupted material? | Volcanic mountains grow through eruptions that add material around vents.
Residual mountain | Which mountain type is left after prolonged erosion removes less resistant surrounding material? | Residual mountains are erosional remnants that survive because of resistant rocks or protected structure.
''')
    G('Volcanic forms', '''
Shield volcano | Which volcano type typically has broad gentle slopes built by fluid basaltic lava? | Shield volcanoes grow from repeated low-viscosity lava flows that spread over wide areas.
Composite volcano | Which volcano type is commonly steep and built of alternating lava and fragmental deposits? | Composite volcanoes, or stratovolcanoes, contain layered erupted materials and may produce explosive eruptions.
Caldera | What is a large volcanic depression commonly formed when the roof of a magma chamber collapses? | A caldera is a broad collapse depression, often associated with substantial magma withdrawal during eruption.
Lava plateau | Extensive eruptions through fissures spread repeated lava sheets over a wide area. What landform can result? | A lava plateau is built by widespread flood-lava flows, commonly basaltic.
''')
    G('Weathering mechanisms', '''
Freeze-thaw weathering | Water enters rock cracks, freezes and expands repeatedly. Which weathering mechanism can break the rock? | Repeated freezing of water in fractures exerts stress and can mechanically widen and break the rock.
Oxidation weathering | Iron-bearing minerals react with oxygen and form oxide products. Which weathering mechanism is this? | Oxidation changes mineral chemistry through reaction with oxygen and can weaken iron-bearing rocks.
Carbonation | Weak carbonic acid in water dissolves limestone. What chemical-weathering process is this? | Carbonation uses dissolved carbon dioxide and water to produce acidic reactions that dissolve carbonate rocks.
Hydration | A mineral incorporates water into its structure and may expand. Which chemical-weathering process is this? | Hydration adds water to a mineral structure, altering properties and sometimes causing expansion.
''')
    G('River erosion mechanisms', '''
Hydraulic action | Turbulent flowing water itself forces against and loosens riverbank material. What erosional mechanism is this? | Hydraulic action removes material through the force and pressure of moving water.
Abrasion | Sediment carried by a river scrapes its bed and banks. What erosion mechanism occurs? | Abrasion wears surfaces as transported particles grind and scrape against them.
Attrition | Pebbles carried downstream collide with one another and become smaller and rounder. What process is this? | Attrition breaks and rounds transported particles through mutual collisions.
Solution erosion | A river removes soluble minerals in dissolved form. What process is this? | Solution erosion, or corrosion, chemically dissolves material and transports it as dissolved ions.
''')
    G('Glacial landforms', '''
Cirque | Which bowl-shaped hollow is eroded near the head of a mountain glacier? | A cirque is an amphitheatre-like basin excavated by a glacier near its source.
Arete | Which narrow sharp ridge can form between neighbouring glacial cirques or valleys? | An arete is a knife-like ridge sharpened by glacial erosion on opposite sides.
U-shaped valley | Which valley cross-section is characteristic of a glacier widening and deepening a former river valley? | Glacial erosion commonly produces a broad floor and steep sides, giving a U-shaped cross-section.
Moraine | What is a ridge or accumulation of unsorted debris deposited or pushed by a glacier called? | Moraines consist of glacially transported debris and can mark glacier margins or former positions.
''')
    G('Wind-shaped landforms', '''
Sand dune | Which hill or ridge forms from wind-deposited sand? | Sand dunes grow where wind-blown sand accumulates and may migrate as grains move across them.
Loess | What is an extensive deposit of wind-blown silt called? | Loess consists chiefly of fine wind-deposited silt and can form fertile but erosion-prone soils.
Yardang | Which streamlined ridge is carved by persistent wind erosion in suitable material? | Yardangs are elongated wind-eroded ridges commonly aligned with the prevailing abrasive wind.
Deflation hollow | Which depression forms when wind removes loose fine material from the ground? | A deflation hollow develops where wind excavation lowers the surface by removing transportable particles.
''')
    G('Karst features', '''
Sinkhole | Which closed depression forms where soluble rock dissolves or an underground cavity collapses? | Sinkholes are surface depressions common in karst terrain and may form gradually or by collapse.
Limestone cave | Which underground void develops through dissolution along fractures in carbonate rock? | Limestone caves enlarge as slightly acidic water dissolves carbonate minerals along joints and bedding planes.
Stalactite | Which cave mineral deposit hangs downward from the ceiling? | Stalactites grow downward as dripping water deposits minerals from a cave roof.
Stalagmite | Which cave mineral deposit grows upward from the floor below dripping water? | Stalagmites build upward where mineral-bearing drops deposit material on a cave floor.
''')
    G('Coastal features', '''
Spit | Which narrow sediment ridge projects from a coast into water, often with a curved end? | A spit grows through longshore sediment transport and extends outward from an attached coastal end.
Tombolo | Which sediment bar links an island to the mainland or another island? | A tombolo forms when deposited sediment creates a connecting ridge to an island.
Lagoon | What is a shallow coastal water body separated from the open sea by a barrier called? | A lagoon lies behind a coastal barrier and may retain restricted connections with the sea.
Sea arch | Waves erode through a headland to form an opening. What coastal landform results? | A sea arch is an opening cut through a coastal rock mass, often after caves enlarge and connect.
''')
    G('Major oceans', '''
Pacific Ocean | Which ocean lies between the Americas and Asia-Australia and is the largest ocean basin? | The Pacific is Earth's largest ocean basin, extending between the American and Asian-Australian margins.
Atlantic Ocean | Which ocean separates the Americas from Europe and Africa? | The Atlantic occupies the basin between the Americas to the west and Europe and Africa to the east.
Indian Ocean | Which ocean lies south of Asia, between eastern Africa and western Australia? | The Indian Ocean is bounded by Asia to the north, Africa to the west and Australia to the east.
Arctic Ocean | Which ocean surrounds the North Pole and is largely enclosed by northern landmasses? | The Arctic Ocean occupies the polar region north of Eurasia and North America.
''')
    G('Ocean-floor relief', '''
Continental shelf | Which shallow submerged extension of a continent lies before the steep continental slope? | The continental shelf is the gently sloping submerged continental margin adjoining the coast.
Continental slope | Which relatively steep zone descends from the shelf edge toward the deep ocean? | The continental slope marks a major descent from shallow continental margin to deep-sea depths.
Abyssal plain | Which broad, comparatively flat deep-ocean surface is commonly covered by fine sediment? | Abyssal plains are deep seafloor regions whose irregularities have often been buried by sediment.
Ocean trench | Which long narrow deep-ocean depression commonly marks a subduction zone? | Ocean trenches form near plate boundaries where one plate bends and descends beneath another.
''')
    G('Ocean-water structure', '''
Salinity | Which property measures the concentration of dissolved salts in seawater? | Salinity quantifies dissolved salt content and affects water density and ocean circulation.
Thermocline | What is a water layer with a rapid temperature change with depth called? | A thermocline separates layers with markedly different temperatures across a relatively short depth interval.
Halocline | What is a water layer with a rapid salinity change with depth called? | A halocline is a strong vertical salinity gradient that contributes to density stratification.
Upwelling | Which process brings deeper, often nutrient-rich water toward the ocean surface? | Upwelling replaces displaced surface water with water from depth and can support productive marine food webs.
''',NOAA)
    G('Named ocean currents', '''
Gulf Stream | Which warm western-boundary current flows northward off the eastern United States? | The Gulf Stream carries warm water along the western North Atlantic and continues into the broader North Atlantic circulation.
Labrador Current | Which cold current flows southward along Labrador and toward Newfoundland? | The Labrador Current transports cold water southward along northeastern North America.
Benguela Current | Which cold current flows northward along southwestern Africa? | The Benguela Current and associated coastal upwelling help cool the southwestern African coast.
Kuroshio Current | Which warm western-boundary current flows past Taiwan and Japan in the North Pacific? | The Kuroshio carries warm subtropical water northward along the western North Pacific margin.
''',NOAA)
    G('Tidal patterns', '''
Spring tide | Which tide has a relatively large range when the Sun, Moon and Earth are approximately aligned? | Spring tides occur around new and full moons, when solar and lunar tidal effects reinforce each other.
Neap tide | Which tide has a relatively small range when solar and lunar tidal effects partly oppose each other? | Neap tides occur near the Moon's first and third quarters, reducing the tidal range.
Diurnal tide | What tidal pattern has one high tide and one low tide in a lunar day? | A diurnal tidal regime has one high-water and one low-water period per lunar day.
Semidiurnal tide | What tidal pattern has two high tides and two low tides of roughly similar height in a lunar day? | A semidiurnal regime has two broadly similar tidal cycles during a lunar day.
''',TIDES)
    G('Atmospheric constituents', '''
Water vapour | Which variable atmospheric component is central to cloud formation and precipitation? | Water vapour is gaseous water; condensation and deposition from it help create clouds and precipitation.
Ozone | Which three-oxygen-atom gas absorbs much harmful solar ultraviolet radiation in the stratosphere? | Stratospheric ozone absorbs important ultraviolet wavelengths and protects the surface from much of this radiation.
Argon | Which noble gas is the most abundant noble-gas component of Earth's dry atmosphere? | Argon is an inert atmospheric gas comprising just under one percent of dry air.
Carbon dioxide | Which carbon-containing atmospheric gas supplies the carbon fixed into sugars during photosynthesis and is released during aerobic respiration? | Carbon dioxide supplies carbon for photosynthesis and is released when organic carbon is oxidised during aerobic respiration. Water vapour, ozone and argon contain no carbon.
''')
    G('Global pressure belts', '''
Equatorial low-pressure belt | Which broad pressure zone is associated with strong heating and rising air near the equator? | Equatorial convergence and rising warm air are associated with a low-pressure belt near the equator.
Subtropical high-pressure belts | Which pressure belts near 30° latitude are associated with descending air? | Descending branches of the Hadley circulation help produce subtropical high pressure and many dry climates.
Subpolar low-pressure belts | Which pressure zones near 60° latitude are associated with rising air and frequent frontal activity? | Subpolar lows develop near convergence of midlatitude and polar circulation systems.
Polar high-pressure regions | Which pressure regions are associated with cold dense air over high latitudes? | Cold descending air favours high pressure in polar regions, feeding outward-moving surface winds.
''')
    G('Large-scale wind systems', '''
Trade winds | Which tropical surface winds generally blow from subtropical highs toward the equatorial low? | Trade winds blow toward lower tropical pressure and are deflected into easterly winds by Earth's rotation.
Westerlies | Which prevailing midlatitude winds generally blow from west toward east? | Westerlies dominate much of the midlatitude circulation between subtropical and subpolar pressure zones.
Polar easterlies | Which cold surface winds generally blow outward from polar high-pressure regions with an easterly component? | Polar easterlies flow away from polar highs and are deflected by rotation toward an easterly direction.
Jet streams | What are the narrow bands of very strong winds in the upper troposphere called? | Jet streams are fast upper-level air currents associated with strong horizontal temperature gradients.
''')
    G('Local thermal winds', '''
Sea breeze | On a sunny coast during daytime, cooler air moves from sea to warmer land. What wind is this? | A sea breeze develops as land heats faster than sea and lower pressure over land draws air inland.
Land breeze | On a clear coastal night, air moves from cooler land toward relatively warmer water. What wind is this? | A land breeze develops when land cools faster and relatively higher pressure over land drives air seaward.
Valley breeze | During daytime heating, air moves upslope from a valley toward mountain slopes. What wind is this? | A valley breeze is an upslope flow driven by warming of mountain slopes during the day.
Mountain breeze | During a clear night, dense cooled air drains downslope into a valley. What wind is this? | A mountain breeze is a downslope nocturnal flow caused by cooling over elevated slopes.
''')
    G('Indian monsoon phases', '''
Advancing southwest monsoon | Which seasonal phase brings moisture-bearing southwest winds across much of India in the main summer rainy season? | The advancing southwest monsoon spreads the summer monsoon circulation and rainfall over the country.
Retreating monsoon | What is the seasonal withdrawal of the southwest monsoon during the post-monsoon transition called? | The retreating monsoon marks the southward withdrawal of the summer rain belt and changing circulation.
Monsoon break | What is a temporary lull in rainfall over much of the core monsoon zone during the rainy season called? | A monsoon break is an intraseasonal interruption associated with shifts in the monsoon trough and circulation.
Monsoon burst | What term commonly describes a sudden marked onset of sustained monsoon rains in a region? | A monsoon burst refers to the abrupt increase in rainfall accompanying the onset of monsoon conditions.
''',IMD)
    G('Indian seasonal weather', '''
Western disturbance | Which travelling extratropical weather system brings much winter precipitation to northwestern India? | Western disturbances move eastward in the subtropical westerlies and bring rain or snow to northwestern regions.
Loo | What is the hot, dry summer wind associated with the northern Indian plains? | The loo is a hot dry wind occurring in the pre-monsoon season over parts of northern India.
Mango showers | What name is commonly given to pre-monsoon showers that help mango development in parts of southern India? | Mango showers are pre-monsoon rains in southern regions associated with the mango-ripening season.
Norwesters | Which violent pre-monsoon thunderstorms in eastern India are often called Kalbaisakhi? | Norwesters are strong pre-monsoon convective storms associated with squalls, rain and sometimes hail.
''',IMD)
    G('Tropical ocean-atmosphere variability', '''
El Nino | Which ENSO phase involves unusually warm sea-surface temperatures in the central or eastern equatorial Pacific? | El Nino is the warm phase of ENSO and alters tropical atmospheric circulation and rainfall patterns.
La Nina | Which ENSO phase involves unusually cool central or eastern equatorial Pacific sea-surface temperatures? | La Nina is the cool phase of ENSO, with ocean-atmosphere anomalies generally opposing those of El Nino.
Indian Ocean Dipole | Which climate pattern involves a difference in sea-surface temperature anomalies between western and eastern equatorial Indian Ocean regions? | The Indian Ocean Dipole describes a west-east temperature-anomaly contrast that can affect regional rainfall.
Walker circulation | Which tropical atmospheric circulation has rising and sinking branches connected mainly in the east-west direction? | Walker circulation is the zonal overturning of tropical air linked to longitudinal variations in ocean temperature and convection.
''',IMD)
    G('Climate types', '''
Mediterranean climate | Which climate has characteristic dry summers and mild wetter winters? | Mediterranean climates have summer dryness under subtropical influence and winter rainfall associated with shifting westerlies.
Savanna climate | Which tropical climate has a pronounced wet season and dry season supporting extensive grasslands? | Tropical savanna climates alternate wet and dry seasons and often support grasses with scattered trees.
Tundra climate | Which cold climate has very short cool summers and generally supports low vegetation without forests? | Tundra climates restrict tree growth and favour low plants during a brief growing season.
Steppe climate | Which semi-arid climate supports grassland but is drier than typical forest climates? | Steppe climates receive limited precipitation, commonly supporting grasses rather than dense forests.
''')
    G('Mapping methods', '''
Map scale | What expresses the relationship between distance on a map and the corresponding ground distance? | Map scale is the ratio or graphical relationship linking mapped distance to real-world distance.
Contour line | What map line connects points at equal elevation? | A contour joins locations of the same height relative to a reference surface, allowing relief to be represented.
Geographic information system | Which computer system stores, analyses and displays data linked to geographic locations? | A GIS manages spatial data and combines location with attribute information for analysis and mapping.
Remote sensing | What is obtaining information about Earth's surface from sensors without direct physical contact called? | Remote sensing measures reflected or emitted energy from a distance, commonly using satellites or aircraft.
''')

    G('Major Indian physiographic regions', '''
Himalayan mountain system | Which young fold-mountain region forms India's major northern barrier? | The Himalayas developed through continental collision and form the great mountain arc north of the Indian plains.
Northern plains | Which extensive Indian region was built mainly from alluvium of the Indus, Ganga and Brahmaputra systems? | The northern plains consist largely of deep river-laid alluvium deposited in a broad foreland basin.
Peninsular plateau | Which broad Indian region consists largely of ancient crystalline rocks south of the northern plains? | The Peninsular plateau is an old stable landmass containing extensive igneous and metamorphic rocks.
Coastal plains | Which Indian physiographic regions form comparatively low-lying belts between the sea and the adjoining uplands? | India's coastal plains fringe the peninsula between the coast and the Western or Eastern Ghats.
''',INDIA_PHYS)
    G('Himalayan divisions', '''
Himadri | Which Himalayan division is the northernmost main range and contains many of the highest peaks? | The Himadri, or Greater Himalaya, forms the high continuous core of the main Himalayan ranges.
Himachal | Which Himalayan division lies between the Himadri and the Shiwaliks? | The Himachal, or Lesser Himalaya, lies south of the Greater Himalaya and includes several important hill ranges.
Shiwalik | Which outer Himalayan range consists largely of relatively young unconsolidated sediments? | The Shiwaliks form the outermost southern Himalayan belt and include sediments eroded from higher ranges.
Purvanchal | What name is given to the eastern hills extending along India's northeastern border after the Himalayas bend southward? | Purvanchal includes northeastern hill ranges such as the Patkai, Naga, Manipur and Mizo hills.
''',INDIA_PHYS)
    G('Indian mountain ranges', '''
Aravalli Range | Which ancient eroded range runs broadly southwest to northeast through Rajasthan toward Delhi? | The Aravallis are an old mountain system extending through Rajasthan and adjoining areas.
Vindhya Range | Which upland range lies mainly north of the Narmada valley in central India? | The Vindhyan uplands form a significant central Indian escarpment and range system north of the Narmada.
Satpura Range | Which central Indian range lies mainly between the Narmada and Tapi valleys? | The Satpuras rise south of the Narmada and north of the Tapi across central India.
Western Ghats | Which long escarpment borders the western edge of the Deccan plateau? | The Western Ghats run roughly parallel to India's west coast and form a major orographic barrier.
''',INDIA_PHYS)
    G('Southern Indian hills', '''
Eastern Ghats | Which discontinuous hill system runs broadly along India's eastern side and is cut by major east-flowing rivers? | The Eastern Ghats form broken ranges separated by large river valleys along the peninsula's eastern margin.
Nilgiri Hills | Which southern hill region forms a junction of the Western and Eastern Ghats? | The Nilgiris occupy the meeting region of the two major peninsular hill systems.
Anaimalai Hills | In which southern hill range is Anamudi, the highest peak in Peninsular India, located? | Anamudi rises in the Anaimalai region of the southern Western Ghats.
Cardamom Hills | Which southern Western Ghats hill region is especially associated with spice cultivation and lies south of the Anaimalai region? | The Cardamom Hills occupy the southern Western Ghats and are known for humid uplands and spice cultivation.
''',INDIA_PHYS)
    G('Indian plateaus', '''
Malwa Plateau | Which central-western Indian plateau lies mainly north of the Vindhyan escarpment? | The Malwa Plateau occupies parts of western Madhya Pradesh and southeastern Rajasthan north of the Vindhyan region.
Chota Nagpur Plateau | Which eastern Indian plateau is especially associated with major coal and mineral resources? | The Chota Nagpur Plateau includes much of Jharkhand and adjoining mineral-rich uplands.
Meghalaya Plateau | Which northeastern plateau includes the Garo, Khasi and Jaintia hills? | The Meghalaya Plateau is an elevated block containing the Garo, Khasi and Jaintia hill regions.
Deccan Plateau | Which large triangular plateau lies south of the Narmada and between the two Ghats systems? | The Deccan forms the broad southern plateau, sloping generally eastward and bounded by major upland margins.
''',INDIA_PHYS)
    G('Northern plain belts', '''
Bhabar | Which porous pebble belt along the Himalayan foothills often allows streams to disappear underground? | Bhabar consists of coarse piedmont deposits with high infiltration near the foot of the Shiwaliks.
Terai | Which moist belt south of the Bhabar includes areas where underground streams re-emerge? | The Terai has wetter, finer deposits and historically extensive marshes where subsurface water returns to the surface.
Bhangar | What is the older alluvial terrace material of the northern plains called? | Bhangar is older alluvium lying above the more frequently renewed floodplain deposits.
Khadar | What is the newer river-deposited alluvium in active floodplains called? | Khadar is comparatively recent alluvium replenished by river flooding and deposition.
''',INDIA_PHYS)
    G('Northern and western rivers', '''
Ganga | Which river takes this name after the Bhagirathi and Alaknanda meet at Devprayag? | The confluence of Bhagirathi and Alaknanda at Devprayag marks the beginning of the river named Ganga.
Yamuna | Which major Ganga tributary flows past Delhi and joins the Ganga at Prayagraj? | The Yamuna flows through northern India and meets the Ganga at Prayagraj.
Indus | Which river system includes the Jhelum, Chenab, Ravi, Beas and Sutlej among its major tributary rivers? | These five Punjab rivers form important tributary branches of the Indus drainage system.
Tapi | Which major west-flowing river runs south of the Satpura range toward the Gulf of Khambhat? | The Tapi flows west across central and western India and enters the Arabian Sea near Surat.
''')
    G('Additional peninsular rivers', '''
Mahanadi | Which major east-flowing river traverses Chhattisgarh and Odisha before reaching the Bay of Bengal? | The Mahanadi drains parts of east-central India and builds a delta on the Odisha coast.
Kaveri | Which river rises in the Brahmagiri region and flows through Karnataka and Tamil Nadu? | The Kaveri originates at Talakaveri in the Western Ghats and flows east across southern India.
Sabarmati | Which west-flowing river passes through Ahmedabad? | The Sabarmati flows through Rajasthan and Gujarat, including Ahmedabad, toward the Gulf of Khambhat.
Luni | Which arid-region river flows through western Rajasthan toward the Rann of Kachchh? | The Luni drains parts of western Rajasthan and loses much of its water in the arid lowlands toward the Rann.
''')
    G('Tributaries of northern river systems', '''
Chambal | Which Yamuna tributary is associated with extensive ravines in parts of Madhya Pradesh and Rajasthan? | The Chambal drains central Indian uplands and is known for deeply dissected ravine landscapes.
Betwa | Which Yamuna tributary flows through the Bundelkhand region and past Orchha? | The Betwa rises in central India and flows through Bundelkhand before joining the Yamuna.
Son | Which major southern tributary of the Ganga originates near the Amarkantak region? | The Son flows from central Indian uplands toward the Ganga and has a broad seasonal river bed.
Kosi | Which Himalayan tributary of the Ganga is known for channel shifts and major flooding in Bihar? | The Kosi brings heavy sediment from Himalayan catchments and has historically shifted channels across the plains.
''')
    G('Major dam-river associations', '''
Bhakra Dam — Sutlej | Which dam-river pairing correctly identifies Bhakra Dam? | Bhakra Dam is built across the Sutlej and forms the Gobind Sagar reservoir.
Hirakud Dam — Mahanadi | Which dam-river pairing identifies the large dam near Sambalpur in Odisha? | Hirakud Dam is across the Mahanadi near Sambalpur.
Tehri Dam — Bhagirathi | Which dam-river pairing identifies the major high dam in Uttarakhand's Tehri region? | Tehri Dam is constructed on the Bhagirathi, one of the principal headstreams of the Ganga.
Sardar Sarovar — Narmada | Which dam-river pairing identifies the major multipurpose dam in Gujarat's Narmada valley? | Sardar Sarovar is a major dam on the Narmada River.
''')
    G('Indian lakes and wetlands', '''
Wular Lake | Which large freshwater lake lies in the Kashmir Valley and is associated with the Jhelum system? | Wular is a freshwater lake in the Kashmir Valley connected with the Jhelum drainage.
Chilika Lake | Which large brackish coastal lagoon lies in Odisha? | Chilika is a brackish lagoon on the Odisha coast, linked to the Bay of Bengal.
Loktak Lake | Which Manipur lake is known for floating masses of vegetation called phumdis? | Loktak contains phumdis, floating accumulations of vegetation, soil and organic material.
Vembanad Lake | Which long Kerala lake forms an important part of the state's backwater system? | Vembanad is a major Kerala backwater lake, linked with rivers and coastal waterways.
''')
    G('Indian island settings', '''
Lakshadweep | Which Indian island group in the Arabian Sea is principally associated with coral atolls? | Lakshadweep consists of coral island and atoll formations in the Arabian Sea off southwestern India.
Andaman and Nicobar Islands | Which Indian island group lies in the Bay of Bengal and includes Barren Island volcano? | The Andaman and Nicobar chain lies along an island arc in the eastern Bay of Bengal.
Rameswaram Island | Which Tamil Nadu island is linked to the mainland by the Pamban crossing? | Rameswaram lies off the Tamil Nadu coast and is connected across the Pamban channel.
Sriharikota | Which barrier island on the Andhra Pradesh coast hosts the Satish Dhawan Space Centre? | Sriharikota lies between the Bay of Bengal and Pulicat Lake and hosts India's principal launch centre.
''')
    G('Indian channels and straits', '''
Palk Strait | Which shallow strait lies between southeastern India and northern Sri Lanka? | Palk Strait separates parts of Tamil Nadu from northern Sri Lanka.
Gulf of Mannar | Which gulf lies between southeastern India and western Sri Lanka, south of the Palk region? | The Gulf of Mannar occupies the sea area south of the Palk Strait and Adam's Bridge region.
Nine Degree Channel | Which channel separates Minicoy from the main northern Lakshadweep island group? | The Nine Degree Channel lies north of Minicoy and south of the main Lakshadweep islands.
Ten Degree Channel | Which channel separates the Andaman island group from the Nicobar island group? | The Ten Degree Channel lies between Little Andaman and the northern Nicobar region.
''')
    G('Indian mountain passes and gaps', '''
Nathu La | Which pass in Sikkim connects India with the Tibet Autonomous Region? | Nathu La is a high Himalayan pass in eastern Sikkim on the India-China boundary.
Shipki La | Which pass is associated with Himachal Pradesh and the Sutlej's entry region from Tibet? | Shipki La is in the Kinnaur region near the route by which the Sutlej enters India.
Zoji La | Which pass links the Kashmir Valley with the Ladakh region on the Srinagar-Leh route? | Zoji La is a major high pass on the road connection between Kashmir and Ladakh.
Palghat Gap | Which low gap in the Western Ghats links the Kerala plains with the Coimbatore region? | The Palghat Gap is a broad break between the Nilgiri and Anaimalai hill regions.
''')
    G('Indian ports and coasts', '''
Mumbai | Which major Indian port occupies a natural harbour on the Maharashtra coast? | Mumbai is a west-coast port city with a sheltered natural harbour facing the Arabian Sea.
Chennai | Which major Tamil Nadu port city lies on the Coromandel Coast and has an artificial harbour? | Chennai is an east-coast port developed through engineered harbour protection on a relatively open coast.
Kochi | Which Kerala port is associated with a sheltered backwater-linked harbour on the Malabar Coast? | Kochi's harbour links the Arabian Sea with Kerala's coastal backwater setting.
Deendayal Port at Kandla | Which major Gujarat port lies on the Gulf of Kachchh and was formerly known simply as Kandla Port? | Deendayal Port is situated at Kandla in the Gulf of Kachchh on India's western coast.
''')
    G('Crop environment requirements', '''
Rice | Which major cereal is well suited to warm conditions and abundant water, with many varieties grown in flooded fields? | Rice commonly requires warm growing conditions and plentiful water, though upland and other production systems also exist.
Wheat | Which major cereal in India is generally sown in the cool season and needs drier conditions near ripening? | Wheat is an important rabi cereal, benefiting from cool early growth and relatively dry sunny conditions at maturity.
Tea | Which beverage crop is made from harvested leaves and buds of Camellia sinensis? | Tea is made from the leaves and buds of Camellia sinensis; suitable humid climates and well-drained soils support its cultivation.
Coffee | Which beverage crop uses the processed seeds of Coffea arabica or Coffea canephora? | Coffee uses seeds of Coffea species, chiefly arabica and canephora (Robusta); Indian cultivation commonly uses shade trees.
''')
    G('Soil-conserving agriculture', '''
Terracing | Steep slopes are cut into level steps to reduce runoff and cultivate crops. What practice is this? | Terracing shortens and flattens slopes, slowing runoff and retaining soil and water.
Contour ploughing | Fields are ploughed along lines of equal elevation rather than straight downslope. What practice is this? | Contour ploughing follows the slope's contour and helps impede runoff and erosion.
Crop rotation | Different crop types are grown in a planned sequence on the same field across seasons. What practice is this? | Crop rotation can improve nutrient management and interrupt pest and disease cycles.
Mixed cropping | Two or more crops are grown together on the same field without a fixed row arrangement. What practice is this? | Mixed cropping combines crops in one field and can reduce the risk of total crop failure.
''')
    G('Irrigation systems', '''
Drip irrigation | Which irrigation method delivers small controlled quantities of water near plant roots through emitters? | Drip systems apply water locally, reducing some conveyance and evaporation losses when well managed.
Sprinkler irrigation | Which method distributes irrigation water as an artificial rain-like spray? | Sprinkler irrigation uses pressurised water and nozzles to distribute water over a field.
Canal irrigation | Which irrigation method conveys diverted river or reservoir water through an artificial channel network? | Canal irrigation carries surface water through channels to agricultural land.
Tank irrigation | Which method stores runoff in local reservoirs, often useful in suitable peninsular landscapes? | Tank irrigation collects and stores surface runoff in reservoirs for later use on nearby fields.
''')
    G('Indian mineral resources', '''
Bauxite | Which ore is the main commercial source of aluminium? | Bauxite is an aluminium-rich ore containing hydrated aluminium minerals.
Hematite | Which iron ore mineral has the formula Fe₂O₃? | Hematite is iron oxide and a major iron-ore mineral.
Mica | Which mineral group is valued for splitting into thin sheets and for electrical insulation? | Micas have layered crystal structures that allow thin flexible sheets with useful insulating properties.
Manganese ore | Which mineral resource supplies a metal widely used to improve steel and remove impurities during steelmaking? | Manganese is important in steel production for alloying and metallurgical treatment.
''')
    G('Indian coalfields', '''
Jharia | Which Jharkhand coalfield around Dhanbad is especially associated with India's prime coking-coal resources? | Jharia lies around Dhanbad and contains major prime coking-coal resources. The Coal Directory separately records East and West Bokaro's coking resources as medium coking, so coking coal alone would not distinguish these fields.
Raniganj | Which historic coalfield lies mainly in West Bengal along the Damodar region? | Raniganj is one of India's oldest coal-mining regions and lies chiefly in West Bengal.
Bokaro | Which Jharkhand coalfield shares its name with an important steel-industry city? | Bokaro is a major coal-bearing area of Jharkhand associated with the Damodar valley industrial region.
Talcher | Which major coalfield is located in Odisha's Angul region? | Talcher is an important Odisha coalfield and a major source of thermal coal.
''')
    G('Industrial city associations', '''
Jamshedpur — iron and steel | Which association identifies the major eastern Indian industrial city founded around an integrated steel works? | Jamshedpur in Jharkhand developed as a major iron-and-steel industrial centre.
Chittaranjan — locomotives | Which association identifies the West Bengal industrial town known for locomotive manufacturing? | Chittaranjan is strongly associated with railway locomotive production.
Kanpur — leather | Which association identifies the Uttar Pradesh industrial city well known for leather processing? | Kanpur has a long-established leather and tannery industry among its major industrial activities.
Surat — diamond cutting | Which association identifies the Gujarat city known internationally for diamond cutting and polishing? | Surat is a major centre for diamond processing as well as textile production.
''')
    G('Population measures', '''
Population density | Which measure divides the number of people by the land area they occupy? | Population density expresses people per unit area and indicates how concentrated settlement is.
Sex ratio in Indian census usage | Which measure expresses the number of females per thousand males in Indian census reporting? | India's conventional overall sex ratio is calculated as females divided by males, multiplied by one thousand.
Literacy rate | Which measure describes the share of an eligible population able to read and write with understanding? | Literacy rate is a proportion defined using a stated age threshold and a specified ability criterion.
Urbanisation | What is the process by which an increasing share of the population lives in urban settlements? | Urbanisation refers to growth in the urban share of population and associated settlement changes.
''')
    G('Rural settlement patterns', '''
Nucleated settlement | Houses form a dense, irregular cluster, rather than a ring, an elongated line or widely scattered individual homes. Which settlement description fits? | A nucleated or compact settlement has a concentrated cluster of dwellings. The irregular cluster specified here does not describe the ring-shaped or linear alternatives.
Dispersed settlement | Farmhouses are scattered individually over a wide area. What settlement pattern is this? | A dispersed settlement has widely separated dwellings rather than a dense central cluster.
Linear settlement | Houses extend mainly along a road, river bank or canal. What settlement pattern is this? | A linear settlement follows an elongated transport route or geographic feature.
Circular settlement | Which shape-based label describes dwellings forming a ring around a central pond or open area? | Circular describes the ring-shaped plan of this settlement. Nucleated describes concentration of dwellings rather than this particular geometric shape.
''')
    G('Drainage network patterns', '''
Dendritic drainage | Which drainage pattern resembles branches of a tree on relatively uniform terrain? | A dendritic network forms where tributaries join irregularly without strong structural guidance.
Trellis drainage | Which pattern has long parallel main streams joined by shorter tributaries at near-right angles? | Trellis drainage commonly develops where alternating resistant and weak rock bands guide valleys.
Radial drainage | Streams flow outward from a central highland or volcanic cone. What pattern is this? | A radial drainage network spreads away from a central elevated region.
Centripetal drainage | Streams converge inward toward a closed basin or central depression. What pattern is this? | Centripetal drainage directs water toward a common interior low area rather than outward to the sea.
''')
    G('World mountain locations', '''
Andes | Which major mountain chain runs along the western margin of South America? | The Andes extend along western South America and are associated with an active convergent plate margin.
Rocky Mountains | Which major mountain chain extends through western North America from Canada into the United States? | The Rockies form an extensive mountain system in the interior of western North America.
Alps | Which European mountain system spans countries including France, Switzerland, Italy and Austria? | The Alps form a major curved mountain belt in south-central Europe.
Atlas Mountains | Which mountain system extends across northwestern Africa through countries including Morocco and Algeria? | The Atlas ranges cross the Maghreb region of northwestern Africa.
''')

    # Two distinct geographic reasoning items complete the requested quota.
    def one(skill,prompt,entries,correct,fact):
        order=list(range(4));random.Random(331+len(bank)).shuffle(order)
        bank.append({'id':'','section':'General Studies','topic':'Geography','skill':skill,
                     'conceptKey':'Geography / '+skill,'question':prompt,
                     'options':[{'text':entries[i][0],'explanation':('Correct. ' if i==correct else 'Incorrect. ')+entries[i][1]} for i in order],
                     'answer':order.index(correct),'explanation':fact,'source':dict(NCERT_G),
                     'difficulty':'Standard','origin':'Original practice'})
    one('Indian standard meridian and solar-time offset',
        'India uses 82°30′ E as its standard meridian. At 15° of longitude per hour, what time offset does this give relative to the Greenwich meridian?',
        [('5 hours 30 minutes ahead','82.5° divided by 15° per hour is 5.5 hours. An eastern meridian is ahead of Greenwich.'),
         ('5 hours 30 minutes behind','The magnitude is correct, but eastern longitudes are ahead of Greenwich rather than behind.'),
         ('4 hours ahead','Four hours corresponds to 60° east, not the stated 82.5° east.'),
         ('6 hours ahead','Six hours corresponds to 90° east, not the stated standard meridian.')],0,
        'The longitude difference 82.5° ÷ 15° per hour equals 5 hours 30 minutes; eastward longitudes are ahead, giving UTC+05:30.')
    one('International Date Line crossing',
        'Ignoring local clock-zone changes, a traveller crosses the International Date Line from east to west. What calendar-date adjustment is conventionally made?',
        [('Add one calendar day','Crossing westward moves to the side whose calendar date is one day ahead, so one day is added.'),
         ('Subtract one calendar day','Subtracting a day is the conventional adjustment for crossing the date line eastward.'),
         ('Add one calendar month','The discontinuity corrects one day of global timekeeping, not an entire month.'),
         ('Make no date adjustment','Without a date adjustment, the traveller would not match the calendar date used across the date line.')],0,
        'A westward crossing conventionally adds one calendar day; an eastward crossing subtracts one day.')
    # Assign stable IDs during ordinary imports as well as command-line export.
    for i,q in enumerate(bank):
        q['id']=f'SG-{i+1:04d}'
        if q['id']=='SG-0112':
            q['question']='Which Indian soil group is conventionally classified together with yellow soils and develops on crystalline rocks in parts of the eastern and southern Deccan?'
            q['explanation']='Red and yellow soils form a recognised Indian soil group. Iron in weathered crystalline rocks gives red tones, with hydrated forms appearing yellow; red colour alone would not distinguish them from iron-rich lateritic soils.'
            q['options'][q['answer']]['explanation']='Correct. '+q['explanation']
            for option in q['options']:
                if option['text']=='Laterite soil':option['explanation']='Incorrect. Laterite is classified separately and develops through intense leaching in hot, wet conditions. It can also be red from iron oxides, so colour alone is not a reliable distinction.'
            q['source']={'title':'NCERT Indian Physical Environment — Soils, hosted by Kerala KITE','url':'https://samagra.kite.kerala.gov.in/files/samagra-resource/uploads/tbookscmq/Class_XI/Geography/Indianphysicalenvironment.pdf','page':None}
        if q['id']=='SG-0611':q['source']={'title':'Tea Board India — tea plant FAQ','url':'https://www.teaboard.gov.in/TEABOARDCSM/NDQ%3D','page':None}
        if q['id']=='SG-0612':q['source']={'title':'Plant Variety Authority — Coffee DUS guidelines','url':'https://plantauthority.gov.in/sites/default/files/dusguidelinescoffee-finale.pdf','page':None}
        if q['id']=='SG-0211':q['source']={'title':'NASA Glenn — States of Matter; gas and plasma distinction','url':'https://www.grc.nasa.gov/www/k-12/BGP/state.html','page':None}
        if q['id']=='SG-0433':q['source']={'title':'NCBI Bookshelf — Immunobiology glossary; antigenic determinants and epitopes','url':'https://www.ncbi.nlm.nih.gov/books/NBK10759/','page':None}
        if q['id']=='SG-0625':q['source']={'title':'Ministry of Coal — Coal Directory of India 2024–25, Table 2.3','url':'https://coal.gov.in/sites/default/files/2024-03/28-11-2025a-stc.pdf','page':None}
    return bank


def validate(bank):
    counts=Counter(q['topic'] for q in bank)
    assert counts=={'General Science':400,'Geography':250},counts
    assert len({q['question'] for q in bank})==len(bank)
    assert len({q['conceptKey'] for q in bank})==len(bank)
    for i,q in enumerate(bank):
        q['id']=f'SG-{i+1:04d}'
        assert len(q['options'])==4 and len({x['text'] for x in q['options']})==4
        assert all(len(x['explanation'])>35 for x in q['options'])
        assert q['source']['url'] and q['source']['page'] is None
        assert q['options'][q['answer']]['explanation'].startswith('Correct.')
    return {'count':len(bank),'topics':dict(counts),'uniqueConceptKeys':len({q['conceptKey'] for q in bank}),
            'uniqueStems':len({q['question'] for q in bank}),'duplicateIds':len(bank)-len({q['id'] for q in bank}),
            'options':sum(len(q['options']) for q in bank),'explainedOptions':sum(bool(o['explanation']) for q in bank for o in q['options']),
            'answerPositions':dict(Counter(q['answer'] for q in bank)),
            'sourceCounts':dict(Counter(q['source']['title'] for q in bank)),
            'inheritedDistinctQuestions':128,'newlyAuthoredDistinctQuestions':522,
            'generation':'No number-substitution or rephrasing loops. Each row supplies a distinct assessed concept or fact.',
            'sourceScope':'Reference URLs are authoritative subject references. No textbook page numbers are asserted; most facts were not individually retrieved from a page.',
            'reviewLimit':'Structural and exact-duplicate checks pass. Concept keys and high-overlap wording were reviewed; this is not an independent expert review of all 650 factual explanations.'}


if __name__=='__main__':
    bank=build_science_geo()
    report=validate(bank)
    print(json.dumps(report,indent=2))
    Path(__file__).with_name('gs-science-geo.json').write_text(json.dumps(bank,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    Path(__file__).with_name('gs-science-geo-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
