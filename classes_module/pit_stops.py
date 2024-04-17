from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
from datetime import time

class PitStops(Base):
    __tablename__ = "PitStops"
    Id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    DriverId : Mapped[int] = mapped_column(ForeignKey('Drivers.Id'))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    Stop : Mapped[int]
    Lap : Mapped[int]
    Time : Mapped[time]
    Duration : Mapped[time]
    DurationInMiliseconds : Mapped[time]