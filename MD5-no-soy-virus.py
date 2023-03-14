#!/usr/bin/env python3
import hashlib
import random
import os

def Ncrypt():
    while True:
        word = input("Word to hash: ")
        if not word:
            print("Error: word cannot be empty\n")
        else:
            bword = hashlib.md5(word.encode()).hexdigest()
            print("MD5:", bword)
            break

def Dcrypt():
    while True:
        hpass = input("Hash to crack: ")
        if not hpass:
            print("Error: hash cannot be empty\n")
        else:
            wordl = input("Wordlist file: ")
            if not os.path.exists(wordl):
                print(f"Error: file '{wordl}' not found\n")
                return False
            try:
                with open(wordl, 'r') as file:
                    for line in file:
                        cpass = line.strip()
                        if hashlib.md5(cpass.encode('utf-8')).hexdigest() == hpass:
                            print('Password:', cpass)
                            return True
            except Exception as e:
                print(f"Error: {e}")
                return False
            print("Error: Password not found in wordlist!\n")
            return False

def UrOK():
    n = random.randint(1,3)
    if n == 1:
        print("Error: The fucking fucker has fucking fucked up\n")
    elif n == 2:
        print("Error: YOU fucking dickhead try again\n")
    elif n == 3:
        print("Error... Asshole there are only 3 options, 1, 2, 3 is it that difficult?\n")
    else:
        print("\n\nEaster Egg: Hentai Kyaa\n\n")

def main():
    while True:
        print("1) Word 2 Hash")
        print("2) Crack Hash")
        print("3) Exit")
        o = input("Option: ")
        if o == "1":
            Ncrypt()
        elif o == "2":
            Dcrypt()
        elif o == "3":
            print("Bye pussyfart!!\n")
            break
        else:
            UrOK()

if __name__ == '__main__':
    main()