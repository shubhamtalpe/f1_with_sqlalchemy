import os
import pandas as pd
from typing import List
from classes_module.lap_times import LapTimes
from supporing_scripts.custom_decorators import get_time
import multiprocessing as mp
import numpy as np
from functools import reduce
from operator import add
from sqlalchemy.orm import Session

class LapTimesReader:
    
    file_path : str = None
    data : pd.DataFrame = None
        
    def __init__(self) -> None :
        self.file_path = os.path.join(os.getcwd(), os.path.join('data', 'lap_times.csv'))
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f'Required file not found at path {self.file_path}')

    def create_lap_times_obj(self, chunk : np.ndarray) -> List[LapTimes] :
        return [LapTimes(RaceId=data[0],
                        DriverId=data[1],
                        LapNumber=data[2],
                        Position=data[3],
                        Time=data[4],
                        TimeInMiliseconds=data[5]) for data in chunk]
    
    def readFile(self) -> List[LapTimes] :
        self.data = pd.read_csv(self.file_path)
        data_values : np.ndarray = self.data.values
        num_processes : int = mp.cpu_count()
        chunk_size : int = data_values.shape[0] // num_processes
        chunks : List[np.ndarray] = [data_values[idx : idx + chunk_size : ] for idx in range(0, data_values.shape[0], chunk_size)]
        with mp.Pool(processes=num_processes) as pool:
            LapTimesData : List[LapTimes] = reduce(add, pool.map(self.create_lap_times_obj, chunks))
        return LapTimesData