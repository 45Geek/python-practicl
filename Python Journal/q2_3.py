import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\EMP.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    qurry="""select * from Employee1;"""
    cursor.execute(qurry)
    records=cursor.fetchall()
    print('total records',len(records))
    print('--------Employee Details--------')
    for row in records:
        print("ID : ",row[0])
        print("Name : ",row[1])
        print("Desg : ",row[2])
        print("Salary : ",row[3])
        print("\n----------------------------------\n")
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
