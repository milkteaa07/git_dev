#!/usr/bin/env/python3

"""
palindrome_checker.py
https://www.crashwhite.com/advtopicscompsci/materials/assignments/daily/4-07p-palindrome_checker.md.html
"""

__author__ = "Ava Teng"
__version__ = "2023-02-17"

import string
from atds import Deque


class palindromeChecker(object):
    def __init__(self):
        self.string = ''
        
    def get_string(self):
        return self.string
        
    def set_strict_mode(self, x):
        if x == 1:
            return True
        if x == 2:
            return False
    
    def is_palindrome(self, phrase, sm):
        if sm == False:
            #ignore punctuation
            phrase = phrase.translate(str.maketrans('', '', string.punctuation))
            phrase = phrase.lower().replace(' ', '')
        else:
            pass
        p = Deque()
        for letter in phrase:
            p.add_rear(letter)  
        if p.size() > 0:
            while p.get_queue()[0] == p.get_queue()[-1] and p.size() > 1:
                p.remove_front()
                p.remove_rear()
            else:
                pass
            if p.size() <= 1:
                return True
        return False
            

def main():
    print()
    s = palindromeChecker()
    print("PALINDROME CHECKER")
    x = int(input("Do you want strict mode 1) on, or 2) off? "))
    sm = s.set_strict_mode(x)
    phrase = input("Phrase: ")
    flag = s.is_palindrome(phrase, sm)
    if flag == True:
        print("It's a palindrome!")
    else:
        print("No palindrome here...")
    print()

    
if __name__ == "__main__":
    main()

