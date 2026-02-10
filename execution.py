from calculator import *
from levelUp import *
from user_id_function import *

def main():
    user_info()
    calories = levelUp_calculator(weight, height, age, activity_level, goal)
    print(f"\nYour daily calorie needs to {goal} weight is: {calories:.2f} calories.")