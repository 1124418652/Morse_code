# -*- coding: utf-8 -*-
import re

def get_string():
    print("please choose the mode:")
    print("mode \"a\" means change Morse code to English letters,")
    print("mode \"b\" means change English letters to Morse code.")
    mode = input("mode \"a\" or mode \"b\":")

    str = ""
    if mode=="a":            #模式a
        print("please input the Morse code you want to change:")
        str = input()
        if(not re.match(r'^[\.\/\-\ ]', str)):          #如果不是摩斯电码，退出
            exit(1)
    elif mode=="b":         #模式b
        print("please input the English letters you want to change:")
        str = input()
        if(not re.match(r'^[a-zA-Z0-9\s\.]+$', str)):       #如果不是由字母和数字组成，退出
            exit(1)
    return mode, str
                
def pre_process(mode, str):
    if mode=="a":               #将摩斯电码中的间隔删除
        Morse_code = re.split(r'[\s+,\/]', str)
        return Morse_code
    if mode=="b":               #将字符串中的空格删除
        string = re.split(r'\s+', str)
        string = ''.join(string).upper()
        return [i for i in string]
        
def get_Morse_ref(mode):
    Morse_ref = {               #摩斯电码表
        'A':'.-',
        'B':'-...',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---',
        'P':'.--.',
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-',
        'V':'...-',
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..',
        '0':'-----',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '.':'.-.-.-'
    }
    if mode=="b":
        return Morse_ref
    if mode=="a":
        letter_ref = {}
        for i in Morse_ref.keys():
            letter_ref[Morse_ref[i]] = i
        return letter_ref
        
def Code(string):
    pass
    
def Decode(Morse_code):
    pass

if __name__ == "__main__":
    mode,str = get_string()
    string = pre_process(mode, str)
    print(string)
    ref = get_Morse_ref(mode)
    print(ref)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
