from flask import  render_template, session, request, redirect, url_for

from src.shop import  app, db

@app.route("/")
def home():
    return "Homepage of your shop"