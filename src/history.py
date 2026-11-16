# NAVIGATION HISTORY - Stack (LIFO: Last In, First Out) built on a Linked List
# The HEAD of the linked list is the TOP of the stack, so the newest search
# is always the first node. push = add at the head, pop = remove the head.

from linked_list import LinkedList

history_stack = LinkedList()


def push(term):
    # Put a new search on top of the stack
    history_stack.push_front(term)


def pop():
    # Take the top (newest) search off the stack
    # Returns None if the stack is empty
    return history_stack.pop_front()


def is_empty():
    return history_stack.is_empty()


def view_history():
    # Walk the chain from the head (newest) to the end (oldest) without removing anything
    print("\n[-------------------------------------------]")
    print("        [-NAVIGATION HISTORY-]")
    if is_empty():
        print("       [-NO SEARCH HISTORY FOUND-]")
    else:
        number = 1
        current = history_stack.head
        while current is not None:
            print(f"{number}. {current.data}")
            number += 1
            current = current.next
        print(f"Total searches: {history_stack.size}")
    print("[-------------------------------------------]\n")


def remove_latest():
    removed = pop()
    print("\n[-------------------------------------------]")
    if removed is None:
        print("       [-NOTHING TO REMOVE-]")
    else:
        print(f"  [-REMOVED MOST RECENT SEARCH: {removed}-]")
    print("[-------------------------------------------]\n")


def clear_history():
    # Pop until the stack is empty
    count = 0
    while not is_empty():
        pop()
        count += 1
    print("\n[-------------------------------------------]")
    if count == 0:
        print("       [-NOTHING TO CLEAR-]")
    else:
        print(f"  [-CLEARED {count} SEARCH(ES)-]")
    print("[-------------------------------------------]\n")


def history_menu():
    while True:
        print("[-------------------------------------------]")
        print("        [-NAVIGATION HISTORY-]")
        print("[1] View history (newest first)")
        print("[2] Remove most recent search")
        print("[3] Clear all history")
        print("[4] Back")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 4]: ").strip()

        if choice == "1":
            view_history()
        elif choice == "2":
            remove_latest()
        elif choice == "3":
            clear_history()
        elif choice == "4":
            return
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 4]-]\n")