from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

#create flask instance
app = Flask(__name__)

#CSRF Token
app.config["SECRET_KEY"] = "wasklefgheakmhrfgblkj"

#login form class
class LoginForm(FlaskForm):
    username = StringField(label="username: ", validators=[DataRequired()])
    password = PasswordField(label="password: ", validators=[DataRequired()])
    submit = SubmitField(label="login")


#set up routing
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    username = None
    password = None
    form = LoginForm()
    #validate form
    if form.validate_on_submit():
        username = form.username.data
        form.username.data = ''
        password = form.password.data
        form.password.data = ''
    return render_template("login.html", username=username, password=password, form=form)

#run app
if __name__ == '__main__':
    app.run(debug=True)