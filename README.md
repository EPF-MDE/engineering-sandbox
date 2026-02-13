🥗 Level Up – Calorie Calculator (Python)

Level Up is a small Python program that helps users calculate how many calories they need per day to lose, gain, or maintain weight.

The program asks the user for personal information (age, weight, height, activity level, goal) and then calculates the daily calorie needs.

📁 Project Structure

calculator.py → contains the calorie calculation functions

user_id_function.py → asks the user for information

main.py → runs the program

⚙️ How It Works

The program uses 3 main steps:

Calculate BMR (Basal Metabolic Rate)
This is the number of calories your body needs at rest.

Apply Activity Level
The calories are multiplied depending on how active the user is:

low

medium

high

Adjust for the Goal

Lose weight → −300 calories

Gain weight → +300 calories

Maintain weight → no change

▶️ How to Run

Make sure you have Python 3 installed.

Put all files in the same folder.

Run the program:

python main.py


Answer the questions in the terminal.

🧮 Formula Used

The program uses this formula to calculate BMR:

BMR = 10 × weight + 6.25 × height − 5 × age + 5


Then it multiplies by the activity level and adjusts for the goal.

💬 Example
Welcome to Level Up !
We will help you to achieve your desire physique

Name: John
Surname: Doe
Age: 25
Gender: male
Weight (kg): 70
Height (cm): 175
Goal (lose / gain / maintain): lose
Activity level (low / medium / high): medium

Your daily calorie needs to lose weight is: 2200.50 calories.

✅ Features

Simple user input

Input validation (age, weight, height, goal, activity)

Clear calorie result

Easy to understand code

🚀 Goal of the Project

This project is made for learning Python basics:

Functions

Conditions

Loops

User input

Working with multiple files