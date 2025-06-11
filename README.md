# Wordle GUI in Python

This is a simple graphical version of the popular **Wordle** game built using **Python** and **Tkinter**. It allows you to guess randomly chosen words of a specified length, provides visual feedback for each letter, and limits the number of attempts—just like the original Wordle!

## 🎮 Features

- Customizable word length (default is 5 letters)
- Clean GUI using Tkinter
- Visual letter feedback with color-coding:
  - 🟩 **Green**: Correct letter and position
  - 🟧 **Orange**: Correct letter, wrong position
  - ⬜ **Gray**: Incorrect letter
- Six attempts to guess the correct word
- Random word selection from a local word list

## 🖼️ Screenshot

![image](https://github.com/user-attachments/assets/702e1707-006d-4002-b393-1c1c34dd1266)

## 🛠️ Requirements

- Python 3.x
- Tkinter (comes pre-installed with most Python distributions)

Ensure you have a `words.txt` file in the same directory, containing a list of valid English words (one per line). You can use [SCOWL](http://wordlist.aspell.net/) or any standard dictionary list.

## 📁 Project Structure
├── wordle_gui.py # Main application
├── words.txt # List of valid words
└── README.md # You're here!

## ▶️ How to Run

1. Clone or download this repository:

   bash
   git clone https://github.com/your-username/wordle-gui-python.git
   cd wordle-gui-python
2. Make sure words.txt exists and has a list of words (e.g., 4-7 letter words):
3. Run the game: python wordle_gui.py

🧠 How to Play
Enter a word length (e.g., 5) and click Start Game.

Type your guess and press Enter.

Use the color-coded hints to guess the word in 6 tries or less!

📌 Notes
The game uses a local words.txt file instead of relying on external libraries like NLTK for faster and simpler setup.

Words must contain only alphabetic characters.

GUI automatically resets with a new game when you click "Start Game."

🧑‍💻 Author
Developed by Your Name
