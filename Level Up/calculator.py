# Function to calculate the user's caloric maintenance
def calculate_bmr(weight, height, age):

    return 10 * weight + 6.25 * height - 5 * age + 5


# Function to multiply according to user activity
def activity(activity_level):

    levels = {"low": 1.2, "medium": 1.55, "high": 1.9}

    return levels.get(activity_level.lower(), 1.2)


# Function to ask the user if they want to gain/lose/maintain weight
def adjust_goal(goal, calories):

    if goal == "lose":
        return calories - 300

    elif goal == "gain":
        return calories + 300

    return calories


# Principal function (using 3 others)
def level_up_calculator(weight, height, age, activity_level, goal):

    bmr = calculate_bmr(weight, height, age)
    multiplier = activity(activity_level)
    maintenance = bmr * multiplier

    result = adjust_goal(goal, maintenance)

    return result
