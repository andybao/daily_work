from pgconnect import PgConnect

pgdb=PgConnect()
conn = pgdb.get_connection()
c=pgdb.get_cursor()