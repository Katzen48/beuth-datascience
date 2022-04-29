# Basic word guessing game.
# Words database is taken from https://github.com/dwyl/english-words
import random
import signal
import sys

found = set()
word = ''
words = []


def signal_handler(sig, frame):
    print('Bye')
    sys.exit(1)


def read_database():
    global words
    words = []

    file = open('words.txt')
    while file:
        line = file.readline()
        if line == '':
            break

        words.append(line.strip().lower())
    file.close()


def select_word():
    global found
    global word

    found = set()
    word = words[random.randint(0, len(words) - 1)]


def print_word():
    global found
    global word
    output = ''

    for char in word:
        if char in found:
            output += char
        else:
            output += '_'

    print('Word: ' + output)


def guess(char):
    global found
    global word

    if not char in found and char in word:
        found.add(char)

    if len(set(word)) == len(found):
        print('Congratulations. You found the word.')
        print('Here is a new one.')
        select_word()

    print_word()


if sys.platform.startswith('win'):
    import win32api

    win32api.SetConsoleCtrlHandler(signal_handler, True)
else:
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()

print('Press Ctrl+C to exit')

read_database()
select_word()
print_word()

while True:
    char = input('Guess a character: ')
    if len(char) != 1:
        print_word()
    else:
        guess(char.lower())
