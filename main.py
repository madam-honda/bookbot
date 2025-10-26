from stats import word_count
from stats import character_count
from stats import fancy
import sys

def main():
   # book_path = "books/frankenstein.txt"
    #sys.exit
    #print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text=get_book_text(book_path)
    #print("Found "+str(word_count(text))+" total words")
    #print(character_count(text))
    #print(fancy(character_count(text)))

    # printing it to look fancy
    orderedlist=fancy(character_count(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found "+str(word_count(text))+" total words")
    print("--------- Character Count -------")
    
    a=[]
    for k in orderedlist:
        if k["char"].isalpha():
            a.append({k["char"],k["num"]})
            print(k["char"]+": "+str(k["num"]))
    
    print("============= END ===============")

    
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()