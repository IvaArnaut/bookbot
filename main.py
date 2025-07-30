import sys
from stats import num_of_words, character_stats, sorted_dict_list

def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    fpath = sys.argv[1]
    book = get_book_text(fpath)
    num_words = num_of_words(book)
    dict_of_characters = character_stats(book)
    sorted_list = sorted_dict_list(dict_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {fpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f'{dict["char"]}: {dict["num"]}')
    print("============= END ===============")
    

main()