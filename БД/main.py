import sqlite3  # импортируем библиотеку sqlite3 для работы с бд
connection = sqlite3.connect("tutorial.db")  # мы создаём подключение к базе данных tutorial.db
cur = connection.cursor()

# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
#
# connection.commit()

# res = cur.execute("SELECT * FROM movie")
#
# for data in res.fetchall():
#     print(data)

data = [
    ('Monty Python and the Holy Grail', 1975, 8.2),
    ("And Now for Something Completely Different", 1971, 7.5),
    ('Monty Python blablabla', 1986, 9.9)
]
# cur.executemany('insert into movie values(?, ?, ?)', data)
res = cur.execute('SELECT name FROM sqlite_master')
# res.fetchone()
# for data in res.fetchall():
#     print(data)
print(res.fetchone())