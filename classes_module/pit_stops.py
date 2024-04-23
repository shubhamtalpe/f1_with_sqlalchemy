from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

class PitStops(Base):
    __tablename__ = "PitStops"
    Id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    DriverId : Mapped[int] = mapped_column(ForeignKey('Drivers.Id'))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    Stop : Mapped[int]
    Lap : Mapped[int]
    Time : Mapped[str]
    Duration : Mapped[str]
    DurationInMiliseconds : Mapped[int]