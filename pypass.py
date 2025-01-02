#!/usr/bin/env python3

import secrets

def generate_index():
    index = ""
    for i in range(5):
        index += str(secrets.randbelow(6) + 1)
    return index

if __name__ == "__main__":
    word_dict = {}
    with open('word_lists/eff_large_wordlist.txt', 'r', encoding="utf-8") as word_list:
        for line in word_list:
            current = line.rstrip().split(',')
            index = current[0]
            word = current[1]
            word_dict[index] = word
    word_list.close()
    passphrase = []
    for i in range(6):
        index = generate_index()
        passphrase.append(word_dict[index])
    print(" ".join(passphrase))