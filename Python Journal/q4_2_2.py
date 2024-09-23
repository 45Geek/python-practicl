import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Hotel.db')
    print('connected')
    cursor=conn.cursor()
    print('cursor connected')
    insert='''insert into Customer values(?,?,?,?,?);'''
    data=[
                    ('Indrajeet','Surat',1,'10-09-2024',12),
                    ('Rohit','Mumbai',2,'12-09-2024',10),
                    ('Shubham','Delhi',3,'15-09-2024',7),
                    ('Ankit','Delhi',4,'16-09-2024',6),
                    ('Nidhi','Surta',5,'18-09-2024',4),
                    ('Diksha','Mumbai',6,'21-09-2024',1),
                    ('Krishna','Bhopal',7,'10-09-2024',12),
                    ('Dharmesh','Gurugram',8,'19-09-2024',3),
                    ('Chandan','Lucknow',9,'18-09-2024',4),
                    ('Shyam','Noida',10,'16-09-2024',6)
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
