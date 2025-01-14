#!/usr/bin/env python3

import argparse
import os
import secrets
import string

def set_up_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--character", action="store_true", help="Allows the user to insert a random special character into a random word in the passphrase.")
    parser.add_argument("-k", "--kind", type=str, choices=["passphrase", "password", "pin"], default="passphrase", help="Allows the user to choose which kind of password to generate.")
    parser.add_argument("-l", "--length", type=int, help="Allows the user to choose the length of the password.")
    parser.add_argument("-p", "--provide", type=str, default="word_lists/eff_large_wordlist.txt", const="word_lists/eff_large_wordlist.txt", nargs="?", help="Allows the user to provide a custom word list for passphrases.")
    parser.add_argument("-q", "--quiet", action="store_true", help="Allows the user to not print the password to the terminal.")
    parser.add_argument("-r", "--repeat", type=int, default=1, help="Allows the user to generate multiple passwords at once.")
    parser.add_argument("-s", "--separator", type=str, default=" ", help="Allows the user to choose the separator character for the passphrase.")
    parser.add_argument("-w", "--write", type=str, const="passwords.txt", nargs="?", help="Allows the user to save the password to a file.")
    return parser.parse_args()

def populate_word_dict(provided_file):
    word_dict = {}
    if provided_file:
        validate_provided_file(provided_file)
    with open(provided_file, "r", encoding="utf-8") as word_list:
        for line in word_list:
            current = line.rstrip().split(",")
            index = current[0]
            word = current[1]
            word_dict[index] = word
    word_list.close()
    return word_dict

def validate_provided_file(provided_file):
    if not os.path.isfile(provided_file):
        raise FileNotFoundError(f"The file specified by the --provide flag ({provided_file}) was not found.")
    with open(provided_file, "r") as word_list:
        line_count = word_list.readlines()
        if len(line_count) != 7776:
            raise RuntimeError(f"The file specified by the --provide flag ({provided_file}) did not have the expected number of lines. Please look at the included word list (word_lists/eff_large_wordlist.txt) as an example for word list formatting.")

def get_password_length(kind, length):
    default_lengths = {
        "passphrase": 6,
        "password": 12,
        "pin": 4
    }

    if not length:
        return default_lengths[kind]
    else:
        return length

def generate_passwords(word_dict, character, kind, length, repeat, separator):
    passwords = []
    for i in range(repeat):
        passwords.append(generate_password(word_dict, character, kind, length, separator))
    return passwords

def generate_password(word_dict, character, kind, length, separator):
    if kind == "password":
        alphabet = string.ascii_letters + string.digits
        return "".join(secrets.choice(alphabet) for i in range(length))
    elif kind == "passphrase":
        return generate_passphrase(word_dict, character, length, separator)
    elif kind == "pin":
        return generate_pin(length)
    
def generate_passphrase(word_dict, character, length, separator):
    passphrase = []
    for i in range(length):
        index = generate_index()
        passphrase.append(word_dict[index])
    if character:
        chosen_word = secrets.choice(passphrase)
        chosen_word_index = passphrase.index(chosen_word)
        special_characters = string.digits + string.punctuation
        chosen_index = secrets.choice(range(1, len(chosen_word)))
        chosen_word = chosen_word[0:chosen_index] + secrets.choice(special_characters) + chosen_word[chosen_index:len(chosen_word)]
        passphrase[chosen_word_index] = chosen_word
    return separator.join(passphrase)

def generate_index():
    index = ""
    for i in range(5):
        index += str(secrets.randbelow(6) + 1)
    return index

def generate_pin(length):
    return "".join(secrets.choice(string.digits) for i in range(length))

def print_passwords(passwords, quiet):
    if quiet:
        print("Quiet argument was chosen. Passwords will not be printed.")
    else:
        print("\n".join(passwords))

def write_passwords(passwords, write):
    if os.path.isfile(write):
        os.remove(write)
    with open(write, "w") as output_file:
        output_file.write("\n".join(passwords))

if __name__ == "__main__":
    args = set_up_parser()
    word_dict = populate_word_dict(args.provide)
    passwords = generate_passwords(word_dict, args.character, args.kind, get_password_length(args.kind, args.length), args.repeat, args.separator)
    print_passwords(passwords, args.quiet)
    if args.write:
        write_passwords(passwords, args.write)