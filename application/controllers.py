from flask import current_app as app
from flask import render_template
from .product import Product

PRODUCTS = [
    Product("static/airpods.jpg", "Air Pods"),
    Product("https://m.media-amazon.com/images/I/41ElkS-Z9ML._SX300_SY300_QL70_FMwebp_.jpg", "Smart Watch")

]
@app.route("/")
def home():
    return render_template("index.html", products = PRODUCTS)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/refer")
def refer():
    return render_template("refer.html")