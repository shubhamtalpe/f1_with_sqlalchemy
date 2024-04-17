from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from datetime import date, time

class Races(Base):
    __tablename__ = "Races"
    Id : Mapped[int] = mapped_column(primary_key=True)
    Year : Mapped[int] = mapped_column(ForeignKey("Seasons.Year"))
    Round : Mapped[int]
    CircuitId : Mapped[int] = mapped_column(ForeignKey("Circuits.Id"))
    Name : Mapped[str]
    Date : Mapped[date]
    Time : Mapped[time]
    URL : Mapped[str]
    FP1Date : Mapped[date]
    FP1Time : Mapped[time]
    FP2Date : Mapped[date]
    FP2Time : Mapped[time]
    FP3Date : Mapped[date]
    FP3Time : Mapped[time]
    QualiDate : Mapped[date]
    QualiTime : Mapped[time]
    SprintDate : Mapped[date]
    SprintTime : Mapped[time]