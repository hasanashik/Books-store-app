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
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            database.prompt_add_book()
        elif  user_input == 'l':
            counter = 1
            for i in database.list_books():
                read_status = None
                if i['read'] == 1:
                    read_status =  'Yes'
                elif i['read'] == 0:
                    read_status =  'No'
                else:
                    read_status =  'Not found'
                
                print(f"{counter}) {i['name']} is written by {i['author']}. Read status: {read_status}")
                counter = counter + 1
        elif  user_input == 'r':
            database.prompt_read_book()
        elif  user_input == 'd':
            database.prompt_delete_book()
        else:
            print('Invalid choice!')
        user_input = input(USER_CHOICE)


menu()
