from sqlalchemy import Column, Integer, String
from main_module.base import Base

class Status(Base):
    __tablename__ = "Status"
    StatusId = Column(Integer, primary_key=True)
    StatusName = Column(String)

    def __init__(self, *, StatusId : int, StatusName : str) -> None :
        self.StatusId = StatusId
        self.StatusName = StatusName
    
    def __repr__(self) -> str:
        return f"""{'Status ID' : <20} : {self.StatusId}
{'Status Name' : <20} : {self.StatusName}"""