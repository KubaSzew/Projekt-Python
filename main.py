from library import Library
from storage import load_books, save_books

def menu():
    print("\n📚 Book Manager CLI")
    print("1. Dodaj książkę")
    print("2. Wyświetl książki")
    print("3. Szukaj książki")
    print("4. Usuń książkę")
    print("5. Edytuj książkę")
    print("6. Zapisz i wyjdź")

def main():
    books = load_books("books.json")
    lib = Library(books)

    while True:
        menu()
        choice = input("Wybierz opcję: ")
        if choice == "1":
            title = input("Tytuł: ")
            author = input("Autor: ")
            year = input("Rok wydania: ")
            genre = input("Gatunek: ")
            lib.add_book(title, author, year, genre)
        elif choice == "2":
            lib.list_books()
        elif choice == "3":
            keyword = input("Szukaj tytuł/autor: ")
            lib.search_books(keyword)
        elif choice == "4":
            book_id = input("ID książki do usunięcia: ")
            lib.remove_book(book_id)
        elif choice == "5":
            book_id = input("ID książki do edycji: ")
            lib.edit_book(book_id)
        elif choice == "6":
            save_books("books.json", lib.books)
            print("📁 Zapisano. Do zobaczenia!")
            break
        else:
            print("❌ Nieprawidłowy wybór!")

if __name__ == "__main__":
    main()
