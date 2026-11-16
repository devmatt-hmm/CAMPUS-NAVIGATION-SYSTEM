# BUILDING SEARCH
#   Search by name -> Linear Search (checks every building one by one)
#   Search by ID   -> Binary Search (needs the list to be in order by ID)

from database import campus_locations
from history import push


def search_by_name():
    # Linear Search Algorithm
    # Every building is checked, no matter what. Matches are sorted into three
    # groups so the best matches are printed first:
    #   1. exact name   2. name starts with the term   3. name contains the term
    term = input("\nEnter the name of the building to search: ").strip().lower()
    if term == "":
        print("\n  [-SEARCH CANNOT BE EMPTY-]\n")
        return

    exact = []
    starts = []
    contains = []

    for loc in campus_locations:
        name = loc.name.lower()
        if name == term:
            exact.append(loc)
        elif name.startswith(term):
            starts.append(loc)
        elif term in name:
            contains.append(loc)

    results = exact + starts + contains

    push(f"NAME: {term} ({len(results)} found)")  # save the search in the history stack

    print("\n[-------------------------------------------]")
    print("           [-SEARCH RESULTS-]")
    if len(results) == 0:
        print("   [-BUILDING NOT FOUND, TRY ANOTHER NAME-]")
    else:
        for loc in results:
            print(loc.display_info())
        print(f"Matches found: {len(results)}")
    print("[-------------------------------------------]\n")


def search_by_id():
    # Binary Search Algorithm
    # campus_locations is already in order by building ID, so we can keep
    # cutting the search area in half.
    text = input("\nEnter the building ID to search: ").strip()
    if not text.isdecimal():
        print("\n  [-PLEASE ENTER A WHOLE NUMBER-]\n")
        return

    target = int(text)

    low = 0
    high = len(campus_locations) - 1
    found = None

    while low <= high:
        mid = (low + high) // 2
        mid_id = campus_locations[mid].building_id
        if mid_id == target:
            found = campus_locations[mid]
            break
        elif mid_id < target:
            low = mid + 1
        else:
            high = mid - 1

    if found is not None:
        push(f"ID: {target} (found)")  # save the search in the history stack
    else:
        push(f"ID: {target} (not found)")

    print("\n[-------------------------------------------]")
    print("           [-SEARCH RESULTS-]")
    if found is not None:
        print(found.display_info())
    else:
        print("   [-BUILDING ID NOT FOUND-]")
        print(f"   Valid IDs are 1 to {len(campus_locations)}")
    print("[-------------------------------------------]\n")


def search_menu():
    while True:
        print("[-------------------------------------------]")
        print("        [-SEARCH FOR A BUILDING-]")
        print("[1] Search by name")
        print("[2] Search by ID")
        print("[3] Back")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 3]: ").strip()

        if choice == "1":
            search_by_name()
        elif choice == "2":
            search_by_id()
        elif choice == "3":
            return
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 3]-]\n")
