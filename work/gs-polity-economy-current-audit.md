# Polity, economy and dated-events content audit

Checked: 19 October 2026. Local authoring only; nothing published.

## Deliverables

- `gs-polity-economy-current.json`: 650 records.
- `gs_polity_economy_current.py`: existing integrated builder retained.
- `current_supplement.py`: completed 100 original additional current-affairs records, using primary-source pages consulted during this task.

## Counts and automated checks

| Check | Result |
|---|---:|
| Indian Polity | 300 |
| Indian Economy | 200 |
| Current affairs | 150 |
| Total | 650 |
| Distinct IDs | 650 |
| Distinct normalised stems | 650 |
| Records with four distinct options | 650 |
| Valid answer index, 0 through 3 | 650 |
| Records with all four option explanations | 650 |
| Records with an overall explanation | 650 |
| Supplement records with primary-source URLs | 100/100 |
| Unicode replacement characters in records | 0 |

Normalisation ignores letter case and punctuation. A lexical overlap scan was also run; its candidates mostly compare distinct provisions, economic classifications or awards. Exact-string checks alone do not prove semantic uniqueness, and the complete bank still needs editorial review across the other topic modules.

## Editorial work performed

- Completed the missing 100-item current-events supplement instead of restarting the 500 existing polity/economy records.
- Kept every new current-events question tied to a specified year or dated policy announcement, so later programme revisions do not silently alter the question.
- Used official ISRO, PIB, UNESCO, UN/UNEP, MEA, Brazilian-government, Nobel Committee and ICC sources. Source URLs identify the consulted pages; PDF page numbers are omitted where not verified.
- Wrote original questions and explanations rather than copying source prose or past-paper questions.
- Kept answer positions varied while preserving the explanation-to-option mapping.
- Replaced a Paralympic medal-breakdown item that overlapped the total-tally question with the 2024 Chess Olympiad venue.
- Replaced an item counting the five new Classical Languages with the distinct fact of Tamil's initial 2004 recognition, explicitly framed as the history reported in the October 2024 Cabinet note.
- Dated projections in the 2024 space roadmap are not presented as completed events. Questions ask approved capabilities rather than assuming projected completion dates were met.

## Inherited limitations requiring integration review

The pre-existing 500 polity/economy records contain **64 records without a source URL**, using named supplied or general educational references. No page number was invented. These are outside the restricted supplement-edit scope and must not be represented as individually web-verified.

Missing-URL skills: Sectors of production, Output measurement, Price-level changes, Budget deficits, Tax concepts, Unemployment concepts, International transactions, Choice and markets, Food-security mechanisms, Constitution-making dates, Constituent Assembly responsibilities, Constitutional architecture, Citizenship Act concepts, Parliamentary financial committees, Parliament questions and devices, Statutory and executive institutions. Each has four records.

Verified primary references available to improve these citations:

- Constituent Assembly: https://sansad.in/rs/about/constituent-assembly
- Constitution, official 2024 text: https://lddashboard.legislative.gov.in/sites/default/files/coi/COI_2024.pdf
- Citizenship Act: https://www.mha.gov.in/sites/default/files/2024-09/TheCitizenshipAct1955_10092024.pdf
- NCERT Introductory Microeconomics: https://ncert.nic.in/textbook.php?leec2=3-6

The 50 earlier current-events records were retained from `current_content.py`; they were not independently re-researched in this completion task. The new supplement spans 2024–2025 and is a selected practice collection, not an exhaustive news digest through October 2026.
