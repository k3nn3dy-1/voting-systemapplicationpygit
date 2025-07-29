import json

# Store candidates in a dictionary by position
candidates = {}

def add_candidate():
    name = input("Enter candidate's full name: ").title()
    position = input("Enter position (e.g., President, Secretary, Treasurer): ").title()

    if position not in candidates:
        candidates[position] = []

    candidates[position].append(name)
    print(f"{name} has been nominated for {position}.\n")

def view_candidates():
    if not candidates:
        print("No recent nominations yet.\n")
        return

    print("Nominated Candidates by Position:")
    for position, names in candidates.items():
        print(f"\n{position}:")
        for i, name in enumerate(names, 1):
            print(f"  {i}. {name}")
    print()

def search_candidate():
    search_name = input("Enter name to search: ").title()
    found = False
    for position, names in candidates.items():
        if search_name in names:
            print(f"{search_name} is nominated for {position}.\n")
            found = True
    if not found:
        print(f"{search_name} not found in nominations.\n")

def delete_candidate():
    name = input("Enter candidate's full name to delete: ").title()
    for position in candidates:
        if name in candidates[position]:
            candidates[position].remove(name)
            print(f"{name} has been removed from the nominations for {position}.\n")
            return
    print(f"{name} not found in any nomination.\n")

def save_to_file():
    with open("nominations.json", "w") as file:
        json.dump(candidates, file, indent=4)
    print("Nominations saved to 'nominations.json'.\n")

def menu():
    while True:
        print("=== UNIVERSITY COUNCIL NOMINATION SYSTEM ===")
        print("1. Add Candidate")
        print("2. View Nominated Candidates")
        print("3. Search Candidate")
        print("4. Delete Candidate")
        print("5. Save and Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_candidate()
        elif choice == '2':
            view_candidates()
        elif choice == '3':
            search_candidate()
        elif choice == '4':
            delete_candidate()
        elif choice == '5':
            save_to_file()
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
