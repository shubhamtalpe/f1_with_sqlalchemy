import os
import pandas as pd
from classes_module.constructors import Constructors
from typing import List
from supporing_scripts.custom_decorators import get_time

class ConstructorsReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'constructors.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def readFile(self) -> List[Constructors] :
        self.data = pd.read_csv(self.file_path)
        constructorsData : List[Constructors] = []
        for _, row in self.data.iterrows():
            constructor : Constructors = Constructors(Id=row['constructorId'], 
                                                      ConstructorRef=row['constructorRef'], 
                                                      Name=row['name'], 
                                                      Nationality=row['nationality'],
                                                      URL=row['url'])
            constructorsData.append(constructor)
        return constructorsData