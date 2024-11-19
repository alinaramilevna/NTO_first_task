import datetime

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    '''Base database model class (DeclarativeBase)'''
    pass


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True
    )

    name = sqlalchemy.Column(
        sqlalchemy.String
    )

    surname = sqlalchemy.Column(
        sqlalchemy.String
    )


class Type(Base):
    __tablename__ = 'types'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True
    )
    title = sqlalchemy.Column(
        sqlalchemy.String,
        unique=True
    )


class Order(Base):
    __tablename__ = 'orders'
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True
    )

    time_registration = sqlalchemy.Column(
        sqlalchemy.String
    )

    time_ready = sqlalchemy.Column(
        sqlalchemy.String
    )

    user = sqlalchemy.Column(
        sqlalchemy.String
    )

    count = sqlalchemy.Column(
        sqlalchemy.Integer
    )

    comment = sqlalchemy.Column(
        sqlalchemy.String
    )

    type = sqlalchemy.Column(
        sqlalchemy.String
    )

    status = sqlalchemy.Column(
        sqlalchemy.String
    )
