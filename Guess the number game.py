import tkinter as tk
import random


# Game Class
class NumberGuessingGame:

    def __init__(self):

        # Window Configuration
        self.window = tk.Tk()
        #backgroun is buttercream
        self.window.title("Lucky Number Club")
        self.window.geometry("500x600")
        self.window.configure(bg="#FFF1B8")
        self.window.resizable(False, False)

        # Game Variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.high_scores = []

        # Title Label
        self.title_label = tk.Label(
            self.window,
            text="LUCKY NUMBER CLUB",
            font=("Arial", 22, "bold"),
            fg="#264653",
            bg="#FFF1B8"
        )
        self.title_label.pack(pady=25)
        
        # Star Character and Sparkles
        self.decoration = tk.Canvas(
            self.window,
            width=400,
            height=120,
            bg="#FFF1B8",
            highlightthickness=0
            )
        self.decoration.pack()
        
        #Main Cartoon Star
        self.decoration.create_polygon(
            200, 8,
            214, 40,
            248, 43,
            223, 66,
            230, 100,
            200, 83,
            170, 100,
            177, 66,
            152, 43,
            186, 40,
            fill="#FFD84D",
            outline="#264653",
            width=3
            )

        # Star's Eyes
        self.decoration.create_oval(
            187, 51, 193, 59,
            fill="#264653",
            outline=""
        )
        self.decoration.create_oval(
            207, 51, 213, 59,
            fill="#264653",
            outline=""
        )

        # Star's Smile
        self.decoration.create_arc(
            188, 53, 212, 76,
            start=200,
            extent=140,
            style="arc",
            outline="#264653",
            width=2
        )

        # Colorful Sparkles
        self.decoration.create_text(
            125, 35,
            text="✦",
            font=("Arial", 25),
            fill="#F28C8C"
        )
        self.decoration.create_text(
            275, 35,
            text="✦",
            font=("Arial", 25),
            fill="#249D8F"
        )
        self.decoration.create_text(
            145, 90,
            text="✧",
            font=("Arial", 20),
            fill="#A66DD4"
        )
        self.decoration.create_text(
            255, 90,
            text="✧",
            font=("Arial", 20),
            fill="#F28C8C"
        )
        
        # Decorative Canvas
        self.decoration = tk.Canvas(
            self.window,
            width=400,
            height=90,
            bg="#FFF1B8",
            highlightthickness=0
            )
        self.decoration.pack()
        
        #Decorative Stars
        self.decoration.create_text(
            50,30,
            text="★",
            font=("Arial", 28),
            fill="#F28C8C"
            )
        
        self.decoration.create_text(
            350, 25,
            text="★",
            font=("Arial", 28),
            fill="#2A9D8F"
            )
        
        self.decoration.create_text(
            100, 75,
            text="✦",
            font=("Arial", 20),
            fill="#264653"
            )
        
        self.decoration.create_text(
            300, 65,
            text="✦",
            font=("Arial", 20),
            fill="#F28C8C"
        )        

        # Player Input
        self.number_input = tk.Entry(
            self.window,
            font=("Arial", 18),
            fg="#264653",
            bg="white",
            insertbackground="#264653",
            justify="center",
            relief="flat",
            width=12
            )
        self.number_input.pack(pady=15, ipady=8)

        # Attempts Label
        self.attempt_label = tk.Label(
            self.window,
            text="ATTEMPTS: 0",
            font=("Arial", 14, "bold"),
            fg="#264653",
            bg="#FFF1B8"
        )
        self.attempt_label.pack(pady=15)

        # High Scores Label
        self.high_scores_label = tk.Label(
            self.window,
            text="",
            font=("Arial", 12, "bold"),
            fg="#264653",
            bg="#FFF1B8",
            justify="center"
        )

        # Guess Button
        self.submit_button = tk.Button(
            self.window,
            text="Guess",
            font=("Arial", 14, "bold"),
            fg="white",
            bg="#249D8F",
            activebackground="#238579",
            activeforeground="white",
            relief="flat",
            width=14,
            pady=8,
            command=self.check_guess
        )
        self.submit_button.pack(pady=15)

        # Enter Key Binding
        self.window.bind(
            "<Return>",
            lambda event: self.submit_button.invoke()
        )

        # Guess Feedback Label
        self.guess = tk.Label(
            self.window,
            text="Make your first guess!",
            font=("Arial", 13, "bold"),
            fg="#F28C8C",
            bg="#FFF1B8",
            wraplength=400
        )
        self.guess.pack(pady=15)


    # New Game
    def new_game(self):

        self.secret_number = random.randint(1, 100)
        
        # Reset Attempts
        self.attempts = 0

        # Reset Attempts Display
        self.attempt_label.config(text="ATTEMPTS: 0")

        # Clear Feedback
        self.guess.config(text="Make your first guess!")

        # Clear Input
        self.number_input.delete(0, tk.END)

        # Change Button Back to Guess
        self.submit_button.config(
            text="Guess",
            command=self.check_guess
        )


    # Check Guess
    def check_guess(self):

        try:
            guess = int(self.number_input.get().strip())

            self.number_input.delete(0, tk.END)

            if guess < 1 or guess > 100:

                self.guess.config(
                    text="Not a valid number, please guess 1-100"
                )

            else:

                self.attempts += 1

                self.attempt_label.config(
                    text=f"ATTEMPTS: {self.attempts}"
                )

                if guess > self.secret_number:

                    self.guess.config(
                        text="Guess is too high"
                    )

                elif guess < self.secret_number:

                    self.guess.config(
                        text="Guess is too low"
                    )

                else:

                    self.guess.config(
                        text=f"Winning number is {guess}!"
                    )

                    self.high_scores.append(self.attempts)
                    self.high_scores.sort()

                    self.update_leaderboard()

                    # Change Guess Button to New Game
                    self.submit_button.config(
                        text="New Game",
                        command=self.new_game
                    )

        except ValueError:

            self.guess.config(
                text="Please enter a number!"
            )


    # Update Leaderboard
    def update_leaderboard(self):

        leaderboard = "🏆 HIGH SCORES 🏆\n\n"

        for place, score in enumerate(self.high_scores, start=1):

            if place == 1:
                suffix = "st"
            elif place == 2:
                suffix = "nd"
            elif place == 3:
                suffix = "rd"
            else:
                suffix = "th"

            leaderboard += (
                f"{place}{suffix} Place: {score} guesses\n"
            )

        self.high_scores_label.config(text=leaderboard)
        self.high_scores_label.pack(pady=10)


    # Run Window
    def run(self):

        self.window.mainloop()


# Start Application
app = NumberGuessingGame()
app.run()
