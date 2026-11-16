# BUILDING STATS / FILTER - Array counting, linear filtering, Linked List grouping

from database import campus_locations
from linked_list import LinkedList


def get_categories():
    # Build a list of each category once (no repeats)
    categories = []
    for loc in campus_locations:
        if loc.category not in categories:
            categories.append(loc.category)
    return categories


def count_per_category():
    categories = get_categories()
    print("\n[-------------------------------------------]")
    print("       [-BUILDING COUNT PER CATEGORY-]")
    for cat in categories:
        count = 0
        for loc in campus_locations:
            if loc.category == cat:
                count += 1
        print(f"{cat}: {count}")
    print(f"Total buildings: {len(campus_locations)}")
    print("[-------------------------------------------]\n")


def filter_by_category():
    categories = get_categories()
    print("\nAVAILABLE CATEGORIES:", ", ".join(categories))
    cat_input = input("Enter category to filter: ").strip()
    if cat_input == "":
        print("\n  [-CATEGORY CANNOT BE EMPTY-]\n")
        return

    matches = []
    for loc in campus_locations:
        if loc.category.lower() == cat_input.lower():
            matches.append(loc)

    print("\n[-------------------------------------------]")
    if len(matches) > 0:
        print(f"     [-BUILDINGS UNDER {cat_input.upper()}-]")
        for loc in matches:
            print(loc.display_info())
        print(f"Total: {len(matches)}")
    else:
        print(f"   [-NO BUILDINGS FOUND UNDER CATEGORY '{cat_input}'-]")
    print("[-------------------------------------------]\n")


def group_by_category():
    # One Linked List per category. Each building is added to the end of its
    # category's chain, then every chain is walked from head to tail.
    categories = get_categories()
    groups = []                       # array: groups[i] is the chain for categories[i]
    for cat in categories:
        groups.append(LinkedList())

    for loc in campus_locations:
        for i in range(len(categories)):
            if loc.category == categories[i]:
                groups[i].append(loc)
                break

    print("\n[-------------------------------------------]")
    print("      [-BUILDINGS GROUPED BY CATEGORY-]")
    for i in range(len(categories)):
        print(f"{categories[i]} ({groups[i].size})")
        current = groups[i].head
        while current is not None:
            print(f"   -> {current.data.display_info()}")
            current = current.next
    print("[-------------------------------------------]\n")


def stats_menu():
    while True:
        print("\n[-------------------------------------------]")
        print("   [-BUILDING STATS / FILTER BY CATEGORY-]")
        print("[1] View building count per category")
        print("[2] Filter buildings by category")
        print("[3] View buildings grouped by category")
        print("[4] Back")
        print("[-------------------------------------------]\n")

        # The choice is read as text (not int) so typing letters cannot crash the program
        choice = input("Select an option [1 - 4]: ").strip()

        if choice == "1":
            count_per_category()
        elif choice == "2":
            filter_by_category()
        elif choice == "3":
            group_by_category()
        elif choice == "4":
            return
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 4]-]\n")