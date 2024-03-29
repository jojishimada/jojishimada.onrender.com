from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def novocontato():
    return render_template('contato.html')

@app.route('/desenvolvimentoAndroidKotlin/<path:subpath>')
def novoandroidkotlin(subpath):
    return render_template(subpath)

@app.route('/artigos/<nomeartigo>')
def novonomeartigo(nomeartigo):
    return render_template(nomeartigo)

@app.route('/zero')
def novo():
    return render_template('zero2.html')


