import sys

from stats import get_word_count

from stats import get_character_count

from stats import sort_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    character_count = get_character_count(text)
    sorted_count = sort_count(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in sorted_count:
        character = key["char"]
        if character.isalpha():
            print(f"{key["char"]}: {key["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        book_text = f.read()
    return book_text


main()

