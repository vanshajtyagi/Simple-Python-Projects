from tkinter import *
import pyperclip
import random
root = Tk()
root.geometry("400x400")
passStr = StringVar()
passLen = IntVar()
passLen.set(0)

def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', '.', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')','~','-','_','[',']','{','}',':',';','<','>','?','/']
    password = ""
    for x in range(passLen.get()):
        password = password + random.choice(pass1)
    
    passStr.set(password)

def copytoclipboard():
    randomPassword = passStr.get()
    pyperclip.copy(randomPassword)

Label(root,text="PassWord Generator Application",font="calibri 20 bold").pack()
Label(root, text="Enter password length").pack(pady=3)
Entry(root, textvariable=passLen).pack(pady=3)
Button(root, text="Generate Password", command=generate).pack(pady=7)
Entry(root, textvariable=passStr).pack(pady=3)
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()
Label(root, text="Made by Vanshaj",font="calibri 16 italic").place(x=170,y=230)

root.mainloop()
