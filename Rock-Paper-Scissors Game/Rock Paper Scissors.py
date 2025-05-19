import random

options = ["Rock", "Paper", "Scissors"]

game = {
    ("Scissors", "Paper"): "You Win",
    ("Rock", "Scissors"): "You Win",
    ("Paper", "Rock"): "You Win",
    ("Rock", "Paper"): "You Lose",
    ("Paper", "Scissors"): "You Lose",
    ("Scissors", "Rock"): "You Lose",
}

win_streak = 0

while True:
    choice = random.choice(options)

    while True:
        user_input = input("Enter your Choice \n(Type Exit to quit)\nRock, Paper, Scissors : ")
        user_input = user_input.title()
        if user_input == "Exit" or user_input in options:
            break
        else:
            print("Enter a valid Input.")

    print("Your Pick :",user_input,"\n","Computer's Pick :", choice)

    if user_input == "Exit":
        break
    elif user_input == choice:
        print("Draw")
    else:
        result = game.get((user_input, choice), "Invalid Input")
        print(result)

        if result == "You Win":
            win_streak += 1

        elif result == "You Lose":
            win_streak = 0

    print("Your Win Streak =>", win_streak)