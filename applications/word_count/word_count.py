import re

def word_count(s):
    # Your code here
    if not s:
        return {}
    counter = {}
    ignored = "\":;,=/\\|[]{}()*^&\t\n.+-"
    words_arr = re.split("[\n\t\r ]", s)
    for x in words_arr:
        x = x.strip(ignored)
        x = x.lower()
        if x in counter:
            counter[x] += 1
        elif len(x):
            counter[x] = 1
     
    return counter  



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))


## Output

'''
It returns a dictionary of words and their counts:

```
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
```

Case should be ignored. Output keys must be lowercase.

Key order in the dictionary doesn't matter.

Split the strings into words on any whitespace.

Ignore each of the following characters:

```
" : ; , . - + = / | [ ] { } ( ) * ^ &
```

If the input contains no ignored characters, return an empty dictionary.
'''
