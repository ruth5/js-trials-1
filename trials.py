"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    result = []

    for i in len(items):
        if i % 2 != 0:
            result.append(items[i])
    return result


def print_as_numbered_list(items):
    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    range_list = []

    i = start

    while i < stop:
        range_list.append(i)
        i += 1
        
    return range_list

def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    return ''.join(chars)


def snake_to_camel(string):
    camel_case = []

    for word in string.split("_"):
        capital_word = word.title()
        camel_case.append(capital_word)

    return "".join(camel_case)


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest

def truncate(string):
    result = []

    for letter in string:
        if len(result) == 0 or letter != result[len(result)-1]:
            result.append(letter)
    
    return "".join(result)

def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
    
    return parens == 0

def compress(string):
    compressed = []

    curr_char = ""
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char
            char_count = 0
        char_count += 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return "".join(compressed)