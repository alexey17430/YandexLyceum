file = open('cyrillic.txt', mode='r', encoding='UTF-8')
ans = open('transliteration.txt', mode='w')
lines = file.read()
dictionary = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
              "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
              "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
              "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
              "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
              "б": "b", "ю": "ju", "ё": "jo"}
new_line = ''
for letter in lines:
    if letter in dictionary.keys():
        new_line += dictionary[letter]
    elif letter.lower() in dictionary.keys():
        new_line += dictionary[letter.lower()].title()
    else:
        new_line += letter

print(new_line, file=ans)