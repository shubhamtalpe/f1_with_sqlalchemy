from main_module.base import Base
from sqlalchemy.orm import mapped_column, Mapped

class Seasons(Base):
    __tablename__ = "Seasons"
    Year : Mapped[int] = mapped_column(primary_key=True)
    URL : Mapped[str]