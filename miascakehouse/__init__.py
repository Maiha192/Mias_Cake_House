from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
app=Flask(__name__)

def create_app():
    app.debug=True
    app.secret_key='Mi4sC4k3H0us3!*'
    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///miascakehouse.sqlite' #create database with SQLite
    
    db.init_app(app)

    bootstrap = Bootstrap(app)
    
    from . import views
    app.register_blueprint(views.bp)
    from . import admin #after the data is loaded, this line can be commented out
    app.register_blueprint(admin.bp) #after the data is loaded, this line can be commented out
   
    return app

@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html")

@app.errorhandler(500)
def internal_error(e):
  return render_template("500.html")
