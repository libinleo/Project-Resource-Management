import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "myproject"
)


mydb_Create_Table_Query = """CREATE TABLE user
( fullname varchar(50) not null,
username varchar(50) not null,
email varchar(50) not null,
password varchar(50) not null
 
)"""


cursor = mydb.cursor()
result = cursor.execute(mydb_Create_Table_Query)

print(" Table created successfully ")
