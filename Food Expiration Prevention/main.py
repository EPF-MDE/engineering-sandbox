import src.registered_items as registered_items
import src.modify_items as modify_items

ended = False

while not ended:
    print("What do you want to do ?")
    print("1. Add an item")
    print("2. See the list of items")
    print("3. Delete an item")
    print("4. Exit")
    choice = input("Enter your choice (1, 2, 3 or 4): ")
    if choice == "1":
        modify_items.RegisterNewProduct()
    elif choice == "2":
        registered_items.PrintItems()
    elif choice == "3":
        modify_items.DeleteExistingProduct()
    elif choice == "4":
        ended = True
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
