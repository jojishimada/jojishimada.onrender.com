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

@app.route('/zero')
def novo():
    return render_template('zero.html')


