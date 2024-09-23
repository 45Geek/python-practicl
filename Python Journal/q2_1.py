import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\EMP.db')
    print('connection successful')
    cursor=conn.cursor()
    print('cursor connected')
    qurry='''create table Employee1
                (
                  eid int primary key,
                  ename text,
                  desg text,
                  salary number
                );'''
    cursor.execute(qurry)
    print('Table created')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('connection closed')
