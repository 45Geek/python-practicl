import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Hotel.db')
    print('connected')
    cursor=conn.cursor()
    print('cursor connected')
    insert='''insert into Roommast values(?,?,?);'''
    data=[
                    (1,'Super',8000),
                    (2,'Normal',5000),
                    (3,'Double',3500),
                    (4,'Single',2500),
                    (5,'Super',8000),
                    (6,'Normal',5000),
                    (7,'Double',3500),
                    (8,'Single',2500),
                    (9,'Double',3500),
                    (10,'Single',2500)
                ]
    cursor.executemany(insert,data)
    print('Data Inserted')
    conn.commit()
    cursor.close()
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('connection closed')
