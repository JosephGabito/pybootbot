from stats import count_letters, sort_dictionary, count_words
import sys


def get_book_text(path_to_text_file):

    file_contents = ""

    try:
        with open(path_to_text_file) as f:
            file_contents = f.read()
    except FileNotFoundError as e:
        print("File not found" + path_to_text_file)

    return file_contents


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)

    words_count = count_words(text)
    letters_count = count_letters(text)

    sorted_result = sort_dictionary(letters_count)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_result:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

    return text


main()
