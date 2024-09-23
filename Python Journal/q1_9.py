import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\ESM.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    qurry="""select dept,count(*) from employee where dept in ('Account','Inventory') group by dept;"""
    cursor.execute(qurry)
    records=cursor.fetchall()
    for row in records:
        print("Dept Name = ",row[0])
        print("No of Count =  ",row[1])
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
