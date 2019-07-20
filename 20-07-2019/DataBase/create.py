import sqlite3
conn=sqlite3.connect("APSSDC.db")# Create New databse
cur=conn.cursor()# Create Object
query = "create table student(name text,id text primary key,branch text,phone integer)"
cur.execute(query)
print("Create table sucessfully")
conn.commit()
cur.close()
conn.close()
