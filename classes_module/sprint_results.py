from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from datetime import time

class SprintResults(Base):
    __tablename__ = "SprintResults"
    Id : Mapped[int] = mapped_column(primary_key=True)
    ConstructorId : Mapped[int] = mapped_column(ForeignKey("Constructors.Id"))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    DriverId : Mapped[int] = mapped_column(ForeignKey("Drivers.Id"))
    CarNumber : Mapped[int]
    GridPosition : Mapped[int]
    FinalPosition : Mapped[int]
    FinalPositionText : Mapped[str]
    PositionOrder : Mapped[int]
    Points : Mapped[float]
    Laps : Mapped[int]
    Time : Mapped[time]
    TimeInMiliseconds : Mapped[int]
    FastestLap : Mapped[int]
    FastestLapTime : Mapped[time]
    StatusId : Mapped[int] = mapped_column(ForeignKey('Status.Id'))