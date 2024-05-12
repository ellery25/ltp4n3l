from config.bd import db, ma, app

class V1s1t(db.Model):
    __tablename__ = 'v1s1t'

    contador = db.Column(db.Integer, primary_key=True)

    def __init__(self, contador):
        self.contador = contador

with app.app_context():
    db.create_all()

class V1s1tSchema(ma.Schema):
    class Meta:
        fields = ('contador',)