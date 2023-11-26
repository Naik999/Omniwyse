import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "R@vindra",
    auth_plugin = "mysql_native_password",
    database = "movie_rental_store"
)
mycursor = mydb.cursor()
Q1 = "SELECT * FROM films_data WHERE actor_first_name = 'yash'"
mycursor.execute(Q1)
my = mycursor.fetchall()
for a in my:
  print(a)

Q2 = "SELECT * FROM films_data WHERE actor_last_name = 'nandamuri'"
mycursor.execute(Q2)
my = mycursor.fetchall()
for a in my:
  print(a)

Q3 = "SELECT DISTINCT actor_last_name FROM films_data"
mycursor.execute(Q3)
my = mycursor.fetchall()
for a in my:
  print(a)

Q4 = "SELECT actor_last_name FROM films_data GROUP BY actor_last_name HAVING count(actor_last_name) <2"
mycursor.execute(Q4)
my = mycursor.fetchall()
for a in my:
  print(a)

Q5 = "SELECT actor_last_name FROM films_data GROUP BY actor_last_name HAVING count(actor_last_name) >1"
mycursor.execute(Q5)
my = mycursor.fetchall()
for a in my:
  print(a)

Q6 = "SELECT * FROM films_data WHERE 'Academy Dinosaur'"
mycursor.execute(Q6)
my = mycursor.fetchall()
for a in my:
  print(a)

Q7 = "INSERT INTO films_data VALUE (1008,'Academy Dinosaur', 'Mike','Hillyer',180,5000,'family drama')"
mycursor.execute(Q7)
mydb.commit()

Q8 = "SELECT due FROM films_data WHERE due = 'Academy Dinosaur'"
mycursor.execute(Q8)
my = mycursor.fetchall()
for a in my:
  print(a)

Q9 = "SELECT avg(length) FROM films_data "
mycursor.execute(Q9)
my = mycursor.fetchall()
for a in my:
  print(a)

Qa1 = "SELECT avg(length), category  FROM films_data GROUP BY category"

mycursor.execute(Qa1)
my = mycursor.fetchall()
for a in my:
  print(a)

mycursor.close()
mydb.close()
 




































