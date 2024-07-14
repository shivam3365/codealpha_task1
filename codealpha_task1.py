import random

def select_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'random', 'word']
    return random.choice(words)

def display_current_state(word, correct_guesses):
    display = ''.join([letter if letter in correct_guesses else '_' for letter in word])
    print(f"Current state: {display}")

def hangman():
    word = select_random_word()
    correct_guesses = set()
    incorrect_guesses = set()
    max_incorrect = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while len(incorrect_guesses) < max_incorrect:
        display_current_state(word, correct_guesses)
        guess = input("Guess a letter: ").lower()
        
        if guess in correct_guesses or guess in incorrect_guesses:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            correct_guesses.add(guess)
            if all(letter in correct_guesses for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect guess. You have {max_incorrect - len(incorrect_guesses)} incorrect guesses left.")
        
        if len(incorrect_guesses) >= max_incorrect:
            print(f"Game over! The word was: {word}")
            break

if __name__ == "__main__":
    hangman()
