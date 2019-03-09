import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yesno = input("Did you mean '%s' instead? Enter Y for YES and N for NO: " % get_close_matches(word, data.keys())[0])
        if yesno == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yesno == 'N':
            return "The entered word '%s' doesn't exist. Please re-check it" %entered_word
        else:
            return "We didn't understand your entry."
    else:
        return "The entered word doesn't exist. Please re-check it"

entered_word = input("Enter any word you want to know the meaning of: ")
#entered_word = entered_word.lower()

output = meaning(entered_word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
