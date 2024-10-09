

path_to_file = "books/frankenstein.txt"

def main():

    with open(path_to_file) as f:
        file_contents = f.read()




if __name__ == "__main__":
    main()