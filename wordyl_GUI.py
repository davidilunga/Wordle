import tkinter as tk
from tkinter import messagebox
import random
#import nltk
#from nltk.corpus import words

# Download word list once if not already done
#nltk.download('words')

class WordleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle GUI")
        self.root.geometry("400x500")
        self.root.resizable(True, True)

        self.word_length = tk.IntVar(value=5)
        self.max_attempts = 6
        self.attempt = 0
        self.word = ""
        self.words_list = open('words.txt').read().splitlines()

        self.setup_widgets()

    def setup_widgets(self):
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=10)

        tk.Label(self.top_frame, text="Word length:").pack(side="left")
        self.word_length_entry = tk.Entry(self.top_frame, textvariable=self.word_length, width=5)
        self.word_length_entry.pack(side="left")
        tk.Button(self.top_frame, text="Start Game", command=self.start_game).pack(side="left", padx=10)

        self.guess_entry = tk.Entry(self.root, font=("Courier", 18), justify="center")
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=10)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.status_label.pack()

    def start_game(self):
        self.clear_board()
        self.attempt = 0
        length = self.word_length.get()
        self.valid_words = [word for word in self.words_list if len(word) == length and word.isalpha()]
        if not self.valid_words:
            messagebox.showerror("No Words", f"No words found with length {length}")
            return
        self.word = random.choice(self.valid_words)
        self.status_label.config(text=f"Game started! Guess the {length}-letter word.")
        self.guess_entry.focus()

    def check_guess(self):
        if self.attempt >= self.max_attempts:
            return

        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != len(self.word) or not guess.isalpha():
            self.status_label.config(text="Invalid word. Try again.")
            return

        row = tk.Frame(self.board_frame)
        row.pack()

        for i, char in enumerate(guess):
            color = "gray"
            if char == self.word[i]:
                color = "green"
            elif char in self.word:
                color = "orange"

            label = tk.Label(row, text=char.upper(), width=4, height=2, font=("Courier", 16), bg=color, fg="white")
            label.pack(side="left", padx=2, pady=2)

        self.attempt += 1

        if guess == self.word:
            self.status_label.config(text=f"Congrats! You guessed the word in {self.attempt} tries.")
            messagebox.showinfo("Wordle", f"🎉 You guessed the word: {self.word.upper()}!")
        elif self.attempt == self.max_attempts:
            self.status_label.config(text=f"Out of tries! The word was: {self.word.upper()}")
            messagebox.showinfo("Game Over", f"You didn't guess it. The word was: {self.word.upper()}")

    def clear_board(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = WordleGUI(root)
    root.mainloop()
