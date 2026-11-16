# ROUTE PLANNING - uses a 2D array (the grid), a Queue and a Stack
#   Array: GRID in database.py is the campus map. 0 = nothing, 1 = road,
#          101 to 118 = a building (100 + building ID).
#   Queue: explores the roads outward from the start, one step at a time
#          (FIFO - the first cell added is the first one explored)
#   Stack: flips the path around so it reads from start to destination
#          (LIFO - the last cell added is the first one taken out)
# Every step on the grid is the same size, so the first time the Queue reaches
# the destination, it has used the FEWEST STEPS (the shortest walk).
# A building can only be stepped on when it is the destination, so a route
# never cuts through another building.

from database import campus_locations, GRID, BUILDING_BASE, BUILDING_COUNT

ROWS = len(GRID)
COLS = len(GRID[0])

# The four moves: up, down, left, right (no diagonals)
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def make_grid(value):
    # A new 2D array the same size as GRID, with every cell set to one value
    grid = []
    for r in range(ROWS):
        grid.append([value] * COLS)
    return grid


def inside_grid(r, c):
    return r >= 0 and r < ROWS and c >= 0 and c < COLS


def find_building(building_id):
    # Scan the grid (row by row) for the cell that holds this building.
    # Returns (row, col), or None if it is not on the grid.
    target = BUILDING_BASE + building_id
    for r in range(ROWS):
        for c in range(COLS):
            if GRID[r][c] == target:
                return (r, c)
    return None


def find_route(start, destination):
    # Returns the path as a list of (row, col) cells from the start building
    # to the destination building, or an empty list if there is no route.
    start_cell = find_building(start)
    dest_cell = find_building(destination)
    if start_cell is None or dest_cell is None:
        return []

    visited = make_grid(False)     # True once a cell has been added to the queue
    came_from = make_grid(None)    # the cell we stepped from to reach this one

    # --- Queue: explore the roads ---
    queue = []
    queue.append(start_cell)         # enqueue
    visited[start_cell[0]][start_cell[1]] = True

    while len(queue) > 0:
        r, c = queue.pop(0)          # dequeue (take from the front)
        if (r, c) == dest_cell:
            break
        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc
            if inside_grid(nr, nc) and not visited[nr][nc]:
                # Walk on roads, or step onto the destination building
                if GRID[nr][nc] == 1 or (nr, nc) == dest_cell:
                    visited[nr][nc] = True
                    came_from[nr][nc] = (r, c)   # remember where we came from
                    queue.append((nr, nc))

    if not visited[dest_cell[0]][dest_cell[1]]:
        return []   # no route found

    # --- Stack: walk back from the destination, then pop to read forward ---
    stack = []
    cell = dest_cell
    while cell != start_cell:
        stack.append(cell)           # push
        cell = came_from[cell[0]][cell[1]]
    stack.append(start_cell)

    path = []
    while len(stack) > 0:
        path.append(stack.pop())     # pop gives start first, destination last
    return path


def buildings_passed(path, start, destination):
    # Buildings that touch the path (above, below, left or right of a road
    # cell on the route), in the order the route reaches them.
    passed = []
    for i in range(1, len(path) - 1):
        r, c = path[i]
        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc
            if inside_grid(nr, nc) and GRID[nr][nc] > BUILDING_BASE:
                building_id = GRID[nr][nc] - BUILDING_BASE
                if building_id != start and building_id != destination and building_id not in passed:
                    passed.append(building_id)
    return passed


def show_map(path, start, destination):
    # Mark the path on a copy of the grid, then print it row by row.
    # S = start, D = destination, * = route, . = road, number = other building
    on_path = make_grid(False)
    for r, c in path:
        on_path[r][c] = True

    print("   S = start   D = destination   * = your route   . = road")
    for r in range(ROWS):
        line = ""
        for c in range(COLS):
            value = GRID[r][c]
            if value > BUILDING_BASE:
                building_id = value - BUILDING_BASE
                if building_id == start:
                    line += " S "
                elif building_id == destination:
                    line += " D "
                else:
                    line += f"{building_id:>2} "
            elif on_path[r][c]:
                line += " * "
            elif value == 1:
                line += " . "
            else:
                line += "   "
        if line.strip() != "":       # skip completely empty rows
            print(line.rstrip())


def ask_building(label):
    while True:
        text = input(label).strip()
        if text.isdecimal() and int(text) >= 1 and int(text) <= BUILDING_COUNT:
            return int(text)
        print(f"  [-INVALID CHOICE. ENTER A NUMBER FROM 1 TO {BUILDING_COUNT}-]")


def plan_route():
    print("\n[-------------------------------------------]")
    print("            [-PLAN A ROUTE-]")
    for loc in campus_locations:
        print(loc.display_info())
    print("[-------------------------------------------]\n")

    start = ask_building("Enter the ID of your current location: ")
    destination = ask_building("Enter the ID of your destination: ")

    print("\n[-------------------------------------------]")
    if start == destination:
        print("   [-START AND DESTINATION ARE THE SAME-]")
    else:
        path = find_route(start, destination)
        if len(path) == 0:
            print("        [-NO ROUTE FOUND-]")
        else:
            print("              [-ROUTE-]")
            print(f"  From: {campus_locations[start - 1].name}")
            passed = buildings_passed(path, start, destination)
            if len(passed) > 0:
                print("  Passing by:")
                for building_id in passed:
                    print(f"    - {campus_locations[building_id - 1].name}")
            print(f"  To:   {campus_locations[destination - 1].name}")
            print(f"Steps: {len(path) - 1}")
            print()
            show_map(path, start, destination)
    print("[-------------------------------------------]\n")
