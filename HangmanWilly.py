# -*- coding: utf-8 -*-
"""
Hangman Game
JHub Coding Challenge Task
Created on Mon May 18 2020
@author: James Raraty
"""

import random

def readwords(): #get the list of words from file and shuffle
    words = []
    for line in open('word_list.txt'):
        words.append(line[:-1])
    random.shuffle(words)
    return words

def show(guessword,lives): #display lives remaining and current guess
    lifelives = 'lives'
    if lives == 1:
        lifelives = 'life'
    print(f'\nYou have {lives} ' + lifelives + ' remaining\n')
    print(f'The word is {guessword}\n')
    
def pickaletter(letters): #ask the player to guess a letter
    while True:
            try:
                nextletter=input("Please enter your next guess: ")[0]
            except:
                print ("\nInput must be a letter!")
                continue
            else:
                if nextletter in letters:
                    print ("\nYou've already guessed that letter, please try again")
                    continue
                elif not nextletter.isalpha():
                    print ("\nInput must be a letter!")
                    continue
                else:
                    return nextletter

def replay(): #ask the player whether to play again
    playagain = ""
    while playagain not in ["Y","N"]:
        playagain = input("Play again? (Y/N): ").upper()
    return playagain == "Y"

# Main routine starts here
# ========================
    
print ("\n\nWelcome to Hangman\n==================\n")

wordlist = readwords()

while True:
    lives = 7
    lettersguessed = []
    gameword = wordlist.pop()
    guessword = '*' * len(gameword)
    
    while True:
        show(guessword,lives)
        nextguess = pickaletter(lettersguessed) #ask player to guess a letter
        lettersguessed.append(nextguess) #remember which letters have been guessed
        if nextguess in gameword: #correct guess
            print(f"\nYes, the word contains the letter {nextguess}")
            newguessword = ''
            index = 0
            for letter in gameword:
                if letter == nextguess:
                    newguessword += letter
                else:
                    newguessword += guessword[index]
                index += 1
            guessword = newguessword
        else: #incorrect guess
            print(f"\nNo, the word does not contain the letter {nextguess}")
            lives -= 1 
            if lives == 0: #check if player has run out of lives
                print(f"\nSorry you lose! The word was {gameword}")
                break
        if guessword == gameword: #check if player has won
            print(f"\nCongratulations you win! The word was {gameword}")
            break
        
    print('\n---------------------------------')
    
    if replay(): #play again?
        continue
    else:
        break