from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
 for i in range(1, valeur + 1):
         espaces = ' ' * (valeur - i) 
        partie_croissante= for j in range(1, i + 1))
        partie_decroissante = for j in range(i - 1, 0, -1))
        print(espaces + partie_croissante + partie_decroissante)
     return etoiles
