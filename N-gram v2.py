import random
from random import randint

# the base material
source = open("AI/sonnet 18.txt", "r")

# variables

n = 1
temperature = 0
line = True
word_count = 140

# functions

def ChooseStartWord():
    word = random.choice(list(words))
    word_a = str(word[0])
    word_b = str(word[1])
    print(word_a, word_b, end=" ")
    return word_b

def ChooseNextWord(word_a):
    #add loop that searches through the dict for list that has word_b as it's start word and picks one (based on amount of use + temp)
    str(word_a)
    dict_list = words.keys()
    for x in dict_list:
        if x[0] == word_a:
            print(x[1], end=" ")
            return x[1]
        else: 
            continue


# creating the dictionary that the result is based on
content = source.read()
content_strip = content.lower().strip(".?")
content_split = content_strip.split()

words = {}
word_list = []

for x in content_split:
    word_list.append(x)
    if len(word_list) > n:
        word_tuple = tuple(word_list)
        if word_tuple not in words:
            words.update({word_tuple:1})
            word_list.pop(0)
        elif word_tuple in words:
            words[word_tuple] = int(words.get(word_tuple)) + 1
            word_list.pop(0)
        else: continue


word = ChooseStartWord()

for x in range(0, word_count):
    next_word = ChooseNextWord(word)
    new_word = ChooseNextWord(next_word)
    word = ChooseNextWord(new_word)
    if x % 10 == 0:
        line = False
    else: line = True
    continue
