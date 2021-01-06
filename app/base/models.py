# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String

from app import db, login_manager

from app.base.util import hash_pass

class User(db.Model, UserMixin):
    __tablename__ = 'SystemUser'
    uid = Column(String(25), primary_key=True)
    name = Column(String(15), nullable=False)
    token = Column(String(30), nullable=True)
    password = Column(String(30), nullable=True)
    group = Column(String(15), default=True, nullable=True)
    certificate_package_name = Column(String(30), nullable=True, default=None)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            setattr(self, property, value)

    def get_id(self):
        return self.uid

    def __repr__(self):
        return str(self.name)


@login_manager.user_loader
def user_loader(uid):
    return User.query.filter_by(uid=uid).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(name=username).first()
    return user if user else None