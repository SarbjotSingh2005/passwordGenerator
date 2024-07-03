#Project of Codsoft internship 
#Project name :- Password generator
import random 
import secrets
import string 
print('''welcome to password generator!
        created by :- Sarbjot singh''')
#take the length by user for the password
password_length = int(input(" enter the length of password:-"))
print(''' select the character datatype which are mentioned below:-
      1. numbers 
      2. Alphabets
      3. Special symbols 
      4. Exit ''')
# check this input that it should be more than 8
list_of_character = " "
# now get the character datatype from user
while(True):
    choice = int(input(" pick a datatype from mentioned above:-"))
    if(choice==1):
        list_of_character += string.ascii_letters
    elif(choice==2):
        list_of_character+= string.digits
    elif(choice==3):
        list_of_character+=string.punctuation
    elif(choice==4):
        break 
    else:
        print(" choose a valid option ! ")
Password = []
for i in range(password_length):
    #selecting a random character from list of character
    randomchar = random.choice(list_of_character)
    Password.append(randomchar)
print("The password suggestion is:-"+" ".join(Password))