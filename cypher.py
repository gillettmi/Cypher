#!/usr/bin/python3
# Based on the work of Al Sweigart's book, "Cracking Codes with Python"
# https://nostarch.com/crackingcodes/

import os

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

current_directory = os.curdir

main_menu = '''
   ______            __             
  / ____/_  ______  / /_  ___  _____
 / /   / / / / __ \/ __ \/ _ \/ ___/
/ /___/ /_/ / /_/ / / / /  __/ /    
\____/\__, / .___/_/ /_/\___/_/     
     /____/_/
   Version 1 | 7/8/2020
------------------------------------
1. Encode message
2. Decode message
3. Exit                                                                              
'''


def press_enter():
    input('\nPress enter to continue...')


def error(message):
    print(message)
    press_enter()


def write_output(message, output_file):
    with open(output_file, 'w') as f:
        f.write(message)
        f.close()


def vigenere_cypher(mode=''):

    message = str(input('Message:'))
    key = str(input('Encryption Key:'))

    index = 0
    key = key.upper()
    skipped_chars = []
    converted = []

    for letter in message:

        num = letters.find(letter.upper())
        if num != -1:

            if mode == 'encode':
                num += letters.find(key[index])

            elif mode == 'decode':
                num -= letters.find(key[index])

            num %= len(letters)
            converted.append(letters[num])

            index += 1

            if index == len(key):
                index = 0

        elif letter == ' ':
            converted.append(letter)

        else:
            skipped_chars.append(letter)

    if skipped_chars != '':
        print('\nSkipped Characters:', ''.join(skipped_chars))

    output = ''.join(converted)
    return output


def transmit(text):
    print('\nConverted Message:', text)
    write_output(message=text,
                 output_file=(os.path.join(current_directory, 'output.txt')))
    press_enter()


def main():
    while True:
        print(main_menu)
        try:
            choice = int(input('Input:'))

            if choice == 1:
                output = vigenere_cypher('encode')
                transmit(output)

            elif choice == 2:
                output = vigenere_cypher('decode')
                transmit(output)

            elif choice == 3:
                print('\nGoodbye')
                break

            else:
                error('Please enter an integer from the menu.')

        except ValueError:
            error('Please enter an integer from the menu.')


if __name__ == '__main__':
    main()
