import os
import pandas as pd
from typing import List
from classes_module.constructor_standings import ConstructorStandings
from supporing_scripts.custom_decorators import get_time

class ConstructorStandingsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'constructor_standings.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[ConstructorStandings] :
        self.data = pd.read_csv(self.file_path)
        self.data.positionText = self.data.positionText.replace('E', None)
        constructorStandingsData : List[ConstructorStandings] = []
        for _, row in self.data.iterrows():
            constructorStanding : ConstructorStandings = ConstructorStandings(Id=row['constructorStandingsId'],
                                                                              RaceId=row['raceId'],
                                                                              ConstructorId=row['constructorId'],
                                                                              Points=row['points'],
                                                                              Position=row['position'],
                                                                              PositionText=row['positionText'],
                                                                              Wins=row['wins'])
            constructorStandingsData.append(constructorStanding)
        return constructorStandingsData