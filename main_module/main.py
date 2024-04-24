import sys, os
sys.path.append(os.getcwd())
from supporing_scripts.base import Base
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
from data_readers.constructor_standings_reader import ConstructorStandingsReader
from data_readers.constructor_results_reader import ConstructorResultsReader
from data_readers.sprint_results_reader import SprintResultsReader
from data_readers.results_reader import ResultsReader
from data_readers.qualifying_reader import QualifyingReader
from data_readers.pit_stops_reader import PitStopsReader
from data_readers.driver_standings_reader import DriverStandingsReader
from data_readers.lap_times_reader import LapTimesReader
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from supporing_scripts.custom_decorators import get_time
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import logging

@get_time
def read_data_from_files() -> None :
    logging.info("Reading files and loading data to database")
    
    logging.debug("Creating engine object")
    engine = create_engine("sqlite:///:memory:")
    # engine = create_engine("sqlite:///sample.db")

    logging.debug("Creating session object")
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine, checkfirst=True)
    
    with Session() as session:
        logging.debug("Session created")

        logging.debug("Starting to read files")
        with tqdm(total=14) as pbar:
            obj = CircuitReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Circuits data loaded")

            obj = SeasonsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Seasons data loaded")

            obj = StatusReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Status data loaded")

            obj = ConstructorsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Constructor data loaded")

            obj = DriversReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Driver data loaded")

            obj = RacesReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Races data loaded")

            obj = ConstructorStandingsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Constructor Standings data loaded")

            obj = ConstructorResultsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Constructor Results data loaded")

            obj = SprintResultsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Sprint Results data loaded")

            obj = ResultsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Results data loaded")

            obj = QualifyingReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Qualifying data loaded")

            obj = PitStopsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Pit Stops data loaded")

            obj = DriverStandingsReader()
            session.add_all(obj.readFile())
            session.commit()
            del obj
            pbar.update(1)
            logging.debug("Driver Standings data loaded")

            obj = LapTimesReader()
            threadPoolExecutor : ThreadPoolExecutor = ThreadPoolExecutor()
            threadPoolExecutor.submit(session.add_all, obj.readFile())
            del obj
            pbar.update(1)
            logging.debug("Lap Times data loaded")
    logging.info("All data loaded successfully")

if __name__ == "__main__" :
    logging.basicConfig(format=f'[%(levelname)s] : [%(asctime)s] : %(message)s | (Line : %(lineno)d) [%(filename)s]',
                        level=logging.DEBUG,
                        filename='logs/main.log')
    logging.debug("Logger initialized")
    logging.debug("Calling read file function")
    read_data_from_files()
    logging.debug("Read file function execution complete")

    logging.info("Script execution complete")