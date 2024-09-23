import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\ESM.db')
    print('connection successful')
    cursor=conn.cursor()
    print('cursor connected')
    qurry='''create table employee
                (
                  eid int primary key,
                  ename text,
                  dept text,
                  basic real,
                  branch text
                );'''
    cursor.execute(qurry)
    print('Table created')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('connection closed')
