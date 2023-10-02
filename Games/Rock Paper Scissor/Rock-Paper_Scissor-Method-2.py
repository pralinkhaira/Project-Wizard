# Import necessary libraries
import random
import tkinter

# Initialize a list to store game statistics (Wins, Draws, Losses)
stats = []

# Define a function to determine the winner of a game round
def get_winner(call):
    # Generate a random choice for the computer (Rock, Paper, or Scissors)
    if random.random() <= (1 / 3):
        throw = "rock"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw = "scissors"
    else:
        throw = "paper"

    # Determine the game result and update the stats list
    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") \
            or (throw == "scissors" and call == "rock"):
        stats.append('W')  # Player wins
        result = "You won!"
    elif throw == call:
        stats.append('D')  # It's a draw
        result = "It's a draw"
    else:
        stats.append('L')  # Player loses
        result = "You lost!"

    # Update the output label in the GUI window
    global output
    output.config(text="Computer did: " + throw + "\n" + result)

# Define functions for the Scissors, Rock, and Paper buttons
def pass_s():
    get_winner("scissors")

def pass_r():
    get_winner("rock")

def pass_p():
    get_winner("paper")

# Create the main window using tkinter
window = tkinter.Tk()

# Create buttons for Scissors, Rock, and Paper
scissors = tkinter.Button(window, text="Scissors", bg="#ff9999", padx=10, pady=5, command=pass_s, width=20)
rock = tkinter.Button(window, text="Rock", bg="#80ff80", padx=10, pady=5, command=pass_r, width=20)
paper = tkinter.Button(window, text="Paper", bg="#3399ff", padx=10, pady=5, command=pass_p, width=20)

# Create an output label
output = tkinter.Label(window, width=20, fg="red", text="What's your call?")

# Pack the buttons and label in the window
scissors.pack(side="left")
rock.pack(side="left")
paper.pack(side="left")
output.pack(side="right")

# Start the GUI event loop
window.mainloop()

# After the game ends, print the game statistics and series result
for i in stats:
    print(i, end=" ")

if stats.count('L') > stats.count('W'):
    result = "\nYou lose the series."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou win the series."

print(result)
