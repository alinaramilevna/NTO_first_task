from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base


class EngineController:
    def __init__(self) -> None:
        self._engine = create_engine(
            f"sqlite:///db.sqlite",
            echo=False
        )
        self._sessionmaker = sessionmaker(
            bind=self._engine,
            expire_on_commit=False
        )

    @property
    def engine(self):
        return self._engine

    def create_session(self):
        return self._sessionmaker()

    @contextmanager
    def get_session(self):
        session = self.create_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def init_db(self):
        with self._engine.begin() as conn:
            Base.metadata.create_all(conn)

    def drop_db(self):
        with self._engine.begin() as conn:
            Base.metadata.drop_all(conn)
controller = EngineController()
controller.init_db()