import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\EMP.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    qurry="""select * from Employee1 where desg='Manager';"""
    cursor.execute(qurry)
    records=cursor.fetchall()
    for row in records:
        print(row)
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
