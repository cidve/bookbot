
def main():
    book_path = "books/frankenstein.txt"
    # test_path = "books/test.txt"
    # book_path = test_path
    generate_report(book_path)
    # return (number_of_words)

def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    text_split = text.split()
    return len(text_split)

def count_letters(text):
    text = text.lower()
    text_split = text.split()
    letter_count = {}
    for word in text_split:
        for i in word:
            if i.isalpha():
                if i not in letter_count:
                    letter_count[i] = 1
                else:
                    letter_count[i] += 1
    return letter_count

def order_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

def generate_report(book_path):
    text = get_text(book_path)
    number_of_words = count_words(text)
    letters_count = count_letters(text)
    letters_ordered = order_dict(letters_count)
    print('-'*5, f"Start report of {book_path}", '-'*5)
    print(f'{number_of_words} words found in the document')
    print()
    for c in letters_ordered:
        print(f"The '{c}' character was found {letters_ordered[c]} times")
    print('-'*5, "End report", '-'*5)
# tests
if __name__ == '__main__':
    main()