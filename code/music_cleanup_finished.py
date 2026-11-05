"""
Streaming History Cleanup Lab - FINISHED VERSION

This is the starter file with every TODO filled in, line for line.
Try each step yourself first, then use this file to compare.

Run it from the repository folder:
    Windows:  python code/music_cleanup_finished.py
    Mac:      python3 code/music_cleanup_finished.py
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
minutes_listened = minutes * plays

print("Minutes listened:", minutes_listened)  # Expected: [7.  4.  7.5 6. ]
print("Total:", minutes_listened.sum())  # Expected: 24.5

# ----------------------------------------------------------------------
# STEP 2: Load and inspect the data
# ----------------------------------------------------------------------

# TODO 2: load the CSV file into a DataFrame
listens = pd.read_csv(DATA_FILE)

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

# TODO 3: fix each problem. Remember to assign the result back!
clean["Genre"] = clean["Genre"].str.strip().str.title()
clean["SongLength"] = clean["SongLength"].str.replace(" min", "", regex=False).astype(float)
clean["PlayCount"] = clean["PlayCount"].fillna(1)
clean = clean.drop_duplicates()

print("\nShape after cleaning:", clean.shape)  # Expected: (45, 9)
print("Genres:", sorted(clean["Genre"].unique()))  # Expected: ['Electronic', 'Hip-Hop', 'Lo-Fi', 'Pop', 'Rock']
print("SongLength type:", clean["SongLength"].dtype)  # Expected: float64
print("Missing play counts:", clean["PlayCount"].isna().sum())  # Expected: 0

# ----------------------------------------------------------------------
# STEP 4: New column and filtering
# ----------------------------------------------------------------------

# TODO 4a: add a TotalMinutes column (song length times play count)
clean["TotalMinutes"] = clean["SongLength"] * clean["PlayCount"]

# TODO 4b: keep only the Pop listens
pop_listens = clean.query('Genre == "Pop"')

# TODO 4c: keep the Phone listens that add up to 10 minutes or more
long_phone = clean.query('Device == "Phone" and TotalMinutes >= 10')

print("\nTotal listening time:", round(clean["TotalMinutes"].sum(), 1))  # Expected: 354.2
print("Pop listens:", len(pop_listens))  # Expected: 12
print("Long phone listens:", len(long_phone))  # Expected: 7
print(long_phone[["Artist", "Track", "TotalMinutes"]])

# ----------------------------------------------------------------------
# STEP 5: Summarize and plot
# ----------------------------------------------------------------------

# TODO 5a: total TotalMinutes for each genre
genre_minutes = clean.groupby("Genre")["TotalMinutes"].sum()
print("\n", genre_minutes)  # Expected: Pop is the biggest (95.0), Lo-Fi the smallest (31.3)

# TODO 5b: draw it as a bar chart with a title and a y-axis label
genre_minutes.plot.bar(title="Listening time by genre", ylabel="Total minutes")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
