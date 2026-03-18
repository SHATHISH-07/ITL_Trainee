import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="12345678",
    port=5432
    )

cur = conn.cursor()

# creating a user table
cur.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name VARCHAR(50), age INTEGER, email VARCHAR(100) UNIQUE, native_place VARCHAR(25), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# inserting values to the user table
cur.executemany("INSERT INTO users (name, age, email, native_place) VALUES (%s, %s, %s, %s)",
           [ ('Shathish',21,'shathish@gmail.com','Chennai'),
            ('Kumaran',22,'kumaran@gmail.com','Salem'),
            ('Santhoush',19,'santhoush@gmail.com','Banglore'),
            ('Vikranth',31,'vikranth@gmail.com','Madurai'),
            ('Vivin',41,'vivin@gmail.com','Chennai')])

# updating the user table
cur.execute("UPDATE users SET native_place=%s WHERE email=%s",
            ("Coimbatore", "vivin@gmail.com"))

# deleting a recoed from the user table
cur.execute("DELETE FROM users WHERE id=%s",
            (4,))

conn.commit()

# selecting all users from the table
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# updating a single user record
cur.execute("UPDATE users SET native_place=%s WHERE id=%s",
            ("Salem",5))

conn.commit()

# using select with group by
cur.execute("SELECT native_place, COUNT(*) as user_per_place FROM users GROUP BY native_place")
rows = cur.fetchall()
for row in rows:
    print(row)

# selecting user and displaying in decending order
cur.execute("SELECT * FROM users ORDER BY age DESC")
rows = cur.fetchall()
for row in rows:
    print(row)

# using aggegrate functions
cur.execute("SELECT COUNT(*) AS total_users, AVG(age) AS avg_age MAX(age) AS elderly_user FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

# selecting all the users implementing fetchmany, fetchone and fetchall
cur.execute("SELECT * FROM users")
rows = cur.fetchmany(2)
for row in rows:
    print(row)
row = cur.fetchone()
print(row)

# selected user by limit
cur.execute("SELECT * FROM users LIMIT 2")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()