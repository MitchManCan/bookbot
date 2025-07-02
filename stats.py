def wordcounter(book_text):
    words = book_text.split()
    num = len(words)
    return num
def charcounter(book_text):
    counts = {}
    for char in book_text.lower():
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts [char] = 1
    return counts
def sortingmachine(counts):
    char_list = []
    for char, num in counts.items():
        char_dict ={"char": char, "num": num}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on) 
    return char_list
def sort_on(char_data):
    return char_data["num"]
    


