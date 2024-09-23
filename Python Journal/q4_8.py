import sqlite3
try:
    conn=sqlite3.connect('c:/sqlite3/Hotel.db')
    cursor=conn.cursor()
    querry="""select * from Customer inner join Roommast
                        on Customer.Room_no=Roommast.Room_no where
                        Room_type="Normal";"""
    cursor.execute(querry)
    rows=cursor.fetchall()
    print("------Customer Details------")
    for row in rows:
        print("Customer Name = ",row[0])
        print("City = ",row[1])
        print("Room no = ",row[2])
        print("Allocate day = ",row[3])
        print("No of days = ",row[4])
        print("\n")
    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    conn.close()
    print('connection close')
