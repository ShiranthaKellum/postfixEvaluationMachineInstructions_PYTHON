
from queue import LifoQueue                         # import queue module

stack = LifoQueue (maxsize=50)                      # declare the stack

tempCount = '1'                                     # count number of the temp variables

def addition ():
    x = stack.get ()                                # return the 1st popped element
    y = stack.get ()                                # return the 2nd popped element

    if 'a' <= y <= 'z' or 'A' <= y <= 'Z':          # check for a user input variable
        print ("    LD       ", y)

    else:
        print ("    LD      TEMP ", y)              # check for temp variable

    if 'a' <= x <= 'z' or 'A' <= x <= 'Z':          # check for a user input variable
        print("    AD       ", x)

    else:
        print("    AD      TEMP ",  x)              # check for temp variable
    
    global tempCount                                # specify as a global variable
    
    print ("    ST      TEMP ",  tempCount)
    stack.put(tempCount)                            # push temp variable
    tempCount = chr(ord(tempCount)+1)

def substraction ():
    x = stack.get()                                 # return the 1st popped element
    y = stack.get()                                 # return the 2nd popped element

    if 'a' <= y <= 'z' or 'A' <= y <= 'Z':          # check for a user input variable
        print("    LD      ", y)

    else:
        print("    LD      TEMP ", y)               # check for temp variable

    if 'a' <= x <= 'z' or 'A' <= x <= 'Z':          # check for a user input variable
        print("    SB       ", x)

    else:
        print("    SB      TEMP ", x)               # check for temp variable

    global tempCount
    print("    ST      TEMP ",  tempCount)
    stack.put(tempCount)                            # push temp variable
    tempCount = chr(ord(tempCount)+1)

def multipication ():
    x = stack.get()                                 # return the 1st popped element
    y = stack.get()                                 # return the 2nd popped element

    if 'a' <= y <= 'z' or 'A' <= y <= 'Z':          # check for a user input variable
        print("    LD      ", y)

    else:
        print("    LD      TEMP ", y)               # check for temp variable

    if 'a' <= x <= 'z' or 'A' <= x <= 'Z':          # check for a user input variable
        print("    ML       ", x)

    else:
        print("    ML      TEMP ", x)               # check for temp variable

    global tempCount
    print("    ST      TEMP ", tempCount)
    stack.put(tempCount)                            # push temp variable
    tempCount = chr(ord(tempCount)+1)
    
def division ():
    x = stack.get()                                 # return the 1st popped element
    y = stack.get()                                 # return the 2nd popped element

    if 'a' <= y <= 'z' or 'A' <= y <= 'Z':          # check for a user input variable
        print("    LD      ", y)

    else:
        print("    LD      TEMP ", y)               # check for temp variable

    if 'a' <= x <= 'z' or 'A' <= x <= 'Z':          # check for a user input variable
        print("    DV       ", x)

    else:
        print("    DV      TEMP ", x)               # check for temp variable

    global tempCount
    print("    ST      TEMP ",  tempCount)
    stack.put(tempCount)                            # push temp variable
    tempCount = chr(ord(tempCount)+1)
    
expression = input ()                               #'ABC*+DE-/, A+B/*C*+, AB+CD-*E+, ABCD+-*, AB+C*D/'

for i in expression:
    if 'a' <= i <='z' or 'A' <= i <= 'Z':           # if it is an alphabet, push
        stack.put (i)                               # push method

    elif i == '+':                                  # else (operators), functions are called
        addition ()

    elif i == '-':
        substraction ()

    elif i == '*':
        multipication ()

    else:
        division ()
