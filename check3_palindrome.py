def check_palindrome(text):
  if text == text[::-1]:
    print(f"{text} is a palindrome")
  else:
    print(f"{text} is not a palindrome")
choice = input("Enter 't' for text or 'f' for file:")
if choice == "t":
   text = input("Enter text to check for palindrome:")
   check_palindrome(text)
elif choice == "f":
  
  try:
       file = input("Enter filepath for palindrome check:")
       text = open(file, "r").read()
       check_palindrome(text)
  except(OSError):
        print(f"Unable to process file at {file}")
  else:
       print("Invalid choice")

import random 

def guess_number():
    number = random.randint(1, 100)
    while True:
        guess = input("Guess a number between 1 and 100, or 'q' to quite: ")
        if guess.lower()== 'q':
            print(f"The number was {number}.")
            break
        try:
            guess = int(guess)
            if guess == number:
                print("Congratulation! You guessed the correct number.")
                break
            else:
                print("Incorrect guess. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")



guess_number()
