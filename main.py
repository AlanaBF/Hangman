import os
import random
import hangman_words
import hangman_art

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet character.")
        continue  # Skip the rest of the loop and ask for a new guess

    if guess in display:
        print(f"You have already guessed {guess}")
        continue  # Skip the rest of the loop and ask for a new guess
    #Check guessed letter
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
  
    #Check if user is wrong.
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word, lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


    print(hangman_art.stages[lives])