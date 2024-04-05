from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

logs = []

@app.route('/')
def ola():
    return render_template('dash.html')

@app.route('/ping', methods=['GET'])
def ping():
    entrada = {
        "rota": "/ping",
        "metodo": "GET",
        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    logs.append(entrada)
    return "pong"

@app.route('/echo', methods=['GET','POST'])
def echo():
    dados = request.form.get('dados', '')
    entrada = {
        "rota": "/echo",
        "metodo": "POST",
        "dados": dados,
        "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    logs.append(entrada)
    return dados

@app.route('/dash')
def dash():
    return render_template('dash.html', logs=logs)

@app.route('/info')
def info():
    info = ''.join(f"{entrada['rota']}, {entrada['metodo']}, {entrada['hora']}" for entrada in logs)
    return info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
