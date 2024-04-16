from sqlalchemy import Column, Integer, String, Float
from main_module.base import Base

class Circuits(Base):
    __tablename__ = "Circuits"
    CircuitId = Column(Integer, primary_key=True)
    CircuitRef = Column(String)
    Name = Column(String)
    Location = Column(String)
    Country = Column(String)
    Latitude = Column(Float)
    Longitude = Column(Float)
    Altitude = Column(Integer)
    URL = Column(String)

    def __init__(self, *, CircuitId : int, CircuitRef : str, Name : str, Location : str, Country : str, Latitude : float, Longitude : float, Altitude : int, URL : str) -> None:
        self.CircuitId = CircuitId
        self.CircuitRef = CircuitRef
        self.Name = Name
        self.Location = Location
        self.Country = Country
        self.Latitude = Latitude
        self.Longitude = Longitude
        self.Altitude = Altitude
        self.URL = URL

    def __repr__(self) -> str:
        return f"""{'Circuit Id' : <20} : {self.CircuitId}
{'Circuit Ref' : <20} : {self.CircuitRef}
{'Name' : <20} : {self.Name}
{'Location' : <20} : {self.Location}
{'Country' : <20} : {self.Country}
{'Latitude' : <20} : {self.Latitude}
{'Longitude' : <20} : {self.Longitude}
{'Altitude' : <20} : {self.Altitude}
{'URL' : <20} : {self.URL}"""


if __name__ == "__main__":
    pass