from flask import request, blueprints, redirect,session, render_template, jsonify
from models.User import User, db, UserSchema

users_routes = blueprints.Blueprint("users", __name__)


@users_routes.route('/getUsers', methods=['GET'])
def getUsers():
    users = User.query.all()
    schema = UserSchema(many=True)
    result = schema.dump(users)
    return jsonify(result)

@users_routes.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if 'username' in session:
        return redirect('/monitoring')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(name=username).first()

        if user is None or user.password != password:
            error_message = 'Usuario no encontrado o contraseña incorrecta'
        else:
            session['username'] = username
            return redirect('/monitoring')

    return render_template('login.html', error_message=error_message)


@users_routes.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')

    return redirect('/')