import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result, user_point, computer_point = determine_winner(user_choice, computer_choice)
    user_score += user_point
    computer_score += computer_point
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def on_choice(user_choice):
    play_game(user_choice)

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

label = tk.Label(root, text="Choose rock, paper, or scissors:")
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: on_choice('rock'))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: on_choice('paper'))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: on_choice('scissors'))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Score - You: {user_score}  Computer: {computer_score}")
score_label.pack(pady=10)

root.mainloop()
