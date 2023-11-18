import random

MAX_ATTEMPTS = 8
WORD_LIST = ['javascript', 'python', 'java', 'swift']
total_wins = 0
total_losses = 0


def decision():
    while True:
        choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ').lower()
        if choice == 'play' or choice == 'exit' or choice == 'results':
            return choice
        else:
            print('Wrong input.')


def select_random_word(words):
    return random.choice(words)


def create_shadow_word(word):
    return len(word) * '-'


def get_input(letter_template):
    while True:
        print(letter_template)
        letter = input('Input a letter: ')
        if letter.isalpha() and len(letter) == 1 and letter.islower():
            return letter
        else:
            if len(letter) >= 2 or len(letter) == 0:
                print('Please, input a single letter.\n')
            else:
                print('Please, enter a lowercase letter from the English alphabet.\n')


def update_shadow_word(guess, word, shadow_word, attempts, guessed_letters):
    letter_found = False
    if guess in guessed_letters:
        print("You've already guessed this letter.")
    else:
        for i in range(len(word)):
            if word[i] == guess:
                shadow_word = shadow_word[:i] + guess + shadow_word[i + 1:]
                letter_found = True
                guessed_letters.add(guess)
        if not letter_found:
            guessed_letters.add(guess)
            attempts -= 1
            print("That letter doesn't appear in the word.")
    return shadow_word, attempts


def main():
    print('H A N G M A N')
    global total_wins
    global total_losses

    while True:
        user_decision = decision()

        if user_decision == 'play':
            print()
            attempts_left = MAX_ATTEMPTS
            guessed_letter = set()
            chosen_word = select_random_word(WORD_LIST)
            shadowed = create_shadow_word(chosen_word)

            while True:
                if shadowed != chosen_word:
                    guess = get_input(shadowed)
                    shadowed, attempts_left = update_shadow_word(guess, chosen_word, shadowed, attempts_left,
                                                                 guessed_letter)
                    print()

                    if attempts_left == 0:
                        total_losses += 1
                        print('You lost!')
                        break
                else:
                    total_wins += 1
                    print(f'You guessed the word {shadowed}!')
                    print('You survived!')
                    break

        elif user_decision == 'exit':
            print('Goodbye')
            break

        elif user_decision == 'results':
            print(f'You won: {total_wins} times.')
            print(f'You lost: {total_losses} times.')


if __name__ == '__main__':
    main()
