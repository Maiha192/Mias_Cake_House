1.  Before testing this application, you must create a fresh database. Do this by invoking a python interpreter shell in the directory just above the miascakehouse package (in same directory as run.py). Create database by typing in the terminal:

    from miascakehouse import db, create_app
    db.create_all(app=create_app())
    quit()

2.  You should check that the database has been created (miascakehouse.sqlite)

3.  Then run application. There is no data in the database so you need to seed database by navigating to the dbseed route:
    
    127.0.0.1:5000/admin/dbseed/
    If the seeding process has worked then you should be greeted by 'DATA LOADED'.  

4.  Once the database has been seeded you should comment out the admin Blueprint in the __init.py__ package constructor.

    #from . import admin
    #app.register_blueprint(admin.bp)
            
