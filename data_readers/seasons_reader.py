import os
import pandas as pd
from classes_module.seasons import Seasons
from typing import List

class SeasonsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'seasons.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')
    
    def readFile(self) -> List[Seasons] :
        self.data = pd.read_csv(self.file_path)
        seasonsData : List[Seasons] = []
        for _, row in self.data.iterrows():
            season : Seasons = Seasons(Year=row['year'], URL=row['url'])
            seasonsData.append(season)
        return seasonsData