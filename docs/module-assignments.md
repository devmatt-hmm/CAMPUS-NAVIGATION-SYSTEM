# Module Assignments

Each member owns one module for the full semester. As new DSA topics are taught,
you upgrade your own module rather than switching — this keeps ownership clear
for grading while covering more concepts as a group.

Rule: only use topics already taught in class (Arrays, Bubble/Insertion/Selection
Sort, Linear/Binary Search, Linked List, Stack, Queue).

## Assignments

### 1. Building Search — Carl Davin Ravago (`src/search.py`)
- **Responsibilities:** Search buildings by name or by ID; keep results readable.
- **Built:** Linear Search by name (partial match, empty search rejected) and
  Binary Search by ID (the building list is kept in order by ID).
- **Planned upgrade:** Hash Map lookup

### 2. Navigation History — Kyla Pelaez (`src/history.py`)
- **Responsibilities:** Log searches; show the history; remove the latest search.
- **Built:** Stack on a plain list. Newest search on top, view newest first,
  remove the most recent, no size limit.
- **Optional upgrade:** Rebuild the Stack with Linked List nodes.

### 3. Building Stats / Filter — Francis Danao (`src/stats.py`)
- **Responsibilities:** Count buildings per category; filter by category.
- **Built:** Array counting and linear filtering. Menu input is read as text so
  typing letters no longer crashes the program.
- **Planned upgrade:** Hash Map grouping

### 4. Route Planning — Mateo Orpiana (`src/route.py`)
- **Responsibilities:** Find a route between two buildings.
- **Built:** A Queue explores the roads outward from the start, and a Stack flips
  the path so it prints from start to destination. The result is the fewest
  road steps, not the fewest meters. The 32 road links come from Mateo's original
  road map and are stored in `database.py`.
- **Original version:** The Dijkstra/ASCII-map version (`display_route.py`) is
  saved on the `mateo-graph-route` branch to revisit once Graph is taught.
- **Planned upgrade:** ~

### 5. Directory Sort / Rank — Sherwin Gil (`src/sort_rank.py`)
- **Responsibilities:** List buildings sorted by name or ID.
- **Built:** Bubble Sort, Insertion Sort, and Selection Sort. The user picks the
  sort key and the method. Sorting works on a copy so the original list stays in order.
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
- [merge date] - Refactor merged into main under src/. Both regressions from 10/03 resolved (Stats crash fixed, Directory Sort/Rank back in the menu). display_route.py removed from main and kept on the mateo-graph-route branch