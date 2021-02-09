


def oobify(phrase):
    phrase_parsed = []
    lower_vowels = ['a','e','i','o','u']
    upper_vowels = ['A','E','I','O','U']
    new_phrase = ""
    for char in phrase:
        phrase_parsed.append(char)
    # print('the list is:')
    # print(phrase_parsed)
    for element in phrase_parsed:
        if element in lower_vowels:
            element = 'oob'
        if element in upper_vowels:
            element = 'Oob'
        new_phrase += element
    return new_phrase

print(oobify("Batey"))



