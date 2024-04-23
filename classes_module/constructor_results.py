from supporing_scripts.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

class ConstructorResults(Base):
    __tablename__ = "ConstructorResults"
    Id : Mapped[int] = mapped_column(primary_key=True)
    ConstructorId : Mapped[int] = mapped_column(ForeignKey("Constructors.Id"))
    RaceId : Mapped[int] = mapped_column(ForeignKey("Races.Id"))
    Points : Mapped[float]
    Status : Mapped[str] = mapped_column(nullable=True)