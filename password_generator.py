iimport random #This module implements pseudo-random number generators. 
import string #This module lets you do stuff with strings

#get input from the user. Find out their password needs
min_len = int(input("Your password must be at least how many characters long? Please enter a number: ")) #int() converts user input to integer since input() returns string
has_number = input("Do you want your password to include numbers? (Y/N) ").upper() == "Y" 
has_special = input("Do you want to have special characters? (Y/N) ").upper() == "Y"
#the upper() method converts user input to uppercase and 
#The '==' operator asks if the two values on either side are equal. 
#Hence why both has_number and has_special return True
#regardless of whether the user enters and uppercase or lowercase 'y'. 

#function to generate password. 
#the parameters reflect the user's pw needs. 
#number and sp_char are optional
def generate_password(min_len, numbers=True,sp_char=True):
    
    #these variables hold built-in constants of the string module
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #creates list of usable, possible characters for the user's pw 
    characters = letters
    if numbers:
        characters += digits
    if sp_char:
        characters += special
    
    #user pw and initializes variables to be used in the following loop. 
    pwd = ""
    criteria_met = False
    has_number = False
    has_special = False 

    #Loop to choose characters until password requirements are met
    while not criteria_met or len(pwd) < min_len:
        new_character = random.choice(characters)
        pwd += new_character
    
        #check to see if pw contains a number if it needs to and/or a special character if it needs to
        if new_character in digits:
            has_number = True
        elif new_character in special:
            has_special = True 

        #check to see if pw meets user's criteria
        criteria_met = True
        if numbers:
            criteria_met = has_number
        if sp_char:
            criteria_met = has_special
    return pwd 

pwd = generate_password(min_len, has_number, has_special) 
#the parameter names when called don't have to exactly match the definition. 
print("Your password is: ", pwd)
generate_password(min_len)   
