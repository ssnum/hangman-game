import requests
import random

def get_random_words(num_words, word_length):
    # Function to fetch random words from the API
    url = "https://random-word-api.herokuapp.com/word"
    params = {"number": num_words, "length": word_length}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch random words.")
        return []

def choose_word(word_length):
    # Function to choose a random word from the fetched words
    words = get_random_words(10, word_length)  # Fetch 10 random words with the specified length
    return random.choice(words)

def display_word(word, guessed_letters):
    # Function to display the word with guessed letters filled in
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    # Main function to play the Hangman game
    word_length = 6  # Set the desired length of the words
    word = choose_word(word_length).lower()  # Choose a random word with the specified length
    guessed_letters = []  # List to store guessed letters
    attempts = 6  # Number of attempts allowed

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Enter a letter or guess the word: ").lower()

        if len(guess) == 1:
            # If a single letter is guessed
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Correct!")
                print(display_word(word, guessed_letters))
            else:
                attempts -= 1
                print(f"Incorrect! You have {attempts} attempts left.")
                if attempts == 0:
                    print("Game over! You ran out of attempts.")
                    print(f"The word was: {word}")
                    break
        else:
            # If the entire word is guessed
            if guess == word:
                print("Congratulations! You guessed the word.")
                break
            else:
                attempts -= 1
                print(f"Incorrect! You have {attempts} attempts left.")
                if attempts == 0:
                    print("Game over! You ran out of attempts.")
                    print(f"The word was: {word}")
                    break

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word.")
            break

if __name__ == "__main__":
    hangman()
