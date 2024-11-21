def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def wordcount(file_contents):
    count = 0
    words = file_contents.split()
    count = len(words)

    #print(count)
    return count

def character_count(file_contents):
    lowercase = file_contents.lower()
    char_counts = {}

    for char in lowercase:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        else:
            pass
    #print(char_counts)
    return char_counts

def report(char_counts, count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    print()
    
    current_max = 0
    biggest_char = ""

    while(len(char_counts) != 0):
        for char in char_counts:
            if char_counts[char] >= current_max:
                biggest_char = char
                current_max = char_counts[biggest_char]
            
        print(f"The '{biggest_char}' character was found {current_max} times")
        del char_counts[biggest_char]
        current_max = 0

    print("--- End Report ---")


main()

file_contents = main()
wordcount(file_contents)
character_count(file_contents)

char_counts = character_count(file_contents)
wordcount = wordcount(file_contents)
report(char_counts, wordcount)