import random
import itertools
from nltk.corpus import words
from nltk.corpus import wordnet

word_list = words.words()
stage = 0

print("Welcome to my hangman game!")
print("Choosing random word from English dictionary...")

word = random.choice(word_list)
Wlen = (len(word))
print(("The word is %d letters long") % Wlen)

blanks = list(itertools.repeat(" ___ ",Wlen))
#print(blanks) #test
letters = list(word)
print(letters) #test
wrongs = []

#Hangman stages
stage1 =  """
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|
"""
stage2 = """
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|
"""
stage3 = """
   ____
  |    |
  |    o
  |    |
  |
  |
 _|_
|   |______
|          |
|__________|
"""
stage4 = """
   ____
  |    |
  |    o
  |   /|
  |
  |
 _|_
|   |______
|          |
|__________|
"""
stage5 = """
   ____
  |    |
  |    o
  |   /|\.
  |
  |
 _|_
|   |______
|          |
|__________|
"""
stage6 = """
   ____
  |    |
  |    o
  |   /|\.
  |    |
  |
 _|_
|   |______
|          |
|__________|
"""
stage7 = """
   ____
  |    |
  |    o
  |   /|\.
  |    |
  |   /
 _|_
|   |______
|          |
|__________|
"""
stage8 = """
   ____
  |    |
  |    o
  |   /|\.
  |    |
  |   / \.
 _|_
|   |______
|          |
|__________|
 """
stages = [stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8]
print(stages[0]) #prints empty hangman image

while ((stage > 6) or (" ___ " not in blanks))==False:

    print("Make a guess: ")
    guess = input("> ")

    if guess in letters:
        print(("Your guess %s was correct!") %guess)
        occurences = [i for i, x in enumerate(letters) if x == guess]

        for dupe in occurences:
            blanks[dupe] = guess
    else:
        print(("Your guess %s was wrong!") %guess)
        wrongs.append(guess)
        stage = stage + 1

    print("[%s]" % ' '.join(map(str, blanks)))
    print("Wrong guesses so far: ",wrongs)
    print("Stage: ",stage) #test
    print(stages[stage])


if stage == 7:
    print("You lose!")
else:
    print("You won!")

syns = wordnet.synsets(word)

print("The word was... %s" % word)

try:
    meaning = syns[0].definition()
    print("It means: %s" % meaning)
except IndexError:
    print("Google the word to find its meaning!")
