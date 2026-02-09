# Fonction pour calculer la maintenance calorique de l'utilisateur
def calculate_bmr(weight, height, age):
    return 10 * weight + 6.25 * height - 5 * age + 5


# Fonction pour multiplier selon l'activité de l'utilisateur
def activity(activity_level):
    levels = {"low": 1.2, "medium": 1.55, "high": 1.9}
    return levels.get(activity_level.lower(), 1.2)


# Fonction pour demander à l'utilisateur si il veut prendre/perdre/gagner du poids
def adjust_goal(goal, calories):
    if goal == "lose":
        return calories - 300
    elif goal == "gain":
        return calories + 300
    return calories


# Fonction principale (qui utilise les 3 autres)
def levelUp_calculator(weight, height, age, activity_level, goal):
    bmr = calculate_bmr(weight, height, age)
    multiplier = activity(activity_level)
    maintenance = bmr * multiplier
    result = adjust_goal(goal, maintenance)
    return result
