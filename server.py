from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    vartitle = request.form['input-title']
    varauthor = request.form['input-author']
    return redirect(f'/books/{vartitle}/{varauthor}')

@app.route('/books/<routetitle>/<routeauthor>')
def books(routetitle, routeauthor):
    return render_template("book.html", jinjatitle = routetitle, jinjaauthor = routeauthor)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 