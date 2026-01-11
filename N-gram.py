import random
from random import randint

# the base material
source = open("AI/sonnet 18.txt", "r")

# variables

temperature = 0
line = True

# functions

def chooseWord(a):
   word = random.choice(list(words))
   if a == True:
       print(word, end=" ")
   if a == False:
       print(word)

# creating the dictionary that the result is based on
content = source.read()
content_strip = content.lower()

words = {}

for x in content_strip.split():
   if x not in words:
       new_word = x.strip(":,'-.")
       words.update({new_word:1})
   if x in words:
       words[x] = int(words.get(x)) + 1

for x in range(0, 140):
   chooseWord(line)
   if x % 10 == 0:
       line = False
   else: line = True