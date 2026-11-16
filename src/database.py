from models import Location

# 18 campus buildings, kept in order by building ID (1 to 18).
# Search by ID (Binary Search) needs this list to stay in order.
campus_locations = [
    Location(1, "Main Gate", "Entrance"),
    Location(2, "Audio Visual Room", "Academic"),
    Location(3, "Salceda Building", "Academic"),
    Location(4, "Administration Building", "Academic"),
    Location(5, "Computing and Engineering Building", "Academic"),
    Location(6, "Center for Student Services (CSC) Building", "Administrative"),
    Location(7, "Registrar Office", "Administrative"),
    Location(8, "Automotive Building", "Technical"),
    Location(9, "Research and Development Management Office", "Administrative"),
    Location(10, "Physical Development Management Office", "Administrative"),
    Location(11, "Electronics and Electrical Building", "Technical"),
    Location(12, "Machine and Welding Shop", "Technical"),
    Location(13, "Gym", "Facility"),
    Location(14, "Technology and Entrepreneurship Building", "Academic"),
    Location(15, "Canteen", "Facility"),
    Location(16, "Dormitory", "Residential"),
    Location(17, "Food Lab", "Academic"),
    Location(18, "Nursing Department", "Academic"),
]

BUILDING_COUNT = len(campus_locations)

# ---------------------------------------------------------------------------
# CAMPUS GRID used by Route Planning (a 2D array: a list of rows, each row a list of cells).
# Traced from the campus map; one cell is about one step of walking.
# 0   = nothing (not walkable)
# 1   = road (walkable)
# 101 to 118 = building (100 + building ID, so 101 = Main Gate, 118 = Nursing Department)
# A building can only be entered when it is the destination. Routes never cut through one.

BUILDING_BASE = 100

#       0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
GRID = [
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # row 0
    [  0,   0,   0,   0,   0,   0,   0, 114,   0,   0,   0,   0,   0,   0,   0, 117,   0,   0,   0,   0,   0],  # row 1
    [  0, 112,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0],  # row 2
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 3
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 4
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 5
    [  0,   0,   1,   0,   0,   1,   1,   1, 113,   1,   1,   1,   1, 118,   1,   1,   0,   0,   0,   1,   0],  # row 6
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 7
    [  0, 111,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 8
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 9
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 10
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1, 115,   1,   1,   1,   1,   1,   1,   0,   1,   0],  # row 11
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0, 116,   0,   1,   0],  # row 12
    [  0, 110,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0],  # row 13
    [  0,   0,   1,   0,   0, 105,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 14
    [  0, 109,   1,   0,   0,   1,   0,   0,   0,   0,   1,   1, 106,   1,   1,   1,   0,   0,   0,   1,   0],  # row 15
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 16
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 17
    [  0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 18
    [  0, 108,   1,   0,   0,   1,   0,   0,   0,   0,   1,   1,   1,   1,   1,   1,   0,   0,   0,   1,   0],  # row 19
    [  0,   0,   1,   0,   0, 104,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 20
    [  0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 21
    [  0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],  # row 22
    [  0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1, 103,   0,   0,   1,   0],  # row 23
    [  0, 107,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   1,   1,   1,   1,   1,   1,   0],  # row 24
    [  0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1, 102,   1,   1,   1,   0,   0,   0,   0,   1,   0],  # row 25
    [  0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0],  # row 26
    [  0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0],  # row 27
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 28
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 29
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 30
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 31
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 32
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 33
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 34
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 35
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 36
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 37
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],  # row 38
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 101,   0,   0,   0,   0,   0],  # row 39
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # row 40
]


def check_grid():
    # Returns a list of problems (empty list = the grid looks good).
    problems = []
    rows = len(GRID)
    cols = len(GRID[0])

    # 1. Every row must be the same length
    for r in range(rows):
        if len(GRID[r]) != cols:
            problems.append(f"Row {r} has {len(GRID[r])} cells (expected {cols})")
    if len(problems) > 0:
        return problems

    # 2. Find every building (array scan). Each ID from 1 up to the number of buildings must appear exactly once.
    found = [0] * (BUILDING_COUNT + 1)
    positions = [None] * (BUILDING_COUNT + 1)   # positions[id] = (row, col)
    for r in range(rows):
        for c in range(cols):
            v = GRID[r][c]
            if v > BUILDING_BASE:
                bid = v - BUILDING_BASE
                if bid < 1 or bid > BUILDING_COUNT:
                    problems.append(f"Unknown building code {v} at row {r}, col {c}")
                else:
                    found[bid] += 1
                    positions[bid] = (r, c)
            elif v != 0 and v != 1:
                problems.append(f"Unknown value {v} at row {r}, col {c}")
    for bid in range(1, BUILDING_COUNT + 1):
        if found[bid] != 1:
            problems.append(f"Building {bid} appears {found[bid]} time(s) (expected 1)")
    if len(problems) > 0:
        return problems

    # 3. Every building must be able to reach the Main Gate.
    #    Queue-based exploration; buildings can only be entered as the destination.
    start = positions[1]
    for bid in range(2, BUILDING_COUNT + 1):
        dest = positions[bid]
        visited = []
        for r in range(rows):
            visited.append([False] * cols)
        queue = [start]
        visited[start[0]][start[1]] = True
        reached = False
        while len(queue) > 0:
            r, c = queue.pop(0)
            if (r, c) == dest:
                reached = True
                break
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and not visited[nr][nc]:
                    if GRID[nr][nc] == 1 or (nr, nc) == dest:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        if not reached:
            problems.append(f"Building {bid} cannot be reached from the Main Gate")
    return problems


def check_database():
    # Startup sanity check. Returns a list of problems (empty list = all good).
    # Binary Search by ID and Route Planning both depend on this data being correct.
    problems = []

    # 1. Buildings must be in order by ID, 1 to N, with no gaps
    for i in range(len(campus_locations)):
        if campus_locations[i].building_id != i + 1:
            problems.append(f"Building at position {i + 1} has ID {campus_locations[i].building_id} (expected {i + 1})")

    # 2. The grid itself: valid cells, every building in the list exactly once,
    #    every building reachable
    for problem in check_grid():
        problems.append("Grid: " + problem)

    return problems