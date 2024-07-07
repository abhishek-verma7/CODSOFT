#ROCK PAPER SCISSOR GAME
import tkinter as tk
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result, user_point, computer_point = determine_winner(user_choice, computer_choice)
    user_score += user_point
    computer_score += computer_point
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}", fg="#333")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}", fg="#333")
    play_again_button.pack(pady=10)

def on_choice(user_choice):
    play_game(user_choice)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="", fg="#0096DC")
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}", fg="#0096DC")
    play_again_button.pack_forget()


user_score = 0
computer_score = 0


root = tk.Tk()
root.title("Rock-Paper-Scissors Game") 
root.configure(background='#FFD700')  


label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=('Arial', 18), bg='#FFD700', fg='#333333')
label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", width=10, command=lambda: on_choice('Rock'), bg='#6495ED', fg='white', font=('Arial', 12)) 
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: on_choice('Paper'), bg='#6495ED', fg='white', font=('Arial', 12))  
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: on_choice('Scissors'), bg='#6495ED', fg='white', font=('Arial', 12))  
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=('Arial', 16), bg='#FFD700', fg='#0096DC')  
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Score - You: {user_score}  Computer: {computer_score}", font=('Arial', 16), bg='#FFD700', fg='#333333') 
score_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", width=10, command=reset_game, bg='#6495ED', fg='white', font=('Arial', 12))  
play_again_button.pack()

root.mainloop()
