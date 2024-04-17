from main_module.base import Base
from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import date

class Drivers(Base):
    __tablename__ = "Drivers"
    Id : Mapped[int] = mapped_column(primary_key=True)
    DriverRef : Mapped[str]
    Number : Mapped[int] | None
    Code : Mapped[str] | None
    FirstName : Mapped[str]
    LastName : Mapped[str]
    DateOfBirth : Mapped[date]
    Nationality : Mapped[str]
    URL : Mapped[str]
    DriverStandings : Mapped[List['DriverStandings']] = relationship(backref='Driver', init=False) # type: ignore
    Results : Mapped[List['Results']] = relationship(backref='Driver', init=False) # type: ignore
    PitStops : Mapped[List['PitStops']] = relationship(backref='Driver', init=False) # type: ignore
    LapTimes : Mapped[List['LapTimes']] = relationship(backref='Driver', init=False) # type: ignore
    Qualifying : Mapped[List['Qualifying']] = relationship(backref='Driver', init=False) # type: ignore
    SprintResults : Mapped[List['SprintResults']] = relationship(backref='Driver', init=False) # type: ignore