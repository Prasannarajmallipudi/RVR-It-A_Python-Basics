import sqlite3
conn=sqlite3.connect("APSSDC.db")# Create New databse
cur=conn.cursor()# Create Object
name=input("enter name")
ide=input("enter id:")
branch=input("enter branch:")
phone=int(input("enter mobile num:"))
query = "insert into student values(?,?,?,?)"
cur.execute(query,(name,ide,branch,phone))
print("insertion sucessfully")
conn.commit()
cur.close()
conn.close()
