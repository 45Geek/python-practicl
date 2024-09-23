import sqlite3
try:
    conn=sqlite3.connect('c:/sqlite3/Hotel.db')
    cursor=conn.cursor()
    querry="""Select * Customer where city='Surat';"""
    cursor.execute(querry)
    rows=cursor.fetchall()
    for row in rows:
        print("Customer Name = ",row[0])
    cursor.close()
except sqlite3.Error as error:
    if(error):
        print("No Data Available in data base , on your reference")
finally:
    conn.close()
    print('connection close')
