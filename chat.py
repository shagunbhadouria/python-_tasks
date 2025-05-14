import random 
import string

def generate_password(length, use_letters, use_digits, use_symbols): 
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
            characters += string.digits 
    if use_symbols: 
                characters += string.punctuation
    if not characters:
       print("Error: No character types selected.")
       return None
 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    print("Welcome to the Random Password Generator!") 
    try:
         length = int(input("Enter desired password length: ")) 
         if length <= 0:
             raise ValueError 
    except ValueError: 
      print("Invalid input. Please enter a positive integer.")
      return None

    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    return length, use_letters, use_digits, use_symbols

if __name__ =="__main__":
     prefs = get_user_preferences()
     if prefs:
          password = generate_password(*prefs) 
          if password:
             print(f"\nGenerated Password: {password}") 
             print("Keep it safe!")
    