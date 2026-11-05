# Facilitator Notes: Streaming History Cleanup

These notes are for **me (the presenter)**. I am a student too, so the goal is not to be the expert. The goal is to run a clear activity, let classmates try the code, and be honest about what I know and what I looked up.

## Before I present (checklist)

- [ ] **Verify every page number against the physical book.** The page references in the README came from study notes that ChatGPT wrote from photos of my book pages, so they could contain mistakes. Confirm each one in the "essential methods" table: Ch. 2 pp. 46-49, 52-57, 54-55, 60-65, 66-67, 70-71, 72-73, 80-85, and Ch. 3 pp. 104-105, 110-113.
- [ ] **Check the topic wording against the schedule.** Confirm with the instructor that "Section 1" on the schedule matches Chapters 2 and 3 in my copy of the book.
- [ ] **Know what is book and what is supplementary.** The NumPy warm-up, `.astype()`, `.fillna()`, and `.drop_duplicates()` are *not* taught in detail in the book pages I used. I must say so out loud, and be able to explain them myself.
- [ ] **Fill in the README blanks.** Search the README for `[FILL IN]` (homework connection) and `[EDIT THIS]` (AI statement).
- [ ] **Replace the clone link** in the README with my real repository link.
- [ ] **Clean-start test.** On a computer with nothing opened: clone the repo, follow only the README, install the packages, and finish TODOs 1 to 5 in the starter. Write down anything confusing in `docs/peer_test_log.md`.
- [ ] **Peer test.** Ask at least one classmate to follow the README **without my help**. Fix the README where they got stuck.
- [ ] **Backup.** Save a screenshot of the chart window, in case a live demo fails.
- [ ] **Access.** Confirm classmates and the instructor can open the repository.
- [ ] **Repository link** (and slides, if any) submitted in Canvas by the deadline.

## What I need to be able to explain (in my own words)

Only four things. If I can say these clearly, I know enough:

1. **A DataFrame is a table; a column is a Series.** Math on columns works on every row at once. (Book pp. 46-47, 70-71.)
2. **Inspect before cleaning.** `head()`, `info()`, and `nunique()` tell me what is wrong. (Book pp. 52-57.)
3. **Cleaning methods return a new result, so I assign it back.** The four problems here: messy text, numbers stored as text, missing values, duplicates. (Book pp. 54-55, 72-73.)
4. **Filter, group, plot.** `query()` keeps matching rows, `groupby()` gives one answer per category, `.plot.bar()` draws it. Text inside `query()` needs quotes. (Book pp. 60-65, 80-85; Ch. 3 pp. 104-113.)

## Honest answers for questions I can't answer

It is okay to not know. Some phrases that work:

- "Good question. I'm not sure. Let's look it up in the pandas documentation together."
- "I only covered the parts in Chapters 2 and 3. That might be in a later chapter."
- "That step is supplementary. The book pages I used don't cover it, so I checked the pandas documentation."
- "I picked `fillna(1)` as a reasonable choice. Other people might drop those rows instead. Both are defensible."

Likely questions and short answers:

| Question | Short answer |
|---|---|
| Why `.copy()`? | So `listens` (the raw data) stays untouched and we can always compare before and after. |
| What is `.str`? | It lets me use text methods (like `strip`) on every value in a column at once. |
| What is `regex=False`? | It says "treat this as plain text." Some characters have special meanings in regular expressions, so `regex=False` keeps things simple. |
| Why `.astype(float)`? | `.str.replace` leaves the values as text. `astype(float)` turns them into real numbers so we can do math. |
| Why do the row numbers skip after `drop_duplicates()`? | Removed rows leave gaps in the index. It doesn't affect any of our results. |
| Can I use `and` in a filter? | Inside `query("... and ...")`, yes. (Outside `query()`, the filtering style uses `&` with parentheses. We don't cover that here.) |
| What is `groupby` doing? | It sorts the rows into piles by genre, then `.sum()` adds up each pile. |
| Why does the starter give an error before I fill in TODO 1? | The TODOs start as `None`. The error just means a TODO is still empty. |
| Are these real songs? | No. The artists and tracks are made up, and so is the data. |

## Run of show (about 15 minutes; shrink or stretch as needed)

The instructor announces the real time limit.

| Time | What I do | What the class does |
|---|---|---|
| 0:00 to 2:00 | **Introduce.** Show the before/after picture (`docs/images/messy_vs_clean.png`). Say the topic, the chapters and pages, and ask the guiding question: "How do we turn a table of raw data into an understandable result?" Point at the "essential methods" table. | Listen, look at the picture |
| 2:00 to 4:00 | **Get set up.** Share the repo link. Make sure everyone has pandas installed (this is where Mac users may need the virtual environment note). | Clone, install, open the starter |
| 4:00 to 6:00 | **TODO 1 and 2.** Explain "math on a whole column." Then ask: "What is wrong with this data?" Take 2 or 3 answers from the three diagnosis lines. | TODO 1, TODO 2 |
| 6:00 to 10:00 | **TODO 3 (cleaning).** Say the common mistake out loud **before** they hit it: "assign it back." Walk around and help. Tell them to compare with the `Expected` comments. | TODO 3 |
| 10:00 to 13:00 | **TODO 4 (new column and filtering).** Explain `query()` and the quotes inside the string. | TODO 4 |
| 13:00 to 15:00 | **TODO 5 and debrief.** Run the plot. Ask the reflection questions. Bonus A or B for anyone finished. | TODO 5, answer reflection |

### If I'm short on time

- **About 10 minutes:** do TODOs 1 to 3 together as a group, then paste TODO 4 and 5 from `music_cleanup_finished.py` and talk through the chart.
- **About 20 minutes:** let people work at their own pace, and use Bonus A as the extra discussion.

## What to say at key moments

- **Opening (30 seconds):** "Real data is messy. Today we will take a messy music listening history, clean it up with pandas, and make a chart. You will write about a dozen lines of code. I will help."
- **Before TODO 3:** "The most common mistake is forgetting to assign the result back. If your printed numbers don't match the `Expected` comment, check for `clean[...] =` at the start of the line."
- **Before TODO 4:** "Inside `query()`, text goes in quotes. If you get an error that says a name like `Pop` is not defined, you forgot the quotes."
- **Debrief:** "If we had skipped `drop_duplicates()`, which number would be wrong?" (Answer: total listening time would be too high, and nothing would crash.)

## Things that can go wrong, and what I do

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Packages not installed. Run the install command. On a Mac, use the virtual environment note in the README if `pip` complains. |
| Someone can't install pandas | Pair them with a neighbor, or have them follow along with the screenshots in `docs/images`. |
| Chart window won't open | Add `plt.savefig("chart.png")` above `plt.show()` and open the saved picture. |
| Everyone is behind | Use the "short on time" plan above. |
| Everyone is ahead | Point them to Bonus A and B. |
| Output looks different (`object` vs `str`) | Different pandas versions. Say "same results, slightly different labels." |
| Repo access error | Have the backup ZIP ready to share. |

## Debrief answers (for my reference)

Reflection question 1 (which step would cause the biggest mistake if skipped?): there is no single right answer. Good answers explain a consequence. Dropping duplicates affects totals directly (5 repeated listens inflate the numbers), and skipping the text cleanup splits one genre into several bars on the chart (`Pop`, `pop`, `POP` group separately).

Bonus A talking point: Electronic has fewer listens than Lo-Fi (6 vs 8) but more total minutes (56.0 vs 31.3), because its songs are longer (average 9.33 vs 3.91 minutes per listen). Counting rows and adding up a measurement can tell different stories.

Expected final numbers (to check my own run): shape `(45, 9)` after cleaning, total listening time 354.2, 12 Pop listens, 7 long phone listens, and Pop 95.0 / Lo-Fi 31.3 on the chart.

## After the presentation

- [ ] Record what I changed after testing in `docs/peer_test_log.md` (Part C).
- [ ] Make sure the last commit is pushed and the Canvas link works.
