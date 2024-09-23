import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Hotel.db')
    print('connected')
    cursor=conn.cursor()
    print('cursor connected')
    create="""create table Roommast
                        (
                        Room_no int primary key,
                        Room_type text,
                        Rate int
                        );"""
    cursor.execute(create)
    print('Table created')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('connection closed')
