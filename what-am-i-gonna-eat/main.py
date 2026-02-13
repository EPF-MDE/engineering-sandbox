import pandas as pd

recette_table = pd.read_csv("what-am-i-gonna-eat//recettes.csv", sep=";")

choice = int(
    input(
        "Hello, do you need ingredients for a recipe [1] or a recipe for your ingredients [2] ?  \n>>  "
    )
)

if choice == 1:
    user_recette = input("What dish would you like to cook today ?  \n>>  ")
    recette_index = 0

    for idx, recette in recette_table.iterrows():
        if user_recette == recette["nom_recette"]:
            print(f"Here is the list of ingredient: {recette['ingredients']}")
            condition = True
            break
        else:
            condition = False

    if not condition:
        print("That recipe does not exist")

if choice == 2:
    # use .countains('ingredient')
    print("Not implemented yet, sorry")
