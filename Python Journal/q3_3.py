import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Library.db')
    cursor=conn.cursor()
    insert='''insert into Books values(?,?,?,?,?);'''
    for i in range(3):
        bookid=input('Enter Bookid : ')
        title=input('Enter Title : ')
        author=input('Enter Author name : ')
        publisher=input('Enter Publisher name : ')
        year=int(input('Enter Publishing Date : '))
        cursor.execute(insert,(bookid,title,author,publisher,year))
    print('Data Inserted')
    conn.commit()
    cursor.close()
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('connection closed')
