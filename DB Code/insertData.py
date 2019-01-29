#Connect to Database
import psycopg2

conn = psycopg2.connect("dbname=Vuilcontainers user=postgres password=0000 host=127.0.0.1 port=5432")
cur = conn.cursor()

print("Connection is made!")


#Insert data
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_1", "Utrecht", "Aarhuslaan", "Nee"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_2", "Utrecht", "Toulouselaan", "Nee"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_3", "Utrecht", "Helsinkilaan", "Nee"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_4", "Utrecht", "Cambridgelaan", "Ja"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_5", "Utrecht", "Cambridgelaan", "Nee"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_6", "Utrecht", "Heidelberglaan", "Nee"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_7", "Utrecht", "Heidelberglaan", "Ja"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_8", "Utrecht", "Padualaan", "Ja"))
cur.execute("INSERT INTO trashbins (trashbin_id, city, street, filled) VALUES (%s, %s, %s, %s)", ("Uithof_9", "Utrecht", "Padualaan", "Ja"))
conn.commit()

print("Data has been inserted!")