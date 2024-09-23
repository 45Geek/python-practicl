import sqlite3
try:
    conn=sqlite3.connect('C:\sqlite3\ESM.db')
    print('connection successful',conn.total_changes)
    cursor=conn.cursor()
    print('cursor connected')
    qurry="""update employee set basic=basic*1.10 where branch='surat';"""
    cursor.execute(qurry)
    conn.commit()
    print('data update')
except sqlite3. Error as error:
    print(error)
finally:
    conn.close()
    print('Connection closed')
