from sqlalchemy import Column, Integer, String
from main_module.base import Base

class Constructors(Base):
    __tablename__ = "Constructors"
    ConstructorId = Column(Integer, primary_key=True)
    ConstructorRef = Column(String)
    Name = Column(String)
    Nationality = Column(String)
    URL = Column(String)

    def __init__(self, *, ConstructorId : int, ConstructorRef : str, Name : str, Nationality : str, URL : str) -> None :
        self.ConstructorId = ConstructorId
        self.ConstructorRef = ConstructorRef
        self.Name = Name
        self.Nationality = Nationality
        self.URL = URL
    
    def __repr__(self) -> str :
        return f"""{'Constructor ID' : <20} : {self.ConstructorId}
{'Constructor Ref' : <20} : {self.ConstructorRef}
{'Name' : <20} : {self.Name}
{'Nationality' : <20} : {self.Nationality}
{'URL' : <20} : {self.URL}"""