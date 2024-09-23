import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Library.db')
    print('connection successful')
    cursor=conn.cursor()
    print('cursor connected')
    qurry="""select * from Books where title like 'C%' and length(title)>=10;"""
    cursor.execute(qurry)
    records=cursor.fetchall()
    print('total records',len(records))
    print('--------Books Details--------')
    for row in records:
        print("Book ID : ",row[0])
        print("Title : ",row[1])
        print("Author : ",row[2])
        print("Publisher : ",row[3])
        print("Year : ",row[4])
        print("\n----------------------------------\n")
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
