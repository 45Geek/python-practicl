import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\EMP.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    qurry="delete from Employee1 where eid=10;"""
    cursor.execute(qurry)
    conn.commit()
    print('data update')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
