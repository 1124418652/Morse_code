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
        
def Code(Morse_ref, string):                 #编码字符串
    code = []
    for chr in string:
        tmp = Morse_ref[chr]
        if(not tmp):
            print("can't find the Morse code\n")
            exit(1)
        code.append(tmp)
    code = '/'.join(code)
    return code
    
def Decode(letter_ref, Morse_code):          #解码字符串
    decode = []
    for chr in Morse_code:
        try:
            tmp = letter_ref[chr]
        except ValueError as e:
            print("can't find the Morse_code\n'")
        finally:
            decode.append(tmp)
    decode = ''.join(decode)
    return decode

if __name__ == "__main__":
    mode,str = get_string()
    string = pre_process(mode, str)
    ref = get_Morse_ref(mode)            #获取摩斯电码的参考表
    
    if mode == 'a':
        decode = Decode(ref, string)
        print("the result:")
        print(decode)
    
    else:
        code = Code(ref, string)
        print("the result:")
        print(code)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
