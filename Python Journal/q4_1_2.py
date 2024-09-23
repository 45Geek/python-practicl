import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\Hotel.db')
    print('connected')
    cursor=conn.cursor()
    print('cursor connected')
    create="""create table Customer
                        (
                        Customer_name text,
                        City text,
                        Room_no int,
                        Allocate_day date,
                        No_od_days int,
                        foreign key (Room_no) references Roommast(Room_no)
                        );"""
    cursor.execute(create)
    print('Table created')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('connection closed')
