

path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(file):
    count = 0
    words = file.split()
    for word in words:
        count += 1
    print(f"our book has {count} number of words")


def char_count(file):
    #returns the number of times a char occurs in the text
    
    hm = {}
    words = file.lower().split()
    for word in words:
        for char in word:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1
    print("Start of the character count report:")
    print()
    for key, val in hm.items():
        print(f"The character '{key}' was found '{val}' times.")
    print("___end of the report___")




if __name__ == "__main__":
    # main()
    count_words(main())
    char_count(main())