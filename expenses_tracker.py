# Voici le code à réaliser pour le projet de suivi des dépenses personnelles en Python. Ce code permet de suivre les dépenses, de les catégoriser.
# Projet de suivi des dépenses personnelles avec dictionnaire

expenses = {
    "F": [],  # Food
    "D": [],  # Divertissement
    "T": []   # Taxes
}

compte = 0

while True:
    user_choice_expenses = input("Which category would you like to record your expense in? (F : Food | D : Divertissement | T : Taxes) : ").upper()

    if user_choice_expenses in expenses:
        compte += 1
        user_price = int(input("How much '€' is your expenses ? "))
        expenses[user_choice_expenses].append(user_price)
    else:
        print("Error, please try again with only the values 'F' or 'D' or 'T")

    choice_user = input("Do you want to exit your dashboard? (Y | N) ").upper()

    if choice_user == "Y":
        total_expenses = sum(expenses["F"]) + sum(expenses["D"]) + sum(expenses["T"])

        print(f"\nYour Dashboard (You have {compte} expenses):")
        print("Food expenses:", sum(expenses["F"]))
        print("Divertissement expenses:", sum(expenses["D"]))
        print("Taxes expenses:", sum(expenses["T"]))

        if total_expenses > 0:
            print("\nBreakdown of expenses :")
            print("Food :", (sum(expenses["F"]) / total_expenses) * 100, "%")
            print("Divertissement :", (sum(expenses["D"]) / total_expenses) * 100, "%")
            print("Taxes :", (sum(expenses["T"]) / total_expenses) * 100, "%")
        else:
            print("No expenses recorded.")

        break
