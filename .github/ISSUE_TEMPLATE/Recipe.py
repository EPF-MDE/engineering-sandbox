choice = int(
    input(
        "Hello, do you need ingredients for a recipe [1] or a recipe for your ingredients [2] ?  \n>>  "
    )
)

if choice == 1:
    user_recette = input("What dish would you like to cook today ?  \n>>  ")

    liste_recette = [
        ["Tiramisu", "Mascarpone", "Oeufs"],
        ["Bolognaise", "Pâtes", "Sauce tomate"],
        ["Poulet", "Filet de poulet", "Paprika"],
    ]

    for recette in liste_recette:
        if user_recette == recette[0]:
            print(f"Here is the list of ingredient: {recette[1]}")
            condition = True
            break
        else:
            condition = False

    if condition == False:
        print("That recipe does not exist")

if choice == 2:
    print("zob")
user_ingredient = input("What would you like to cook today ? /n >>  ")
