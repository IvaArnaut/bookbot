def sort_on(items):
    return items["num"]

def num_of_words(text):
    words = text.split()
    return len(words)

def character_stats(text):
    char_dict = {}
    for char in text.lower():
        char_dict[char] = char_dict.get(char.lower(), 0) + 1
    return char_dict

def sorted_dict_list(any_dict):
    list_of_dict = []
    for k,v in any_dict.items():
        list_of_dict.append({"char": k, "num": v})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

