"""Accuracy: dated, source-checked current-event practice. Checked 2026-10-18.

Selected events from 2024 through July 2026, not an exhaustive news syllabus.
Every question is original; sources substantiate the keyed event facts.
"""

SOURCES = {
    "spadex_undock": ("ISRO: SpaDeX undocking, 13 March 2025", "https://www.isro.gov.in/ISRO_EN/spadex_undocking_successful.html", None),
    "spadex": ("ISRO: SpaDeX mission objectives", "https://www.isro.gov.in/ISRO_EN/mission_SpaDeX.html?timeline=timeline", None),
    "nisar": ("ISRO: GSLV-F16/NISAR mission", "https://www.isro.gov.in/Mission_GSLVF16_NISAR_Home.html", None),
    "nisar_science": ("ISRO: NISAR enters science phase", "https://www.isro.gov.in/NISAR_Mission_Science_Phase.html", None),
    "nisar_data": ("ISRO: NISAR S-band data release, 2026", "https://www.isro.gov.in/NISARS_Band_SAR_Data_Products_Release.html", None),
    "maratha": ("UNESCO: Maratha inscription, 2025", "https://www.unesco.org/en/articles/maratha-military-landscapes-india-inscribed-unesco-world-heritage-list-indias-44th-world-heritage-0", None),
    "maratha_entry": ("UNESCO World Heritage: Maratha Military Landscapes", "https://whc.unesco.org/en/list/1739", None),
    "moidams": ("UNESCO World Heritage: Moidams", "https://whc.unesco.org/en/list/1711", None),
    "state_song": ("Telangana G.O.Ms.No.783, 2 June 2024", "https://www.telangana.gov.in/wp-content/uploads/2024/10/Telangana-State-Song.pdf", 1),
    "song_portal": ("Telangana State Portal: official state-song versions", "https://www.telangana.gov.in/telangana-state-song/", None),
    "chilli": ("GI Registry: Warangal Chapata Chilli, application 984", "https://search.ipindia.gov.in/GIRPublicSearch/Application/Details/984", None),
    "miss_world": ("Miss World: 72nd edition, 31 May 2025", "https://www.missworld.com/contestants/72ndmissworld", None),
    "t20": ("ICC: 2026 Men's T20 World Cup final", "https://www.icc-cricket.com/matches/268129/india-vs-new-zealand", None),
    "ai_declaration": ("PIB/MeitY: AI Summit declaration, 21 February 2026", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2231208&lang=2&reg=48", None),
    "ai_summit": ("PIB/MeitY: AI Summit outcomes, 11 March 2026", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2238195&lang=1&reg=1", None),
    "olympics": ("PIB: Indian Army Olympians, 16 August 2024", "https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2045963&lang=2&reg=48", None),
    "gukesh": ("FIDE: Gukesh wins the 2024 World Championship", "https://www.fide.com/fide-world-championship-game-14-gukesh-d-claims-title/", None),
    "divya": ("FIDE: Divya wins the 2025 Women's World Cup", "https://www.fide.com/divya-deshmukh-becomes-third-womens-world-cup-champion-defeats-humpy-koneru-in-tiebreak/", None),
    "divya_details": ("FIDE Women's Commission: 2025 World Cup results", "https://wom.fide.com/divya-deshmukh-makes-history-youngest-ever-womens-world-cup-champion/", None),
    "budget": ("PIB/Finance: manufacturing proposals, Budget 2026–27", "https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2221451&lang=2&reg=3", None),
    "law_date": ("PIB/Home Affairs: new criminal laws, 10 December 2024", "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2082757", None),
    "law_names": ("PIB/Home Affairs: 2024 year-end review", "https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2088945&lang=2&reg=48", None),
    "upi": ("NPCI International: UPI in France, 2 February 2024", "https://www.npci.org.in/PDF/npci/press-releases/2024/Press-Release-UPI-is-Now-Accepted-in-France.pdf", 1),
    "cop29": ("UNFCCC: COP29, Baku 2024", "https://unfccc.int/cop29", None),
    "cop_finance": ("UNCTAD: the COP29 climate-finance goal", "https://unctad.org/news/countries-agree-300-billion-2035-new-climate-finance-goal-what-next", None),
    "cop30": ("UNFCCC: COP30, Belém 2025", "https://unfccc.int/cop30", None),
}


def build_current_bank():
    bank = []

    def add(skill, question, correct, wrongs, explanation, source, difficulty="Easy"):
        """Keep supplied option explanations attached while varying answer positions."""
        assert len(wrongs) == 3
        raw = [correct] + wrongs
        pos = len(bank) % 4
        order = raw[-pos:] + raw[:-pos] if pos else raw
        title, url, page = SOURCES[source]
        bank.append({
            "id": f"CA-{len(bank)+1:03d}", "section": "General Studies",
            "topic": "Current affairs", "skill": skill, "question": question,
            "options": [{"text": t, "explanation": e} for t, e in order],
            "answer": pos, "explanation": explanation,
            "source": {"title": title, "page": page, "url": url},
            "difficulty": difficulty, "origin": "Original practice",
        })

    add("Space milestones", "On which date did ISRO first successfully dock the two SpaDeX satellites in 2025?",
        ("16 January 2025", "Correct: ISRO records the first docking on this date."),
        [("13 March 2025", "This was the successful undocking date, a different operation."),
         ("16 February 2025", "The first docking had already occurred in January."),
         ("13 April 2025", "This is not the first docking date reported by ISRO.")],
        "Separate the two milestones: docking occurred on 16 January; undocking followed on 13 March 2025.", "spadex_undock")
    add("Space technology", "ISRO announced SpaDeX undocking on 13 March 2025. What did this operation achieve?",
        ("Separation of previously joined spacecraft", "Correct: the two satellites resumed independent orbital operation."),
        [("Landing a rover on the Moon", "Undocking separates spacecraft; it does not describe a lunar landing."),
         ("Launching a satellite from Earth", "The satellites were already in orbit when they undocked."),
         ("Destroying both satellites", "ISRO reported both spacecraft healthy and orbiting independently.")],
        "Docking joins spacecraft; undocking separates them in a controlled manner.", "spadex_undock")
    add("Space missions", "Which capability was the main purpose of the SpaDeX mission demonstrated in 2025?",
        ("Rendezvous, docking and undocking in orbit", "Correct: SpaDeX tests spacecraft approach, joining and separation."),
        [("Returning samples from the Moon", "Docking can support future sample-return missions; SpaDeX itself did not return lunar samples."),
         ("Launching a crew into orbit", "SpaDeX uses two small uncrewed spacecraft, not a crew capsule."),
         ("Operating a navigation constellation", "SpaDeX demonstrates spacecraft interaction rather than a navigation service.")],
        "The mission develops technology needed when separately launched spacecraft must work together.", "spadex")
    add("Spacecraft roles", "In the SpaDeX mission prominent in 2025, which pairing correctly identifies the nominal spacecraft roles?",
        ("SDX01: Chaser; SDX02: Target", "Correct: these are ISRO's nominal designations."),
        [("SDX01: Target; SDX02: Chaser", "This reverses the mission's nominal roles."),
         ("SDX01: Lander; SDX02: Rover", "These are not the roles of the two docking spacecraft."),
         ("SDX01: Crew module; SDX02: Service module", "These are not the nominal identities of the two SpaDeX experiment satellites.")],
        "The Chaser approaches the Target for orbital rendezvous and docking.", "spadex")
    add("International space cooperation", "NISAR, launched in July 2025, is a joint mission of which agencies?",
        ("NASA and ISRO", "Correct: the mission name identifies the US and Indian partners."),
        [("ESA and JAXA", "These European and Japanese agencies are not the NISAR partnership."),
         ("ISRO and Roscosmos", "Russia's agency is not the partner identified by NISAR."),
         ("NASA and CNSA", "This substitutes China's agency for the Indian partner.")],
        "NISAR expands to NASA–ISRO Synthetic Aperture Radar.", "nisar")
    add("Space applications", "Which task best describes the NISAR satellite launched in 2025?",
        ("Radar observation of changes on Earth's surface", "Correct: NISAR is an Earth-observation radar mission."),
        [("Human transport to the Moon", "NISAR is an uncrewed observation satellite, not a crew vehicle."),
         ("Collection of Martian soil", "Its observing target is Earth, not the Martian surface."),
         ("Measurement only of distant galaxies", "The mission studies terrestrial surfaces rather than distant galaxies.")],
        "Synthetic-aperture radar provides measurements useful for land, ice and ecosystem monitoring.", "nisar")
    add("Space instrumentation", "Which radar contribution pairing is correct for NISAR's 2025 mission?",
        ("ISRO: S-band; NASA: L-band", "Correct: each agency contributed the indicated radar payload."),
        [("ISRO: L-band; NASA: S-band", "This reverses the two agencies' radar contributions."),
         ("ISRO: S-band; NASA: S-band", "This incorrectly assigns S-band to NASA's L-band payload."),
         ("ISRO: L-band; NASA: L-band", "This incorrectly assigns L-band to ISRO's S-band payload.")],
        "Remember the agency-to-band pairing, not just that NISAR has two radar frequencies.", "nisar_science", "Medium")
    add("Indian remote sensing", "NISAR's first S-band SAR image, acquired on 19 August 2025, showed which Indian region?",
        ("Godavari River Delta in Andhra Pradesh", "Correct: ISRO identified this delta in its first-image report."),
        [("Thar Desert in Rajasthan", "This desert was not the delta shown in that first image."),
         ("Siachen Glacier", "This Himalayan glacier was not the reported first-image location."),
         ("Rann of Kachchh", "This western salt-marsh region is not the Godavari delta.")],
        "The first image illustrated the radar's ability to map deltaic and agricultural landscapes.", "nisar_science", "Medium")
    add("Space-data access", "ISRO's 2026 release made processed NISAR S-band data available through which portal?",
        ("Bhoonidhi", "Correct: this is ISRO's Earth-observation data distribution hub."),
        [("DigiLocker", "DigiLocker stores digital documents; it is not this satellite-data hub."),
         ("e-Shram", "e-Shram is a worker-registration platform, not a radar-data portal."),
         ("GeM", "GeM is a procurement marketplace, not the NISAR distribution portal.")],
        "The release includes operational processing from Cycle 25, which began on 8 July 2026.", "nisar_data", "Medium")
    add("Satellite observation cycles", "In ISRO's 2026 NISAR data-release description, what is the satellite's repeat cycle?",
        ("12 days", "Correct: the mission description specifies a 12-day repeat cycle."),
        [("12 hours", "This confuses the stated number with a much shorter time unit."),
         ("12 months", "An annual cycle is far longer than NISAR's stated repeat cycle."),
         ("120 days", "This is ten times the reported repeat interval.")],
        "Repeated radar observations help compare surface changes over time.", "nisar_data", "Medium")
    add("World heritage", "Which property became India's 44th UNESCO World Heritage property in 2025?",
        ("Maratha Military Landscapes of India", "Correct: UNESCO recorded this as India's 44th inscription."),
        [("Moidams of the Ahom Dynasty", "Moidams were inscribed in 2024, not this 2025 entry."),
         ("Taj Mahal", "The Taj Mahal was already listed long before 2025."),
         ("Ajanta Caves", "Ajanta was already a World Heritage property before 2025.")],
        "Keep the year attached to a numbered heritage milestone; the national total can later change.", "maratha")
    add("Heritage geography", "The Maratha Military Landscapes inscribed by UNESCO in 2025 span which two states?",
        ("Maharashtra and Tamil Nadu", "Correct: the serial property extends across these states."),
        [("Maharashtra and Telangana", "Telangana is not the second state in this inscription."),
         ("Gujarat and Rajasthan", "Neither identifies the two-state distribution of this property."),
         ("Assam and Meghalaya", "These northeastern states are not the Maratha fort network's locations.")],
        "A serial World Heritage property can include related sites in more than one state.", "maratha")
    add("Heritage composition", "How many major fortifications make up the Maratha Military Landscapes inscribed in 2025?",
        ("12", "Correct: UNESCO describes twelve component fortifications."),
        [("2", "Two is the number of states, not the number of forts."),
         ("44", "Forty-four was India's property total after inscription, not this site's fort count."),
         ("7", "Seven is not the total of the inscribed fortifications.")],
        "Distinguish component sites from the national count of World Heritage properties.", "maratha_entry")
    add("Interpreting heritage", "What is the principal character of the Maratha Military Landscapes recognized in 2025?",
        ("A network of strategically situated forts", "Correct: the components form a military defence landscape."),
        [("An Ahom royal burial complex", "That description belongs to Moidams, a different heritage property."),
         ("A single astronomical observatory", "The property is a fort network, not one observatory."),
         ("Only a collection of manuscripts", "The inscribed components are physical fortifications.")],
        "UNESCO recognizes the relationship between fortifications, terrain and military strategy.", "maratha_entry")
    add("World heritage geography", "Moidams, inscribed on the UNESCO World Heritage List in 2024, are in which state?",
        ("Assam", "Correct: the Charaideo royal burial landscape is in eastern Assam."),
        [("Telangana", "Telangana is not the location of the Charaideo necropolis."),
         ("Kerala", "The Moidams property is in northeastern India, not Kerala."),
         ("Punjab", "Punjab is not the state containing this Ahom burial landscape.")],
        "Associate Moidams with Charaideo in Assam.", "moidams")
    add("Heritage and dynasties", "The Moidams World Heritage property recognized in 2024 is associated with which dynasty?",
        ("Ahom", "Correct: these mounds express Tai-Ahom royal funerary traditions."),
        [("Kakatiya", "The Kakatiyas are not the dynasty responsible for the Charaideo Moidams."),
         ("Chola", "Chola heritage is distinct from the Ahom burial landscape."),
         ("Maurya", "The Moidams are associated with the later Ahom tradition, not the Mauryas.")],
        "Moidams are royal burial mounds, not temple towers or Buddhist stupas.", "moidams")
    add("Telangana cultural policy", "Which song was adopted by Telangana through G.O.Ms.No.783 dated 2 June 2024?",
        ("Jaya Jayahe Telangana", "Correct: this is the title specified in the adoption order."),
        [("Maa Telugu Talliki", "This is not the song named in Telangana's June 2024 order."),
         ("Vande Mataram", "India's national song is not the state song adopted by this order."),
         ("Jana Gana Mana", "India's national anthem is distinct from the adopted Telangana state song.")],
        "The question asks about the dated adoption order, not earlier proposals or performances.", "state_song")
    add("Telangana writers", "Whom does Telangana's 2 June 2024 state-song order credit as the writer of Jaya Jayahe Telangana?",
        ("Andhe Sri (Ande Sri)", "Correct: the order names Sri Andhe Sri as the writer."),
        [("Rabindranath Tagore", "He is not the writer credited in this Telangana order."),
         ("Bankim Chandra Chattopadhyay", "He wrote Vande Mataram, not this state song."),
         ("Sri Sri", "This different poet is not the writer named in the adoption order.")],
        "Remember the lyricist named in the order; do not confuse authorship with musical rendition.", "state_song")
    add("Telangana official symbols", "For the state song adopted in 2024, which two stanza versions are listed on Telangana's official portal?",
        ("3 stanzas and 12 stanzas", "Correct: the portal lists these shorter and longer renditions."),
        [("1 stanza and 2 stanzas", "These are not the two versions listed on the portal."),
         ("5 stanzas and 10 stanzas", "These counts do not match the listed official versions."),
         ("Only a single 20-stanza version", "The portal provides two versions rather than this single version.")],
        "The official state-song page distinguishes the 3-stanza and 12-stanza recordings.", "song_portal", "Medium")
    add("Telangana GI registrations", "Warangal Chapata Chilli received a GI certificate in March 2025. Which state is its registered geographical area?",
        ("Telangana", "Correct: the GI Registry names Telangana."),
        [("Andhra Pradesh", "Nearby chilli-growing regions do not change this registration's Telangana area."),
         ("Karnataka", "Karnataka is not the geographical area of this named registration."),
         ("Maharashtra", "Maharashtra is not the state listed for Warangal Chapata Chilli.")],
        "Use the exact registered product name; different chilli varieties may have separate registrations.", "chilli")
    add("Reading official records", "The GI Registry lists a filing date of 6 September 2022 and a certificate date in 2025 for Warangal Chapata Chilli. Which is the certificate date?",
        ("28 March 2025", "Correct: this is the registry's certificate date."),
        [("6 September 2022", "This is the application filing date, not the certificate date."),
         ("27 November 2024", "This is the listed journal availability date, not the certificate date."),
         ("5 September 2032", "This is the listed validity end date, not the certificate date.")],
        "Filing, publication, certification and expiry are different milestones in a GI record.", "chilli", "Medium")
    add("Telangana international events", "Which city hosted the 72nd Miss World grand finale on 31 May 2025?",
        ("Hyderabad", "Correct: the finale took place at the HITEX Exhibition Centre in Hyderabad."),
        [("New Delhi", "New Delhi was not the host city of this finale."),
         ("Mumbai", "Mumbai was not the location of the 31 May 2025 finale."),
         ("Chennai", "Chennai was not the city named by the event organizer.")],
        "The 2025 event provides a Telangana-specific example of international cultural hosting.", "miss_world")
    add("International awards", "Opal Suchata, crowned Miss World in Hyderabad in May 2025, represented which country?",
        ("Thailand", "Correct: the organizer identifies her as Thailand's representative."),
        [("India", "Hosting the event did not make the winner an Indian representative."),
         ("Ethiopia", "The 2025 title was won by Thailand's representative."),
         ("Czech Republic", "The outgoing titleholder was from that country, not the 2025 winner.")],
        "Keep the host country and the winner's country separate.", "miss_world")
    add("Cricket results", "Which team won the ICC Men's T20 World Cup final against New Zealand on 8 March 2026?",
        ("India", "Correct: India won the final by 96 runs."),
        [("New Zealand", "New Zealand was the runner-up in that final."),
         ("Australia", "Australia was not a finalist in this match."),
         ("South Africa", "South Africa was not the opposing finalist in 2026.")],
        "Dated questions prevent confusion with earlier finals.", "t20")
    add("Sports awards", "Who was Player of the Match in the 8 March 2026 Men's T20 World Cup final?",
        ("Jasprit Bumrah", "Correct: the ICC scorecard gives Bumrah the final's award."),
        [("Sanju Samson", "Samson won the tournament award, not this match award."),
         ("Mitchell Santner", "The ICC record does not name Santner as Player of the Match."),
         ("Suryakumar Yadav", "India's captain was not the award recipient for this final.")],
        "Bumrah took four wickets for 15 runs in the final.", "t20")
    add("Sports distinctions", "Who was named Player of the Tournament at the 2026 ICC Men's T20 World Cup?",
        ("Sanju Samson", "Correct: Samson received the tournament-wide award."),
        [("Jasprit Bumrah", "Bumrah received the final's Player of the Match award."),
         ("Tim Seifert", "Seifert was not the tournament-award recipient."),
         ("Axar Patel", "Patel was not named Player of the Tournament.")],
        "Distinguish recognition for a single final from performance across the tournament.", "t20")
    add("Technology diplomacy", "Which declaration was adopted at the AI Impact Summit in February 2026?",
        ("New Delhi Declaration on AI Impact", "Correct: this is the declaration identified by MeitY."),
        [("Paris Agreement", "That is a climate agreement, not this AI summit's declaration."),
         ("Montreal Protocol", "That agreement addresses ozone-depleting substances, not this AI event."),
         ("Kyoto Protocol", "That is a climate instrument, not the February 2026 AI declaration.")],
        "The declaration concerns international cooperation and shared benefits from AI.", "ai_declaration")
    add("AI governance principles", "The February 2026 AI Impact Summit declaration invoked Sarvajan Hitaya, Sarvajan Sukhaya. What does that principle emphasize?",
        ("Welfare and happiness for all", "Correct: it frames AI benefits as broadly shared."),
        [("Benefits reserved for one country", "The stated principle extends benefits across humanity."),
         ("Replacing all human judgment immediately", "The phrase concerns shared welfare, not this blanket replacement claim."),
         ("Ending international cooperation", "The declaration calls for cooperation, not its termination.")],
        "Read the guiding principle as an inclusion goal, not a technical description of AI.", "ai_declaration", "Medium")
    add("Summit venues", "Where was the India-AI Impact Summit held from 16–21 February 2026?",
        ("Bharat Mandapam, New Delhi", "Correct: MeitY's March 2026 account specifies this venue."),
        [("HITEX, Hyderabad", "HITEX hosted the 2025 Miss World finale, not this AI summit."),
         ("Narendra Modi Stadium, Ahmedabad", "That stadium is a sports venue, not the named AI summit venue."),
         ("Satish Dhawan Space Centre, Sriharikota", "This is a launch centre, not the summit's venue.")],
        "Use the whole event's date range; individual summit sessions had narrower dates.", "ai_summit")
    add("Technology supply chains", "According to MeitY's March 2026 report, which coalition did India join at the India-AI Impact Summit?",
        ("Pax Silica", "Correct: the report links this coalition to silicon supply-chain resilience."),
        [("OPEC", "OPEC concerns petroleum exporters, not the reported silicon initiative."),
         ("NATO", "NATO is a defence alliance, not the coalition named in this report."),
         ("Mercosur", "Mercosur is a South American trade bloc, not this technology coalition.")],
        "The reported focus was a resilient technology ecosystem and the global silicon supply chain.", "ai_summit", "Medium")
    add("Olympic performance", "What was India's medal tally at the Paris 2024 Olympic Games?",
        ("1 silver and 5 bronze", "Correct: these six medals formed India's final tally."),
        [("1 gold and 5 bronze", "India's single non-bronze medal was silver, not gold."),
         ("2 gold and 4 silver", "This distribution does not match India's Paris tally."),
         ("7 gold", "India did not win seven gold medals at Paris.")],
        "The tally was six medals; do not substitute a different Olympic edition's total.", "olympics")
    add("Olympic disciplines", "Neeraj Chopra won India's only silver medal at Paris 2024 in which event?",
        ("Men's javelin throw", "Correct: Chopra's medal came in the javelin event."),
        [("Men's shot put", "Shot put is a different throwing discipline."),
         ("Men's 100 metres", "This is a sprint, not Chopra's medal event."),
         ("Men's high jump", "High jump is a jumping event, not javelin throwing.")],
        "Associate the athlete, discipline and dated medal correctly.", "olympics")
    add("Chess milestones", "Which Indian became the youngest FIDE classical World Champion at age 18 in December 2024?",
        ("Gukesh D", "Correct: Gukesh won the 2024 title at eighteen."),
        [("Viswanathan Anand", "Anand is a former champion, but not the eighteen-year-old 2024 winner."),
         ("R. Praggnanandhaa", "He was not the winner of the 2024 championship match."),
         ("Arjun Erigaisi", "He was not the player who won this 2024 match.")],
        "The claim is tied to the classical World Championship, not a different chess event.", "gukesh")
    add("Chess championship matches", "Whom did Gukesh defeat in the 2024 FIDE World Championship match in Singapore?",
        ("Ding Liren", "Correct: the defending champion faced Gukesh in the title match."),
        [("Magnus Carlsen", "Carlsen was not Gukesh's opponent in that championship match."),
         ("Hikaru Nakamura", "Nakamura was not the defending champion in the Singapore match."),
         ("Ian Nepomniachtchi", "Nepomniachtchi did not face Gukesh in this title match.")],
        "Gukesh finished the fourteen-game match ahead by 7.5–6.5.", "gukesh")
    add("Women's chess", "Who won the FIDE Women's World Cup concluded on 28 July 2025?",
        ("Divya Deshmukh", "Correct: Divya won the title in Batumi."),
        [("Koneru Humpy", "Humpy was the runner-up after the final tiebreak."),
         ("Tan Zhongyi", "Tan finished third rather than winning the title."),
         ("Lei Tingjie", "Lei was not the champion of this World Cup.")],
        "This was the Women's World Cup, a distinct event from the Women's World Championship.", "divya")
    add("Indian chess finalists", "The 2025 FIDE Women's World Cup had an all-Indian final. Who was Divya Deshmukh's opponent?",
        ("Koneru Humpy", "Correct: Humpy faced Divya in the final."),
        [("Tan Zhongyi", "Tan was a Chinese semifinalist, not Divya's final opponent."),
         ("Lei Tingjie", "Lei was not the other player in the all-Indian final."),
         ("Ju Wenjun", "Ju was not the opponent in this World Cup final.")],
        "Divya prevailed in the rapid tiebreak after the classical games were drawn.", "divya")
    add("International sports geography", "Which city hosted the July 2025 FIDE Women's World Cup won by Divya Deshmukh?",
        ("Batumi, Georgia", "Correct: the tournament was held in this Black Sea city."),
        [("Singapore", "Singapore hosted the 2024 open World Championship match, a different event."),
         ("Chennai, India", "Chennai was not the venue of this 2025 World Cup."),
         ("Baku, Azerbaijan", "Baku is not Batumi and was not the named venue for this edition.")],
        "Link the event and year to its venue rather than relying on a famous chess host.", "divya_details")
    add("Chess qualification pathways", "What qualification did the top three finishers of the 2025 FIDE Women's World Cup earn?",
        ("Places in the next Women's Candidates Tournament", "Correct: the top three advanced in the championship qualification pathway."),
        [("Automatic joint world-champion titles", "A World Cup podium is not the award of the World Championship title."),
         ("Places directly in the next World Championship match", "They qualified for Candidates, which precedes selection of the championship challenger."),
         ("Qualification only for their national championships", "The earned qualification was international: the Women's Candidates Tournament.")],
        "The Candidates Tournament is a step toward a World Championship challenge.", "divya_details", "Medium")
    add("Union Budget proposals", "The Union Budget 2026–27 proposed what outlay for Biopharma SHAKTI over five years?",
        ("₹10,000 crore", "Correct: the proposal specified this five-year outlay."),
        [("₹5,000 crore", "This is half the announced outlay."),
         ("₹20,000 crore", "This doubles the announced outlay."),
         ("₹1,000 crore", "This is one-tenth of the announced outlay.")],
        "The figure is planned spending over five years, not expenditure already completed.", "budget")
    add("Biopharma policy", "In the Union Budget 2026–27, Biopharma SHAKTI was proposed mainly to strengthen which production ecosystem?",
        ("Biologics and biosimilars", "Correct: the proposal targets domestic biopharma manufacturing."),
        [("Semiconductor wafers", "Semiconductor manufacturing is addressed separately, not by Biopharma SHAKTI."),
         ("Chemical fertilizers", "The stated focus is biological medicines, not agricultural fertilizers."),
         ("Medical tourism infrastructure only", "The proposal concerns manufacturing, not solely tourism infrastructure.")],
        "Connect the scheme's name to the sector and intended capability.", "budget")
    add("Semiconductor policy", "ISM 2.0, proposed in the Union Budget 2026–27, relates principally to which sector?",
        ("Semiconductors", "Correct: it expands India's semiconductor capabilities and supply chains."),
        [("Biopharmaceutical clinical trials", "Clinical-trial expansion belongs to the separate biopharma proposal."),
         ("Rare-earth mining alone", "Rare-earth corridors are a separate proposal; ISM concerns semiconductors."),
         ("Commercial aircraft leasing", "Aircraft leasing is not this mission's focus.")],
        "ISM 2.0 includes equipment, materials, intellectual property and supply chains.", "budget")
    add("Dated legal developments", "On which date did the three new Indian criminal laws generally come into force in 2024, subject to the notified exceptions?",
        ("1 July 2024", "Correct: this is the commencement date reported by the Home Ministry."),
        [("26 January 2024", "Republic Day was not the notified general commencement date."),
         ("15 August 2024", "The laws generally commenced before Independence Day."),
         ("2 October 2024", "They had already generally commenced in July.")],
        "The date must be stated with the notified exceptions; not every provision commenced on that day.", "law_date")
    add("Criminal-law transition", "In the 2024 criminal-law transition, which statute replaced the Indian Penal Code as the principal substantive criminal code?",
        ("Bharatiya Nyaya Sanhita", "Correct: BNS is the substantive criminal-code replacement."),
        [("Bharatiya Nagarik Suraksha Sanhita", "BNSS concerns criminal procedure rather than replacing the IPC."),
         ("Bharatiya Sakshya Adhiniyam", "BSA addresses evidence rather than the principal catalogue of offences."),
         ("Right to Information Act", "RTI concerns access to information, not this criminal-code replacement.")],
        "Separate substantive offences, procedure and evidence.", "law_names")
    add("Criminal procedure", "Which new law replaced the Code of Criminal Procedure in the 2024 transition?",
        ("Bharatiya Nagarik Suraksha Sanhita", "Correct: BNSS is the criminal-procedure statute."),
        [("Bharatiya Nyaya Sanhita", "BNS replaced the substantive penal code, not CrPC."),
         ("Bharatiya Sakshya Adhiniyam", "BSA replaced evidence legislation, not CrPC."),
         ("Consumer Protection Act", "Consumer law is not the replacement for criminal procedure.")],
        "Procedure governs investigation and trial processes.", "law_names")
    add("Evidence legislation", "Which law replaced the Indian Evidence Act in the 2024 criminal-law transition?",
        ("Bharatiya Sakshya Adhiniyam", "Correct: BSA is the new evidence statute."),
        [("Bharatiya Nyaya Sanhita", "BNS addresses substantive offences rather than replacing the Evidence Act."),
         ("Bharatiya Nagarik Suraksha Sanhita", "BNSS concerns criminal procedure, not the evidence-law replacement."),
         ("Companies Act", "Company regulation is not the evidence-law replacement.")],
        "Sakshya identifies the evidence component of the trio.", "law_names")
    add("Digital payments abroad", "NPCI International's 2 February 2024 France announcement began UPI ticket-payment acceptance at which landmark?",
        ("Eiffel Tower", "Correct: the announcement identified Eiffel Tower ticket purchases."),
        [("Colosseum", "The Colosseum is in Rome and was not this France launch location."),
         ("Statue of Liberty", "This New York landmark was not the French acceptance site."),
         ("Taj Mahal", "The Taj Mahal is in India, not the landmark in the France announcement.")],
        "The event concerns UPI acceptance abroad, not a change in the landmark's location or ownership.", "upi")
    add("Payment partnerships", "Which French company partnered with NPCI International for the UPI acceptance announcement of February 2024?",
        ("Lyra", "Correct: NIPL named Lyra as its French payments partner."),
        [("Worldline", "Worldline is not the partner named in this dated NIPL announcement."),
         ("Adyen", "Adyen is not the company named for this France launch."),
         ("PayPal", "The announcement identifies Lyra, not PayPal, as the partner.")],
        "Identify the implementing partner separately from the Indian payment-network organization.", "upi")
    add("Climate diplomacy venues", "Where was the UN climate conference COP29 held in November 2024?",
        ("Baku, Azerbaijan", "Correct: Baku hosted COP29."),
        [("Belém, Brazil", "Belém hosted COP30 in 2025, not COP29."),
         ("Paris, France", "Paris is associated with COP21 in 2015, not COP29."),
         ("New Delhi, India", "New Delhi was not the COP29 host city.")],
        "Use the COP number together with the year to distinguish conference venues.", "cop29")
    add("Climate finance", "At COP29 in 2024, the new climate-finance goal called for finance to developing countries to reach at least what annual amount by 2035, with developed countries taking the lead?",
        ("US$300 billion", "Correct: this is the central annual finance goal for 2035."),
        [("US$100 billion", "This was the previous annual goal, before the new US$300 billion goal."),
         ("US$1.3 trillion", "This refers to the broader all-source scaling effort, not the central goal asked here."),
         ("US$300 million", "This is one-thousandth of the stated billion-dollar figure.")],
        "Distinguish the US$300 billion goal from the broader effort to scale all-source finance to US$1.3 trillion.", "cop_finance", "Medium")
    add("Climate diplomacy venues", "Which city hosted COP30 in November 2025?",
        ("Belém, Brazil", "Correct: UNFCCC identifies Belém as the COP30 host."),
        [("Baku, Azerbaijan", "Baku hosted COP29 in 2024, the preceding conference."),
         ("Hyderabad, India", "Hyderabad did not host COP30."),
         ("Tokyo, Japan", "Tokyo was not the COP30 host city.")],
        "The sequence is Baku 2024 followed by Belém 2025.", "cop30")

    assert len(bank) == 50, len(bank)
    for q in bank:
        assert len(q["options"]) == 4 and 0 <= q["answer"] < 4
        assert len({o["text"] for o in q["options"]}) == 4
        assert q["options"][q["answer"]]["explanation"].startswith("Correct:")
    return bank


if __name__ == "__main__":
    import json
    print(json.dumps(build_current_bank(), ensure_ascii=False, indent=2))
