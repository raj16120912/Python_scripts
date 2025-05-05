import psycopg2

db = psycopg2.connect(dbname="postgres", host="db01-raj.ops", user="rajp", password="N!d@vell!r2018")
cur = db.cursor()
cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public';")

for each in cur.fetchall:
    for db in each:
        print (db)