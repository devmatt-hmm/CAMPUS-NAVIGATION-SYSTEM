# Module Assignments

Each member owns one module for the full semester. As new DSA topics are taught,
you upgrade your own module rather than switching — this keeps ownership clear
for grading while covering more concepts as a group.

Rule: only use topics already taught in class (Arrays, Bubble/Insertion/Selection
Sort, Linear/Binary Search, Linked List, Stack, Queue).

## Assignments

### 1. Building Search — Carl Davin Ravago (`src/search.py`)
- **Responsibilities:** Search buildings by name or by ID; keep results readable.
- **Built:** Linear Search by name (partial match, empty search rejected) with
  results ranked exact match first, then "starts with", then "contains". Binary
  Search by ID (the building list is kept in order by ID), with a "valid IDs"
  hint when nothing is found. Both searches print how many comparisons they made
  (Linear always checks all buildings; Binary needs at most 5 for 18). A
  "List all buildings" option was added to the search menu.
- **Planned upgrade:** Binary Search Tree for name lookup, only once Trees are taught.

### 2. Navigation History — Kyla Pelaez (`src/history.py`, `src/linked_list.py`)
- **Responsibilities:** Log searches; show the history; remove the latest search.
- **Built:** Stack rebuilt on a Linked List (`linked_list.py`). The head node is
  the top of the stack: push adds at the head, pop removes the head. Entries
  record the search type and result (e.g. `NAME: gym (1 found)`, `ID: 99 (not found)`).
  View newest first with a total count, remove the most recent, clear all
  history, no size limit.

### 3. Building Stats / Filter — Francis Danao (`src/stats.py`)
- **Responsibilities:** Count buildings per category; filter by category.
- **Built:** Array counting (with total) and linear filtering (empty input
  rejected). New "grouped by category" view: one Linked List per category, each
  building appended to its category's chain and printed head to tail. Menu input
  is read as text so typing letters does not crash the program, and the menu now
  loops with a Back option.

### 4. Route Planning — Mateo Orpiana (`src/route.py`)
- **Responsibilities:** Find a route between two buildings.
- **Built:** The campus map is a grid (a 2D array) stored in `database.py`: `0` is
  nothing, `1` is road, and `101` to `118` are buildings (100 + building ID). It was
  traced from the campus map and checked at startup (valid cells, every building once,
  every building reachable from the Main Gate). A Queue explores the roads outward from
  the start (up, down, left, right), and a Stack flips the trail so the path prints
  from start to destination. A building can only be stepped on when it is the
  destination, so routes never cut through other buildings. Every step on the grid is
  the same size, so the result is the shortest walk in grid steps. The program prints
  the buildings passed, the step count, and a map with the route drawn on it.

### 5. Directory Sort / Rank — Sherwin Gil (`src/sort_rank.py`)
- **Responsibilities:** List buildings sorted by name, ID, or category; rank categories.
- **Built:** Bubble Sort, Insertion Sort, and Selection Sort. The user picks the
  sort key (name, ID, or category then name) and the method. Each sort reports
  its comparison count (e.g. 153 for Bubble and Selection on 18 buildings).
  Sorting works on a copy so the original list stays in order. New ranking view:
  categories ranked by building count using Insertion Sort on parallel arrays,
  with ties sharing a rank.
- **Planned upgrade:** Binary Search Tree for ranked lookup, only once Trees are taught.

## Notes / Meeting Log

- 08/26/2026 — Group formed
- 08/31/2026 — First online meeting, chose Campus Navigation System, discussed future of project and workflow
- 09/19/2026 — Second online meeting, discussed assignment of modules, Lab Report for Arrays started
- 09/20/2026 — 3/5 Arrays built for Building Search, Navigation History, Building Stats/Filter.
- 09/21/2026 - Expanded database.py campus_locations (5 -> 17)
- 09/30/2026 - Added one missing location to database.py campus_locations (Nursing Department)
- 09/30/2026 - Added workflow text file to guide other group members with handling the repository
- 10/01/2026 - Improved the system's UI (Menus)
- 10/02/2026 - Minor changes to workflow
- 10/03/2026 - Route Planning rebuilt as a full Graph (Dijkstra's shortest path) with ASCII map rendering in display_route.py; module ownership swapped (Route Planning -> Mateo, Directory Sort/Rank -> Sherwin)
- 10/03/2026 - Found 2 regressions during testing: building_stats() crash bug is back, and Directory Sort/Rank is missing from main.py - both logged in Revisions Log
- 10/16/2026 - Reviewed the code against the "taught topics only" rule. Taught so far: Arrays, Bubble/Insertion/Selection Sort, Linear/Binary Search, Linked List, Stack, Queue. Dijkstra/heapq route code was not covered, so a refactor was planned and built: one file per module, Navigation History as a Stack, Binary Search by ID, three sorts, Route Planning with Queue + Stack
- 10/16/2026 - Refactor merged into main under src/. Both regressions from 10/03 resolved (Stats crash fixed, Directory Sort/Rank back in the menu). display_route.py removed from main and kept on the mateo-graph-route branch
- 11/15/2026 - Finalized all modules except Route Planning: added shared `linked_list.py`; Navigation History rebuilt as a Stack on a Linked List (plus clear all); Stats gained a Linked List grouping view; Search gained ranked name matches, comparison counts, and a list-all option; Sort/Rank gained a category key, comparison counts, and a category ranking view; `database.py` gained a startup data check. "Hash Map" planned upgrades removed since Hash Map has not been taught. Linked List concept now covered (6 concepts total)
- 11/16/2026 - Route Planning rebuilt on a 2D grid of the campus (Array + Queue + Stack). The grid was drawn from the campus map, then corrected by the team (inner walkway added, Salceda Building moved onto its street). `database.py` now holds the grid instead of the road-link list. Tested all modules together through the main menu (all 306 building-to-building routes checked, bad input in every menu) and saved sample input/output logs per module in `tests/`. All modules now work together