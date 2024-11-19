from contextlib import contextmanager
from typing import Type, Optional, Callable

from sqlalchemy.exc import SQLAlchemyError

from db.models import Base


class CRUDBase:
    def __init__(self, model: Type[Base]):
        self.model = model

    def get(self, db_session: Callable[[], contextmanager], id: int) -> Optional[Base]:
        try:
            with db_session() as session:
                return session.query(self.model).filter(self.model.id == id).first()
        except SQLAlchemyError as e:
            print(f"Error fetching record by ID: {e}")
            return None

    def get_all(self, db_session: Callable[[], contextmanager]) -> list[Base]:
        try:
            with db_session() as session:
                return session.query(self.model).all()
        except SQLAlchemyError as e:
            print(f"Error fetching all records: {e}")
            return []

    def create(self, db_session: Callable[[], contextmanager], obj_in: dict) -> Optional[Base]:
        try:
            with db_session() as session:
                db_obj = self.model(**obj_in)
                session.add(db_obj)
                session.commit()
                session.refresh(db_obj)
                return db_obj
        except SQLAlchemyError as e:
            print(f"Error creating record: {e}")
            return None

    def update(self, db_session: Callable[[], contextmanager], db_obj: Base, obj_in: dict) -> Optional[Base]:
        try:
            with db_session() as session:
                for field, value in obj_in.items():
                    setattr(db_obj, field, value)
                session.add(db_obj)
                session.commit()
                session.refresh(db_obj)
                return db_obj
        except SQLAlchemyError as e:
            print(f"Error updating record: {e}")
            return None

    def delete(self, db_session: Callable[[], contextmanager], db_obj: Base) -> bool:
        try:
            with db_session() as session:
                session.delete(db_obj)
                session.commit()
                return True
        except SQLAlchemyError as e:
            print(f"Error deleting record: {e}")
            return False


class CRUDUser(CRUDBase):
    pass


class CRUDType(CRUDBase):
    pass


class CRUDStatus(CRUDBase):
    pass


class CRUDOrder(CRUDBase):
    pass
