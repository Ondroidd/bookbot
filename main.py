from stats import count_words, count_chars, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as fp:
        read_string = fp.read()
    return read_string   


def main():

    # Verify proper usage
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Analyze data
    text_as_string = get_book_text(sys.argv[1])
    word_count = count_words(text_as_string)
    char_count =  count_chars(text_as_string)
    sorted_char_count = sort_chars(char_count)

    # Print the final report
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for item in sorted_char_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print(f"============= END ===============")


if __name__ == "__main__":
    main()

