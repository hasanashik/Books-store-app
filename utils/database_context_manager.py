# -*- coding: utf-8 -*-
import sqlite3
class DatabaseConnection:
    def __init__(self, db_name,mode='r'):
        self.connection = None
        self.db_name = db_name
        self.mode = mode
    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        if  exc_type or exc_val or exc_tb:
            self.connection.close()
        elif self.mode == 'w':
            print('Commiting database')
            self.connection.commit()
            self.connection.close()
        elif self.mode == 'r':
            print('Closing database from read')
            self.connection.close()
        else:
            print('Closing database anyway')
            self.connection.close()