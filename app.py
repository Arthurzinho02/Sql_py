from flask import Flask, render_template, request
import pandas as pd
import mysql.connector


app = Flask(__name__)
       
@app.route("/")
def homepage():  
    return render_template("login.html", logado=False)

@app.route("/login", methods=['POST'])
def submit():
    conexao = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password ='',
        database = 'SENAI'
    )

    if conexao.is_connected():
        print("Conexão estabelecida com sucesso!")
    cursor = conexao.cursor()
    email = request.form['email']
    password = request.form['password']
    comando = "SELECT email, password FROM users WHERE email= %s and password = %s"
    cursor.execute(comando, (email, password))

    resultados = cursor.fetchall()
    if resultados:
        cursor.close()
        conexao.close()
        return render_template("login.html", logado = True)
    else:
        cursor.close()
        conexao.close()
        return render_template("login.html", logado= False)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

