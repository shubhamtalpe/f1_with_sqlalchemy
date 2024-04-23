from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

class Qualifying(Base):
    __tablename__ = "Qualifying"
    Id : Mapped[int] = mapped_column(primary_key=True)
    ConstructorId : Mapped[int] = mapped_column(ForeignKey("Constructors.Id"))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    DriverId : Mapped[int] = mapped_column(ForeignKey("Drivers.Id"))
    CarNumber : Mapped[int]
    Position : Mapped[int]
    Q1Time : Mapped[str] = mapped_column(nullable=True)
    Q2Time : Mapped[str] = mapped_column(nullable=True)
    Q3Time : Mapped[str] = mapped_column(nullable=True)