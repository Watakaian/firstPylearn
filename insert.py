import sqlite3
conn = sqlite3.connect('test.db')
print('Opened database successfully!')
conn.execute("INSERT INTO EMPLOYEES VALUES (11,'FAITH KARIMI',34,450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12,'JANE MUTHONI',51,250000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (13,'PAUL KAMAU',28,85000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (14,'JOB HARRISON',31,450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (15,'MARTHA MBOTELA',26,450000.00);")
conn.commit()
print('records inserted!')
conn.close()

