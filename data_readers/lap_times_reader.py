import os
import pandas as pd
from typing import List
from classes_module.lap_times import LapTimes

class LapTimesReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'lap_times.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')
    
    def readFile(self) -> List[LapTimes] :
        self.data = pd.read_csv(self.file_path)
        LapTimesData : List[LapTimes] = []
        for _, row in self.data.iterrows():
            LapTime : LapTimes = LapTimes(RaceId=row['raceId'],
                                          DriverId=row['driverId'],
                                          LapNumber=row['lap'],
                                          Position=row['position'],
                                          Time=row['time'],
                                          TimeInMiliseconds=row['milliseconds'])
            LapTimesData.append(LapTime)
        return LapTimesData