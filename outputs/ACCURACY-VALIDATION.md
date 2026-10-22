# Accuracy — local review report

Checked on 20 October 2026. This is a local review build, awaiting your inspection and explicit approval before website deployment.

## Included

| Item | Count |
|---|---:|
| Complete preliminary mock papers | 20 |
| Questions per paper | 200 |
| Arithmetic & Reasoning questions | 2,000 |
| General Studies questions | 2,000 |
| Option-specific explanations | 16,000 |
| Topics in Learn & Tricks | 39 |
| Methods and study techniques | 86 |

The official preliminary structure is 100 Arithmetic & Reasoning plus 100 General Studies questions, 180 minutes, +1 correct, −0.20 wrong, and 0 unanswered. The source is the [TGPRB notification of 29 July 2026](https://www.tgprb.in/SI_PC_2026/SI%20(Civil%20et%20al)%202026%20Notification%20dated%2029-07-2026.pdf), printed pages 19–20. Topic allocations within those two sections are editorial practice choices.

## Checks completed

- Each of the 4,000 question IDs occurs in exactly one paper.
- No duplicate complete questions or normalized question stems.
- Every question has four distinct options, a valid answer index, an overall explanation and an explanation for each option.
- Independent arithmetic/reasoning checks passed for all 2,000 quantitative items, including exhaustive finite-model checks for the supplied syllogisms and independent geometry calculations.
- Targeted General Studies review removed identified repeated facts across subjects and corrected ambiguous science, geography, economy and history wording.
- The final lexical similarity review found 14 pairs requiring inspection. These test different facts, such as melting versus freezing or presidential versus vice-presidential qualifications. No same-answer pair remained under that scan's thresholds. This scan is not proof that every possible semantic overlap has been eliminated.
- All 39 bank topics have lessons. The 62 quantitative methods have worked bank examples. The 24 General Studies techniques have distinct supplementary examples.
- JavaScript syntax, grading, negative marks, blank-answer handling, coverage, timer boundaries and backup validation passed.

## Browser checks completed

| Student action | Observed result |
|---|---|
| Start a mock | 200-question instructions and three-hour timer |
| Answer and flag | Answer selection retained keyboard focus; flag recorded |
| Save, reload and resume | Answer and remaining timer restored |
| Switch sections | Moved between questions 1 and 101 |
| Submit one correct and one wrong answer | 0.8/200, 50% accuracy, 1% coverage |
| Review results | Correct choice and all four option explanations shown |
| Search and practise | Filtered questions, checked answer and bookmarked item |
| Export and import backup | Downloaded JSON and restored after confirmation |
| Import a synthetic expired attempt | Automatically submitted saved answer; score 1/200 |
| Choose a learning topic | Relevant methods and examples displayed |
| Expand example reasoning | Worked solution revealed |
| Practise this topic | Bank opened with the matching topic filter |
| Responsive layout | No horizontal overflow at 390px and 1440px widths |
| Browser errors | No JavaScript errors observed during these flows |

## Privacy

The app has no upload endpoint, account service, analytics, external script or remote font dependency. Original PDFs are not bundled. Public reference links use `noopener noreferrer` and open only after a click. Answers, bookmarks and test history remain in that browser's local storage. Downloaded progress backups are local files.

The earlier OCR paper search is a separate local artifact. OCR text is not automatically treated as a verified scored answer.

## Limits to review before release

1. **Structural variety:** the 2,000 quantitative questions include numerical/scenario variants from 50 method families and 62 named problem forms. They are not 2,000 different problem structures. The complete-question check passes; a requirement that every structure also be different is not met by this draft.
2. **Factual review:** the full factual bank has not received independent subject-expert certification. Some source records cite supplied textbooks without a verified page or public URL. They are not presented as individually web-verified.
3. **Coverage:** this is an English preliminary edition. It does not include a separate mains simulator or every current event. Internet research is selective and relevant to the syllabus, not an exhaustive copy of the internet.
4. **Outcome:** 85% accuracy is a practice goal, not a guaranteed exam result.
5. **Persistence:** browser storage may be cleared or unavailable. Keep the same browser and file location, and export backups.

Please review both content and the interface. Website deployment remains subject to your explicit approval.
