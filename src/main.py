# CAMPUS NAVIGATION SYSTEM - main menu
# Each option calls a function from its own file:
#   search.py      - Building Search       (Linear Search, Binary Search)
#   history.py     - Navigation History    (Stack on a Linked List)
#   stats.py       - Building Stats/Filter (Arrays, Linked List grouping)
#   sort_rank.py   - Directory Sort/Rank   (Bubble, Insertion, Selection Sort)
#   route.py       - Route Planning        (Queue, Stack)
#   linked_list.py - shared Linked List used by history.py and stats.py

from database import check_database
from search import search_menu
from history import history_menu
from stats import stats_menu
from sort_rank import sort_rank_menu
from route import plan_route


def main_menu():
    while True:
        print("[-------------------------------------------]")
        print("      [-CAMPUS NAVIGATION SYSTEM-]")
        print("[1] Search for a Building")
        print("[2] View Navigation History")
        print("[3] Building Stats / Filter")
        print("[4] Directory Sort / Rank")
        print("[5] Plan a Route")
        print("[6] Exit")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 6]: ").strip()

        if choice == "1":
            search_menu()
        elif choice == "2":
            history_menu()
        elif choice == "3":
            stats_menu()
        elif choice == "4":
            sort_rank_menu()
        elif choice == "5":
            plan_route()
        elif choice == "6":
            print("EXITING SYSTEM...")
            break
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 6]-]\n")


if __name__ == "__main__":
    # Make sure the building list and road data are valid before starting
    problems = check_database()
    if len(problems) > 0:
        print("[-DATABASE PROBLEM(S) FOUND-]")
        for problem in problems:
            print(f"  - {problem}")
        print("Fix database.py and run again.")
    else:
        main_menu()