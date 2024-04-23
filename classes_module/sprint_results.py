from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

class SprintResults(Base):
    __tablename__ = "SprintResults"
    Id : Mapped[int] = mapped_column(primary_key=True)
    ConstructorId : Mapped[int] = mapped_column(ForeignKey("Constructors.Id"))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    DriverId : Mapped[int] = mapped_column(ForeignKey("Drivers.Id"))
    CarNumber : Mapped[int]
    GridPosition : Mapped[int]
    FinalPosition : Mapped[int] = mapped_column(nullable=True)
    FinalPositionText : Mapped[str] = mapped_column(nullable=True)
    PositionOrder : Mapped[int]
    Points : Mapped[float]
    Laps : Mapped[int]
    Time : Mapped[str] = mapped_column(nullable=True)
    TimeInMiliseconds : Mapped[int] = mapped_column(nullable=True)
    FastestLap : Mapped[int] = mapped_column(nullable=True)
    FastestLapTime : Mapped[str] = mapped_column(nullable=True)
    StatusId : Mapped[int] = mapped_column(ForeignKey('Status.Id'))