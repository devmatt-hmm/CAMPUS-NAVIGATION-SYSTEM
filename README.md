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

Standard Python 3, no extra libraries.

## Project Structure

```
campus-navigation-system/
├── src/
│   ├── main.py            # Menu
│   ├── models.py          # Location class
│   ├── database.py        # Buildings + road connections
│   ├── search.py          # Building Search (Linear + Binary Search)
│   ├── history.py         # Navigation History (Stack)
│   ├── stats.py           # Building Stats / Filter (Arrays)
│   ├── sort_rank.py       # Directory Sort / Rank (Bubble, Insertion, Selection)
│   └── route.py           # Route Planning (Queue + Stack)
├── docs/
│   ├── module-assignments.md
│   ├── workflow.txt
│   ├── lab-reports/       # One per DSA topic
│   └── flowcharts/
└── tests/                 # Sample input/output logs per module
```

## Team

| Member | Module | File | DSA used | Status |
|---|---|---|---|---|
| Carl Davin Ravago | Building Search | `search.py` | Linear Search, Binary Search | Done |
| Kyla Pelaez | Navigation History | `history.py` | Stack | Done |
| Francis Danao | Building Stats / Filter | `stats.py` | Arrays | Done |
| Mateo Orpiana | Route Planning | `route.py` | Queue, Stack | Done |
| Sherwin Gil | Directory Sort / Rank | `sort_rank.py` | Bubble, Insertion, Selection Sort | Done |

See `docs/module-assignments.md` for responsibilities and DSA concepts per module.

## DSA Concepts Roadmap

- [x] Arrays — Building Stats / Filter, building list
- [x] Sorting — Bubble, Insertion, Selection (Directory Sort / Rank)
- [x] Searching — Linear (by name) and Binary (by ID)
- [x] Stack — Navigation History, Route Planning (path reversal)
- [x] Queue — Route Planning (exploring the roads)
- [ ] Linked List 
- [ ] Trees

Target: 5+ DSA concepts by end of semester, per course rubric.