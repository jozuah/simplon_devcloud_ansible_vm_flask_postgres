import psycopg2

class Create_and_set_database():

    def __init__(self):
        self.conn = self.connection_db()
        self.createTable()
        self.insertData()

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
            #sql_query.execute("DROP TABLE MaTable")
            sql_query.execute("CREATE TABLE IF NOT EXISTS matable (id serial PRIMARY KEY NOT NULL)")
            self.conn.commit()
        except Exception as e:
            print("Error :", e)
    
    def insertData(self):
        try:
            sql_query = self.conn.cursor()
            sql_query.execute("INSERT INTO matable (id) VALUES (DEFAULT);")
            self.conn.commit()
        except Exception as e:
            print("Error :", e)
    




db = Create_and_set_database ()