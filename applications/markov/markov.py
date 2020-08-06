import random



# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

    words_list = words.split(" ")
    for i, x in enumerate(words_list):
        if "\n" in x:
            split_words = x.split("\n")
            words_list[i] = split_words[0]
            words_list.extend(split_words[1:])

# TODO: analyze which words can follow other words
# Your code here
words_map = {}
start_words = []

for i in range(len(words_list) - 1): 
    next_word = words_list[i + 1]
    current = words_list[i]
    if len(current) > 1 and current[0] == "\"" and current[1].isupper():
        start_words.append(current)
    if current in words_map:
        words_map[current].append(next_word)
    else:
        words_map[current] = [next_word]

# TODO: construct 5 random sentences
# Your code here
punc_list = ".!?\""


def make_sentence():
    stopped = False
    word = random.choice(start_words)

    while not stopped:
        if len(word) > 1 and word[-1:] in punc_list:
            stopped = True
            print(word)
        elif len(word):    
            print(word, end=" ")

        word = random.choice(words_map[word])

make_sentence()



# for i in range(5):
#     make_sentence(random.choice(start_words))

