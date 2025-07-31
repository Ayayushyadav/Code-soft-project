import tkinter as tk
import random

# choice list
choices = ["rock", "paper", "scissors" ]

# determine the winner
def determine_winner (player, computer):
    if player == computer:
        return "it's a tie !"
    elif(
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")

    ):
        return "you win !"
    else:
        return "computer win !"

# hamdle user's choice
def play (player_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice,computer_choice)
    result_label.config(text=f"computer choice: {computer_choice}\n {result}")

#create window
root = tk.Tk()
root.title("Rook paper scissors")

#title
title_label = tk.Label(root, text="Rook, paper, scissors", font=("arial, 20"))
title_label.pack(pady=10)

#Buttons
button_frame = tk.Frame(root)
button_frame.pack()


for choice in choices:
    btn = tk.Button(button_frame, text=choice, width=10, font=("Arial", 14),
                    command=lambda c=choice: play(c))
    btn.pack(side=tk.LEFT, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 16), pady=20)
result_label.pack()

#start the GUI Eevent loop
root.mainloop()

    
