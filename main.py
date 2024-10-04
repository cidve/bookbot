
def main():
    book_path = "books/frankenstein.txt"
    # test_path = "books/test.txt"
    # book_path = test_path
    text = get_text(book_path)
    number_of_words = count_words(text)
    print(number_of_words)
    return (number_of_words)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    text_split = text.split()
    return len(text_split)

# tests
if __name__ == '__main__':
    main()