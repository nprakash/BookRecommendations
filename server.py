from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    vartitle = request.form['in-title']
    varauthor = request.form['in-author']
    return redirect(f'/books/{vartitle}/{varauthor}')

@app.route('/books/<booktitle>/<bookauthor>')
def books(booktitle, bookauthor):
    return render_template("book.html", title = booktitle, author = bookauthor)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 