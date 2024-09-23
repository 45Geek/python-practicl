import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\EMP.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    qurry="update Employee1 set salary=salary+10000 where desg='Counsellor';"""
    cursor.execute(qurry)
    conn.commit()
    print('data update')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
