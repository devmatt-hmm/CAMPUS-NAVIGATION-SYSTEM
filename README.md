# Campus Navigation System

Progressive DSA Application Portfolio — Bicol University Polangui, Computer Engineering.

This project is a lab requirement, not a commercial application. Its purpose is to
demonstrate Data Structures and Algorithms (DSA) concepts through a simple
console-based campus navigation tool, built as new topics are taught.

## Rule

The code only uses topics that have already been taught in class: Arrays,
Sorting (Bubble, Insertion, Selection), Searching (Linear, Binary), Linked List,
Stack, and Queue. If a feature would normally need a topic we haven't covered,
we build it with the topics we have.

## How to Run

```
python src/main.py
```

Standard Python 3, no extra libraries. On startup the program checks that the
building list and the campus grid in `database.py` are valid before showing the menu.

## Project Structure

```
campus-navigation-system/
├── src/
│   ├── main.py            # Menu + startup data check
│   ├── models.py          # Location class
│   ├── database.py        # Buildings + campus grid (2D array) + data check
│   ├── linked_list.py     # Shared Linked List (used by history.py and stats.py)
│   ├── search.py          # Building Search (Linear + Binary Search)
│   ├── history.py         # Navigation History (Stack on a Linked List)
│   ├── stats.py           # Building Stats / Filter (Arrays + Linked List grouping)
│   ├── sort_rank.py       # Directory Sort / Rank (Bubble, Insertion, Selection)
│   └── route.py           # Route Planning (2D array + Queue + Stack)
├── docs/
│   ├── module-assignments.md
│   ├── workflow.txt
│   ├── lab-reports/       # One per DSA topic
│   └── flowcharts/
└── tests/                 # Sample input/output logs per module (log_*.txt)
```

## Features

| Menu option | What it does |
|---|---|
| Search for a Building | Search by name (ranked: exact, starts with, contains) or by ID, or list all buildings. Each search shows how many comparisons it made. |
| View Navigation History | View, remove the latest, or clear all past searches (newest first). |
| Building Stats / Filter | Count buildings per category, filter by category, or view buildings grouped by category. |
| Directory Sort / Rank | Sort by name, ID, or category with any of three sorts (shows comparisons made), or rank categories by building count. |
| Plan a Route | Finds the shortest walk between two buildings on the campus grid. Shows the buildings you pass, the number of steps, and a map with the route drawn on it. |

## How Route Planning Works

The campus is a grid (a 2D array): `0` is nothing, `1` is road, and `101` to `118` are
buildings (100 + building ID). A Queue explores the roads outward from the start one
step at a time, so the first time it reaches the destination it has used the fewest
steps. Every cell remembers where it came from, and a Stack flips that trail around so
the path reads from start to destination. A building can only be stepped on when it is
the destination, so a route never cuts through another building.

## Team

| Member | Module | File | DSA used | Status |
|---|---|---|---|---|
| Carl Davin Ravago | Building Search | `search.py` | Linear Search, Binary Search | Done |
| Kyla Pelaez | Navigation History | `history.py`, `linked_list.py` | Stack, Linked List | Done |
| Francis Danao | Building Stats / Filter | `stats.py` | Arrays, Linked List | Done |
| Mateo Orpiana | Route Planning | `route.py` | 2D Array, Queue, Stack | Done |
| Sherwin Gil | Directory Sort / Rank | `sort_rank.py` | Bubble, Insertion, Selection Sort | Done |

See `docs/module-assignments.md` for responsibilities and DSA concepts per module.

## DSA Concepts Roadmap

- [x] Arrays — building list, Stats counting, the campus grid (2D array) in Route Planning
- [x] Sorting — Bubble, Insertion, Selection (Directory Sort / Rank)
- [x] Searching — Linear (by name) and Binary (by ID)
- [x] Stack — Navigation History, Route Planning (path reversal)
- [x] Queue — Route Planning (exploring the roads)
- [x] Linked List — Navigation History (the Stack's storage), Stats grouping by category
- [ ] Trees

Target: 5+ DSA concepts by end of semester, per course rubric. Currently 6.