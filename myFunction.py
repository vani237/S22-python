

import os

def hello():
    print("hello Dianna")

def hello1(name): 
    print(f"hello{name}")

hello1("Romeo")
hello1('Vianie')

def Addition(x,Y):
    print(x+Y)
Addition(2,5)  

def Addition2(x,y):
    return x+y
s=Addition2(5,2)
print(s)

def Commands(cmd):

    os.system(cmd)
def ClearScreen():
    os.system('clear')    
