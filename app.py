from flask import Flask, request, render_template

from flask import jsonify

import psycopg2

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


@app.route('/test')
def showData():
    try:
        conn = psycopg2.connect(host='localhost',
                                    user='test',
                                    database='dbtest',
                                    password='pw')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table_test;")
        print("Je suis laaaaaaaaa")
        myresult = cursor.fetchall()
        #fermeture de la base de donnée
        conn.close()
        return jsonify(myresult)
    except Exception as e :
        print("Error :", e)  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2999, debug=True)