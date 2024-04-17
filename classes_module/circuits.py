from main_module.base import Base
from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship

class Circuits(Base):
    __tablename__ = "Circuits"
    Id : Mapped[int] = mapped_column(primary_key=True)
    CircuitRef : Mapped[str]
    Name : Mapped[str]
    Location : Mapped[str]
    Country : Mapped[str]
    Latitude : Mapped[float]
    Longitude : Mapped[float]
    Altitude : Mapped[int]
    URL : Mapped[str]
    Races : Mapped[List['Races']] = relationship(backref="Circuit", init=False) # type: ignore