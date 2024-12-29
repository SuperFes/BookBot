import re

def sort_on_num(item):
    return item["num"]

def word_count(file_contents):
    words = file_contents.split()

    return len(words)

def character_count(file_contents):
    char_counts = {}

    for character in file_contents:
        lcase_character = character.lower()

        if re.match(r'[a-z]', lcase_character) is None:
            continue

        if lcase_character in char_counts:
            char_counts[lcase_character] += 1
        else:
            char_counts[lcase_character] = 1

    char_list = []

    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    return char_list

def main():
    file_path = 'books/frankenstein.txt'

    with open(file_path, 'r') as file:
        file_contents = file.read()

    words = word_count(file_contents)
    char_counts = character_count(file_contents)

    char_counts.sort(reverse=True, key=sort_on_num)

    print(f"Word count: {words}\n")

    for char in char_counts:
        print(f"The character '{char["char"]}' was found {char["num"]} time(s)")

main()
