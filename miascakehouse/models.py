from . import db

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False, default = 'Pink_rosette.webp')
    cakes = db.relationship('Cake', backref='Category', cascade="all, delete-orphan")

    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}\n" 
        str =str.format( self.id, self.name,self.description,self.image)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('cake_id',db.Integer,db.ForeignKey('cakes.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'cake_id') )

class Cake(db.Model):
    __tablename__='cakes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    size = db.Column(db.String(64),nullable=False)
    serves = db.Column(db.String(64),nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    def __repr__(self):
        str = "Id: {}, Name: {}, Description: {}, Image: {}, Size: {}, Serves: {}, Price: {}, Category: {}\n" 
        str =str.format( self.id, self.name,self.description,self.image, self.size, self.serves, self.price, self.category_id)
        return str

class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    deliverydate = db.Column(db.DateTime)
    deliveryaddress = db.Column(db.String(128))
    totalprice = db.Column(db.Float)
    date = db.Column(db.DateTime)
    cakes = db.relationship("Cake", secondary=orderdetails, backref="orders")
    
    def __repr__(self):
        str = "id: {}, Status: {}, Firstname: {}, Lastname: {}, Email: {}, Phone: {}, Delivery Date: {}, Delivery Address: {}, Date: {}, Cakes: {}, Total Price: {}\n" 
        str =str.format( self.id, self.status,self.firstname,self.lastname, self.email, self.phone, self.deliverydate, self.deliveryaddress, self.date, self.cakes, self.totalprice)
        return str
