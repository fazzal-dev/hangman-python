import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)  # what the user guessed
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have', lives, 'lives left and you have used these letters: ',
              ' '.join(used_letters))
        # what the current word is (ie W - O R D  )
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a Letter: ').upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('letter not in the word')

        elif user_letter in used_letters:
            print('You already have used that character,please try again.')

        else:
            print('Invalid character. please try again.')
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, the word was', word)
    else:
        print('You have guessed the word', word, '!')


if __name__ == '__main__':
    hangman()
