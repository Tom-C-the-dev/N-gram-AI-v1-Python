import random
from random import randint

# the base material
source = open("AI/sonnet 18.txt", "r")

# variables

n = 1 
temperature = 1
line = False
word_count = 140

# functions

def ChooseStartWord():
    word = random.choice(list(words))
    word_a = str(word[0])
    word_b = str(word[1])
    print(word_a, word_b)
    return word_b

def ChooseNextWord(word_a):
    str(word_a)
    dict_list = words.keys()
    next_words = []
    next_words_weights = []
    for x in dict_list:
        if x[0] == word_a:
            next_words.append(x[1])
            next_words_weights.append(float((int(words.get(x))*10) * (1 + temperature))) # linear scaling of weights depending on temperature
    if not next_words:
        return ChooseStartWord()
    word_next = random.choices(next_words, weights=(next_words_weights), k=1)
    return str(word_next[0])

# creating the corpus that the result is based on
content = source.read()
content_strip = content.lower().strip(".?;,")
content_split = content_strip.split()

words = {}
word_list = []

# creating the keys + counting them

for x in content_split:
    word_list.append(x)
    if len(word_list) > n:
        word_tuple = tuple(word_list)
        if word_tuple not in words:
            words.update({word_tuple:1})
            word_list.pop(0)
        elif word_tuple in words:
            word_tuple_value = int(words.get(word_tuple)) + 1
            words.update({word_tuple:word_tuple_value})
            word_list.pop(0)
        else: continue

# text generation

word = ChooseStartWord()

for x in range(0, word_count):
    next_word = ChooseNextWord(word)
    print(next_word)
    new_word = ChooseNextWord(next_word)
    print(new_word)
    word = ChooseNextWord(new_word)
    print(word)
