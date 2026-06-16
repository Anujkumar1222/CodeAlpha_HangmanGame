import random

# List of predefined words
words = ["python", "computer", "program", "coding", "internship"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_guesses:
    # Display current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print(f"Remaining attempts: {max_guesses - incorrect_guesses}")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)