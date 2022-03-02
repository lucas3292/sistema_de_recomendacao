from email import header
from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


software = Flask(__name__)
Bootstrap(software)

@software.route("/")
def index():
    return "<a href = '/posts '>Posts</a>"

@software.route("/redirect")
def redirectUser():
    return redirect(url_for("response"))

@software.route("/response")
def response():
    return render_template("response.html")

@software.route("/posts")
@software.route("/posts/<int:id>")
def posts(id):
    titulo = request.args.get("titulo")
    data = dict(
        path = request.path,
        referrer = request.referrer,
        content_type =  request.content_type,
        method = request.method,
        titulo = titulo,
        id = id if id else 0
    )
    return data

from software.controllers import default