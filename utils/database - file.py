books = []

def prompt_add_book():
    name = input("Book name: ")
    author = input("Author name: ")
    books.append({'name':name,'author':author,'read':False})

def list_books():
    for book in books:
       print(f" Book name: {book['name']}\n Author name: {book['author']}\n Book read status: {book['read']}\n") 

def prompt_read_book():
    name = input("Book name: ")
    for book in books:
        if book['name'] == name:
            book['read'] = True

def prompt_delete_book():
    name = input("Book name: ")
    for book in books:
        if book['name'] == name:
            books.remove(book)

            
