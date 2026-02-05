# Voici le code à réaliser pour le projet de suivi des dépenses personnelles en Python. Ce code permet de suivre les dépenses, de les catégoriser.
list_expenses_Food =[]
list_expenses_Divertissement =[]
list_expenses_Taxes =[]
user_choice = input(str("Dans quelle catégorie souhaitez-vous enregistrer votre dépense ? (F : Food | D : Divertissement | T : Taxes) : "))

if user_choice == "F":
    user_price_F = input(int("Combien d'€ est votre dépense ? :"))
    list_expenses_Food.append(user_price_F)

elif user_choice == "D":
    user_price_D = input(int("Combien d'€ est votre dépense ? :"))
    list_expenses_Food.append(user_price_D)

elif user_choice == "T":
    user_price_T = input(int("Combien d'€ est votre dépense ? :"))
    list_expenses_Food.append(user_price_T)
else:
    print("Error")

print("Voici à présent vos dépenses actuelles: \n", sum(list_expenses_Food) + sum(list_expenses_Divertissement) + sum(list_expenses_Taxes))