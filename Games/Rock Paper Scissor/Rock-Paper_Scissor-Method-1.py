# Import the random module to generate a random choice for player 2
import random

# Get input from player 1, converting it to lowercase to ensure case insensitivity
player1 = input("Select Rock, Paper, or Scissor: ").lower()

# Generate a random choice for player 2 (Rock, Paper, or Scissor) and convert it to lowercase
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()

# Print player 2's selection
print("Player 2 selected: ", player2)

# Check the game outcomes
if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won")
