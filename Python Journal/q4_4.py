import sqlite3
try:
    conn=sqlite3.connect('c:/sqlite3/Hotel.db')
    cursor=conn.cursor()
    querry="""select Customer_name
                        from Customer where Allocate_day between '18-09-2024' and '22-09-2024';"""
    cursor.execute(querry)
    rows=cursor.fetchall()
    for row in rows:
        print("Customer Name = ",row[0])
    cursor.close()
except sqlite3.Error as error:
    print(error)
finally:
    conn.close()
    print('connection close')
