from . import db
from cryptography.fernet import Fernet
import json

# for type annotation
from datetime import datetime as dt


class Bsn(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    bsn = db.Column(db.String)

    # relationships
    owner_id = db.Column(db.Integer, db.ForeignKey('civilian.id'))

    def __repr__(self) -> str:
        return f"<Bsn {(self.id, self.bsn)}>"

    def __init__(self, bsn: str, owner_id: int):
        self.bsn, self.owner_id = bsn, owner_id


class Civilian(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date)
    key = db.Column(db.LargeBinary)

    # relationships
    bsns = db.relationship('Bsn', backref="owner", lazy=True)

    def __init__(self, name: str, birthday: dt):
        self.name, self.birthday = name, birthday

        self.key = Fernet.generate_key()

    def verify_bsn(self, bsn: str):
        f = Fernet(self.key)
        message = f.decrypt(bsn)
        try:
            data = json.loads(message)
            data = {
                **data,
                "owner": {
                    "name": self.name,
                    "birthday": self.birthday.strftime("%Y-%m-%d")
                }
            }
            return data
        except json.decoder.JSONDecodeError:
            return False

    def generate_key(self, usecase: str, expiry_date: dt) -> str:
        data = {
            "usecase": usecase,
            "expiry_date": expiry_date.strftime("%Y-%m-%d")
        }
        message = json.dumps(data).encode()
        f = Fernet(self.key)

        encrypted_message = f.encrypt(message)

        new_bsn = Bsn(encrypted_message, self.id)

        db.session.add(new_bsn)
        db.session.commit()

        return new_bsn
