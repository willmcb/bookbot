
path_to_file = 'books/frankenstein.txt'


def wordcount(text):
    return len(text.split())


def char_count(text):
    chars = list(text.lower())
    counts = {}
    for char in chars:
        if char.islower():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)


with open(path_to_file) as f:
    file_contents = f.read()
    wc = wordcount(file_contents)
    counts = char_count(file_contents)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{wc} words found in the document\n")
    for entry in counts:
        print(f"The '{entry[0]}' character was found {entry[1]} times")
    print('--- End report - --')
