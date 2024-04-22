from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from datetime import datetime

class Races(Base):
    __tablename__ = "Races"
    Id : Mapped[int] = mapped_column(primary_key=True)
    Year : Mapped[int] = mapped_column(ForeignKey("Seasons.Year"))
    Round : Mapped[int]
    CircuitId : Mapped[int] = mapped_column(ForeignKey("Circuits.Id"))
    Name : Mapped[str]
    Date_Time : Mapped[datetime] = mapped_column(nullable=True)
    URL : Mapped[str]
    FP1Date_Time : Mapped[datetime] = mapped_column(nullable=True)
    FP2Date_Time : Mapped[datetime] = mapped_column(nullable=True)
    FP3Date_Time : Mapped[datetime] = mapped_column(nullable=True)
    QualiDate_Time : Mapped[datetime] = mapped_column(nullable=True)
    SprintDate_Time : Mapped[datetime] = mapped_column(nullable=True)