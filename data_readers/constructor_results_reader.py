import os
import pandas as pd
from typing import List
from classes_module.constructor_results import ConstructorResults
from supporing_scripts.custom_decorators import get_time

class ConstructorResultsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'constructor_results.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[ConstructorResults] :
        self.data = pd.read_csv(self.file_path)
        self.data.status.replace('\\N', None, inplace=True)
        self.data.status.replace('D', 'Disqualified', inplace=True)
        constructorResultsData : List[ConstructorResults] = []
        for _, row in self.data.iterrows():
            constructorResult : ConstructorResults = ConstructorResults(Id=row['constructorResultsId'],
                                                                        ConstructorId=row['constructorId'],
                                                                        RaceId=row['raceId'],
                                                                        Points=row['points'],
                                                                        Status=row['status'])
            constructorResultsData.append(constructorResult)
        return constructorResultsData