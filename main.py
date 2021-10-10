import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "makeuc",
    password = "makeuc",
    database = "testdb",
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")

my_cursor.execute('''CREATE TABLE IF NOT EXISTS map (latitude VARCHAR(20),
                                        longitude VARCHAR(20),
                                        category VARCHAR(255),
                                        sev VARCHAR(2),
                                        dummy VARCHAR(255))''')

sqlInsert = "INSERT INTO map (latitude, longitude, category, sev, dummy) VALUES (%s, %s, %s, %s, %s)"

#insert = "44.23451, 34.12345, road damage, 7, attention"
#list = insert.split(',')
#recordX = (list[0], list[1], list[2], list[3], list[4])
#my_cursor.execute(sqlInsert,recordX)
#mydb.commit()



my_cursor.execute("SELECT * FROM map")
#mydb.commit()
myresult = my_cursor.fetchall()
for x in myresult:
  print(x)
