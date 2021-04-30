# -*- coding: utf-8 -*-

import tkinter as tk, re
from .Calculator import Calculator

class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Calculator')
        self.addScreen()
        self.addButtons()
        self.operation = ""
        return

    def clicked(self, value, state):
        screenText = self.screen.get(1.0, tk.END)
        if state:
            if screenText.strip() == "Error":
                print("Nothing")
            elif value == "=":
                self.screen.configure(state="normal")
                res = self.processEntry(screenText)
                if res is False:
                    self.screen.delete(1.0, tk.END)            
                    self.screen.insert(tk.END, "Error")
                else:
                    self.screen.delete(1.0, tk.END)            
                    self.screen.insert(tk.END, res)
                self.screen.configure(state="disable")
            else:
                self.screen.configure(state="normal")
                self.screen.insert(tk.END, value)
                self.screen.configure(state="disable")
        else:
            self.screen.configure(state="normal")
            self.screen.delete(1.0, tk.END)            
            self.screen.configure(state="disable")

    def addScreen(self):
        self.screen = tk.Text(self.master, state='disabled', width=30, height=1, background='#f5f5f5', foreground='#232323', font=('monospace', 24))
        self.screen.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

    def processEntry(self, string):
        if re.match(r"^(\d+[+])+\d$", string.strip()):
            data = self.getValues("+", string)
            result = (Calculator()).add(data)
        elif re.match(r"^(\d+-)+\d$", string):
            data = self.getValues("-", string)
            result = (Calculator()).substract(data)
        elif re.match(r"^(\d+\*)+\d$", string):
            data = self.getValues("*", string)
            result = (Calculator()).multiply(data)
        elif re.match(r"^(\d+/){1}\d$", string):
            data = self.getValues("/", string)
            result = (Calculator()).div(data)
        elif re.match(r"^(\d+\D)+$",string.strip()) or re.match(r"^(\d+[+-/*])+\D$",string.strip()):
            result = False
        elif re.match(r"\d+", string.strip()):
            result = string.strip()
        else:
            result = False

        return result

    def getValues(self, separator, data):
        arr = data.strip().split(separator)
        return [ int(x) for x in arr]

    def createButtons(self):
        buttons = []
        button1 = tk.Button(self.master, text=7, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(7,True))       
        button2 = tk.Button(self.master, text=8, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(8,True))       
        button3 = tk.Button(self.master, text=9, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(9,True))       
        button4 = tk.Button(self.master, text="/", width=9, height=1, font=("monospace",15), command=lambda:self.clicked("/",True))       
        button5 = tk.Button(self.master, text=4, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(4,True))       
        button6 = tk.Button(self.master, text=5, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(5,True)) 
        button7 = tk.Button(self.master, text=6, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(6,True))       
        button8 = tk.Button(self.master, text="*", width=9, height=1, font=("monospace",15), command=lambda:self.clicked("*",True))       
        button9 = tk.Button(self.master, text=1, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(1,True))       
        button10 = tk.Button(self.master, text=2, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(2,True))       
        button11 = tk.Button(self.master, text=3, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(3,True))       
        button12 = tk.Button(self.master, text="+", width=9, height=1, font=("monospace",15), command=lambda:self.clicked("+",True))       
        button13 = tk.Button(self.master, text=0, width=9, height=1, font=("monospace",15), command=lambda:self.clicked(0,True))       
        button14 = tk.Button(self.master, text="DEL", width=9, height=1, font=("monospace",15), command=lambda:self.clicked("DEL",False))       
        button15 = tk.Button(self.master, text="=", width=9, height=1, font=("monospace",15), command=lambda:self.clicked("=",True))       
        button16 = tk.Button(self.master, text="-", width=9, height=1, font=("monospace",15), command=lambda:self.clicked("-",True))       

        buttons.append(button1)
        buttons.append(button2)
        buttons.append(button3)
        buttons.append(button4)
        buttons.append(button5)
        buttons.append(button6)
        buttons.append(button7)
        buttons.append(button8)
        buttons.append(button9)
        buttons.append(button10)
        buttons.append(button11)
        buttons.append(button12)
        buttons.append(button13)
        buttons.append(button14)
        buttons.append(button15)
        buttons.append(button16)        

        return buttons

    def addButtons(self):
        buttonsToAdd = self.createButtons()
        flag = 0
        for i in range(1,5):
            for j in range(4):
                buttonsToAdd[flag].grid(row=i, column=j)
                flag += 1
