"""
Your job is to complete the definitions of each function so that it achieves its indicated behavior.

Do not run this file directly... 
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

def bark():
  """
  Asks the user to enter the name, age, and breed of a dog, as three separate inputs.  
  Then prints out a bark message on behalf of the dog, in the following format:
    'Spot, the 4 year old Schnauzer, says, "Woof!"'
  Requirements: 
    1. The proper nouns (name and breed) must be capitalized in the output, as is standard in English writing, regardless of how the user entered them.
  """
  name = input("What's the name of this dog? ")
  age = input("How old is the dog? ")
  breed = input("What's the breed of this dog? ")
  print(f'{name.capitalize()}, the {age} year old {breed.capitalize()}, says, "Woof!"')
        
def bark_with_validation():
  """
  Do everything the same as in the previous bark() function, with the following additional validation requirements:

  Requirements: 
    2. If the user enters an invalid name, the string, "Name error!", must be printed and nothing else.  An invalid name is any input that is not 2 or more alphabetic characters.
    3. If the user enters an invalid age, the string, "Age error!", must be printed and nothing else.  An invalid age is any input that is not an integer between 0 and 15, inclusive.
    4. If the user enters an invalid breed, the string, "Breed error!", must be printed and nothing else.  An invalid breed is any breed that is not in the list, ["Schnauzer", "Terrier", "Poodle", "Mastiff"]
  """
  name = input("What's the name of this dog? ")
  if len(name) < 2 or not name.isalpha():
      print("Name error!")
      return
  
  age = input("How old is the dog? ")
  if not age.isdigit() or int(age) < 0 or int(age) > 15:
      print("Age error!")
      return
  
  breed = input("What's the breed of this dog? ").lower()
  if breed.capitalize() not in ["Schnauzer", "Terrier", "Poodle", "Mastiff"]:
      print("Breed error!")
      return
  
  print(f'{name.capitalize()}, the {age} year old {breed.capitalize()}, says, "Woof!"')

def respond_to_anything():
  """
  Ask the user to input a sentence.  Print a response based on the input according to the requirements below.

  Requirements: 
    1. If the user enters text ending in the "." character, print the response, "That's true."
    2. If the user enters text ending in the "?" character, print the response, "I'm sorry, I don't know."
    3. If the user enters text ending in the "!" character, print the response, "Exciting!"
    4. If the user enters text that does not include a punctuation mark at the end (punctuation marks include ".", "?", and "!"), print the response, "Please include a punctuation mark at the end of your sentence!"
  """
  sentence = input("Enter a sentence: ")
  if sentence[-1] == ".":
    print("That's true.")
  elif sentence[-1] == "?":
    print("I'm sorry, I don't know.")
  elif sentence[-1] == "!":
     print("Exciting!")
  elif sentence[-1] != "." or sentence[1] != "?" or sentence[-1] != "!":
     print("Please include a punctuation mark at the end of your sentence!")


def respond_to_anything_but_nonsense():
  """
  Do everything the same as in the previous respond_to_anything() function, with the following additional validation requirements:

  Requirements:
    5. If the user includes the word, 'nonsense', anywhere in the response, regardless of capitalization, do not print any output.
  """
  sentence = input("Enter a sentence: ")
  if sentence.lower().find("nonsense") != -1:
    return
  elif sentence[-1] == ".":
    print("That's true.")
  elif sentence[-1] == "?":
    print("I'm sorry, I don't know.")
  elif sentence[-1] == "!":
    print("Exciting!")
  elif sentence[-1] != "." or sentence[1] != "?" or sentence[-1] != "!":
    print("Please include a punctuation mark at the end of your sentence!")