import sqlite3 

conn = sqlite3.connect('ages.sqlite') 
cur = conn.cursor() 

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

cur.execute('DELETE FROM Ages')
cur.execute('INSERT INTO Ages (name,age) VALUES (?,?)', 
	('Derek',36)) 
cur.execute('INSERT INTO Ages (name,age) VALUES(?,?)', 
	('Joshua',30))
cur.execute('INSERT INTO Ages (name,age) VALUES(?,?)', 
	('Diella',26))
cur.execute('INSERT INTO Ages (name,age) VALUES(?,?)', 
	('Reice',17)) 
cur.execute('INSERT INTO Ages (name,age) VALUES(?,?)', 
	('Tibet',40))

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')

conn.commit()
for row in cur:
	print(row)
	break 
cur.close() 
conn.close()