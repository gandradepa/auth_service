# /home/developer/auth_service/auth_model.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

# Initialize the extensions, but don't tie them to an app yet.
# This allows us to use them in different apps.
db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model, UserMixin):
    """Defines the User database model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hashes and sets the user's password."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Checks if a provided password matches the hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class FLSAsset(db.Model):
    __tablename__ = 'fls_assets'
    index = db.Column(db.String(50), primary_key=True)
    work_order = db.Column(db.String(100))
    asset_tag = db.Column(db.String(100))
    asset_group = db.Column(db.String(255))
    description = db.Column(db.String(500))
    property = db.Column(db.String(255))
    space = db.Column(db.String(255))
    attribute_set = db.Column(db.String(255))
    device_address = db.Column(db.String(100))
    device_type = db.Column(db.String(255))
    un_account_number = db.Column(db.String(100))
    planon_code = db.Column(db.String(100))
    creation_date = db.Column(db.String(20))
    status = db.Column(db.String(20))
    workflow = db.Column(db.String(100))

    def to_dict(self):
        """Serializes the object to a dictionary."""
        return {
            'index': self.index,
            'work_order': self.work_order,
            'asset_tag': self.asset_tag,
            'asset_group': self.asset_group,
            'description': self.description,
            'property': self.property,
            'space': self.space,
            'attribute_set': self.attribute_set,
            'device_address': self.device_address,
            'device_type': self.device_type,
            'un_account_number': self.un_account_number,
            'planon_code': self.planon_code,
            'creation_date': self.creation_date,
            'status': self.status,
            'workflow': self.workflow
        }

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False, index=True)
    spaces = db.relationship('Space', backref='property', lazy=True, cascade="all, delete-orphan")

class Space(db.Model):
    __tablename__ = 'spaces'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.id'), nullable=False)

class AssetGroup(db.Model):
    __tablename__ = 'asset_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class DeviceTypeMap(db.Model):
    __tablename__ = 'device_type_map'
    id = db.Column(db.Integer, primary_key=True)
    classification_key = db.Column(db.String(255), unique=True, nullable=False, index=True)
    device_type = db.Column(db.String(255), nullable=False)