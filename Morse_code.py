# -*- coding: utf-8 -*-
import re

def get_string():
    print("please choose the mode:")
    print("mode \"a\" means change Morse code to English letters,")
    print("mode \"b\" means change English letters to Morse code.")
    mode = input("mode \"a\" or mode \"b\":")

    str = ""
    if mode=="a":
        print("please input the Morse code you want to change:")
        str = input()
        print(str)

if __name__ == "__main__":
    get_string()
