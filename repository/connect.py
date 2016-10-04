import psycopg2

class Connection:

    def __init__(self, database, user, pw, host, port):
        self.conn = psycopg2.connect(database=database, user=user, password=pw, host=host, port=port)
        print 'Successfully connected to database at ' + host + ' as user ' + user

    def begin(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def finish(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        print "Connection finished and closed"

