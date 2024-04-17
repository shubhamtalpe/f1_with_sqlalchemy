from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

class ConstructorStandings(Base):
    __tablename__ = "ConstructorStandings"
    Id : Mapped[int] = mapped_column(primary_key=True)
    ConstructorId : Mapped[int] = mapped_column(ForeignKey("Constructors.Id"))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    Points : Mapped[float]
    Position : Mapped[int] | None
    PositionText : Mapped[str]
    Wins : Mapped[int]