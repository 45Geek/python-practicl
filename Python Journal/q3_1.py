import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Library.db')
    print('connected')
    cursor=conn.cursor()
    print('cursor connected')
    insert='''insert into Books values(?,?,?,?,?);'''
    data=[
                    ('B001','Bahunari','Ankruti Upadhaya','Fourth Estate India','2019'),
                    ('B002','Godaan','Munshi Premchand','Anubhav Publishing House','2003'),
                    ('B003','Gunahon Ka devta','DharamVeer Bharti','Indra Publisher ltd.','2009'),
                    ('B004','Neelu','Mahadevi Varma','Hindi Kavya Ltd.','2020'),
                    ('B005','Basant','Sumitra Nandan Pant','Hindi Kavya Ltd.','2019'),
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
