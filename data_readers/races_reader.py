import os
import pandas as pd
from typing import List
from classes_module.races import Races

class RacesReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'races.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')
    
    def readFile(self) -> List[Races] :
        self.data = pd.read_csv(self.file_path)
        self.data = self.data.replace('\\N', None)
        self.data['date_time'] = self.data.date + ' ' + self.data.time
        self.data['date_time'] = pd.to_datetime(self.data.date_time, format='%Y-%m-%d %H:%M:%S')
        self.data['fp1_date_time'] = self.data.fp1_date + ' ' + self.data.fp1_time
        self.data['fp1_date_time'] = pd.to_datetime(self.data.fp1_date_time, format='%Y-%m-%d %H:%M:%S')
        self.data['fp2_date_time'] = self.data.fp2_date + ' ' + self.data.fp2_time
        self.data['fp2_date_time'] = pd.to_datetime(self.data.fp2_date_time, format='%Y-%m-%d %H:%M:%S')
        self.data['fp3_date_time'] = self.data.fp3_date + ' ' + self.data.fp3_time
        self.data['fp3_date_time'] = pd.to_datetime(self.data.fp3_date_time, format='%Y-%m-%d %H:%M:%S')
        self.data['quali_date_time'] = self.data.quali_date + ' ' + self.data.quali_time
        self.data['quali_date_time'] = pd.to_datetime(self.data.quali_date_time, format='%Y-%m-%d %H:%M:%S')
        self.data['sprint_date_time'] = self.data.sprint_date + ' ' + self.data.sprint_time
        self.data['sprint_date_time'] = pd.to_datetime(self.data.sprint_date_time, format='%Y-%m-%d %H:%M:%S')
        self.data.drop(['date', 'time', 'fp1_date', 'fp1_time', 'fp2_date', 'fp2_time', 'fp3_date', 'fp3_time', 'quali_date', 'quali_time', 'sprint_date', 'sprint_time'], axis=1, inplace=True)
        self.data = self.data.replace({pd.NaT : None})
        racesData : List[Races] = []
        for _, row in self.data.iterrows():
            race : Races = Races(Id=row['raceId'],
                                 Year=row['year'],
                                 Round=row['round'],
                                 CircuitId=row['circuitId'],
                                 Name=row['name'],
                                 URL=row['url'],
                                 Date_Time=row['date_time'],
                                 FP1Date_Time=row['fp1_date_time'],
                                 FP2Date_Time=row['fp2_date_time'],
                                 FP3Date_Time=row['fp3_date_time'],
                                 QualiDate_Time=row['quali_date_time'],
                                 SprintDate_Time=row['sprint_date_time'])
            racesData.append(race)
        return racesData