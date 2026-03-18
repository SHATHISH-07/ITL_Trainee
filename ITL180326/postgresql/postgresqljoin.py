import psycopg2

conn = psycopg2.connect(
    user="postgres",
    host="localhost",
    database="mydb",
    password="12345678",
    port=5432,
    )

cur = conn.cursor()

# joining of two tables
cur.execute('SELECT s.name, c.course_name FROM users AS s JOIN courses AS c ON s.id = c.user_id ')
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()