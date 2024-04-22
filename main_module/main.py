import sys, os
sys.path.append(os.getcwd())
from main_module.base import Base
from classes_module.circuits import Circuits
from classes_module.constructor_results import ConstructorResults
from classes_module.constructor_standings import ConstructorStandings
from classes_module.constructors import Constructors
from classes_module.driver_standings import DriverStandings
from classes_module.drivers import Drivers
from classes_module.lap_times import LapTimes
from classes_module.pit_stops import PitStops
from classes_module.qualifying import Qualifying
from classes_module.races import Races
from classes_module.results import Results
from classes_module.seasons import Seasons
from classes_module.sprint_results import SprintResults
from classes_module.status import Status
from data_readers.circuits_reader import CircuitReader
from data_readers.seasons_reader import SeasonsReader
from data_readers.status_reader import StatusReader
from data_readers.constructors_reader import ConstructorsReader
from data_readers.drivers_reader import DriversReader
from data_readers.races_reader import RacesReader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main() -> None :
    # engine = create_engine("sqlite:///:memory:")
    engine = create_engine("sqlite:///sample.db")
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine, checkfirst=True)
    session = Session()

    obj = CircuitReader()
    session.add_all(obj.readFile())
    session.commit()
    del obj

    obj = SeasonsReader()
    session.add_all(obj.readFile())
    session.commit()
    del obj

    obj = StatusReader()
    session.add_all(obj.readFile())
    session.commit()
    del obj

    obj = ConstructorsReader()
    session.add_all(obj.readFile())
    session.commit()
    del obj

    obj = DriversReader()
    session.add_all(obj.readFile())
    session.commit()
    del obj

    obj = RacesReader()
    session.add_all(obj.readFile())
    session.commit()
    del obj

    # obj = ConstructorStandingsReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

    # obj = ConstructorResultsReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

    # obj = SprintResultsReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

    # obj = ResultsReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

    # obj = QualifyingReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

    # obj = PitStopsReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

    # obj = DriverStandingsReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

    # obj = LapTimesReader()
    # session.add_all(obj.readFile())
    # session.commit()
    # del obj

if __name__ == "__main__" :
    main()