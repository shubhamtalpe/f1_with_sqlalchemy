from supporing_scripts.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

class Seasons(Base):
    __tablename__ = "Seasons"
    Year : Mapped[int] = mapped_column(primary_key=True)
    URL : Mapped[str]
    Races : Mapped[List['Races']] = relationship(backref="Season", init=False) # type: ignore