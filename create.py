import sqlite3
# connecting to a database
conn = sqlite3.connect('test.db')
print('opened database successfully!')
conn.execute('''CREATE TABLE EMPLOYEES(
ID INT PRIMARY KEY NOT NULL ,
NAME TEXT NOT NULL ,
AGE INT NOT NULL,
SALARY REAL NOT NULL );
''')
print('table created successfully!')
conn.close()