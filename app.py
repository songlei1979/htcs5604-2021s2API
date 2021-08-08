import decimal

from flask import Flask, send_from_directory, request, redirect, url_for, session, render_template
import simplejson as json

from Classes import DataShow
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
# secret key
app.secret_key = 'cairocoders-ednalar'

@app.route('/')
def home():
    # check if user is loggedin
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # output message if something goes wrong...
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if username == "ISCG5604" and password == "ISCG5604":
            session['loggedin'] = True
            session['username'] = "ISCG5604"
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/viewaproduct')
def viewaproduct():
    # check if user is loggedin
    if 'loggedin' in session:
        return render_template('viewaproduct.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/viewanoutlet')
def viewanoutlet():
    # check if user is loggedin
    if 'loggedin' in session:
        return render_template('viewanoutlet.html', username=session['username'])
    return redirect(url_for('login'))

# products
@app.route('/products')
def getProducts():
    ds = DataShow()
    products = ds.products()
    return json.dumps(products)

@app.route('/product/<product_id>')
def getProduct(product_id):
    ds = DataShow()
    return json.dumps(ds.product(product_id))

#Product Category
@app.route('/productcategories')
def getCategories():
    ds = DataShow()
    categories = ds.productCategories()
    return json.dumps(categories)

@app.route('/productcategory/<category_id>')
def getCategory(category_id):
    ds = DataShow()
    return json.dumps(ds.productCategory(category_id))

#Outlet
@app.route('/outlets')
def getOutlets():
    ds = DataShow()
    outlets = ds.outlets()
    return json.dumps(outlets)

@app.route('/outlet/<outlet_id>')
def getOutlet(outlet_id):
    ds = DataShow()
    return json.dumps(ds.outlet(outlet_id))

#Order
@app.route('/orders')
def getOrders():
    ds = DataShow()
    orders = ds.orders()
    return json.dumps(orders)

@app.route('/order/<order_id>')
def getOrder(order_id):
    ds = DataShow()
    return json.dumps(ds.order(order_id))

#Orderline
@app.route('/orderlines')
def getOrderlines():
    ds = DataShow()
    orders = ds.orderlines()
    return json.dumps(orders)

@app.route('/orderline/<orderline_id>')
def getOrderline(orderline_id):
    ds = DataShow()
    return json.dumps(ds.orderline(orderline_id))

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

if __name__ == '__main__':
    app.run()
