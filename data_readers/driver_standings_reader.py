import os
import pandas as pd
from typing import List
from classes_module.driver_standings import DriverStandings

class DriverStandingsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'driver_standings.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')
    
    def readFile(self) -> List[DriverStandings] :
        self.data = pd.read_csv(self.file_path)
        self.data.positionText.replace('D', 'Disqualified', inplace=True)
        DriverStandingsData : List[DriverStandings] = []
        for _, row in self.data.iterrows():
            DriverStanding : DriverStandings = DriverStandings(Id=row['driverStandingsId'],
                                                               DriverId=row['driverId'],
                                                               RaceId=row['raceId'],
                                                               Points=row['points'],
                                                               Position=row['position'],
                                                               PositionText=row['positionText'],
                                                               Wins=row['wins'])
            DriverStandingsData.append(DriverStanding)
        return DriverStandingsData