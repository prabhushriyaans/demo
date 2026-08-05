import mysql.connector  as con
server=con.connect(
    host="localhost",
    port=3307,
    user="root",
    password="shri@77yaans",
    database="w3schools"
)
cursor=server.cursor()
cursor.execute("SELECT * FROM Products")
rows =cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
server.close()
