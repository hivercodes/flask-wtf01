from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

#create flask instance
app = Flask(__name__)

#CSRF Token
app.config["SECRET_KEY"] = "wasklefgheakmhrfgblkj"

#login form class
class LoginForm(FlaskForm):
    username = StringField(label="username: ", validators=[DataRequired(), Email()])
    password = PasswordField(label="password: ", validators=[DataRequired(), Length(min=8)])
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
        if username == "admin@email.com" and password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", username=username, password=password, form=form)

#run app
if __name__ == '__main__':
    app.run(debug=True)