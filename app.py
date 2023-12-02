from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def novocontato():
    return render_template('contato.html')

@app.route('/desenvolvimentoAndroidKotlin')
def novodevandroidkotlin():
    return render_template('devandroidkotlin.html')

@app.route('/templates/android_kotlim_introducao.html')
def android_kotlim_introducao():
    return render_template('android_kotlim_introducao.html')


@app.route('/zero')
def novo():
    return render_template('zero.html')


