def count_words_in_text(text):
    return len(text.split())


def get_number_of_characters(text):
    result = {}
    for character in text:
        c = character.lower()
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def sort_dictionary(char_dict):
    characters = []
    for key in char_dict:
        characters.append({"char": key, "num": char_dict[key]})
    characters.sort(reverse=True, key=lambda d: d["num"])
    return characters

