import os
import pandas as pd
from typing import List
from classes_module.qualifying import Qualifying
from supporing_scripts.custom_decorators import get_time

class QualifyingReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'qualifying.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[Qualifying] :
        self.data = pd.read_csv(self.file_path)
        self.data.replace('\\N', None, inplace=True)
        QualifyingData : List[Qualifying] = []
        for _, row in self.data.iterrows():
            Quali : Qualifying = Qualifying(Id=row['qualifyId'],
                                            RaceId=row['raceId'],
                                            DriverId=row['driverId'],
                                            ConstructorId=row['constructorId'],
                                            CarNumber=row['number'],
                                            Position=row['position'],
                                            Q1Time=row['q1'],
                                            Q2Time=row['q2'],
                                            Q3Time=row['q3'])
            QualifyingData.append(Quali)
        return QualifyingData