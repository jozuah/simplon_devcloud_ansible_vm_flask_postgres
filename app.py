from flask import Flask, request, render_template

from flask import jsonify

import psycopg2

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/inc')
def addData():
    try:
        conn = psycopg2.connect(host='localhost',
                                    user='test',
                                    database='dbtest',
                                    password='pw')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO matable (id) VALUES (DEFAULT);")
        conn.commit()
        return "Une valeur à été ajouté"
    except Exception as e :
        print("Error :", e)  

@app.route('/id')
def showData():
    try:
        conn = psycopg2.connect(host='localhost',
                                    user='test',
                                    database='dbtest',
                                    password='pw')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM matable ORDER BY id DESC LIMIT 1;")
        myresult = cursor.fetchall()
        conn.close()
        return jsonify(myresult)
    except Exception as e :

        print("Error :", e)  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)