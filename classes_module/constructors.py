from main_module.base import Base
from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship

class Constructors(Base):
    __tablename__ = "Constructors"
    Id : Mapped[int] = mapped_column(primary_key=True)
    ConstructorRef : Mapped[str]
    Name : Mapped[str]
    Nationality : Mapped[str]
    URL : Mapped[str]
    ConstructorStandings : Mapped[List['ConstructorStandings']] = relationship(backref='Constructor', init=False) # type: ignore
    ConstructorResults : Mapped[List['ConstructorResults']] = relationship(backref='Constructor', init=False) # type: ignore
    SprintResults : Mapped[List['SprintResults']] = relationship(backref='Constructor', init=False) # type: ignore
    Results : Mapped[List['Results']] = relationship(backref='Constructor', init=False) # type: ignore
    Qualifying : Mapped[List['Qualifying']] = relationship(backref='Constructor', init=False) # type: ignore