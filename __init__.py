from flask import Flask
from flask import render_template
from flask import json

app = Flask(name)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for j in range(valeur):
        for i in range(J+1):
            etoiles += '*'
        etoiles += '<br>'
    return etoiles

if name == "main":
    app.run(debug=True)
