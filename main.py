from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
   return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/contact")
def contact():
     return render_template('contact.html')
@app.route("/category")
def shop():
     return render_template('category.html')
@app.route("/product")
def single():
     return render_template('product.html')
@app.route("/boat")
def boat():
     return render_template('boat.html')
@app.route("/oppo")
def oppo():
     return render_template('oppo.html')
@app.route("/pandrive")
def pan():
     return render_template('pandrive.html')
@app.route("/earbuds")
def earbuds():
     return render_template('earbuds.html')
@app.route("/smartwatch")
def watch():
     return render_template('smartwatch.html')
app.run(debug=True)