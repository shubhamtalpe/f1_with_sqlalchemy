from supporing_scripts.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

class DriverStandings(Base):
    __tablename__ = "DriverStandings"
    Id : Mapped[int] = mapped_column(primary_key=True)
    DriverId : Mapped[int] = mapped_column(ForeignKey('Drivers.Id'))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    Points : Mapped[float]
    Position : Mapped[int]
    PositionText : Mapped[str] = mapped_column(nullable=True)
    Wins : Mapped[int]