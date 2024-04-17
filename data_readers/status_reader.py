import os
import pandas as pd
from classes_module.status import Status
from typing import List

class StatusReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'status.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')
    
    def readFile(self) -> List[Status] :
        self.data = pd.read_csv(self.file_path)
        statusData : List[Status] = []
        for _, row in self.data.iterrows():
            status : Status = Status(Id=row['statusId'], StatusName=row['status'])
            statusData.append(status)
        return statusData