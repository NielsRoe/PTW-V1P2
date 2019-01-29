#Connect to Database
import psycopg2

conn = psycopg2.connect("dbname=Vuilcontainers user=postgres password=0000 host=127.0.0.1 port=5432")
cur = conn.cursor()

print("Connection is made!")


#Show the current Table
SELECT * FROM trashbins;