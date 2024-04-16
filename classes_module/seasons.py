from sqlalchemy import Column, Integer, String
from main_module.base import Base

class Seasons(Base):
    __tablename__ = "Seasons"
    Year = Column(Integer, primary_key=True)
    URL = Column(String)

    def __init__(self, *, Year : int, URL : str) -> None :
        self.Year = Year
        self.URL = URL
    
    def __repr__(self) -> str :
        return f"""{'Year' : <20} : {self.Year}
{'URL' : <20} : {self.URL}"""