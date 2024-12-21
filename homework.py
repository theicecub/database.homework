import sqlite3

connection = sqlite3.connect("weather.db")

print("Connection with data base")

cut = connection.cursor()
cut.execute("""
    CREATE TABLE IF NOT EXISTS weather(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        temperature TEXT
    );
"""
)

cut.execute("INSERT INTO weather (date,time,temperature) VALUES ('21 december', '18:39', '-10 Celcium');")
cut.execute("INSERT INTO weather (date,time,temperature) VALUES ('27 december', '7:24', '-12 Celcium');")

cut.execute("SELECT * FROM weather;")

weather = cut.fetchall()

for i in weather:
    print(i)

connection.commit()
connection.close()