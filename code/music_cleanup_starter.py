"""
Streaming History Cleanup Lab - STARTER FILE

This is the ONLY file you edit. Work from top to bottom.
Fill in each line marked TODO, then run the file after every TODO.
Compare what it prints with the "Expected" notes (and the README).

    Windows:  python code/music_cleanup_starter.py
    Mac:      python3 code/music_cleanup_starter.py

Seeing "NoneType" in an error? A TODO above it is still None. That is normal
until you fill it in.

Stuck? The finished version is code/music_cleanup_finished.py.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).parent / "data" / "music_history_messy.csv"
pd.set_option("display.width", 130)  # keep wide tables on one line
pd.set_option("display.max_columns", None)  # show every column

# ----------------------------------------------------------------------
# STEP 1: NumPy warm-up (supplementary: not a section in the book)
# ----------------------------------------------------------------------
minutes = np.array([3.5, 4.0, 2.5, 3.0])  # song lengths
plays = np.array([2, 1, 3, 2])  # times each song was played

# TODO 1: multiply the two arrays. No loop needed!
minutes_listened = None  # Hint: multiply the two arrays with *

print("Minutes listened:", minutes_listened)  # Expected: [7.  4.  7.5 6. ]
print("Total:", minutes_listened.sum())  # Expected: 24.5

# ----------------------------------------------------------------------
# STEP 2: Load and inspect the data
# ----------------------------------------------------------------------

# TODO 2: load the CSV file into a DataFrame
listens = None  # Hint: pd.read_csv(...). DATA_FILE already holds the path

print("\nShape:", listens.shape)  # Expected: (50, 9)
print(listens.head())
listens.info()
print("\nDifferent genre spellings:", listens["Genre"].nunique())  # Expected: 13 (should be 5!)
print("Missing play counts:", listens["PlayCount"].isna().sum())  # Expected: 4
print("Duplicate rows:", listens.duplicated().sum())  # Expected: 5

# ----------------------------------------------------------------------
# STEP 3: Clean the data (one fix for each problem)
# ----------------------------------------------------------------------
clean = listens.copy()  # work on a copy; the original stays untouched

# TODO 3: fix each problem. Add the fix to the end of each line below.
clean["Genre"] = clean["Genre"]  # Hint: .str.strip() then .str.title()
clean["SongLength"] = clean["SongLength"]  # Hint: .str.replace(" min", "", regex=False) then .astype(float)
clean["PlayCount"] = clean["PlayCount"]  # Hint: .fillna(1)
clean = clean  # Hint: .drop_duplicates()

print("\nShape after cleaning:", clean.shape)  # Expected: (45, 9)
print("Genres:", sorted(clean["Genre"].unique()))  # Expected: ['Electronic', 'Hip-Hop', 'Lo-Fi', 'Pop', 'Rock']
print("SongLength type:", clean["SongLength"].dtype)  # Expected: float64
print("Missing play counts:", clean["PlayCount"].isna().sum())  # Expected: 0

# ----------------------------------------------------------------------
# STEP 4: New column and filtering
# ----------------------------------------------------------------------

# TODO 4a: add a TotalMinutes column (song length times play count)
clean["TotalMinutes"] = None  # Hint: multiply two columns, just like STEP 1

# TODO 4b: keep only the Pop listens
pop_listens = None  # Hint: clean.query("...") takes a STRING. Text goes in quotes inside it

# TODO 4c: keep the Phone listens that add up to 10 minutes or more
long_phone = None  # Hint: one query string, two conditions joined with the word and

print("\nTotal listening time:", round(clean["TotalMinutes"].sum(), 1))  # Expected: 354.2
print("Pop listens:", len(pop_listens))  # Expected: 12
print("Long phone listens:", len(long_phone))  # Expected: 7
print(long_phone[["Artist", "Track", "TotalMinutes"]])

# ----------------------------------------------------------------------
# STEP 5: Summarize and plot
# ----------------------------------------------------------------------

# TODO 5a: total TotalMinutes for each genre
genre_minutes = None  # Hint: .groupby("Genre"), pick TotalMinutes, then .sum()
print("\n", genre_minutes)  # Expected: Pop is the biggest (95.0), Lo-Fi the smallest (31.3)

# TODO 5b: draw it as a bar chart with a title and a y-axis label
# Hint: genre_minutes.plot.bar(title=..., ylabel=...)
# your code here

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
