def user_info():
    
    print("To create a specific programme for you, please fill in the following information:")

   
    name = str(input(" Name: "))
        

    surname = input(" Surname: ")
        

    while True:
        try:
            age = int(input("Age: "))
            if 6 <= age <= 100:
                break
            print("Age must be between 10 and 100.")
        except:
            print(" Please enter a number.")

    while True:
        gender = input("Gender (male/female): ")
        if gender in ["male", "female"]:
            break
        print(" Please enter 'male' or 'female'.")

    
    while True:
        try:
            weight = float(input("Weight (kg): "))
            if weight > 20:
                break
            print(" Weight must be positive.")
        except:
            print(" Please enter a number.")

    
    while True:
        try:
            height = float(input("Height (cm): "))
            if height > 110:
                break
            print(" Height must be realistic.")
        except:
            print(" Please enter a number.")

    print("\n Profile created successfully!\n")

    while True:
        goal = input("Goal (lose / gain / maintain): ")
        if goal in ["lose", "gain", "maintain"]:
            break
        print(" Choose: lose, gain or maintain.")

    # Activity level
    while True:
        activity_level = input("Activity level (low / medium / high): ")
        if activity_level in ["low", "medium", "high"]:
            break
        print(" Choose: low, medium or high.")

    return name, surname, age, gender, weight, height, goal, activity_level
