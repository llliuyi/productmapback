from app import db
from flask import url_for


class Product(db.Model):
    __tablename__='productinfo'
    id = db.Column(db.INTEGER,primary_key=True, unique = True, autoincrement = True, nullable = False)
    productname = db.Column(db.String(80))
    position = db.Column(db.String(100))
    rank = db.Column(db.String(80))
    company = db.Column(db.String(80))
    type = db.Column(db.String(80))
    firsttime = db.Column(db.Date)
    newtime = db.Column(db.Date)
    downcount = db.Column(db.INTEGER)
    info = db.Column(db.String(255))
    gzh = db.Column(db.String(255))
    xcx = db.Column(db.String(255))
    cloudfirm = db.Column(db.String(255))
    tencent = db.Column(db.String(255))
