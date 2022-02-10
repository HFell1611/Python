books = {"the handmaid's tale":"Margaret Atwood", "the hobbit":"J.R.R. Tolkien", "charlie and the chocolate factory":"Roald Dahl", "the shining":"Steven King", "the time machine":"H.G. Wells"}
title = input("Enter a book title: ")
print(f'{title} was written by: {books.get(title.lower(), "Unknown")}')
