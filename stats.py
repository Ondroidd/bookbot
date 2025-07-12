def count_words(text):
    """Returns text word count"""
    return len(text.split()) 


def count_chars(text):
    """Returns a dictionary of character counts in text"""
    char_counts = {}
    for char in text:
        standardized_char = char.lower()
        if standardized_char not in char_counts:
            char_counts[standardized_char] = 1
        else:
            char_counts[standardized_char] += 1
    return char_counts


def sort_chars(char_counts):
    """Returns reverse-sorted list of character counts dictionaries"""
    sorted_chars = []

    for char in char_counts:
        temp_dict ={}
        temp_dict["char"] = char
        temp_dict["num"] = char_counts[char]
        sorted_chars.append(temp_dict)

    sorted_chars.sort(reverse=True, key=lambda sorted_chars: sorted_chars["num"])
    return sorted_chars
