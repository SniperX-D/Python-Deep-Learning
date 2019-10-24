# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def init_dict():
    tel = {}
    for i in range(3):
        key = input("enter key")
        value = int(input("enter value"))
        tel[key] = value
    return tel

def check_key(dic):
     if (input("enter key") in dic) :
         print ("yes")
         return
     print("no")

def dicx():
    tel = {}
    for x in range(5):
        tel[x] = x**2
    return tel

def main():
    print(dicx())
    
    
if __name__ == "__main__":
        main()