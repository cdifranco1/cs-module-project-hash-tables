def no_dups(s):
    str_arr = s.split(" ")
    de_dups = {}
    for x in str_arr:
        if x not in de_dups:
            de_dups[x] = None

    str_arr = list(de_dups.keys())
    return " ".join(str_arr)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))


'''
create a set
split string into an array
for each word in array:
    try to add the word to the set

make the set into a list
join the list
'''
