# Your code here

ignored = '\" : ; , . - + = / \\ | [ ] { } ( ) * ^ &?!'.replace(" ", "")


class Histogram:
    def __init__(self, file):
        self.store = {}
        self.longest_word_length = 0
        self.read_file(file)

    def read_file(self, file):
        with open(file) as f:
            for line in f:
                words_arr = line.split(" ")
                for x in words_arr:
                    for l in ignored:
                        x = x.replace(l, "")
                    x = x.lower()
                    x = x.rstrip()
                    self.longest_word_length = max(len(x), self.longest_word_length)
                    if x in self.store:
                        self.store[x] += 1
                    else:
                        self.store[x] = 1

    def display_all_data(self, order=None):
        if order == "alphabetical":
            alph_list = sorted(list(self.store.items()), key=lambda x: x[0])
        elif order == "frequency":
            alph_list = sorted(list(self.store.items()), key=lambda x: x[1], reverse=True)
        else:
            alph_list = list(self.store.items())
        for key, value in alph_list:
            self.display_word(key, value)
        
    def display_word(self, word, freq):
        histo_str = "" 
        while freq > 0:
            histo_str = f'{histo_str}#'
            freq -= 1
        word = word + (" " * (self.longest_word_length - len(word)))
        print(word, histo_str)
            


h = Histogram("./robin.txt")
