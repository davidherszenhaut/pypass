#!/usr/bin/env python3

import argparse
import secrets
import string

def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--kind", type=str, choices=["passphrase", "password", "pin"], default="passphrase", help="Allows the user to choose which kind of password to generate.")
    parser.add_argument("-l", "--length", type=int, default=6, help="Allows the user to choose the length of the password.")
    parser.add_argument("-r", "--repeat", type=int, default=1, help="Allows the user to generate multiple passwords at once.")
    parser.add_argument("-s", "--separator", type=str, default=" ", help="Allows the user to choose the separator character for passphrases.")
    return parser.parse_args()

def populate_word_dict():
    word_dict = {}
    with open('word_lists/eff_large_wordlist.txt', 'r', encoding="utf-8") as word_list:
        for line in word_list:
            current = line.rstrip().split(',')
            index = current[0]
            word = current[1]
            word_dict[index] = word
    word_list.close()
    return word_dict

def generate_passwords(word_dict, kind, length, repeat, separator):
    print(kind)
    passwords = []
    for i in range(repeat):
        passwords.append(generate_password(word_dict, kind, length, separator))
    return passwords

def generate_password(word_dict, kind, length, separator):
    if kind == "password":
        alphabet = string.ascii_letters + string.digits
        return "".join(secrets.choice(alphabet) for i in range(length))
    elif kind == "passphrase":
        return generate_passphrase(word_dict, length, separator)
    elif kind == "pin":
        return generate_pin(length)
    
def generate_passphrase(word_dict, length, separator):
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

def generate_pin(length):
    return "".join(secrets.choice(string.digits) for i in range(length))

def print_passwords(passwords):
    print("\n".join(passwords))

if __name__ == "__main__":
    args = set_up_parser()
    word_dict = populate_word_dict()
    passwords = generate_passwords(word_dict, args.kind, args.length, args.repeat, args.separator)
    print_passwords(passwords)