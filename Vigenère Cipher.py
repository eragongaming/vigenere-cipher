import string

#Polyalphabetic cipher that is known as a Vingenere Cipher

#Initializing Variables
alphabet='abcdefghijklmnopqrstuvwxyz'
tabula_value={}
tabula_alphabet={}
accum1=0
accum2=0
output=''
key_value=[]
phrase_value=[]
cipher_value=[]

#Creating dictionaries to act as the Tabula Recta
for x in alphabet:
    tabula_alphabet[x]=accum1
    accum1+=1
for x in alphabet:
    tabula_value[accum2]=x
    accum2+=1

#Gathering user inputs
choice=input("Type either 'Encryption' or 'Decryption': ").lower()
print("")
key=list(input("Enter the key: ").lower())
print("")
key[:]=[x for x in key if (x!=' ' and (x not in string.punctuation))]

#The core method is where phrase manipulation happens
def core(method,key):
    output=''
    phrase=list(input("Enter the phrase for {}: ".format(method)).lower())  #User inputs phrase to be changed
    while len(key)<len(phrase):     #expanding key to phrase length
        key+=key
    for letter in key:      #Using the dictionary to get value of letters
            key_value.append(tabula_alphabet[letter])
    for letter in phrase:   #Using the dictionary to get value of letters
        if letter in alphabet:
            phrase_value.append(tabula_alphabet[letter])
        else:
            phrase_value.append(letter)   #Adding non-dictionary items such as punctuation and spaces
    for value in range(len(phrase)):
        if type(phrase_value[value])==int:
            if method=='decryption':        #if statements determine encryption or decryption of phrase
                cipher_value=abs(key_value[value]-phrase_value[value])
                output+=tabula_value[cipher_value]
            else:
                cipher_value=key_value[value]+phrase_value[value]
                while cipher_value>25:
                    cipher_value=cipher_value-26
                output+=tabula_value[cipher_value]
        else:       #This is where punctuation and spaces go
            phrase_value.insert(0,phrase_value[value])  #Insert the character at the start of the list to maintain length
            output+=phrase_value.pop(value+1)           #remove the character from the list and add to output (must be removed to match up with key)
    return output

#calling the core function
result=core(choice,key)
print("")
print(result)

