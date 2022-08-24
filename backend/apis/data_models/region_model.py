from apis import db, api
from flask_restx import fields
from apis.data_models.base import BaseMode
from typing import List, Dict


region_params = api.model(
    'Region',
    {
        'id': fields.Integer(),
        'region': fields.String(required=False, default=""),
        'recovered': fields.Integer(required=True),
        'deaths': fields.Integer(required=True),
        'confirmed': fields.Integer(required=True),
        'lat': fields.String(required=False, default=""),
        'long': fields.String(required=False, default=""),
        'updated': fields.String(required=False, default="")
    }
)

region_update_params = api.model(
    'Region',
    {
        'region': fields.String(required=False, default=""),
        'recovered': fields.Integer(required=True),
        'deaths': fields.Integer(required=True),
        'confirmed': fields.Integer(required=True),
        'lat': fields.String(required=False, default=""),
        'long': fields.String(required=False, default=""),
        'updated': fields.String(required=False, default="")
    }
)


class RegionModel(BaseMode, db.Model):
    __tablename__ = 'region'
    id = db.Column(db.Integer(), primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=True)
    region = db.Column(db.String(200), nullable=True)
    recovered = db.Column(db.BigInteger(), nullable=True)
    confirmed = db.Column(db.BigInteger(), nullable=True)
    deaths = db.Column(db.BigInteger(), nullable=True)
    lat = db.Column(db.String(80), nullable=True)
    long = db.Column(db.String(80), nullable=True)
    updated = db.Column(db.String(80), nullable=True)
    db.UniqueConstraint(country_id, region)
