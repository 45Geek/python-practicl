import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Library.db')
    print('connected')
    cursor=conn.cursor()
    print('cursor connected')
    create="""create table Books
                        (
                        bookid int primary key,
                        title text,
                        author text,
                        publisher text,
                        year int
                        );"""
    cursor.execute(create)
    print('Table created')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('connection closed')
