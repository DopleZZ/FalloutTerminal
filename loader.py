import json
import random

with open("data.json", 'r') as data_file:
    data = json.load(data_file)

trash_symbols = data["trash_symbols"]
words_easy = data["words_easy"]
words_medium = data["words_medium"]
words_hard = data["words_hard"]

selected_words=[]
outline_words = []

def gen(selected_dif):

    match selected_dif:
        case 6:
            selected_words = words_easy
        case 8:
            selected_words = words_medium
        case 10:
            selected_words = words_hard

    for i in range(6):
        outline_words.append(random.choice(selected_words))

    term_outline = ''
    for i in range(408):
        term_outline+=random.choice(trash_symbols)

    new_string = list(term_outline)
    indexes = [random.randint(0,408-selected_dif) for i in range(6)]

    i=0
    for word in outline_words:
        start_index = indexes[i]
        end_index = start_index + len(word)
        new_string[start_index:end_index] = word
        i+=1

    answer = random.choice(outline_words)
    result = "".join(new_string)
    #print(result)

    final = [result[i:i+12] for i in range(0, len(result), 12)]

    return (final,answer, outline_words)