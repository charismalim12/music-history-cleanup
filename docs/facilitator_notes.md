# Facilitator Notes: Streaming History Cleanup

These notes are for **me (the presenter)**. I am a student too, so the goal is not to be the expert. The goal is to run a clear activity, let classmates try the code, and be honest about what I know and what I looked up.

## Before I present (checklist)

- [ ] **Fill in the book references.** Search the README for `[FILL IN]` and replace every one with the real chapter and printed page numbers from the textbook (Section 1). *I could not look at the book while making this, so none of these are filled in.*
- [ ] **Check the schedule topic.** Confirm with the instructor that the topic wording on the schedule matches what the README says. (An online table of contents for an earlier edition suggested Section 1 is Chapters 1 to 4 and that some data-cleaning pages may be in Section 2. Compare with my copy of the book, and if cleaning is in a different section, say so in my intro.)
- [ ] **Update the AI statement** at the bottom of the README so it describes what I really did.
- [ ] **Replace the clone link** in the README with my real repository link.
- [ ] **Clean-start test.** On a computer with nothing opened: clone the repo, follow only the README, install the packages, and finish TODOs 1 to 5 using the starter file. Write down anything confusing in `docs/peer_test_log.md`.
- [ ] **Peer test.** Ask at least one classmate to follow the README **without my help**. Use the log. Fix the README where they got stuck.
- [ ] **Backup.** Save a copy of the chart (`code/output/listens_per_genre.png`) and a screenshot of the scoreboard with 13 passes, in case a live demo fails.
- [ ] **Access.** Confirm the repository is private/public as the instructor allows, and that the instructor and classmates can open it.
- [ ] **Repository link** (and slides, if any) submitted in Canvas by the deadline.

## What I need to be able to explain (in my own words)

I do not need to know all of pandas. I need to explain these four things clearly:

1. **A DataFrame is a table.** Each column is a Series, and pandas columns are built on NumPy arrays, so math works on the whole column at once. (Example: `minutes * plays`.)
2. **Cleaning fixes problems before analysis.** The four problems in this data are duplicates, inconsistent text, numbers stored as text, and missing values.
3. **Cleaning methods return a new result.** You have to assign it back (`clean["genre"] = ...`).
4. **Filtering uses a True/False mask.** Conditions are combined with `&` and `|`, not `and` and `or`, and each condition goes in parentheses.

## Honest answers for questions I can't answer

It is okay to not know. Some phrases that work:

- "Good question. I'm not sure. Let's look it up in the pandas documentation together."
- "I only covered the parts in Section 1 of the book. That might be later in the book."
- "I picked `fillna(1)` as a reasonable choice. Other people might drop those rows instead. Both are defensible."

Likely questions and short answers:

| Question | Short answer |
|---|---|
| Why `.copy()`? | So `listens` (the raw data) stays untouched and we can always compare before and after. |
| Why `reset_index(drop=True)`? | After removing rows the row numbers have gaps. This renumbers them 0, 1, 2... `drop=True` stops the old numbers becoming a new column. |
| Why `regex=False` in `.str.replace(" min", ...)`? | It says "treat this as plain text." Some characters (like `$` or `.`) have special meanings in regular expressions, so `regex=False` keeps things safe and simple. |
| Why `astype(int)` after `fillna`? | A column with gaps is stored as decimals (`3.0`). Once the gaps are filled, we can switch back to whole numbers. |
| Do I have to use `value_counts()`? | No, but it is the shortest way to count how many times each value appears. |
| Why does the program stop at `[TODO]`? | It is a built-in check so you always know which step to fix next. It is not an error. |
| Are these real songs? | No. The artists and tracks are made up, and so is the data. |

## Run of show (about 20 minutes; shrink or stretch as needed)

The instructor announces the real time limit. If I get less time, do TODOs 1 to 3 and skip 4 and 5, or have everyone run the finished file for 4 and 5.

| Time | What I do | What the class does |
|---|---|---|
| 0:00 to 2:00 | **Introduce.** Show the before/after picture (`docs/images/messy_vs_clean.png`). Say the topic, the book chapter and pages, and why this matters ("if we skip cleaning, the totals are wrong and nothing warns us"). | Listen, look at the picture |
| 2:00 to 4:00 | **Get set up.** Share the repo link. Make sure everyone has pandas installed. Run the starter once to show the empty scoreboard. | Clone, install, run the starter |
| 4:00 to 6:00 | **Idea 1 (NumPy / DataFrame).** Live explain: arrays do math all at once. Then say "Try TODO 1." | TODO 1 |
| 6:00 to 8:00 | **TODO 2.** Quick walk through the diagnosis report: "What is wrong with this data?" Take 2 or 3 answers. | TODO 2, then discuss |
| 8:00 to 14:00 | **Idea 2 (cleaning).** Explain "assign it back." Say the common mistake out loud **before** they hit it. Let them work on TODO 3. Walk around and help. | TODO 3a to 3e |
| 14:00 to 17:00 | **Idea 3 (filtering).** Explain True/False masks on the screen. Point out `&` and parentheses. | TODO 4 |
| 17:00 to 19:00 | **Plot.** Quick explanation, then they run TODO 5 and see the chart. | TODO 5 |
| 19:00 to 20:00 | **Debrief.** Reflection questions. Bonus TODOs for anyone finished. | Answer reflection aloud or in pairs |

## What to say at key moments

- **Opening (30 seconds):** "Real data is messy. Today we will take a messy music listening history, clean it up with pandas, and make a chart. You will write the code. I will help."
- **Before TODO 3:** "The most common mistake is forgetting to assign the result back. If your data doesn't change, check for `clean[...] =` at the start of the line."
- **Before TODO 4:** "To combine conditions use `&`, not `and`, and put each condition in parentheses. If you get the error 'truth value of a Series is ambiguous,' that is the sign."
- **Debrief:** "The program told us `[PASS]` at each step. What would have happened to our totals if we had skipped step 3c or 3a?" (Answer: without 3c the minutes would still be text, and we could not multiply them. Without 3a, duplicate listens would be counted twice and total listening time would be too high.)

## Things that can go wrong, and what I do

| Problem | Fix |
|---|---|
| Someone can't install pandas | Pair them up with a neighbor, or have them view the finished output screenshots (`docs/images`). |
| Chart window won't open | Set `SHOW_PLOT = False` and open `code/output/listens_per_genre.png`. |
| Everyone is behind | Skip TODO 5 and show the finished chart on my screen. |
| Everyone is ahead | Point them to the bonus TODOs 6 and 7. |
| Repo access error | Have the backup ZIP ready to share (Code > Download ZIP, or a copy in Canvas). |
| Output looks different (`object` vs `str`) | Different pandas versions. Say "same results, slightly different labels." |

## Debrief answers (for my reference)

Reflection question 1 (which step would cause the biggest mistake if skipped?): there is no single right answer. Good answers explain a consequence. Dropping duplicates affects totals directly (5 repeated listens inflate the numbers), and skipping the text cleanup splits one genre into several bars on the chart (`Pop`, `pop`, `POP` count separately).

Bonus 6 talking point: Electronic has fewer listens than Lo-Fi (6 vs 8) but more total minutes (56.0 vs 31.3), because its songs are longer. Counting rows and adding up a measurement can tell different stories.

Expected final numbers (to check my own run): 45 rows after cleaning, total listening time 354.2 minutes, 12 Pop listens, 16 long listens (10+ minutes), 7 long phone listens.

## After the presentation

- [ ] Record what I changed after testing in `docs/peer_test_log.md` (the "Changes I made" section).
- [ ] Make sure the last commit is pushed and the Canvas link works.
