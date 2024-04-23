import os
import pandas as pd
from typing import List
from classes_module.results import Results
from supporing_scripts.custom_decorators import get_time

class ResultsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'results.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[Results] :
        self.data = pd.read_csv(self.file_path)
        self.data.replace('\\N', None, inplace=True)
        self.data.positionText.replace({'R' : 'Retired',
                                        'W' : 'Withdrew',
                                        'N' : 'Not Classified',
                                        'F' : 'Did Not Qualify',
                                        'E' : 'Excluded',
                                        'D' : 'Disqualified'}, inplace=True)
        ResultsData : List[Results] = []
        for _, row in self.data.iterrows():
            result : Results = Results(Id=row['resultId'],
                                       ConstructorId=row['constructorId'],
                                       RaceId=row['raceId'],
                                       DriverId=row['driverId'],
                                       CarNumber=row['number'],
                                       GridPosition=row['grid'],
                                       FinalPosition=row['position'],
                                       FinalPositionText=row['positionText'],
                                       PositionOrder=row['positionOrder'],
                                       Points=row['points'],
                                       Laps=row['laps'],
                                       Time=row['time'],
                                       TimeInMiliseconds=row['milliseconds'],
                                       FastestLap=row['fastestLap'],
                                       FastestLapTime=row['fastestLapTime'],
                                       FastestLapRank=row['rank'],
                                       FastestLapSpeed=row['fastestLapSpeed'],
                                       StatusId=row['statusId'])
            ResultsData.append(result)
        return ResultsData