# Hangman Game 🎮

A command-line Hangman game built using Python. The computer randomly selects a word, and the player tries to guess the word by entering one letter at a time before running out of attempts.

## Features

- Random word selection from a word list file
- Three difficulty levels:
  - Easy: 10 attempts
  - Medium: 6 attempts
  - Difficult: 3 attempts
- Hidden word display using `_`
- Reveals all matching letters when guessed correctly
- Tracks already guessed letters
- Prevents invalid inputs
- Win and lose conditions
- Play again option

## How It Works

1. The program selects a random word from `words.txt`.
2. The word is hidden from the player using underscores.
3. The player guesses one letter at a time.
4. Correct guesses reveal the letter in the word.
5. Wrong guesses reduce the remaining attempts.
6. The player wins by revealing the complete word before running out of attempts.

## Example

```
Welcome to Hangman!
Guess the word before you run out of attempts.

The word has 6 letters.

Word: _ _ _ _ _ _

Guess a letter: p

Correct letter.

Word: p _ _ _ _ _

Remaining guesses: 5
```

## Project Structure

```
Hangman/
│
├── hangman.py
├── words.txt
├── README.md
└── .gitignore
```

## Concepts Practiced

- Variables and data types
- Lists
- Strings
- Loops (`for`, `while`)
- Conditional statements
- Functions
- File handling
- Random module
- Input validation

## How to Run

1. Make sure Python is installed.
2. Clone this repository.
3. Open the project folder in the terminal.
4. Run:

```bash
python hangman.py
```

## Future Improvements

- Add word categories
- Add hints for words
- Add scoring system
- Add a graphical interface using Tkinter
- Improve game design with more features