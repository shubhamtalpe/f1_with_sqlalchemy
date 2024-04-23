import os
import pandas as pd
from typing import List
from classes_module.sprint_results import SprintResults
from supporing_scripts.custom_decorators import get_time

class SprintResultsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'sprint_results.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[SprintResults] :
        self.data = pd.read_csv(self.file_path)
        self.data.replace('\\N', None, inplace=True)
        self.data.positionText.replace({'R' : 'Retired',
                                        'W' : 'Withdrew',
                                        'N' : 'Did Not Start'}, inplace=True)
        SprintResultsData : List[SprintResults] = []
        for _, row in self.data.iterrows():
            sprintResult : SprintResults = SprintResults(Id=row['resultId'],
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
                                                         StatusId=row['statusId'])
            SprintResultsData.append(sprintResult)
        return SprintResultsData