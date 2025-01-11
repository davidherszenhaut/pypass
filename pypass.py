#!/usr/bin/env python3

import secrets
import argparse

def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=6, help="Allows the user to choose the length of the password.")
    parser.add_argument("-t", "--times", type=int, default=1, help="Allows the user to generate multiple passwords at once.")
    parser.add_argument("-s", "--separator", type=str, default=" ", help="Allows the user to choose the separator character for passphrases.")
    return parser.parse_args()

def generate_word_dict():
    word_dict = {}
    with open('word_lists/eff_large_wordlist.txt', 'r', encoding="utf-8") as word_list:
        for line in word_list:
            current = line.rstrip().split(',')
            index = current[0]
            word = current[1]
            word_dict[index] = word
    word_list.close()
    return word_dict

def generate_passwords(word_dict, length, times, separator):
    passwords = []
    for i in range(times):
        passwords.append(generate_password(word_dict, length, separator))
    return passwords

def generate_password(word_dict, length, separator):
    password = []
    for i in range(length):
        index = generate_index()
        password.append(word_dict[index])
    return separator.join(password)

def generate_index():
    index = ""
    for i in range(5):
        index += str(secrets.randbelow(6) + 1)
    return index

def print_passwords(passwords):
    print("\n".join(passwords))

if __name__ == "__main__":
    args = set_up_parser()
    word_dict = generate_word_dict()
    passwords = generate_passwords(word_dict, args.length, args.times, args.separator)
    print_passwords(passwords)