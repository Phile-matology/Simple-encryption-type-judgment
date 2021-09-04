import sys
import pybase100 as base100
import base64
import base58
import re

global Pattern 
Pattern ={"Base64":"^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{4}|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)$",
          "Base32":"^([A-Z2-7]{8})*(([A-Z2-7]{8})|([A-Z2-7]{7}=)|([A-Z2-7]{5}===)|([A-Z2-7]{4}====)|([A-Z2-7]{2}======))$",
          "Base16":"^([A-F0-9]{2})*$",
          "Base58":"^[A-HJ-NP-Za-km-z1-9]*$",
          "Base85":"^[!\"#\$%&'\(\)\*\+,-\./0-9:;<=>\?@A-Z\[\\\]\^_`a-u]*$"}

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
    #Matching ciphertext using regular expressions
    '''
    在这里我有一个想法，应该可以通过统计密文长度关系排除一部分不应匹配的加密方式。
    另一个想法是，开一个选项，让用户设置是省略不匹配的直接放弃，还是以replace的方式弄出来，毕竟有可能有密文有点损失？
    '''
    global Pattern
    for Pt in Pattern.keys():
        if re.match(Pattern[Pt],ciphertext):
            Plaintext[Pt]=""
    #guess the coding method by using the exclusion method and work out the result.
    if "Base100" in Plaintext:
        Plaintext["Base100"]=base100.decode(ciphertext)
    if "Base64" in Plaintext:
        Plaintext["Base64"]=base64.b64decode(ciphertext)
    if "Base32" in Plaintext:
        Plaintext["Base32"]=base64.b32decode(ciphertext)
    if "Base16" in Plaintext:
        Plaintext["Base16"]=base64.b16decode(ciphertext)
    if "Base58" in Plaintext:
        Plaintext["Base58"]=base58.b58decode(ciphertext)
    if "Base85" in Plaintext:
        Plaintext["Base85"]=base64.b85decode(ciphertext)
    #Give out possible answers.
    for ans in Plaintext:
        try:
            print("Method:"+ans+"    Plaintext:"+Plaintext[ans].decode(encoding='utf-8'))
        except UnicodeDecodeError:
            print("Method:"+ans+"    Matched but decoding error, this may be a wrong way.")

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
print("Version: 0.1.1\n")
print("Functions now include: Base100, Base64,Base16.\n")
Client()