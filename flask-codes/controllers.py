from app import app
from flask import render_template, request
from models import Product, Color, Contact, User, Category
from forms import ContactForm, RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

colors = ['black', 'yellow', 'purple']


@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/register", methods = ['GET', 'POST'])
def reg():
    form = RegisterForm()
    if request.method == 'POST':
        print('post')
        form = RegisterForm(request.form)
        if form.validate_on_submit():
            print('valid')
            user = User(
                name = form.name.data,
                email = form.email.data,
                password = generate_password_hash(form.password.data)
            )
            user.save()
    return render_template('register.html', form = form)


@app.route("/login", methods = ['GET', 'POST'])
def log():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(name = form.name.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            print('login')
            return render_template('index.html')

    return render_template('login.html', form = form)



@app.route("/product-list")
def productList():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('product-list.html', products = products, categories = categories)


@app.route("/category/<string:name>/")
def cat(name):
    products = Category.query.filter_by(name = name).first().products
    categories = Category.query.all()
    return render_template('product-list.html', products = products, categories = categories)



@app.route("/product-detail/<int:id>/")
def product(id):
    product = Product.query.filter_by(id = id).first()
    colors = Color.query.all()
    return render_template('product-detail.html', item = product, colors = colors)



@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        print(request.form)
        print('post')
        form = ContactForm(request.form)
        if form.validate_on_submit():
            print('valid')
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                company = form.company.data,
                message = form.message.data,
                is_subscribe = form.is_subscribe.data
            )
            contact.save()
    return render_template('contact.html', form = form)