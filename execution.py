from calculator import *
from levelUp import *
from user_id_function import *


def main():
    name, surname, age, gender, weight, height, goal, activity_level = user_info()
    calories = levelUp_calculator(weight, height, age, activity_level, goal)
    print(f"\nYour daily calorie needs to {goal} weight is: {calories:.2f} calories.")
