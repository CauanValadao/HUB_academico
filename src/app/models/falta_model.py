from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

class Falta(db.Model):
    __tablename__ = 'faltas'
    
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    disciplina_id = db.Column("disciplina_id", db.Integer, db.ForeignKey('disciplinas.id'), nullable=False)
    data_falta = db.Column("data_falta", db.DateTime, nullable=False, default=datetime.utcnow)
    motivo = db.Column("motivo", db.String(255), nullable=True)
