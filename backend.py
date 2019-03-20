import sqlite3

class Database:

    #def connect():      # connect to db
    def __init__(self):     # python-style constructor
        self.connection = sqlite3.connect("books.db")
        self.cursor = self.connection.cursor()
        sql_string = "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, YEAR INTEGER, isbn INTEGER )"
        print(sql_string)
        self.cursor.execute(sql_string)   # table book; db books
        self.connection.commit()
        # self.connection.close()

    def __del__(self):                         # destructor
        self.connection.close()


    def insert(self, title, author, year, isbn):
        # self.connection = sqlite3.connect("books.db")
        # self.cursor = self.connection.cursor()
        sql_string = f"INSERT INTO book VALUES(NULL, \'{title}\', \'{author}\', {year}, {isbn})"   # NULL for auto-increment'ing id - NB f prefix
        print('INSERT sql string: ' + sql_string)
        self.cursor.execute(sql_string)  # table book; db books
        self.connection.commit()
        # self.connection.close()


    def view(self):         #
        # self.connection = sqlite3.connect("books.db")
        # self.cursor = self.connection.cursor()
        sql_string = "SELECT * FROM book"
        self.cursor.execute(sql_string)   # table book; db books
        rows = self.cursor.fetchall()
        # self.connection.close()
        return rows


    def search(self, title="", author="", year="", isbn=""):              # provide empty strings as default values
        # connection = sqlite3.connect("books.db")
        # cursor = connection.cursor()
        sql_string = f"SELECT * FROM book WHERE title=\'{title}\' OR author=\'{author}\' OR year=\'{year}\' or isbn=\'{isbn}\'"
        print("SQL STRING: " + sql_string)
        self.cursor.execute(sql_string)   # table book; db books
        rows = self.cursor.fetchall()
        # connection.close()
        return rows


    def delete(self, id):             # provide empty strings as default values
        # connection = sqlite3.connect("books.db")
        # cursor = connection.cursor()
        sql_string = f"DELETE FROM book WHERE id={id}"
        print("SQL STRING: " + sql_string)
        self.cursor.execute(sql_string)   # table book; db books
        self.connection.commit()
        # connection.close()


    def update(self, id, title, author, year, isbn):
        # connection = sqlite3.connect("books.db")
        # cursor = connection.cursor()
        sql_string = f"UPDATE book SET title=\'{title}\', author=\'{author}\', year={year}, isbn={isbn} WHERE id={id}"   # NULL for auto-increment'ing id - NB f prefix
        print('SQL STRING: ' + sql_string)
        self.cursor.execute(sql_string)  # table book; db books
        self.connection.commit()
        # connection.close()


# TODO decorate with
# TODO try with PostGreSQL

# connect()
# # test
# insert('A desk', 'Lucy Lieu', 2002, 214323213153)
# print(search(author='Lucy Lieu'))
# update(2, 'Lucy Lieu', 'A desk', 2014, 12313124123)
# print(view())
# delete(2)
# print(view())

