def count_words(text):

    words_list = text.split()

    return len(words_list)


def count_letters(text):

    text = text.lower()
    letter_dictionary = {}
    for char in text:
        if char in letter_dictionary:
            letter_dictionary[char] += 1
        else:
            letter_dictionary[char] = 1

    return letter_dictionary


def sort_on(dict):

    return dict["num"]


def sort_dictionary(text_dictionary):

    dict_list = []

    for entry in text_dictionary:
        _subset = {"char": entry, "num": text_dictionary[entry]}
        dict_list.append(_subset)
        pass

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
