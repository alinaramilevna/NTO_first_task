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


class Status(Base):
    __tablename__ = 'statuses'

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
        sqlalchemy.DateTime,
        default=datetime.datetime.now(datetime.UTC)
    )

    time_ready = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now(datetime.UTC)
    )

    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('users.id'),
        nullable=True
    )

    type_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('types.id')
    )

    count = sqlalchemy.Column(
        sqlalchemy.Integer
    )

    comment = sqlalchemy.Column(
        sqlalchemy.String
    )

    status_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('statuses.id')
    )

    def __init__(self, user_id=None, type_id=None, count=None, **kwargs):
        super().__init__(**kwargs)
        self.user_id = user_id
        self.type_id = type_id
        self.count = count
        self.status = 'Черновик' if not user_id or not type_id or not count else 'Согласован клиентом'

    __table_args__ = (
        sqlalchemy.CheckConstraint(count >= 0, name='check_bar_positive'),
        {})
