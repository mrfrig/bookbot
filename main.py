from stats import count_words_in_text
from stats import get_number_of_characters


def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    count = count_words_in_text(text)
    characters = get_number_of_characters(text)
    print(f"{count} words found in the document")
    print(characters)


main()
