import random

print("===== ROCK PAPER SCISSORS =====")

choices = ["rock", "paper", "scissors"]

user = input("Choose rock, paper or scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("It's a Tie!")
elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("You Win!")
else:
    print("You Lose!")