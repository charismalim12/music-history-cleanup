"""
Streaming History Cleanup Lab - FINISHED VERSION (TODOs 1 to 5)

This is the starter file with TODOs 1 to 5 filled in, line for line.
Try each step yourself first, then use this file to compare.

Run from the repository folder:
    Windows:  python code/music_cleanup_finished.py
    Mac:      python3 code/music_cleanup_finished.py
"""

import sys
from pathlib import Path
from pprint import pprint

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Setup (do not edit this part)
# ----------------------------------------------------------------------
HERE = Path(__file__).parent
DATA_FILE = HERE / "data" / "music_history_messy.csv"
OUTPUT_DIR = HERE / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
SHOW_PLOT = True  # set to False if your computer cannot open plot windows

pd.set_option("display.width", 100)
pd.set_option("display.max_columns", 20)

passed = []  # the TODO numbers that have passed their check
ALL_TODOS = ["1", "2", "3a", "3b", "3c", "3d", "3e", "4a", "4b", "4c", "5a", "5b", "5c"]


def scoreboard():
    """Print which TODOs have passed so far."""
    print("\n" + "=" * 60)
    print("SCOREBOARD")
    print("=" * 60)
    for todo in ALL_TODOS:
        mark = "[PASS]" if todo in passed else "[    ]"
        print(f"  {mark} TODO {todo}")
    print(f"\n  {len(passed)} of {len(ALL_TODOS)} checks passed.")


def check(todo, ok, hint):
    """If the check passes, keep going. If not, show a hint and stop here."""
    if ok:
        passed.append(todo)
        print(f"  [PASS] TODO {todo}")
    else:
        print(f"\n  [TODO] TODO {todo} is not finished yet.")
        print(f"         Hint: {hint}")
        scoreboard()
        sys.exit(0)


print("=" * 60)
print("STREAMING HISTORY CLEANUP LAB")
print("=" * 60)

# ----------------------------------------------------------------------
# STEP 1 - NumPy warm-up
# ----------------------------------------------------------------------
print("\n=== STEP 1: NumPy warm-up ===")

minutes = np.array([3.5, 4.0, 2.5, 3.0])  # length of 4 songs, in minutes
plays = np.array([2, 1, 3, 2])  # how many times each song was played

# TODO 1: do math on whole arrays at once (no loops!)
minutes_listened = minutes * plays
total_minutes = minutes_listened.sum()
average_length = minutes.mean()

check(
    "1",
    minutes_listened is not None
    and total_minutes is not None
    and average_length is not None
    and np.allclose(minutes_listened, [7.0, 4.0, 7.5, 6.0]),
    "multiply the two arrays with *, then use .sum() and .mean()",
)
print("Minutes listened per song:", minutes_listened)
print(f"Total listening time     : {total_minutes:.1f} minutes")
print(f"Average song length      : {average_length:.2f} minutes")

# ----------------------------------------------------------------------
# STEP 2 - Load the messy data into a DataFrame
# ----------------------------------------------------------------------
print("\n=== STEP 2: Load the data ===")

# TODO 2: load the CSV file into a DataFrame called listens
listens = pd.read_csv(DATA_FILE)

check(
    "2",
    isinstance(listens, pd.DataFrame) and listens.shape == (50, 9),
    "use pd.read_csv(DATA_FILE) and store it in listens",
)
print("Shape (rows, columns):", listens.shape)
print(listens.head())
print()
listens.info()

print("\n--- Diagnosis: what is wrong with this data? ---")
print("Missing values per column:")
print(listens.isna().sum())
print("\nDuplicate rows:", listens.duplicated().sum())
print("\nGenre names as typed (sorted):")
pprint(sorted(listens["genre"].unique()), width=70)

# ----------------------------------------------------------------------
# STEP 3 - Clean the data
# ----------------------------------------------------------------------
print("\n=== STEP 3: Clean the data ===")

clean = listens.copy()  # work on a copy so the original stays untouched

# TODO 3a: remove duplicate rows (and renumber the index)
clean = clean.drop_duplicates().reset_index(drop=True)
check("3a", len(clean) == 45, "clean = clean.drop_duplicates().reset_index(drop=True)")

# TODO 3b: make the genre names consistent (strip spaces, Title Case)
clean["genre"] = clean["genre"].str.strip().str.title()
check(
    "3b",
    set(clean["genre"].unique()) == {"Pop", "Hip-Hop", "Rock", "Electronic", "Lo-Fi"},
    'clean["genre"] = clean["genre"].str.strip().str.title()  (assign it back!)',
)

# TODO 3c: turn the minutes text ("3.5 min") into numbers
clean["minutes"] = clean["minutes"].str.replace(" min", "", regex=False).astype(float)
check(
    "3c",
    pd.api.types.is_float_dtype(clean["minutes"]),
    'remove " min" with .str.replace(" min", "", regex=False), then .astype(float)',
)

# TODO 3d: fill the missing play counts with 1, then make the column whole numbers
clean["plays"] = clean["plays"].fillna(1).astype(int)
check(
    "3d",
    clean["plays"].isna().sum() == 0 and pd.api.types.is_integer_dtype(clean["plays"]),
    'clean["plays"].fillna(1).astype(int)',
)

# TODO 3e: add a new column called total_minutes = minutes * plays
clean["total_minutes"] = clean["minutes"] * clean["plays"]
check(
    "3e",
    "total_minutes" in clean.columns
    and np.allclose(clean["total_minutes"], clean["minutes"] * clean["plays"]),
    'clean["total_minutes"] = clean["minutes"] * clean["plays"]  (just like STEP 1!)',
)

print("\nCleaned data (first 5 rows, main columns):")
print(clean[["listen_id", "genre", "minutes", "plays", "total_minutes"]].head())
print("\nShape after cleaning:", clean.shape)
print("Genres now:", sorted(clean["genre"].unique()))
print("Minutes column type:", clean["minutes"].dtype)
print(f"Total listening time: {clean['total_minutes'].sum():.1f} minutes")

# ----------------------------------------------------------------------
# STEP 4 - Filter rows
# ----------------------------------------------------------------------
print("\n=== STEP 4: Filter rows ===")

# TODO 4a: keep only the Pop listens
pop_listens = clean[clean["genre"] == "Pop"]
check(
    "4a",
    pop_listens is not None
    and len(pop_listens) == sum(g == "Pop" for g in clean["genre"]),
    'clean[clean["genre"] == "Pop"]',
)

# TODO 4b: keep only the long listens (10 or more total minutes)
long_listens = clean[clean["total_minutes"] >= 10]
check(
    "4b",
    long_listens is not None
    and len(long_listens) == sum(t >= 10 for t in clean["total_minutes"]),
    'clean[clean["total_minutes"] >= 10]',
)

# TODO 4c: keep long listens (10+ minutes) that happened on a Phone
long_phone_listens = clean[(clean["device"] == "Phone") & (clean["total_minutes"] >= 10)]
check(
    "4c",
    long_phone_listens is not None
    and len(long_phone_listens)
    == sum(d == "Phone" and t >= 10 for d, t in zip(clean["device"], clean["total_minutes"])),
    'use & (not "and") and put each condition in its own parentheses',
)

print(f"Pop listens                 : {len(pop_listens)}")
print(f"Long listens (10+ minutes)  : {len(long_listens)}")
print(f"Long listens on a Phone     : {len(long_phone_listens)}")
print("\nLong phone listens:")
print(long_phone_listens[["listen_id", "artist", "track", "plays", "total_minutes"]])

# ----------------------------------------------------------------------
# STEP 5 - A basic plot
# ----------------------------------------------------------------------
print("\n=== STEP 5: Make a plot ===")

# TODO 5a: count how many listens each genre has
genre_counts = clean["genre"].value_counts()
check(
    "5a",
    genre_counts is not None and genre_counts.sum() == len(clean),
    'clean["genre"].value_counts()',
)

fig, ax = plt.subplots(figsize=(7, 4))

# TODO 5b: draw the counts as a bar chart on ax
genre_counts.plot(kind="bar", ax=ax, color="darkorchid")
check("5b", len(ax.patches) == 5, 'genre_counts.plot(kind="bar", ax=ax, color="darkorchid")')

# TODO 5c: give the chart a title and axis labels
ax.set_title("Listens per genre")
ax.set_xlabel("Genre")
ax.set_ylabel("Number of listens")
check("5c", ax.get_title() != "" and ax.get_ylabel() != "", "use ax.set_title(...), ax.set_xlabel(...), ax.set_ylabel(...)")

plt.xticks(rotation=0)
plt.tight_layout()
fig.savefig(OUTPUT_DIR / "listens_per_genre.png")
print("Saved chart to", OUTPUT_DIR / "listens_per_genre.png")

# ----------------------------------------------------------------------
# BONUS AREA - TODOs 6 and 7 (optional). Write your code in the README
# example or your own version below this line, above the scoreboard.
# ----------------------------------------------------------------------

scoreboard()
print("\nAll TODOs passed! Close the chart window to finish.")

if SHOW_PLOT:
    plt.show()
