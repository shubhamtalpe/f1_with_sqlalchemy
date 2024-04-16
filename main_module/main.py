import sys, os
sys.path.append(os.getcwd())
from main_module.base import Base
from classes_module.circuits import Circuits
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main() -> None :
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine, checkfirst=True)
    session = Session()

    c1 = Circuits(CircuitId=1, CircuitRef='asfva', Name='sample', Location='adfvsav',
              Country='vbarsb', Latitude=123.3456, Longitude=-13524.354, Altitude=1345246, URL='vwbrfnos')
    session.add(c1)

    for c in session.query(Circuits).all():
        print(c)

if __name__ == "__main__" :
    main()