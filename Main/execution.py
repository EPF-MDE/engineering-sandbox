from calculator import *
from user_id_function import *


def main():
    print("Welcome to Level Up !")
    print("We will help you to achieve your desire physique")
    name, surname, age, gender, weight, height, goal, activity_level = user_info()
    calories = levelUp_calculator(weight, height, age, activity_level, goal)
    print(f"\nYour daily calorie needs to {goal} weight is: {calories:.2f} calories.")
