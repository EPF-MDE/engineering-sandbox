import pandas as pd

recette_table = pd.read_csv("Recipe//recettes.csv", sep=";")

choice = int(
    input(
        "Hello, do you need ingredients for a recipe [1] or a recipe for your ingredients [2] ?  \n>>  "
    )
)

if choice == 1:
    user_recette = input("What dish would you like to cook today ?  \n>>  ")

    for recette in recette_table["nom_recette"]:
        if user_recette == recette:
            print("Here is the list of ingredient:")
            condition = True
            break
        else:
            condition = False

    if not condition:
        print("That recipe does not exist")

if choice == 2:
    # use .countains('ingredient')
    print("Not implemented yet, sorry")
