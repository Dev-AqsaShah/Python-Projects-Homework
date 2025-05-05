import random

stages = ['''
___________________
    |
    |
    |
    |
    |
    |
-------------------
''',
'''
----------------
    |      |
    |      O
    |
    |
    |
    |
----------------        
''',
'''
----------------
    |      |
    |      O
    |      |
    |
    |
    |
----------------
''',
'''    
----------------
    |      |
    |      O
    |     /|
    |
    |
    |
----------------
''',
'''    
----------------
    |      |
    |      O
    |     /|\\
    |
    |
    |
----------------
''',
''' 
----------------
    |      |
    |      O
    |     /|\\
    |     / 
    |
    |
----------------
''',
'''       
----------------
    |      |
    |      O
    |     /|\\
    |     / \\
    |
    |
----------------
''']

words = ["apple", "kiwi", "banana", "graps", "dates"]
chosen_word = random.choice(words)
word_display = ["_" for _ in chosen_word]
guess_letters = []
lives = len(stages) - 1

print("Welcome to Hangman!")
print("Guess the fruit name.")

while True:
    print("\n" + "".join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in guess_letters:
        print("You already guessed that letter. Try again.\n")
        continue

    guess_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        lives -= 1
        print(stages[len(stages) - lives - 1])
        if lives == 0:
            print(f"\nYou lost! The word was '{chosen_word}'.")
            break

    if "_" not in word_display:
        print("\n" + "".join(word_display))
        print("Congratulations! You guessed the word correctly!")
        break
