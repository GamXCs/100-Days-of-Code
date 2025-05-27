import random
import hangman_art
import hangman_words

word_list = ["aardvark", "baboon", "camel"]
placeholder = ""

chosen_word = random.choice(word_list)
print(chosen_word)

for i in range(len(chosen_word)):
    placeholder = "_"
    print(placeholder, end="")

game_Over = False
guessedLetters = []
lives = 6

while not game_Over:
    display = ""

    guess = input("\nPlease guess a letter. ").lower()
    print(guess)

    for char in chosen_word:
        if guess == char:
            display += char
            guessedLetters.append(char)
        elif char in guessedLetters:
            display += char
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
    if lives <= 0:
        game_Over = True
        print(f"The word was {chosen_word}! You lose.")
    print(f"You have {lives} lives remaining.")

    if "_" not in display:
        game_Over = True
        print("You Won!")
