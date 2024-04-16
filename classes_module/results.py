from sqlalchemy import Column, Integer, String, ForeignKey
from main_module.base import Base

class Results(Base):
    __tablename__ = "Results"
    ResultId = Column(Integer, primary_key=True)
    RaceId = Column(Integer, ForeignKey('Races.RaceId'), nullable=False)
    DriverId = Column(Integer, ForeignKey('Drivers.DriverId'), nullable=False)
    ConstructorId = Column(Integer, ForeignKey('Constructors.ConstructorId'), nullable=False)
    