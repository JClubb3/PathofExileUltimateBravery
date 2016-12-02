# hangman
This is a Hangman game written in Python, using the Scrabble dictionary to randomly choose the word.

sowpods.txt is the Scrabble dictionary from which hangman.py pulls its words. The file will need to be located in the same directory that hangman.py is in, or else hangman.py (in the wordpick() function) will need to be editted to the file location of sowpods.txt.

The file itself is executable and so can be ran normally, but is written in Python 3.5 so a base Linux install will need to get the newer version of Python to run it.

Definitions of the word can be checked, which uses requests and BeautifulSoup to connection to dictionary.com and retreive the part of speech and definition of the word. Obviously this requires an internet connection.
