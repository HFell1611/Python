books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
title = input('Book Title: ')
if title in books:
    print('The author is: ') 
    print(books.get(title))
else:
    print("Book not found")

