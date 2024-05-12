from flask import Flask, render_template, session, redirect
from models import *
from config.bd import db, app, socketio
from flask_socketio import SocketIO

from apis.user_route import users_routes
from apis.datatable_route import dataTables_routes
from apis.events_route import events_routes

app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(dataTables_routes, url_prefix='/dataTables')
app.register_blueprint(events_routes, url_prefix='/events')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/monitoring')
def monitoring():
        
    if 'username' not in session:
        return redirect('/')
    else:
        return render_template('panel.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000, host="0.0.0.0")