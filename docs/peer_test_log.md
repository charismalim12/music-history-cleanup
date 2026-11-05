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
| 3 | TODO 1 gives `[7.  4.  7.5 6. ]` and `Total: 24.5` | [ ] | |
| 4 | TODO 2 gives shape `(50, 9)`, 13 genres, 4 missing, 5 duplicates | [ ] | |
| 5 | TODO 3 gives shape `(45, 9)`, 5 clean genres, `float64`, 0 missing | [ ] | |
| 6 | TODO 4 gives total `354.2`, Pop `12`, long phone listens `7` | [ ] | |
| 7 | TODO 5 prints Pop `95.0` / Lo-Fi `31.3` and opens a bar chart | [ ] | |
| 8 | Finished file (`music_cleanup_finished.py`) runs with no errors | [ ] | |
| 9 | Bonus A table matches the README (Electronic: 6, 56.0, 9.33) | [ ] | |
| 10 | Bonus B top listen is `2017` with `19.2` | [ ] | |
| 11 | Every page number in the README checked against the physical book | [ ] | |

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
| 5 | Open the starter file and understand which lines to edit | [ ] | [ ] | |

### Activity checklist

| # | Did the tester... | Yes | No | Time (min) | Where they got stuck / what they said |
|---|---|---|---|---|---|
| 1 | Complete TODO 1 (NumPy warm-up) | [ ] | [ ] | | |
| 2 | Complete TODO 2 (load the CSV) | [ ] | [ ] | | |
| 3 | Name at least 3 problems in the data after TODO 2 | [ ] | [ ] | | |
| 4 | Complete TODO 3 (all four cleaning fixes) | [ ] | [ ] | | |
| 5 | Notice when their output did not match an `Expected` comment | [ ] | [ ] | | |
| 6 | Complete TODO 4a (TotalMinutes column) | [ ] | [ ] | | |
| 7 | Complete TODO 4b and 4c (`query()` filters) | [ ] | [ ] | | |
| 8 | Complete TODO 5a (`groupby` summary) | [ ] | [ ] | | |
| 9 | Complete TODO 5b (bar chart with title and label) | [ ] | [ ] | | |
| 10 | Match all the `Expected` values without author hints | [ ] | [ ] | | |

### Understanding checks (ask these after the activity, without looking at the README)

| # | Question | Correct | Partly | Not yet | Tester's answer |
|---|---|---|---|---|---|
| 1 | Why do we write `clean["Genre"] = clean["Genre"].str.strip()...` instead of just `clean["Genre"].str.strip()...`? | [ ] | [ ] | [ ] | |
| 2 | Inside `query()`, why are there quotes around `"Pop"`? | [ ] | [ ] | [ ] | |
| 3 | If we skipped `.drop_duplicates()`, which number would be wrong, and which way? | [ ] | [ ] | [ ] | |
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
| Were the `Expected` comments helpful for checking your work? | |
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
| 2 | Textbook chapter and page references verified against the physical book | [ ] |
| 3 | AI-use note mentions both ChatGPT (book notes) and Claude, and describes how I verified | [ ] |
| 4 | Repository link works from a different account / browser | [ ] |
| 5 | Instructor and classmates have access | [ ] |
| 6 | Latest changes committed and pushed; commit history shows steady progress | [ ] |
| 7 | No passwords, API keys, or private information in the repository | [ ] |
| 8 | Backup screenshot of the chart saved | [ ] |
