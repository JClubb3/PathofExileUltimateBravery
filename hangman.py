#!/usr/bin/python3.5

from random import choice
import requests
import re
from bs4 import BeautifulSoup
import sys
from colorama import init, Fore
init(autoreset=True)

#Using choice() to pick a word and strip() to remove whitespace
def wordpick():
    with open("sowpods.txt", "r") as f:
        #Scrabble dictionary from which the word is chosen
        bigdict = f.readlines()
    word = choice(bigdict).strip()
    return word

#splitting the word into a list to make letter checking and eliminating easier
#probably not strictly necessary but I don't want to rework the logic
def listmake(word):
    for l in word:
        wordlist.append(l)

#build a board of underscores equal to the number of letters in the word
def boardreset():
    global board
    board = []
    for i in range(len(wordlist)):
        board.append("_ ")

#printing the board to the screen
def boardprint():
    global board
    for i in board:
        print(i, end='')

#player guessing here
def user(guessed):
    global define, partofspeech
    print("")
    guessedprint(guessed)
    while True:
        guess = input("Guess a letter: ")
        #pulls the defintion of the word if not yet run. If defcheck() has been
        #run already, uses the old value for efficiancy.
        if guess.lower() == "def":
            if len(partofspeech) < 1:
                definition = defcheck()
            else:
                print(Fore.YELLOW + partofspeech)
                for i in define:
                    print(Fore.YELLOW + i, end =" ")
                print("\n")
        #checks that user choice is exactly 1 letter before moving on
        elif guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Please choose only one letter.")
    print("\n" * 2)
    guess = guess.upper()
    return guess

#checking if the guess is in the word, and if so changing the same location in
#board to the letter guessed.
def letcheck(guess, wordlist, guessed):
    global board
    if guess in wordlist and guess not in guessed:
        positions = [pos for pos, char in enumerate(wordlist) if char == guess]
        for pos in positions:
            board[pos] = guess + " "
        guessed.append(guess)
    elif guess in guessed:
        print("You already guessed that!")
        print("")
    elif guess not in wordlist:
        print(Fore.RED + "Sorry, nope!")
        guessed.append(guess)
        wrong()
        print("")

#Function for incorrect guesses: builds the hangman and ends the game.
def wrong():
    global errors, word
    errors += 1
    killem()
    if errors == 6:
        drawhang()
        print(Fore.RED + "He's dead, Jim!")
        print(Fore.BLUE + "The word was: {0}".format(word))
        playagain()

#checking for winning by the contents of board
def wincheck():
    global board
    if "_ " not in board:
        drawhang()
        boardprint()
        print("")
        print(Fore.GREEN + "You win!")
        playagain()

#Shows the user the letters already used
def guessedprint(guessed):
    print("")
    print("Letters already used: ")
    for i in sorted(guessed):
        print(i + " ", end = '')
    print("")

#asks the player to play again or leave, and resets values if yes
def playagain():
    while True:
        user = input("Play again? (y/n) ")
        if user.lower() == "y":
            #pulls global values and resets them all
            global guessed, word, wordlist, errors, toprint, define, partofspeech
            errors = 0
            define = ''
            partofspeech = ''
            guessed = []
            wordlist = []
            hangmanreset()
            word = wordpick()
            listmake(word)
            #print(word) #debug code
            boardreset()
            game()
        elif user.lower() == "n":
            sys.exit()

"""             [[ _______]
                 [ |     |]
                 [ O     |]
                 [\|/    |]
                 [ |     |]
                 [/ \    |]
                 [       |]
                 [-------|]]"""
#Builds an empty gallows
def hangmanreset():
    global hanger
    hanger = [[" ","_","_","_","_","_","_","_"],
              [" ","|"," "," "," "," "," ","|"],
              [" "," "," "," "," "," "," ","|"],
              [" "," "," "," "," "," "," ","|"],
              [" "," "," "," "," "," "," ","|"],
              [" "," "," "," "," "," "," ","|"],
              [" "," "," "," "," "," "," ","|"],
              [" "," "," "," "," "," "," ","|"],
              ["-","-","-","-","-","-","-","|"]]

#Draws the gallows and whatever is on it
def drawhang():
    global hanger
    for lst in hanger:
        for char in lst:
            print(char, end="")
        print("")

#Kills the poor guy
def killem():
    global hanger, errors
    if errors == 1:
        hanger[2][1] = "O"
    elif errors == 2:
        hanger[3][1] = "|"
        hanger[4][1] = "|"
    elif errors == 3:
        hanger[3][0] = "\\"
    elif errors == 4:
        hanger[3][2] = "/"
    elif errors == 5:
        hanger[5][0] = "/"
    elif errors == 6:
        hanger[5][2] = "\\"

#uses requests and beautifulsoup to pull the definition and part of speech of
#the word.
def defcheck():
    global word, partofspeech, define
    url = "http://www.dictionary.com/browse/{0}?s=t".format(word)
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html,"html.parser")

    notfound = soup.find(class_="closest-result")

    if notfound:    
        print(Fore.YELLOW + "No result found, sorry.")
        partofspeech = "No result found, sorry."
        print("\n")
    else:            
        partofspeech = soup.find(class_="dbox-pg")
        partofspeech = partofspeech.text
        print(Fore.YELLOW + partofspeech)
        
        define = soup.find(class_="def-content")
        define = define.text
        define = re.sub(r"^.", "", define)
        define = re.sub(r"^\s*", "", define)
        define = define.split()
        for i in define:
            print(Fore.YELLOW + i, end =" ")
        print("\n")


#the main function, calling the other functions in order.
#made into a function to be callable by playagain()
def game():
    print(Fore.CYAN + "Hangman!")
    print(Fore.YELLOW + "This uses a random word from the Scrabble dictionary, and they are not easy.")
    print(Fore.LIGHTMAGENTA_EX + "Type \"def\" to retrieve the part of speech and defintion of the word from dictionary.com")
    while True:
        drawhang()
        print("")
        boardprint()
        guess = user(guessed)
        letcheck(guess, wordlist, guessed)
        wincheck()

#initialize the global errors and run the game
if __name__=="__main__":
    global word
    wordlist = []
    guessed = [] #list to hold the letters already guessed by the player
    errors = 0
    define = ''
    partofspeech = ''
    hangmanreset()
    word = wordpick()
    listmake(word)
    #print(word) #debug code
    #print(wordlist) #debug code
    boardreset()
    game()

#I'm probably using too many globals when I could be using returns instead
#but it works
