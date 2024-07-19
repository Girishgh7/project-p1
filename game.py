import random

# List of words 
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape","Cryptocurrency","Juxtaposition","Quizzical","Phlegm","Sphinx"
"Pizza","animal","ear","Girish","fox","oj","did","it","frizzled"]

# Choose a random 
word_to_guess = random.choice(words)

# Create a list 
guessed_letters = ["_"] * len(word_to_guess)

# Create a variable to store the number of geusses
incorrect_guesses = 0

# Create a variable to store the maximum number of incorrect guesses
max_incorrect_guesses = 7

# Game loop
while True:
    # Print the current state of the word
    print(" ".join(guessed_letters))

    # Ask the user for a guess
    guess = input("Guess a letter: ")

   
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_letters[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Incorrect! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")


    if "_" not in guessed_letters:
        print(" Congratulations! You won!")
        break
    elif incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was {word_to_guess}.")
        print(''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \+
| |          ||  `/,|
| |          (\\=`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \=
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :                      . .''')
        break