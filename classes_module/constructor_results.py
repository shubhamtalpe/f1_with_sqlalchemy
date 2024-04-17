from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

class ConstructorResults(Base):
    __tablename__ = "ConstructorResults"
    Id : Mapped[int] = mapped_column(primary_key=True)
    CircuitId : Mapped[int] = mapped_column(ForeignKey("Circuits.Id"))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    Points : Mapped[float]
    Status : Mapped[str]