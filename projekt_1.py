"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Pernikář
email: tomworld@seznam.cz
discord: Tomáš P.#9699
"""
import string
from task_template import TEXTS

# registrovaní uživatelé
USERS = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

username = input('username:')
password = input('password:')
if USERS.get(username) == password:
    print('-' * 40)
    print(f'Welcome to the app, {username}')
    print(f'We have {len(TEXTS)} texts to be analyzed.')
    print('-' * 40)
    selection = int(input('Enter a number btw. 1 and 3 to select:'))
    if selection in range(1, len(TEXTS) + 1):
        # analýza textu
        text = TEXTS[selection - 1]
        words = text.split()
        titlecase_words = [word for word in words if word.istitle()]
        uppercase_words = [word for word in words if word.isupper() and not word[0].isnumeric()]
        lowercase_words = [word for word in words if word.islower()]
        numeric_strings = [word for word in words if word.isnumeric()]
        numeric_values = [int(word) for word in numeric_strings]

        numbers = [int(word) for word in words if word.isnumeric()]

        print('-' * 40)
        print(f'There are {len(words)} words in the selected text.')
        print(f'There are {len(titlecase_words)} titlecase words.')
        print(f'There are {len(uppercase_words)} uppercase words.')
        print(f'There are {len(lowercase_words)} lowercase words.')
        print(f'There are {len(numeric_strings)} numeric strings.')
        print(f"The sum of all the numbers {sum(numbers)}")

        # délka slov
        # odstranění interpunkčních znamének ze slov
        remover = str.maketrans('', '', string.punctuation)
        words = [word.translate(remover) for word in text.split()]

        word_lengths = {}
        for word in words:
            length = len(word)
            if length in word_lengths:
                word_lengths[length] += 1
            else:
                word_lengths[length] = 1

        # graf
        print("LEN|  OCCURENCES  |NR.")
        print("-" * 30)
        sorted_word_lengths = sorted(word_lengths.items())
        for length, occurences in sorted_word_lengths:
            print(f"{length:3}|{'*' * occurences:13}|{occurences}")
                                    
    else:    
        print('Invalid input, terminating the program.')
        quit()
else:
    print('unregistered user, terminating the program..')
    quit()

