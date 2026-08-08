import mysql.connector  as con
try:
    server=con.connect(
    host="localhost",
    port=3307,
    user="root",
    password=input("Password:"),
    database="project"
    )
    cursor=server.cursor()
    cursor.execute("SELECT * FROM users")
    rows =cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    server.close()
except :
    print("an unknow error occured.")
    print("Please enter correct passowrd.")
