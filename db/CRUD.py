from typing import Type, List, Optional

from sqlalchemy.orm import Session


class CRUDBase:
    def __init__(self, model: Type[Base]):
        """
        Базовый CRUD класс для работы с моделями.
        :param model: SQLAlchemy модель.
        """
        self.model = model

    def get(self, db: Session, id: int) -> Optional[Base]:
        """
        Получение записи по ID.
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session) -> List[Base]:
        """
        Получение всех записей.
        """
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: dict) -> Base:
        """
        Создание новой записи.
        :param obj_in: Словарь с данными для создания записи.
        """
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Base, obj_in: dict) -> Base:
        """
        Обновление существующей записи.
        :param db_obj: Объект из базы данных.
        :param obj_in: Словарь с обновляемыми данными.
        """
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: Base) -> None:
        """
        Удаление записи.
        """
        db.delete(db_obj)
        db.commit()


class CRUDUser(CRUDBase):
    pass


class CRUDType(CRUDBase):
    pass


class CRUDStatus(CRUDBase):
    pass


class CRUDOrder(CRUDBase):
    pass
