# Code by Garrett Wadley
# Purpose: Create a simple hangman game using for and while loops, lists, and the random function
import random

wordslist = ['Razorbacks', 'Bears', 'Cougars', 'Sooners', 'Cowboys', 'Owls', 'Mustangs', 'Longhorns', 'Aggies',
             'Frogs', 'Raiders', 'Cyclones', 'Jayhawks', 'Wildcats', 'Buffaloes', 'Tigers', 'Huskers']

bevo_stages = ['       \________/\n          (oo)\n   /-------\/\n  / |     ||\n *  ||----||\n    ^^    ^^',
               '        \______/\n          (oo)\n   /-------\/\n  / |     ||\n *  ||----||\n    ^^    ^^',
               '         \____/\n          (oo)\n   /-------\/\n  / |     ||\n *  ||----||\n    ^^    ^^',
               '          \__/\n          (oo)\n   /-------\/\n  / |     ||\n *  ||----||\n    ^^    ^^',
               '           __\n          (oo)\n   /-------\/\n  / |     ||\n *  ||----||\n    ^^    ^^'
               ]

mistakes = 0
letters_guessed = []
wrong_letters = []
mistakes_allowed = len(bevo_stages)
word = random.choice(wordslist)
word = word.upper()
letters_word = list(word)

print('Welcome to Longhorn Hangman!')
print('Guess the Big 12 or SWC team!')
print('There are ' + str(len(letters_word)) + ' letters in the word.')


# loops to ask player for guess inputs (inputs translated to uppercase)
while mistakes < mistakes_allowed:
    print()
    print('Wrong letters: ', end='')
    for letter in wrong_letters:
        print(str(letter) + ', ', end='')
    print()
    print('Guesses left: ' + str(mistakes_allowed - mistakes))
    letter_input = input('Enter a letter --> ')
    letter_input = letter_input.upper()

# this loop allows for a retry if a chosen character has already been tried (successfully or not)
    while letter_input in letters_guessed or letter_input in wrong_letters:
        print()
        print('You have already entered this letter, enter another one')
        letter_input = input('Enter a letter --> ')
        letter_input = letter_input.upper()

# this loop allows you to guess the full word, otherwise only a single character is allowed
    while len(letter_input) != 1 and letter_input != word:
        print()
        print('You may only input a single character OR guess the entire word')
        letter_input = input('Enter a letter --> ')
        letter_input = letter_input.upper()

    if letter_input not in letters_word:
        mistakes += 1
        wrong_letters.append(letter_input)

# Word prints as either guessed letter or blanks
    print()
    print('Word: ', end='')
    for letter in letters_word:
        if letter_input == letter:
            letters_guessed.append(letter_input)

    for letter in letters_word:
        if letter in letters_guessed:
            print(letter + ' ', end='')
        else:
            print('_ ', end='')

    print()
    if mistakes:
        print(bevo_stages[mistakes - 1])
    print()
    print('***************************************************')


# win condition: guess entire word at once or letter by letter
    if letter_input == word or len(letters_guessed) == len(letters_word):
        print(word)
        print()
        print('       \________/\n          (^^)\n   /-------\/\n  / |     ||\n *  ||----||\n    ^^    ^^')
        print('Texas Fight!')
        break

# lose condition: run out of tries
if mistakes == mistakes_allowed:
    print('           __\n          (xx)\n   /-------\/\n  / |13-0 ||\n *  ||----||\n    ^^    ^^')
    print('Oh no! You let the Aggies saw Bevo\'s horns off!')
    print('The word was: ' + word)
