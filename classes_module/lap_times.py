from supporing_scripts.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey
from datetime import time

class LapTimes(Base):
    __tablename__ = "LapTimes"
    Id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    DriverId : Mapped[int] = mapped_column(ForeignKey("Drivers.Id"))
    LapNumber : Mapped[int]
    Position : Mapped[int]
    Time : Mapped[str]
    TimeInMiliseconds : Mapped[int]