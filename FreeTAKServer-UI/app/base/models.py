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
    __tablename__ = 'user'
    uid = Column(String(25))
    id = Column(Integer, primary_key=True, autoincrement=True)
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
        return str(self.uid)


@login_manager.user_loader
def user_loader(uid):
    return User.query.filter_by(uid=uid).first()

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('uid')
    user = User.query.filter_by(uid=username).first()
    return user if user else None