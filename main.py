from stats import count_words_in_text, sort_dictionary, get_number_of_characters


def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("books/frankenstein.txt")
    count = count_words_in_text(text)
    characters = sort_dictionary(get_number_of_characters(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for character in characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")


main()
