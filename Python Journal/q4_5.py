import sqlite3
try:
    conn=sqlite3.connect('c:/sqlite3/Hotel.db')
    cursor=conn.cursor()
    querry="""delete from Customer where city='Surat';"""
    cursor.execute(querry)
    print('Data Delete')
except sqlite3.Error as error:
    print(error)
finally:
    conn.close()
    print('connection close')
