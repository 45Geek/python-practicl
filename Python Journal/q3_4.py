import sqlite3
try:
    conn=sqlite3.connect('c:/sqlite3/Library.db')
    cursor=conn.cursor()
    querry="""select title,year from Books where year>2000;"""
    cursor.execute(querry)
    rows=cursor.fetchall()
    for row in rows:
        print("Customer Name = ",row[0])
        print("\n")
    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    conn.close()
    print('connection close')
