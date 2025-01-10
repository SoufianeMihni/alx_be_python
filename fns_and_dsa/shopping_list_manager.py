
#*OBJECTIVE: UTILIZE PYTHON LISTS TO CREATE A SIMPLE SHOPPING LIST MANAGER THAT ALLOWS USERS TO ADD ITEMS, VIEW THE CURRENT LIST, AND REMOVE ITEMS.

#* TASK DESCRIPTION:

#// CREATE A PYTHON SCRIPT NAMED SHOPPING_LIST_MANAGER.PY THAT IMPLEMENTS A SIMPLE INTERFACE FOR MANAGING A SHOPPING LIST. 
#! THIS TASK FOCUSES ON USING LISTS TO STORE AND MANIPULATE DATA DYNAMICALLY.



#// YOUR SCRIPT SHOULD START WITH AN EMPTY LIST NAMED SHOPPING_LIST.
#! IMPLEMENT FUNCTIONALITY TO ADD ITEMS TO THE LIST, REMOVE ITEMS, AND DISPLAY THE CURRENT LIST.

#* USER INTERFACE:

#// USE A LOOP TO CONTINUOUSLY DISPLAY A MENU WITH OPTIONS TO THE USER UNTIL THEY CHOOSE TO EXIT. THE MENU SHOULD OFFER OPTIONS TO ADD AN ITEM, REMOVE AN ITEM, VIEW THE LIST, AND EXIT.
#// FOR ADDING ITEMS, PROMPT THE USER FOR THE ITEM NAME AND APPEND IT TO SHOPPING_LIST.
#// FOR REMOVING ITEMS, ASK THE USER FOR THE ITEM NAME AND REMOVE IT FROM SHOPPING_LIST. IF THE ITEM IS NOT FOUND, DISPLAY A MESSAGE INDICATING SO.
#// TO VIEW THE LIST, PRINT EACH ITEM IN SHOPPING_LIST TO THE CONSOLE.
#// ENSURE YOUR SCRIPT HANDLES INVALID MENU CHOICES GRACEFULLY.


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

            
        if choice == '1':
            # Prompt for and add an item
            item = input('Enter the item to add: ')
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input('Enter the item to remove: ')
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print('This item not in your shopping list')

            pass
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()