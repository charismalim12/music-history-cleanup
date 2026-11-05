"""
Streaming History Cleanup Lab - STARTER FILE

This is the ONLY file you edit. Work from top to bottom.
Look for the lines marked  TODO  and fill them in.

How it works: after each TODO the program runs a CHECK.
  [PASS]  your code worked, the program keeps going
  [TODO]  not finished yet, you get a hint and the program stops there

Run from the repository folder (use it after every TODO):
    Windows:  python code/music_cleanup_starter.py
    Mac:      python3 code/music_cleanup_starter.py

Stuck? The finished version is code/music_cleanup_finished.py.
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
# Hint: multiply the arrays with *, then use .sum() and .mean()
minutes_listened = None  # <- replace None with your code
total_minutes = None
average_length = None

check(
    "1",
    minutes_listened is not None
    and total_minutes is not None
    and average_length is not None
    and np.allclose(minutes_listened, [7.0, 4.0, 7.5, 6.0]),
    "check the Hint above. Both arrays are NumPy arrays, so * works on every pair at once",
)
print("Minutes listened per song:", minutes_listened)
print(f"Total listening time     : {total_minutes:.1f} minutes")
print(f"Average song length      : {average_length:.2f} minutes")

# ----------------------------------------------------------------------
# STEP 2 - Load the messy data into a DataFrame
# ----------------------------------------------------------------------
print("\n=== STEP 2: Load the data ===")

# TODO 2: load the CSV file into a DataFrame called listens
# Hint: pd.read_csv(...) takes the file path. DATA_FILE already holds it.
listens = None  # <- replace None with your code

check(
    "2",
    isinstance(listens, pd.DataFrame) and listens.shape == (50, 9),
    "listens should be a DataFrame with 50 rows and 9 columns. Did you replace None?",
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
# Hint: .drop_duplicates() then .reset_index(drop=True). Assign it back to clean!
# your code here
check("3a", len(clean) == 45, "there should be 45 rows left. Did you assign the result back to clean?")

# TODO 3b: make the genre names consistent (strip spaces, Title Case)
# Hint: .str.strip() removes spaces, .str.title() fixes the capital letters.
# your code here
check(
    "3b",
    set(clean["genre"].unique()) == {"Pop", "Hip-Hop", "Rock", "Electronic", "Lo-Fi"},
    "every genre should have exactly one spelling. Did you assign the result back?",
)

# TODO 3c: turn the minutes text ("3.5 min") into numbers
# Hint: .str.replace(" min", "", regex=False) then .astype(float)
# your code here
check(
    "3c",
    pd.api.types.is_float_dtype(clean["minutes"]),
    "the minutes column should hold numbers, not text. Remove the ' min' first",
)

# TODO 3d: fill the missing play counts with 1, then make the column whole numbers
# Hint: .fillna(1) fills the gaps, .astype(int) makes whole numbers
# your code here
check(
    "3d",
    clean["plays"].isna().sum() == 0 and pd.api.types.is_integer_dtype(clean["plays"]),
    "no gaps should remain, and the values should be whole numbers",
)

# TODO 3e: add a new column called total_minutes = minutes * plays
# Hint: multiply two columns, just like the two arrays in STEP 1
# your code here
check(
    "3e",
    "total_minutes" in clean.columns
    and np.allclose(clean["total_minutes"], clean["minutes"] * clean["plays"]),
    "you need a new column named total_minutes (lowercase, with an underscore)",
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
# Hint: df[ condition ] keeps the rows where the condition is True
pop_listens = None  # <- replace None with your code
check(
    "4a",
    pop_listens is not None
    and len(pop_listens) == sum(g == "Pop" for g in clean["genre"]),
    "keep only the rows where genre equals Pop. Use == (two equal signs)",
)

# TODO 4b: keep only the long listens (10 or more total minutes)
# Hint: same pattern, but compare the "total_minutes" column with >=
long_listens = None  # <- replace None with your code
check(
    "4b",
    long_listens is not None
    and len(long_listens) == sum(t >= 10 for t in clean["total_minutes"]),
    "compare the total_minutes column with >= and 10",
)

# TODO 4c: keep long listens (10+ minutes) that happened on a Phone
# Hint: two conditions joined with &  (each one inside its own parentheses)
long_phone_listens = None  # <- replace None with your code
check(
    "4c",
    long_phone_listens is not None
    and len(long_phone_listens)
    == sum(d == "Phone" and t >= 10 for d, t in zip(clean["device"], clean["total_minutes"])),
    "use & (not the word \"and\") and put each condition in its own parentheses",
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
# Hint: a column has a .value_counts() method
genre_counts = None  # <- replace None with your code
check(
    "5a",
    genre_counts is not None and genre_counts.sum() == len(clean),
    "call a method on the genre column that counts each value",
)

fig, ax = plt.subplots(figsize=(7, 4))

# TODO 5b: draw the counts as a bar chart on ax
# Hint: genre_counts.plot(kind=..., ax=ax, color=...)   (kind is "bar")
# your code here
check("5b", len(ax.patches) == 5, "you need to draw 5 bars: one per genre")

# TODO 5c: give the chart a title and axis labels
# Hint: ax.set_title(...), ax.set_xlabel(...), ax.set_ylabel(...)
# your code here
check("5c", ax.get_title() != "" and ax.get_ylabel() != "", "set a title AND a y-axis label")

plt.xticks(rotation=0)
plt.tight_layout()
fig.savefig(OUTPUT_DIR / "listens_per_genre.png")
print("Saved chart to", OUTPUT_DIR / "listens_per_genre.png")

# ----------------------------------------------------------------------
# BONUS AREA - TODOs 6 and 7 (optional, not checked by the program).
# Finished early? Read the bonus instructions in the README and write
# your code below this line, above the scoreboard.
# ----------------------------------------------------------------------

scoreboard()
print("\nAll TODOs passed! Close the chart window to finish.")

if SHOW_PLOT:
    plt.show()
