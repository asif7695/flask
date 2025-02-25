from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
app.app_context().push()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length = 30), nullable = False, unique = True)
    barcode = db.Column(db.String(length = 12), nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(length = 1024), nullable = False,)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
        {'Serial': 101, 'Name': 'Pen', 'Barcode': 80124123, 'Price': 1},
        {'Serial': 102, 'Name': 'Pencil', 'Barcode': 47291734, 'Price': 1.5},
        {'Serial': 103, 'Name': 'Book', 'Barcode': 91374178, 'Price': 5},
        {'Serial': 104, 'Name': 'Notebook', 'Barcode': 58261919, 'Price': 3},
    ]
    return render_template('market.html', item=items)


@app.route('/about/<user>')
def about(user):
    return f'<h1>Welcome {user}</h1>'



if __name__ == '__main__':
    app.run(debug=True)