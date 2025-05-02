def get_book_text(file_path):
    return file_path.read()


def main():
    return get_book_text("/books/frankenstein.txt")

if __name__ == "__main__":
    # code à exécuter en tant que script principal
    main()
