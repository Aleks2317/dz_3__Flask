from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Comment: \n({self.id_ = },\n' \
               f'{self.name = },\n' \
               f'{self.surname = },\n' \
               f'{self.email = },\n' \
               f'{self.password = },\n' \
               f'{self.created_at = },\n)'

