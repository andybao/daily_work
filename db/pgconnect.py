"""PgConnect Class"""
import psycopg2 as pgconn


class PgConnect(object):
    """Initial Class for Handling PostgreSQL Connections"""
    _db_conn = None
    _db_cur = None


    def __init__(self):
        """Set DB access parameters"""
        try:
            self._db_conn = pgconn.connect("dbname='ap_pilot' \
			    user='apadmin' host='192.168.3.252' password='dysan100'")
            self._db_conn.autocommit = True
        except pgconn.Error as pgerror:
            print "I am unable to connect to the database. %s" % repr(pgerror)

        self._db_cur = self._db_conn.cursor()

    def get_connection(self):
        """Get the Connection"""
        return self._db_conn

    def get_cursor(self):
        """Get the Cursor"""
        return self._db_cur

    def __del__(self):
        """close database connection"""
        self._db_conn.close()
