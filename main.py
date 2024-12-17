def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_counts = get_num_chars(text)
    chars_list = []

    for char in char_counts:
        if char.isalpha():
            char_dict = {"char": char, "num": char_counts[char]}
            chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]
def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    dict = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
    return dict



def get_book_text(path):
    with open(path) as f:
        return f.read()
main()