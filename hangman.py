#==================================
#Python Hangman Game
#Created by Aidan Roos
#A simple word guessing game
#2020
#==================================

import sys
import time
import random

#Accessing secret_words.txt
file = open('secret_words.txt', 'r')

#Reading the words into an array of strings
word_list = file.readlines()

#Assigning a random word to a variable
word = random.choice(word_list)

def main():
    #Defining useful arrays to hold used letters
    #and the current progress of the users guesses
    letter_list = []
    used_letters = []
    progress = []
    count = 0

    #An array holding ASCII text representing hangman stages
    hang_man_design = [""" 
      +---+
      |   |
          |
          |
          |
          |
    =========
    """, """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """, """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """, """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """, """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """, """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """, """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """]

    #Appending the generated word's letter to an array
    for l in word:
        letter_list.append(l)

    #Main loop for taking input & error checking etc
    while True:

        #Getting input from the user
        guess = str(input("Guess:  "))

        #Checking if the users guess is valid
        #(not in the used letters array)
        if guess not in used_letters:

            #If the users guess is in the word...
            if guess in letter_list:
                for w in letter_list:
                    indices = [w for w, x in enumerate(letter_list) if x == guess]

                for every in word:
                    progress.append("_")

                for all in indices:
                    progress[all] = guess

                used_letters.append(guess)

                final = (progress[:len(word)])
                phrases = ['Nice job!', "You're on a roll!", 'Fantastic!', "Keep it up!"]
                print(random.choice(phrases))
                print(hang_man_design[count])
                print(' '.join(final))


                if final == letter_list:
                    print("YOU GOT THE WORD! HOORAY!")
                    time.sleep(20)
                    sys.exit()

            #If the users guess isn't in the word
            elif guess not in letter_list:
                if count == 5:
                    print("TOO MANY ATTEMPTS! YOU LOSE!")
                    sys.exit()
                try:
                    print("'{}' IS NOT IN THE WORD!".format(guess))
                    count += 1
                    print(hang_man_design[count])
                    print(' '.join(final))

                except:
                    print(len(word) * "_ ")

        #If the user guesses a used letter...
        elif guess in used_letters:
            print("Letter already used!")
            continue

#Displaying an elegant title screen
print("PY-MAN")
time.sleep(0.3)
print("Designed by Aidan Roos")
time.sleep(0.3)
input("Press 'Enter' to get started...")
print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""")

#Displaying correct number of blanks
print(len(word) * "_ ")

#Calling the main function to begin the game
main()
