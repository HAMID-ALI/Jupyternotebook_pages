import json
from difflib import get_close_matches

data = json.load(open("076 data.json"))


def translate(w):
    if w in data.keys():
        return "meaningig is %s" % data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print("Did yo mean instead of " + get_close_matches(w, data.keys())[0])
        cmd = input("Enter y for yes or n for exit: \n ")
        if cmd == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif cmd=="n":
            return "The entered word does not exist please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "Entered word does not exist."


word = input("Entera a word to get its meaning:  ")
output=translate(word)
if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)