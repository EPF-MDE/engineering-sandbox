# Voici le code à réaliser pour le projet de suivi des dépenses personnelles en Python. Ce code permet de suivre les dépenses, de les catégoriser.
list_expenses_Food =[]
list_expenses_Divertissement =[]
list_expenses_Taxes =[]
user_choice_expenses = 0
total_expenses = 0
choice_user = 0
compte = 0

while(True):
    user_choice_expenses = str(input("Dans quelle catégorie souhaitez-vous enregistrer votre dépense ? (F : Food | D : Divertissement | T : Taxes) : "))
    if user_choice_expenses == "F":
        compte = compte +1
        user_price_F = int(input("Combien d'€ est votre dépense ? "))
        list_expenses_Food.append(user_price_F)

    elif user_choice_expenses == "D":
        compte = compte +1
        user_price_D = int(input("Combien d'€ est votre dépense ? "))
        list_expenses_Divertissement.append(user_price_D)

    elif user_choice_expenses == "T":
        compte = compte +1
        user_price_T = int(input("Combien d'€ est votre dépense ? "))
        list_expenses_Taxes.append(user_price_T)

    else:
        print("Error")
    choice_user = str(input("Vous voulez quittez votre dashboard ? (Y | N)"))
    if choice_user == "Y":
        total_expenses = sum(list_expenses_Food) + sum(list_expenses_Divertissement) + sum(list_expenses_Taxes)
        print(f"Your Dashboard (You are {compte} expenses): \n","Food expenses: ", sum(list_expenses_Food), "\n","Divertissment expenses :",sum(list_expenses_Divertissement), "\n", "Taxes expenses :", sum(list_expenses_Taxes))
        print("Here is the expenses proportional :", sum(list_expenses_Food)/total_expenses, "%","of food,", sum(list_expenses_Divertissement)/total_expenses, "%","of divertissment,", sum(list_expenses_Taxes)/total_expenses, "%","of taxes.")
        break