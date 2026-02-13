from calculator import level_up_calculator
from user_id_function import user_info


def main():

    print("Welcome to Level Up !")
    print("We will help you to achieve your desire physique")

    name, surname, age, gender, weight, height, goal, activity_level = user_info()

    calories = level_up_calculator(weight, height, age, activity_level, goal)

    print(f"\nYour daily calorie needs to {goal} weight is: {calories:.2f} calories.")
