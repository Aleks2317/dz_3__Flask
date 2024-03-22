from flask import Flask, request, render_template, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from models_db import db, User
from form import RegistrationForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_user.db'
app.config['SECRET_KEY'] = '16afd6fe0bab986df7a804e633cbe64302b64dbae16eef4b96f1a727ecb37ec3'
csrf = CSRFProtect(app)
db.init_app(app)


@app.route('/')
def index():
    db.create_all()
    content = {
        'title': 'Start',
    }
    return render_template('start_page.html', **content)


@app.route('/user_activate/<name>')
def user_activate(name):
    print(f'{name=}')
    user = User.query.filter(User.name == name)
    print(user)

    # context = {
    #     'title': f'Hello {user.name} {user.surname}',
    #     'user': {
    #         'name': user.name,
    #         'surname': user.surname,
    #         'email': user.email,
    #     }
    # }
    return render_template('user_activate.html')


@app.route('/register/', methods=['POST', 'GET'])
def register():

    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_activate', name=name))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
