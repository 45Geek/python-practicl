import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\EMP.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    insert='''insert into Employee1 values(?,?,?,?);'''
    data=[
                    (1,'Raj','Manager',60000),
                    (2,'Rahul','Executive Manager',90000),
                    (3,'Vikas','Asst. Manager',60000),
                    (4,'Varun','Manager',40000),
                    (5,'Harshit','Manager',45000),
                    (6,'Tarun','Senior Manager',50000),
                    (7,'Rishav','Supervisor',50000),
                    (8,'Diksha','Counsellor',40000),
                    (9,'Rakesh','Asst. Manager',60000),
                    (10,'Pooja','Manager',60000),
                ]
    cursor.executemany(insert,data)
    print('Data Inserted')
    conn.commit()
    cursor.close()
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
