from sqlalchemy import Column, Integer, String, Date
from main_module.base import Base
from datetime import date

class Drivers(Base):
    __tablename__ = "Drivers"
    DriverId = Column(Integer, primary_key=True)
    DriverRef = Column(String)
    Number = Column(Integer)
    Code = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    DateOfBirth = Column(Date)
    Nationality = Column(String)
    URL = Column(String)

    def __init__(self, *, DriverId : int, DriverRef : str, Number : int, Code : str, FirstName : str, LastName : str, DateOfBirth : date, Nationality : str, URL : str) -> None :
        self.DriverId = DriverId
        self.DriverRef = DriverRef
        self.Number = Number
        self.Code = Code
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Nationality = Nationality
        self.URL = URL
    
    def __repr__(self) -> str :
        return f"""{'Driver ID' : <20} : {self.DriverId}
{'Driver Ref' : <20} : {self.DriverRef}
{'Number' : <20} : {self.Number}
{'Code' : <20} : {self.Code}
{'First Name' : <20} : {self.FirstName}
{'Last Name' : <20} : {self.LastName}
{'Date Of Birth' : <20} : {self.DateOfBirth}
{'Nationality' : <20} : {self.Nationality}
{'URL' : <20} : {self.URL}"""