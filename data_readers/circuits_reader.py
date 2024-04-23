import os
import pandas as pd
from classes_module.circuits import Circuits
from typing import List
from supporing_scripts.custom_decorators import get_time

class CircuitReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'circuits.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[Circuits] :
        self.data = pd.read_csv(self.file_path)
        self.data.alt = self.data.alt.replace('\\N', 0)
        circuitsData : List[Circuits] = []
        for _, row in self.data.iterrows():
            circuit : Circuits = Circuits(Id=row['circuitId'], 
                                          CircuitRef=row['circuitRef'], 
                                          Name=row['name'], 
                                          Location=row['location'], 
                                          Country=row['country'], 
                                          Latitude=row['lat'], 
                                          Longitude=row['lng'], 
                                          Altitude=int(row['alt']), 
                                          URL=row['url'])
            circuitsData.append(circuit)
        return circuitsData