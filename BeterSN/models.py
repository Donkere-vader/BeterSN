from . import db
from cryptography.fernet import Fernet
import json

# for type annotation
from datetime import datetime as dt


class Bsn(db.Model):
    """
    Database model met de tijdelijke BSN's
    """
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    bsn = db.Column(db.String)

    # relationships
    owner_id = db.Column(db.Integer, db.ForeignKey('civilian.id'))

    def __init__(self, bsn: str, owner_id: int):
        self.bsn, self.owner_id = bsn, owner_id


class Civilian(db.Model):
    """
    Database model van een burger
    """
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String)
    key = db.Column(db.LargeBinary)

    # relationships
    bsns = db.relationship('Bsn', backref="owner", lazy=True)

    def __init__(self, name: str):
        self.name = name

        self.key = Fernet.generate_key()

    def verify_bsn(self, bsn: str):
        f = Fernet(self.key)
        message = f.decrypt(bsn)
        try:
            data = json.loads(message)
            data = {
                **data,
                "civilian": {
                    "name": self.name
                }
            }
            return data
        except json.decoder.JSONDecodeError:
            return False

    def generate_bsn(self, usecase: str, expiry_date: dt) -> str:
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
