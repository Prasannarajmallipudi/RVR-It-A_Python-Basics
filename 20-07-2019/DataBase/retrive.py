import sqlite3
conn=sqlite3.connect("APSSDC.db")# Create New databse
cur=conn.cursor()# Create Object
query = "select * from student"
cur.execute(query)

print("Retrive Data")
conn.commit()
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
