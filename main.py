def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)


main()
