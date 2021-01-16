from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# print('hello!')
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return f"User('{self.username}', '{self.password}')"


class Keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kyd = db.Column(db.String(100), nullable=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Keyword('{self.kyd}', '{self.date_added}')"


@app.route('/') 
def home():
    return render_template("index.html")

# @app.route('/admin')
# def admin():
#     return render_template("admin.html")


@app.route('/admin', methods=['POST', 'GET']) 
def admin():
    if request.method == 'GET':
        return render_template("admin.html")

    else:
        print('*************************************************')
        print(request.form['newword'])
        wow = request
        new = Keyword(kyd=request.form['newword'], date_added=datetime.utcnow())
        db.session.add(new)
        db.session.commit()
        print(db.session.commit())
        return redirect(url_for('home'))



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    elif request.method == 'POST' and request.form['email'] == 'admin' and request.form['pswd'] == 'changekeys':
        # print(request.form['email'])
        # print(request.form['pswd'])
        request.form['email'] == 'admin'
        request.form['pswd'] == 'changekeys'
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(debug=True)
    