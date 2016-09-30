import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="1234", host="localhost", port="5432")
print 'Sucessfully connected to database'

cur = conn.cursor()
# SQL goes here

conn.commit()
cur.close()
conn.close()