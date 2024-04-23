import os
import pandas as pd
from typing import List
from classes_module.pit_stops import PitStops
from supporing_scripts.custom_decorators import get_time

class PitStopsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'pit_stops.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[PitStops] :
        self.data = pd.read_csv(self.file_path)
        pitStopsData : List[PitStops] = []
        for _, row in self.data.iterrows():
            pitStop : PitStops = PitStops(DriverId=row['driverId'],
                                          RaceId=row['raceId'],
                                          Stop=row['stop'],
                                          Lap=row['lap'],
                                          Time=row['time'],
                                          Duration=row['duration'],
                                          DurationInMiliseconds=row['milliseconds'])
            pitStopsData.append(pitStop)
        return pitStopsData