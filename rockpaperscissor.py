import tkinter as tk 
import random 

class RockPaperScissorsGame:
    def __init__(self, root): 
        self.root = root 
        self.root.title("Rock-Paper-scissors Game") 

        self.user_score = 0
        self.computer_score = 0

        self.choices = ['rock', 'paper', 'scissors']

        self.user_choice_label = tk.Label(root, text="Your choice:")
        self.user_choice_label.pack()

        self.user_choice_var = tk.StringVar()
        self.user_choice_entry = tk.Entry(root, textvariable=self.user_choice_var)
        self.user_choice_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(root, text="")
        self.score_label.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!" 
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'): 
            self.user_score += 1
            return "You win!" 
        else: 
            self.computer_score += 1
            return "You lose!" 

    def play(self): 
        user_choice = self.user_choice_var.get().lower()

        if user_choice not in self.choices: 
            self.result_label.config(text="Invalid choice! please choose rock, paper, or scissors.")
            return 

        computer_choice = random.choice(self.choices) 

        result = self. determine_winner(user_choice,computer_choice)

        self.result_label.config(text=f"computer chooses: {computer_choice}\n{result}")
        self.score_label.config(text=f"Your score: {self.user_score}, Computer's score: {self.computer_score}")

if __name__ =="__main__": 
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
