from typing import List, Dict, Union#for typing hint purpose
from .database_context_manager import DatabaseConnection
def create_book_table() -> None:
    with DatabaseConnection('data.db','w') as conn:
        cursor = conn.cursor()
        cursor.execute('Create table if not exists books(name text primary key, author text, read int) ')



def prompt_add_book() -> None:
    name = input("Book name: ")
    author = input("Author name: ")
    with DatabaseConnection('data.db','w') as conn:
        cursor = conn.cursor()
        cursor.execute('insert into books values(?,?,0)',(name,author))
        


def list_books() -> List[Dict(str,Union(str,int))]:
    with DatabaseConnection('data.db','r') as conn:
        cursor = conn.cursor()
        cursor.execute('select * from books ')
        books = [{'name':item[0],'author':item[1],'read':item[2]} for item in cursor.fetchall()]
        return books

def prompt_read_book() -> None:
    name = input("Book name: ")
    with DatabaseConnection('data.db','w') as conn:
        cursor = conn.cursor()
        cursor.execute('update books set read=1 where name=?',(name,))


def prompt_delete_book() -> None:
    name = input("Book name: ")
    with DatabaseConnection('data.db','w') as conn:
        cursor = conn.cursor()
        cursor.execute('delete from books where name=?',(name,))


            
