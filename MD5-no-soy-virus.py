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
            print("Bye!!\n")
            break
        else:
            print("Unknow\n")
        
main()
