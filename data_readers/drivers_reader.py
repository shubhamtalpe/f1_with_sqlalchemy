import os
import pandas as pd
from typing import List
from classes_module.drivers import Drivers
from supporing_scripts.custom_decorators import get_time

class DriversReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'drivers.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[Drivers] :
        self.data = pd.read_csv(self.file_path)
        self.data['number'] = self.data.number.replace('\\N', None)
        self.data['code'] = self.data.code.replace('\\N', None)
        self.data['dob'] = pd.to_datetime(self.data['dob'], format='%Y-%m-%d')
        driversData : List[Drivers] = []
        for _, row in self.data.iterrows():
            driver : Drivers = Drivers(Id=row['driverId'],
                                       DriverRef=row['driverRef'],
                                       Number=row['number'],
                                       Code=row['code'],
                                       FirstName=row['forename'],
                                       LastName=row['surname'],
                                       DateOfBirth=row['dob'],
                                       Nationality=row['nationality'],
                                       URL=row['url'])
            driversData.append(driver)
        return driversData