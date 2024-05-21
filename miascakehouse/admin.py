from flask import Blueprint
from . import db
from .models import Category, Cake, Order
import datetime

bp = Blueprint('admin', __name__, url_prefix='/admin/')

# Seed database into the website
@bp.route('/dbseed/')
def dbseed():
    category1 = Category(name='Sponge Cakes', image='Vanilla_sponge.webp', \
        description='''Sponge cakes include different flavours like chocolate, vanilla or cookies & cream.''')
    category2 = Category(name='Cheesecakes', image='Passionfruit_cheese.webp', \
        description='''Cheesecakes include chocolate cheesecake, passionfruit cheesecake or mortal sin cake.''')
    category3 = Category(name='Mud Cakes', image='Choc_mud.webp', \
        description='''Mud cakes include chocolate mud cake, caramel mud cake or marble mud cake.''')
    category4 = Category(name='Special Cakes', image='Pink_rosette.webp', \
        description='''Special cakes include black forest cake, pink rosette or carrot cake.''')
      
    try:
        db.session.add(category1)
        db.session.add(category2)
        db.session.add(category3)
        db.session.add(category4)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    c1 = Cake(category_id=category1.id, image='Vanilla_sponge.webp', size='20 cm', serves='10-12 people', price=39.90,\
        name='Vanilla Sponge Cake',\
        description= 'Vanilla sponge cake is a sponge cake filled with vanilla cream and rasplum jam decorated with dark chocolate flakes, finished with a customized hand-piped message on top.') 
    c2 = Cake(category_id=category1.id, image='Choc_sponge.webp', size='20 cm', serves='10-12 people', price=39.90,\
        name='Chocolate Sponge Cake',\
        description= 'Chocolate sponge cake is a scrumptious chocolate birthday sponge cake decorated with chocolate piping and surrounded with chocolate flakes.') 
    c3 = Cake(category_id=category1.id, image='Cookies_cream.webp', size='20 cm', serves='10-12 people', price=39.90,\
        name='Cookies & Cream Cake',\
        description= 'Cookies and cream cake is a vanilla sponge cake filled with vanilla cream with an outside border of crushed cookies, topped with vanilla cream, cookie pieces and choc shavings.')  
    c4 = Cake(category_id=category2.id, image='Choc_cheese.webp', size='20 cm', serves='10-12 people', price=39.90,\
        name='Chocolate Cheescake',\
        description= 'Chocolate cheesecake is a chocolate mud cake topped with mixture of chocolate cheesecake and chocolate fudge finished with a swirl of dark chocolate ganache.') 
    c5 = Cake(category_id=category2.id, image='Passionfruit_cheese.webp', size='20 cm', serves='10-12 people', price=39.90,\
        name='Passionfruit Cheesecake',\
        description= 'Passionfruit cheesecake is a silky smooth cheesecake topped with tangy passionfruit, messsage could be added to customized occasion.') 
    c6 = Cake(category_id=category2.id, image='Mortal_sin.webp', size='20 cm', serves='10-12 people', price=39.90,\
        name='Mortal Sin Cake',\
        description= 'Mortal sin cake includes a chocolate cookie base topped with vanilla cheesecake, chocolate mousse and a marshmallow fluff.') 
    c7 = Cake(category_id=category3.id, image='Choc_mud.webp', size = '20 cm', serves = '10-12 people', price=39.90,\
        name='Chocolate Mud Cake',\
        description= 'Chocolate mud cake is topped with peaks of chocolate ganache.') 
    c8 = Cake(category_id=category3.id, image='Caramel_mud.webp', size = '20 cm', serves = '10-12 people', price=39.90,\
        name='Caramel Mud Cake',\
        description= 'Caramel mud cake is a caramel mud cake covered in chocolate ganache with swirls of caramel ganache.') 
    c9 = Cake(category_id=category3.id, image='Marble_mud.webp', size = '20 cm', serves = '10-12 people', price=39.90,\
        name='Marble Mud Cake',\
        description= 'Marble mud cake is a moist chocolate marbled mud cake topped with swirled white chocolate and dark chocolate ganache.') 
    c10 = Cake(category_id=category4.id, image='Black_forest.webp', size = '20 cm', serves = '10-12 people', price=39.90,\
        name='Black Forest Cake',\
        description= 'Black forest cake is a decadent chocolate cake layered with cream & rich cherries - a traditional old favourite.') 
    c11 = Cake(category_id=category4.id, image='Pink_rosette.webp', size = '20 cm', serves = '10-12 people', price=39.90,\
        name='Pink Rosette Cake',\
        description= 'Pink rosette cake is a beautiful vanilla sponge filled with real cream and decorated in ombre pink shaded buttercream roses.') 
    c12 =  Cake(category_id=category4.id, image='Carrot_cake.webp', size = '20 cm', serves = '10-12 people', price=39.90,\
        name='Carrot Cake',\
        description= 'Carrot cake is a sweet and moist cake filled with carrots, walnuts, pineapple, spices and topped with an irresistible cream cheese icing and finished with walnut pieces.') 
    
    try:
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.add(c5)
        db.session.add(c6)
        db.session.add(c7)
        db.session.add(c8)
        db.session.add(c9)
        db.session.add(c10)
        db.session.add(c11)
        db.session.add(c12)
        db.session.commit()
    except:
        return 'There was an issue adding a cake in dbseed function'

    return 'DATA LOADED'