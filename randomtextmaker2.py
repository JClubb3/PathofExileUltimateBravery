from random import choice
from random import randint
import os


#Picks a random word from the Scrabble dictionary
def wordpick():
    word = choice(bigdict).strip()
    return word

#Has the user pick between iterations and size mode, and requires the user
#submits either S, s, I, or i; else asks again
def userstart():
    while True:
        user = input("Select mode: ")
        if user.lower() == "i" or user.lower() == "s":
            return user.lower()

#One of the two core functions. This one writes a user-specified number of
#30-word blocks to the file.
def iterations():
    #Asks the user for the number of iterations and forces the response to be
    #an integer greater than zero.
    while True:
        times = input("How many times should I write random text? Each time will be 30 words: ")
        if times.isdigit():
            times = int(times)
            if times > 0:
                break
        else:
            print("Please input a number.")
    #Runs wordwrite() times times, passing the current number to wordwrite as t
    for t in range(1, times+1):
        wordwrite(t)
        
#The second core function. The one will continue to write to the file until the
#file size is equal to or greater than the user-speficied size, again in 30-word
#blocks.
def size():
    #Asks the user for the file size and forces the response to be
    #an integer greater than zero.
    while True:
        maxsize = input("Specify a size for the file in bytes: ")
        if maxsize.isdigit():
            if int(maxsize) > 0:
                break
    size = os.path.getsize(file)
    t = 1
    #Runs wordwrite() as many times as need to get the file to proper size.
    #T is the iteration number.
    while size <= int(maxsize):
        wordwrite(t)
        t += 1
        size = os.path.getsize(file)
    
#The meat of the program. Writes one word to the file at a time, each calling
#writing a total of 30 words into a whitespace-seperated paragraph illusion,
#adding puncuation marks randomly. The t variable is the iteration, defined
#differently in size() and iterations(), the two functions that call wordwrite().
def wordwrite(t):
    #print statement just so the user can see things are happening
    print("Writing to {0}, iteration {1}.".format(file, t))
    #mark is used for puncuation marks
    mark = ""
    for i in range(1,31):
        #calling the wordpick() function to pick a word from sowpods.txt
        word = wordpick()
        #a grammer mark is added based on a random integer, with a 20%
        #chance of any character being added
        grammar = randint(1,5)
        if grammar == 1:
            #5 marks can be made, with period having twice the chance to roll
            mark = randint(1,6)
            if mark == 1 or mark == 2:
                mark = "."
                guesser = 1
            elif mark == 3:
                mark = ","
            elif mark == 4:
                mark = ":"
            elif mark == 5:
                mark = ";"
            #apostraphe or apostraphe s can be added; which is decided by the
            #last letter of the word; if an s, only an apostraphe
            elif mark == 6:
                if word[-1:] == "S":
                    mark = "'"
                else:
                    mark = "'s"
        #if grammar above rolls anything apart from a 1, no mark is added
        else:
            mark = ""
        #This case handles the first word of a block, titlecasing it
        if i == 1:
            with open(file, 'a') as open_file:
                open_file.write(word.title() + mark + " ")
        #This case is for the last iteration in a block, adding a period
        elif i == 30:
            with open(file, 'a') as open_file:
                open_file.write(word.lower() + ".")
        #All other iterations take this case, which checks if the last word
        #ended with a period. If so, will titlecase and write the word, along
        #with any marks. If not, will lowercase and write the word, again with
        #marks as needed.
        else:
            #Reads the last two characters of the file (in binary mode).
            #Binary mode is used because nonbinary mode crashes. Don't know
            #why that happens.
            with open(file, 'rb') as open_file:
                open_file.seek(-2,2)
                period = open_file.read()
            #Checks the first character of the string of the last two
            #characters of the file. If it is a period (binary/ASCII code
            #46), will title case the word being written. Else, lowercases it
            if period[0] == 46:
                with open(file, 'a') as open_file:
                    open_file.write(word.title() + mark + " ")
            else:
                with open(file, 'a') as open_file:
                    open_file.write(word.lower() + mark + " ")
    #Adds two newlines to text at end of filethe end of every 30 word block, to make the
    #paragraph illusion more complete
    with open(file, 'a') as open_file:
        open_file.write("\n" + "\n")


#main function
if __name__=="__main__":
    #opens the sowpods.txt file, which is the Scrabble official dictionary,
    #and saves its contents
    with open("sowpods.txt", "r") as f:
        bigdict = f.readlines()
    #Welcome and explanation text
    print("Welcome to RandomTextMaker. Please see README for instructions.")
    print("Use s to select size mode, or i to select iterations mode.")
    #First, has the user pick a mode
    user = userstart()
    #Then has the user name a file, then creates it or adds to it a line of text
    file = input("Name the file to write to: ")
    with open(file, 'a') as f:
        f.write("Randomly generated text document \n Made using randomtextmaker from J Clubb \n \n")
    #Selects the apporpriate mode based on the user choice
    if user == "i":
        iterations()
    elif user == "s":
        size()
    #Final message to let the user know the job is done
    print("All done. File is {} bytes.".format(os.path.getsize(file)))
