from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField,DateField
from wtforms.validators import InputRequired, email

# Create Checkout Form
class CheckoutForm(FlaskForm):
    firstname = StringField("First name", validators=[InputRequired()])
    lastname = StringField("Last name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), email()])
    phone = StringField("Phone number", validators=[InputRequired()])
    deliverydate = DateField("Delivery date",validators=[InputRequired()])
    deliveryaddress = StringField("Delivery address",validators=[InputRequired()])
    submit = SubmitField("SUBMIT ORDER")

# Create Search Form
class SearchForm(FlaskForm):
    searched = StringField("Searched",validators=[InputRequired()])
    submit = SubmitField("Search")
