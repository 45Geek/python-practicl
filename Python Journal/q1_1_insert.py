import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\ESM.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    querry1='''insert into employee values(101,'Indrajeet','IT',7000,'surat');'''
    cursor.execute(querry1)
    querry2='''insert into employee values(102,'Nidhi','HR',6500,'surat');'''
    cursor.execute(querry2)
    querry3='''insert into employee values(103,'Jay','Account',5500,'surat');'''
    cursor.execute(querry3)
    querry4='''insert into employee values(104,'Vikash','Inventary',5000,'surat');'''
    cursor.execute(querry4)
    querry5='''insert into employee values(105,'Darshan','IT',7200,'Mumbai');'''
    cursor.execute(querry5)
    insert='''insert into employee values(?,?,?,?,?);'''
    data=[
                    (106,'Ujala','HR',6700,'Mumbai'),
                    (107,'Rohit','Account',5700,'Mumbai'),
                    (108,'Shubham','Inventory',5200,'Mumbai'),
                    (109,'Aniket','IT',6800,'Bhopal'),
                    (110,'Sanya','HR',6300,'Bhopal')
                ]
    cursor.executemany(insert,data)
    print('Data Inserted')
    print('Take input for 5 records')
    for i in range(5):
        eid=int(input('Enter ID : '))
        ename=input('Enter Name : ')
        dept=input('Enter Dept : ')
        basic=float(input('Enter Salary : '))
        branch=input('Enter Branch : ')
        cursor.execute(insert,(eid,ename,dept,basic,branch))
    print('Data Inserted')
    conn.commit()
    cursor.close()
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
