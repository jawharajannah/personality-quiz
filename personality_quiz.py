import tkinter as tk
from tkinter import *

class PersonalityQuiz:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()

        self.scores = {colour: 0 for colour in self.get_colour_list()}
        self.current_question_index = 0

        self.questions = self.load_questions()
        self.colour_data = self.load_colour_data()

        self.show_welcome_screen()

    def setup_window(self):
        self.root.title("What is your personality colour?")
        self.root.geometry("600x600")
        self.root.configure(bg="ghost white")
        self.root.resizable(False, False)

    def get_colour_list(self):
        return ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink"]

    def load_questions(self):
        return [
            {
            "question": "Which number do you prefer?",
            "answers": {
                "5": ["Red", "Orange"],
                "3": ["Yellow", "Green"],
                "19": ["Blue"],
                "4": ["Pink", "Purple"]
                }
            },
            {
            "question": "What is your favourite season?",
            "answers": {
                "Spring": ["Orange", "Yellow", "Green", "Blue"],
                "Winter": ["Pink"],
                "Autumn": ["Purple"],
                "Summer": ["Red"]
                }
            },
            {
            "question": "What would you choose in a bake sale?" ,
            "answers": {
                "Cookie": ["Yellow", "Blue"],
                "Cupcake": ["Green", "Purple"],
                "Brownie": ["Orange"],
                "Doughnut": ["Red", "Pink"],
                }
            },
            {
            "question": "What is your favourite flower?" ,
            "answers": {
                "Rose": ["Red", "Pink", "Purple"],
                "Tulip": ["Orange", "Blue"],
                "Sunflower": ["Yellow"],
                "Daisy": ["Green"],
                }
            },
            {
            "question": "Which planet is the best?",
            "answers": {
                "Earth": ["Green", "Pink"],
                "Neptune": ["Red", "Purple"],
                "Saturn": ["Orange", "Yellow"],
                "Jupiter": ["Blue"],
                }
            },
        ]
    
    def load_colour_data(self):
        return {
            "Red": {
                "description": "optimistic, social, and confident",
                "display_colour": "orange red"
            },
            "Orange": {
                "description": "energetic, optimistic, and joyful",
                "display_colour": "dark orange"
            },
            "Yellow": {
                "description": "social, joyful, and enthusiastic",
                "display_colour": "goldenrod1"
            },
            "Green": {
                "description": "practical, peaceful, and intelligent",
                "display_colour": "forest green"
            },
            "Blue": {
                "description": "accepting, humble, and peaceful",
                "display_colour": "RoyalBlue1"
            },
            "Purple": {
                "description": "mysterious, compassionate, and artistic",
                "display_colour": "medium orchid"
            },
            "Pink": {
                "description": "calm, kind, and confident",
                "display_colour": "hot pink"
            }
        }
    
    def create_button(self, parent, text, command, **kwargs):
        defaults = {
            'width': 15, 
            'height': 2,
            'font': ("Comfortaa", 16),
            'borderwidth': 2, 
            'relief': "ridge"
        }
        defaults.update(kwargs)
        
        button = tk.Button(parent, text=text, **defaults)
        button.config(command=command)

        return button
    
    def add_exit_button(self, parent_frame):
        exit_button = self.create_button(
            parent_frame, "Exit", 
            command=self.show_goodbye,
            width=8, font=("Comfortaa", 12)
        )
        exit_button.pack(side="left", padx=5)
    
    def start_quiz(self):
        self.clear_screen()
        self.current_question_index = 0
        self.show_question(self.current_question_index)

    def show_question(self, index):
        self.clear_screen()
        current = self.questions[index] 
            
        progress_frame = tk.Frame(self.root, bg="ghost white")
        progress_frame.pack()
        
        progress_text = tk.Label(
            progress_frame, text=f"Question {self.current_question_index + 1} of {len(self.questions)}", fg="black", bg="ghost white", font=("Comfortaa", 12)
        )
        progress_text.pack(pady=12)
        
        question_label = tk.Label(
            self.root, text=current["question"], fg="black", bg="ghost white", font=("Comfortaa", 20, "normal")
        )
        question_label.pack(pady=30)

        answer_frame = tk.Frame(self.root, bg="ghost white")
        answer_frame.pack(pady=40)

        for answer_text, colour_list in current["answers"].items():
            answer_button = self.create_button(
                answer_frame, answer_text, 
                command=lambda c=colour_list: self.update_score(c),
                width=30, bg="ghost white", relief="groove"
            )
            answer_button.pack(pady=10)
        
        navigation_frame = tk.Frame(self.root, bg="ghost white")
        navigation_frame.pack()

        if self.current_question_index > 0:
            back_button = self.create_button(
                navigation_frame, "Back", 
                command=self.go_to_previous_question,
                width=8, font=("Comfortaa", 12)
            )
            back_button.pack(side="left", padx=5)

        self.add_exit_button(navigation_frame)

    def go_to_previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question(self.current_question_index)

    def show_welcome_screen(self): 
        main_frame = tk.Frame(self.root, bg="ghost white")
        main_frame.pack(pady=20)

        title = tk.Label(
            main_frame, text="What is your personality colour?", fg="black", bg="ghost white", font=("Comfortaa", 24, "bold")
        )
        title.pack(pady=5)

        greeting = tk.Label(
            main_frame, text="""Take this personality quiz to find out what colour your personality is!\n""", fg="black", bg="ghost white", font=("Comfortaa", 18, "normal")
        )
        greeting.pack(pady=20)

        button_frame = tk.Frame(main_frame, bg="ghost white")
        button_frame.pack(pady=5, anchor="center")

        start_button = self.create_button(
            button_frame, "Start Quiz", self.start_quiz
        )
        start_button.pack(pady=10)

        exit_frame = tk.Frame(main_frame, bg="ghost white")
        exit_frame.pack(pady=10)
        self.add_exit_button(exit_frame)

    def update_score(self, colours):
        for colour in colours:
            self.scores[colour] += 1

        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question(self.current_question_index)
        else:
            self.show_loading_screen()

    def show_loading_screen(self):
        self.clear_screen()

        loading_label = tk.Label(
            self.root, text="Figuring out your personality colour...", fg="black", bg="ghost white", font=("Comfortaa", 20)
        )
        loading_label.pack(pady=200)

        self.root.after(1200, self.show_result)

    def show_result(self):
        self.clear_screen()
        
        result = max(self.scores, key=self.scores.get)
        colour_info = self.colour_data[result]

        result_frame = tk.Frame(self.root, bg=colour_info["display_colour"])
        result_frame.pack(pady=50)
        
        colour_name = tk.Label(
            result_frame, text=f"Your personality colour is {result}!\n", 
            fg=colour_info["display_colour"], bg="ghost white", font=("Comfortaa", 30, "bold")
        )
        colour_name.pack()

        result_label = tk.Label(
            result_frame, text=f"You are {colour_info['description']}.", fg=colour_info["display_colour"], bg="ghost white", font=("Comfortaa", 18)
        )
        result_label.pack()

        replay_frame = tk.Frame(self.root, bg="ghost white")
        replay_frame.pack(pady=100)

        replay_button = self.create_button(
            replay_frame, "Play Again", self.reset_quiz
        )
        replay_button.pack(pady=20)

        exit_frame = tk.Frame(self.root, bg="ghost white")
        exit_frame.pack(pady=10)
        self.add_exit_button(exit_frame)

    def reset_quiz(self):
        self.scores = {colour: 0 for colour in self.scores}
        self.current_question_index = 0
        self.start_quiz()

    def show_goodbye(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        goodbye_frame = tk.Frame(self.root, bg="ghost white")
        goodbye_frame.pack()

        goodbye_label = tk.Label(goodbye_frame, text="Goodbye", height=3, fg="black", bg="ghost white", font=("Comfortaa", 40, "normal"))
        goodbye_label.pack()

        thank_label = tk.Label(goodbye_frame, text="Thanks for playing!", height=4, fg="black", bg="ghost white", font=("Comfortaa", 20,"italic"))
        thank_label.pack()
        
        self.root.after(1200, self.root.destroy)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):        
        self.root.mainloop()

quiz = PersonalityQuiz()
quiz.run()