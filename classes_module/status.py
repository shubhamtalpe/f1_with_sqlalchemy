from supporing_scripts.base import Base
from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship

class Status(Base):
    __tablename__ = "Status"
    Id : Mapped[int] = mapped_column(primary_key=True)
    StatusName : Mapped[str]
    Results : Mapped[List['Results']] = relationship(backref='Status', init=False) # type: ignore
    SprintResults : Mapped[List['SprintResults']] = relationship(backref='Status', init=False) # type: ignore