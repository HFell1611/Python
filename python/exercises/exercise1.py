# Create a book class, and initialise each book object with author, title, 
# ISBN, year of publication and number of pages. Define a str method which 
# displays information about the book, and a search method which searches
# by book or by author, through a dictionary attribute of the class which 
# tracks the book objects created. Define two subclasses for different genres 
# of books which override the default str method. As a stretch goal, also
# implement a method which checks whether an ISBN is valid

class Book():
    book = {} #start of distionary
    def __init__(self, author, title, isbn, year, pages):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year
        self.pages = pages
        if self.author in Book.book:
            Book.book[self.author].append(self)
        else:
            Book.book[self.author] = [self]
        # adding to dictionary

    @staticmethod 
    def search_books(search_term, search_by = 'author'):
        if search_by == 'author':
            result = Book.book.get(search_term.title(), [])
            return f"Books by {search_term.title()}: {','.join([book.title for book in result]) if result else 'None'}"
        else:
            title = (search_term)
            for author, books in Book.book.items():
                if title in [book.title for book in books]:
                    return f"Book \'{title}\' was written by {author}"
            return f"Book \'{title}'\ was not found"
        # searches for books by certain authors
    def __str__(self):
        return f"{self.title} was written by {self.author}, was published in {self.year} and is {self.pages} pages"


class Fantasy(Book):
    def __str__(self):
        return f"{self.title} is a epic fanyasy novel written by {self.author}, was published in {self.year} and is {self.pages} pages"

class SciFi(Book):
    def __str__(self):
        return f"{self.title} is a Science Fiction novel written by {self.author}, was published in {self.year} and is {self.pages} pages"




book1 = Book("Margaret Atwood", "The Handmaid's Tale", "ISBN-10: 0099740915", 1985, 311)
book2 = Fantasy("J.R.R. Tolkein", "The Hobbit", "ISBN 10: 0006754023", 1937, 310)
book3 = SciFi("Roald Dahl", "Charlie and the Chocolate Factory", "ISBN 10: 0142401080", 1964, 176)

#print(Book.search_books('J.R.R. Tolkein'))
print(book3)