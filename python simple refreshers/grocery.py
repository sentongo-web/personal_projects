# Function to display the menu
def display_menu():
    print("Welcome to My Grocery Shopping List")
    print("1. Add item to the list")
    print("2. Remove item from the list")
    print("3. View shopping list")
    print("4. Check if item is on the list")
    print("5. Clear shopping list")
    print("6. Exit")

# Function to add items to the shopping list
def add_item(item, shopping_list):
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

# Function to remove an item from the shopping list
def remove_item(item, shopping_list):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

# Function to view the current shopping list
def view_list(shopping_list):
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

# Function to check if an item is on the shopping list
def check_item(item, shopping_list):
    if item in shopping_list:
        print(f"Yes, {item} is on the shopping list.")
    else:
        print(f"No, {item} is not on the shopping list.")

# Function to clear the shopping list
def clear_list(shopping_list):
    shopping_list.clear()
    print("Shopping list cleared.")

# Main function to run the program
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item, shopping_list)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item, shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            item = input("Enter the item to check: ")
            check_item(item, shopping_list)
        elif choice == '5':
            clear_list(shopping_list)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
