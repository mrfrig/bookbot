import sys
from stats import count_words_in_text, sort_dictionary, get_number_of_characters


def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)
    count = count_words_in_text(text)
    characters = sort_dictionary(get_number_of_characters(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for character in characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")


main()
