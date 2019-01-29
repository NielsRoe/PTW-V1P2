#Connect to Database
import psycopg2

conn = psycopg2.connect("dbname=Vuilcontainers user=postgres password=0000 host=127.0.0.1 port=5432")
cur = conn.cursor()

print("Connection is made!")


#Create the Table with different datatypes
cur.execute('''CREATE TABLE trashbins (
    trashbin_id VARCHAR(255) primary key not null,
    city VARCHAR(255) not null,
    street VARCHAR(255) not null,
    filled VARCHAR(3) not null)''')
	
print("Table is created!")