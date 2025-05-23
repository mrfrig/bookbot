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
