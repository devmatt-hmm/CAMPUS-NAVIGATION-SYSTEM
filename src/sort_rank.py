# DIRECTORY SORT / RANK - Bubble Sort, Insertion Sort, Selection Sort
# Every sort works on a COPY of campus_locations, so the original list stays
# in order by ID (Binary Search by ID needs that).

from database import campus_locations
from stats import get_categories


def get_key(loc, key_type):
    # The value we compare: building name (A-Z), building ID, or category
    # Category ties are broken by name so every sort gives the same result.
    if key_type == "name":
        return loc.name.lower()
    if key_type == "category":
        return (loc.category.lower(), loc.name.lower())
    return loc.building_id


def bubble_sort(items, key_type):
    # Compare neighbors and swap them if they are in the wrong order
    n = len(items)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if get_key(items[j], key_type) > get_key(items[j + 1], key_type):
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp


def insertion_sort(items, key_type):
    # Take one item at a time and insert it into its place in the sorted part
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and get_key(items[j], key_type) > get_key(current, key_type):
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current


def selection_sort(items, key_type):
    # Find the smallest item in the unsorted part and move it to the front
    n = len(items)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if get_key(items[j], key_type) < get_key(items[smallest], key_type):
                smallest = j
        temp = items[i]
        items[i] = items[smallest]
        items[smallest] = temp


def sort_buildings():
    print("\n[-------------------------------------------]")
    print("          [-SORT THE DIRECTORY-]")
    print("Sort by:")
    print("[1] Name (A - Z)")
    print("[2] Building ID")
    print("[3] Category (then name)")
    print("[-------------------------------------------]\n")
    key_choice = input("Select an option [1 - 3]: ").strip()
    if key_choice == "1":
        key_type = "name"
        label = "NAME (A - Z)"
    elif key_choice == "2":
        key_type = "id"
        label = "BUILDING ID"
    elif key_choice == "3":
        key_type = "category"
        label = "CATEGORY"
    else:
        print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 3]-]\n")
        return

    print("\nSorting method:")
    print("[1] Bubble Sort")
    print("[2] Insertion Sort")
    print("[3] Selection Sort")
    method = input("Select an option [1 - 3]: ").strip()

    items = campus_locations.copy()  # sort a copy, keep the original in order

    if method == "1":
        bubble_sort(items, key_type)
        method_name = "BUBBLE SORT"
    elif method == "2":
        insertion_sort(items, key_type)
        method_name = "INSERTION SORT"
    elif method == "3":
        selection_sort(items, key_type)
        method_name = "SELECTION SORT"
    else:
        print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 3]-]\n")
        return

    print("\n[-------------------------------------------]")
    print(f"  [-SORTED BY {label} USING {method_name}-]")
    for loc in items:
        print(loc.display_info())
    print("[-------------------------------------------]\n")


def rank_categories():
    # Rank the categories from most buildings to fewest.
    # Two parallel arrays (names and counts) are sorted together with
    # Insertion Sort. Categories with the same count stay in their original order.
    names = get_categories()
    counts = []
    for cat in names:
        count = 0
        for loc in campus_locations:
            if loc.category == cat:
                count += 1
        counts.append(count)

    for i in range(1, len(names)):
        cur_name = names[i]
        cur_count = counts[i]
        j = i - 1
        while j >= 0 and counts[j] < cur_count:
            names[j + 1] = names[j]
            counts[j + 1] = counts[j]
            j -= 1
        names[j + 1] = cur_name
        counts[j + 1] = cur_count

    print("\n[-------------------------------------------]")
    print("    [-CATEGORIES RANKED BY BUILDING COUNT-]")
    for i in range(len(names)):
        word = "building" if counts[i] == 1 else "buildings"
        print(f"#{i + 1} {names[i]}: {counts[i]} {word}")
    print("[-------------------------------------------]\n")


def sort_rank_menu():
    while True:
        print("[-------------------------------------------]")
        print("        [-DIRECTORY SORT / RANK-]")
        print("[1] Sort the directory")
        print("[2] Rank categories by building count")
        print("[3] Back")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 3]: ").strip()

        if choice == "1":
            sort_buildings()
        elif choice == "2":
            rank_categories()
        elif choice == "3":
            return
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 3]-]\n")
