import requests
import psycopg2
import psycopg2.extras
import datetime
import config

def populate_etf(response, etfid):
    etf = response.json()['profile'][0]
    print(f"Inserting etf {etf['name']} {etf['symbol']}")
    try:
        cursor.execute("""
        INSERT INTO ark_etf(etfId, name, symbol)
        VALUES(%s, %s, %s)""",
                       (etfid, etf['name'], etf['symbol']))

    except Exception as e:
        print(e)
        connection.rollback()

    connection.commit()
    return


#Connect to Postgres SQL server. Credentials imported from config.py
connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

cursor.execute("SELECT * FROM toy")

print(cursor.fetchall())

ark_symbols = ['ARKK', 'ARKQ', 'ARKW', 'ARKG', 'ARKF', 'PRNT', 'IZRL']

profile_url = 'https://arkfunds.io/api/v1/etf/profile'

r = requests.get(profile_url)

response = r.json()
for symbol in ark_symbols:

    try:
        cursor.execute(f"SELECT id FROM stock WHERE symbol='{symbol}'")
        etfid = cursor.fetchall()
    except Exception as e:
        print(e)
        connection.rollback()

    params = {'symbol':symbol}
    response = requests.get(profile_url, params = params)
    if response.status_code==200:
        populate_etf(response, etfid[0][0])


