import psycopg2

class Create_and_set_database():

    def __init__(self):
        self.conn = self.connection_db()
        self.createTable()

    def connection_db(self):
        try:
            conn = psycopg2.connect(host='localhost',
                                            user='test',
                                            database='dbtest',
                                            password='pw')
                                            
            print("Connected to my database")
            return conn
        except Exception as err:
            print("Error :",err)

    def createTable (self):
        try:
            sql_query = self.conn.cursor()
            sql_query.execute("CREATE TABLE table_test (id serial PRIMARY KEY NOT NULL, nom VARCHAR(100) NOT NULL)")
            self.conn.commit()
        except Exception as e:
            print("Error :", e)


db = Create_and_set_database ()