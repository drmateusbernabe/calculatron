from flask import Flask, request, jsonify
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route('/calculatron')
def calculatron():

    return render_template('calculatron.html')


@app.route('/sobre')
def sobre():

    return render_template('sobre.html')


@app.route('/curriculum')
def curriculum():

    return render_template('curriculum.html')


@app.route('/portifolio')
def portifolio():

    return render_template('portifolio.html')


@app.route('/contato')
def contato():

    return render_template('contato.html')


@app.route('/obrigado')
def obrigado():

    return render_template('obrigado.html')


app.run(debug=True)
