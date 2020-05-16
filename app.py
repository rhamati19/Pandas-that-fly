# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author:
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")
@app.route("/research")
def research():
    return render_template("research.html")
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

#start the server
if __name__ == "__main__":
    app.run()