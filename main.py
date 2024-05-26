class Book:
    def __init__(self, name:str, author: str, year: int, publisher: str)-> None:
        self._name = name
        self._author = author
        self._year = year
        self._publisher = publisher

    def __str__ (self)-> str:
        return (f"Book: Book's title={self._name}, author={self._author}, "
                f"year of publishing={self._year}, publisher={self._publisher}")

    @property
    def name(self)->str:
        return self._name
    @property
    def author(self)->str:
        return self._author
    @property
    def year(self)->int:
        return self._year
    @property
    def publisher(self)->str:
        return self._publisher

 #   @x.setter
 #   def x(self, value: int)-> None:
 #       if value <0:
 #           raise ValueError()
 #       self._x = value

class Library:
    def __init__(self, catalog: list[Book]=[]) -> None:
        self._catalog = catalog

    def add_to_catalog(self,book:Book)-> None:
        self._catalog.append(book)

    def sort_by_year(self):
        return sorted(self.catalog, key=lambda x: x.year, reverse=False)

    def delete_by_name(self,name:str):
        for book in self.catalog:
            if book.name == name:
                self._catalog.remove(book)

    def search_by_name(self, name: str) -> Book:
        for book in self.catalog:
            if book.name == name:
                return book

    def search_by_author(self, author: str) -> Book:
        for book in self.catalog:
                if book.author == author:
                    return book

    def sort_by_author(self):
            return sorted(library.catalog, key=lambda x: x.author, reverse=False)



    @property
    def catalog(self)->list:
        return self._catalog

def func():
    while True:
        a = input ("Enter something ")

        try:
            b = int(a)
            return b
            break
        except ValueError:
            print("!!!!")
            continue

#def search_by_name(catalog:list, name:str)-> Book:
#    for book in catalog:
#        print(f"{book.name} - {book}")
#        print('\n')
#        if book.name == name:
#            return book_description(book)

def add_books():
    pass

def book_description(book:Book)->str:
    print (f"Book: Book's title={book._name}, author={book._author}, "
            f"year of publishing={book._year}, publisher={book._publisher}")

def show_books(library:Library)->str:
    print("Books in our library: ")
    for book in library.catalog:

        print (f"Book: Book's title={book._name}, author={book._author}, "
                f"year of publishing={book._year}, publisher={book._publisher}")
def show_books_from_catalog(library:list)->str:
    print("Books in our library: ")
    for book in library:

        print (f"Book: Book's title={book._name}, author={book._author}, "
                f"year of publishing={book._year}, publisher={book._publisher}")


 #   for book in a:

 #       print (f"Book: Book's title={book.name}, author={book.author}, "
 #               f"year of publishing={book.year}, publisher={book.publisher}")

def add_books(library:Library, book:Book):
    library.add_to_catalog(book)

def main():
    print ("Наполняем библиотеку книгами ...")
 #   a = func()
    book1 = Book("Jungle's book", "BKipling",1900,"AST")
    book2 = Book("The island", "CVonnegut", 1960, "AST")
    book3 = Book("Fairy Tales", "APushkin", 1800, "AST")
    library1 = Library()
    a = 0
    while(a!=6):
        print("Select what you want to do:")
        print("1. Add books to catalog")
        print("2. Show all books in catalog")
        # Доработать это все!!!
        print("2. Search book by author")
        print("3. Delete by title")
        print("4. Sort by year")
        print("5. Sort by name")
        print("6. Exit program")

        a = func()
        if(a==1):
            add_books(library1,book1)
            add_books(library1, book2)
            add_books(library1, book3)
        elif(a==2):
            for book in library1.catalog:
                book_description(book)


    #library1.add_to_catalog(book1)
    #library1.add_to_catalog(book2)
    #library1.add_to_catalog(book3)


    print(library1.catalog)

    print("Search for Fairy Tales...")
    book_description(library1.search_by_name("Fairy Tales"))

    print("Search for author...")
    book_description(library1.search_by_author("CVonnegut"))

    #show_books_from_catalog(library1.sort_by_year())
 #   sort_by_year(library1)
    library1.delete_by_name("Fairy Tales")
    show_books_from_catalog(library1.catalog)

if __name__ == "__main__":
    main()
