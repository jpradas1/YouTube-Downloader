from downloader import Downloader

def main():
    print("Warning: Don't use accents on the words")
    print("Advertencia: No usar tildes en las palabras\n")
    D = Downloader()

    # Don't use accents on the words
    # No usar tildes en las palabras

    D.search_URL('name_input.txt')
    # D.download('urls.csv')

if __name__ == "__main__" :
    main()