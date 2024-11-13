import sqlite3

conn = sqlite3.connect("hokus.db")

cursor = conn.cursor()

input_pizza = input("Choose your pizza: ")

cursor.execute(
    "INSERT INTO pizza (name) VALUES (?)", (input_pizza,)
)

conn.commit()

cursor.execute("SELECT * FROM pizza")
rows = cursor.fetchall()

for row in rows:
    print(row[1])


conn.close()