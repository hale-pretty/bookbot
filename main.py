def count_word(text: str):
    return len(text.split())

def count_letter(text: str):
    count_lett = {}
    words = text.split()
    for word in words:
        lower_word = word.lower() 
        for char in lower_word:
            if char not in count_lett:
                count_lett[char] = 1
            else:
                count_lett[char] += 1
    return count_lett

def compare_tuple(tup1, tup2):
    return tup1[1] < tup2[1]

book_path = "books/frankenstein.txt"
with open(book_path) as f:
    file_contents = f.read()
   
    print (f"--- Begin report of {book_path} ---")
    print (f"{count_word(file_contents)} words found in the document")
    dict_letter = count_letter(file_contents)
    letter_only_count = []
    for key, value in dict_letter.items():
        if key.isalpha():
            letter_only_count.append((value, key))
    letter_only_count.sort(reverse=True)
    for value, key in letter_only_count:
        print (f"The {key} character was found {value} times")
    print("--- End report ---")