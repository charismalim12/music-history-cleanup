# Peer Test Log: Streaming History Cleanup

Use this log to make sure the activity works for someone who is **not** the author. Make one copy of the "Test session" section for each person who tests (copy and paste it below as Test 2, Test 3, and so on).

**Rules for the tester's session**

- The tester uses only the README. The author **does not give hints** and does not talk about the activity while the tester works.
- The author watches silently and writes down every place the tester stops, frowns, asks a question, or gets an error.
- If the tester is stuck for more than 2 minutes, the author notes the spot and then gives a hint, so the session can continue.

---

## Part A: Author's clean-start test (do this first)

Test from a clean start: a fresh folder, no old files.

| | |
|---|---|
| Date | |
| Computer / OS | |
| Python version (`python --version`) | |
| pandas version (`python -m pip show pandas`) | |

| # | Check | Done | Notes |
|---|---|---|---|
| 1 | Cloned (or downloaded) the repository into a new folder | [ ] | |
| 2 | Package install command worked | [ ] | |
| 3 | Starter file runs untouched and shows `0 of 13 checks passed` | [ ] | |
| 4 | TODO 1 gives the Checkpoint 1 output (total `24.5 minutes`) | [ ] | |
| 5 | TODO 2 gives shape `(50, 9)` | [ ] | |
| 6 | TODO 3a to 3e all `[PASS]`; shape `(45, 10)`; total `354.2 minutes` | [ ] | |
| 7 | TODO 4 gives Pop 12, long listens 16, long phone listens 7 | [ ] | |
| 8 | TODO 5 opens a chart and saves `code/output/listens_per_genre.png` | [ ] | |
| 9 | Scoreboard shows `13 of 13 checks passed` | [ ] | |
| 10 | Finished file (`music_cleanup_finished.py`) also runs with 13 of 13 | [ ] | |
| 11 | Bonus TODO 6 gives Pop `95.0` and Lo-Fi `31.3` | [ ] | |
| 12 | Bonus TODO 7 top listen is `2017` with `19.2`, and the clean CSV is saved | [ ] | |

---

## Part B: Test session (copy this section for each peer)

### Tester information

| | |
|---|---|
| Tester name or initials | |
| Date | |
| Operating system (Windows / Mac / Linux) | |
| Python version | |
| Experience with pandas before today (none / a little / some) | |
| Time allowed | |
| Start time / end time | |

### Setup checklist

| # | Did the tester... | Yes | No | Notes (what confused them) |
|---|---|---|---|---|
| 1 | Find and open the repository without help | [ ] | [ ] | |
| 2 | Clone or download it | [ ] | [ ] | |
| 3 | Open the folder in VS Code | [ ] | [ ] | |
| 4 | Install the packages from `requirements.txt` | [ ] | [ ] | |
| 5 | Run the starter file and see the empty scoreboard | [ ] | [ ] | |

### Activity checklist

| # | Did the tester... | Yes | No | Time (min) | Where they got stuck / what they said |
|---|---|---|---|---|---|
| 1 | Complete TODO 1 (NumPy) | [ ] | [ ] | | |
| 2 | Complete TODO 2 (load the CSV) | [ ] | [ ] | | |
| 3 | Name the problems in the data after TODO 2 | [ ] | [ ] | | |
| 4 | Complete TODO 3a (duplicates) | [ ] | [ ] | | |
| 5 | Complete TODO 3b (genre names) | [ ] | [ ] | | |
| 6 | Complete TODO 3c (minutes text to number) | [ ] | [ ] | | |
| 7 | Complete TODO 3d (missing play counts) | [ ] | [ ] | | |
| 8 | Complete TODO 3e (total_minutes column) | [ ] | [ ] | | |
| 9 | Complete TODO 4a to 4c (filters) | [ ] | [ ] | | |
| 10 | Complete TODO 5a to 5c (bar chart) | [ ] | [ ] | | |
| 11 | Reach `13 of 13 checks passed` without author hints | [ ] | [ ] | | |
| 12 | Match the expected outputs shown in the README images | [ ] | [ ] | | |

### Understanding checks (ask these after the activity, without looking at the README)

| # | Question | Correct | Partly | Not yet | Tester's answer |
|---|---|---|---|---|---|
| 1 | Why do we write `clean["genre"] = clean["genre"].str.strip()...` instead of just `clean["genre"].str.strip()...`? | [ ] | [ ] | [ ] | |
| 2 | What does `clean["total_minutes"] >= 10` give back on its own? | [ ] | [ ] | [ ] | |
| 3 | Why `&` and parentheses instead of `and`? | [ ] | [ ] | [ ] | |
| 4 | Name two kinds of messy data we fixed. | [ ] | [ ] | [ ] | |

### Errors the tester hit

| Error message or symptom | Which TODO | Was it already in the Troubleshooting table? | How it was fixed |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

### Tester feedback

| Question | Answer |
|---|---|
| Were the instructions clear? (1 = confusing, 5 = very clear) | |
| Was the activity the right length? (too short / right / too long) | |
| What was the most confusing sentence or step? | |
| What was the most helpful part? | |
| What one thing would you change? | |

---

## Part C: Changes I made after testing

Write each problem found, and the exact change you made to the README, code, or data. This is evidence for the grader that testing led to improvements.

| # | Problem found (who / where) | Change I made | Where (file) | Done |
|---|---|---|---|---|
| 1 | | | | [ ] |
| 2 | | | | [ ] |
| 3 | | | | [ ] |

## Part D: Final pre-presentation checks

| # | Check | Done |
|---|---|---|
| 1 | All `[FILL IN]` and `[EDIT THIS]` markers in the README are replaced | [ ] |
| 2 | Textbook chapter and page references verified against the book | [ ] |
| 3 | Repository link works from a different account / browser | [ ] |
| 4 | Instructor and classmates have access | [ ] |
| 5 | Latest changes committed and pushed; commit history shows steady progress | [ ] |
| 6 | No passwords, API keys, or private information in the repository | [ ] |
| 7 | Backup chart image and scoreboard screenshot saved | [ ] |
