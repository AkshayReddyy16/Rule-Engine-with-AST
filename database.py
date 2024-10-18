from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    condition = db.Column(db.String(255), nullable=False)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
