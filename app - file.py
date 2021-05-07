from utils import database

USER_CHOICE ="""
Enter:
- 'a' to add a new book
- 'l' to list all book
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:"""
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            database.prompt_add_book()
        elif  user_input == 'l':
            database.list_books()
        elif  user_input == 'r':
            database.prompt_read_book()
        elif  user_input == 'd':
            database.prompt_delete_book()
        user_input = input(USER_CHOICE)


menu()
