import src.exctractRegistered as exctractRegistered

ended = False

while not ended:
    print("What do you want to do ?")
    print("1. Add an item")
    print("2. See the list of items")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        print("Feature not implemented yet.")
    elif choice == "2":
        exctractRegistered.PrintItems()
    elif choice == "3":
        ended = True
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
