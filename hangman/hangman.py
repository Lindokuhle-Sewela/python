import random
from wonderwords import RandomWord

def draw_hangman(lives):
    """Returns the visual state of the hangman based on lives left."""
    stages = [
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",  # 0 lives
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # 1 life
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # 2 lives
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  # 3 lives
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  # 4 lives
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",  # 5 lives
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",  # 6 lives
    ]
    return stages[lives]

def play_hangman():
    #Initialize Wonderwords
    rw = RandomWord()
    
    # Generate a random noun between 5 and 10 letters
    try:
        secret_word = rw.word(
            include_parts_of_speech=["nouns"], 
            word_min_length=5, 
            word_max_length=10
        ).lower()
    except:
        #Fallback if library fails
        secret_word = "alphabet"

    guessed_letters = []
    lives = 6
    
    print("---WONDER-HANGMAN---")
    print("I've picked a random noun for you!")

    while lives > 0:
        print(draw_hangman(lives))
        
        display = "".join([letter if letter in guessed_letters else "_ " for letter in secret_word])
        print(f"Word: {display}")
        print(f"Guessed: {', '.join(guessed_letters)}")
        print(f"Lives: {lives}")

        #Win check
        if "_ " not in display:
            print("\n--YOU WIN!--")
            print(f"The word was indeed: {secret_word.upper()}")
            break

        guess = input("\nGuess a letter: ").lower().strip()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Invalid input. Please type a single letter.")
            continue
        if guess in guessed_letters:
            print(f">> You already tried '{guess}'.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f">> Nice! '{guess}' is in there.")
        else:
            lives -= 1
            print(f">> Sorry, '{guess}' is a miss.")

    if lives == 0:
        print(draw_hangman(0))
        print("\n--GAME OVER--")
        print(f"The word was: {secret_word.upper()}")

if __name__ == "__main__":
    play_hangman()
