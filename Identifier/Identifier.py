import sys
import pybase100 as base100

def Client():
    print("Type 'help' or 'h' for more information, 'use'or 'u' to get started, and 'quit' or 'q' to leave. \n>",end="")
    UserFeedback = input()
    while(UserFeedback != "quit" and UserFeedback != 'q'):
        if UserFeedback == "help" or UserFeedback == 'h':
            PrintInstruction()
        elif UserFeedback == "use" or UserFeedback == 'u':
            Identification()
        else:
            print("Input Error: No such function.")
        print("Type 'help' or 'h' for more information, 'use'or 'u' to get started, and 'quit' or 'q' to leave. \n>",end="")
        UserFeedback = input()
    sys.exit(0)

def PrintInstruction():
    print("This is the instruction.")

def Identification():
    ciphertext = input("Please input your ciphertext:\n")
    Plaintext={}
    #Identify some special encryption method.
    if isEmoji(ciphertext[0]):
        Plaintext["Base100"]= ""
    #Traverse the ciphertext and statistical character characteristics.

    #guess the coding method by using the exclusion method and work out the result.
    if "Base100" in Plaintext:
        Plaintext["Base100"]=base100.decode(ciphertext)
    #Give out possible answers.
    for ans in Plaintext:
        print("Method:"+ans+"    Plaintext:"+Plaintext[ans].decode('utf-8'))

def isEmoji(content):
    if not content:
        return False
    if u"\U0001F600" <= content and content <= u"\U0001F64F":
        return True
    elif u"\U0001F300" <= content and content <= u"\U0001F5FF":
        return True
    elif u"\U0001F680" <= content and content <= u"\U0001F6FF":
        return True
    elif u"\U0001F1E0" <= content and content <= u"\U0001F1FF":
        return True
    else:
        return False

#Below are the main function.
print("Welcome to Simple Encryption Type Identifier.\n")
print("Version: 0.1.0\n")
print("Functions now include: Base100.\n")
Client()