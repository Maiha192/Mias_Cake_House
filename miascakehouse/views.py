from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Cake, Order
from datetime import datetime
from .forms import CheckoutForm, SearchForm
from . import db

bp = Blueprint('main', __name__)

# Create homepage
@bp.route('/')
def index():
    categories = Category.query.order_by(Category.name).all()
    return render_template('index.html', categories=categories)

# Create cake details page
@bp.route('/cakes/<int:categoryid>/')
def categorycakes(categoryid):
    cakes = Cake.query.filter(Cake.category_id == categoryid)
    return render_template('categorycakes.html', cakes=cakes)

# Create Shopping Cart function
@bp.route('/order', methods=['POST', 'GET'])
def order():
    cake_id = request.values.get('cake_id')

    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])

    else:
        order = None

    if order is None:
        order = Order(status=False, firstname='', lastname='', email='', phone='', totalprice=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('There was an issue creating a new order!')
            order = None

    totalprice = 0
    if order is not None:
        for cake in order.cakes:
            totalprice = totalprice + cake.price

    if cake_id is not None and order is not None:
        cake = Cake.query.get(cake_id)
        if cake not in order.cakes:
            try:
                order.cakes.append(cake)
                db.session.commit()
            except:
                return 'There was an issue adding the cake to your shopping cart!'
            return redirect(url_for('main.order'))
        else:
            flash('This cake has been successfully added to your shopping cart!')
            return redirect(url_for('main.order'))

    return render_template('order.html', order=order, totalprice=totalprice)

# Create Delete cake from the shopping cart function
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        cake_to_delete = Cake.query.get(id)
        try:
            order.cakes.remove(cake_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'There was an issue deleting this cake from your order'
    return redirect(url_for('main.order'))

# Create delete order/empty cart function
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All cakes have been successfully deleted from your shopping cart!')
    return redirect(url_for('main.index'))

# Create checkout function
@bp.route('/checkout/', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.deliverydate = form.deliverydate.data
            order.deliveryaddress=form.deliveryaddress.data
            totalprice = 0
            for cake in order.cakes:
                totalprice = totalprice + cake.price
            order.totalprice = totalprice
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you! Your order has been received and our team member will contact you shortly!')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order!'

    return render_template('checkout.html', form=form)

# Pass search result to NavBar in base
@bp.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

# Create Search function
@bp.route('/search',methods=['POST'])
def search():
    form = SearchForm()
    cakes = Cake.query
    if form.validate_on_submit():
        searched = form.searched.data
        cakes = cakes.filter(Cake.description.like('%'+searched+'%'))
        cakes = cakes.order_by(Cake.name).all()
        return render_template("search.html",form=form, searched = searched, cakes=cakes)
    else:
        return render_template("404.html")

