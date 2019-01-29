import psycopg2
from config import Config
from flask import Flask

def update_vendor(full):
    hostname = '127.0.0.1'
    username = 'postgres'
    psword = '0000'
    dtbase = 'Vuilcontainers'
    if full == True:
        sql = """ UPDATE trashbins SET filled = 'Ja' WHERE trashbin_id = 'Uithof_6'"""
        conn = None
        updated_rows = 0
    else:
        sql = """ UPDATE trashbins SET filled = 'Nee' WHERE trashbin_id = 'Uithof_6'"""
        conn = None
        updated_rows = 0
    try:
        params = Config()
        #Verbind met de database
        conn = psycopg2.connect(host=hostname, user=username, password=psword, dbname=dtbase)
        #Creeër een nieuwe cursor
        cur = conn.cursor()
        #Voer het UPDATE script uit
        cur.execute(sql, ('filled', 'Uithof_6'))
        # get the number of updated rows
        updated_rows = cur.rowcount
        #Sla de wijzigingen op
        conn.commit()
        #Verbreek de connectie met de database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

#Voor de computer

app = Flask(__name__)   #Standaard gebruik van Flask
#De route bepaalt bij welk pad de onderstaande callback hoort
@app.route("/nietvol")
def niet_vol():
    return str(update_vendor(False))

@app.route("/vol")
def vol():
    return str(update_vendor(True))

if __name__ == '__main__':
    app.run(host='192.168.42.3')