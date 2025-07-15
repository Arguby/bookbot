from stats import word_count, repeats, sortedList
import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    # print(get_book_text(path))
    text = get_book_text(path)
    num_words = word_count(text)
    reps = repeats(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    listFinal = sortedList(reps)
    for thing in listFinal:
        if not thing["char"].isalpha():
            continue
        print(f"{thing["char"]}: {thing["num"]}")
    print("============= END ===============")

main()