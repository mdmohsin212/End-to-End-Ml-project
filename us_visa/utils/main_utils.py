from pandas import DataFrame
import numpy as np
import yaml
import dill

import os
import sys

from us_visa.exception import HandleException
from us_visa.logger import logging

def red_yaml_file(path : str) -> dict:
    try:
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    
    except Exception as e:
        raise HandleException(e, sys) from e


def write_yaml_file(path : str, content : object, replace : bool = False) -> None:
    try:
        if replace:
            if os.path.exists(path):
                os.remove(path)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as file:
            yaml.dump(content, file)
            
    except Exception as e:
        raise HandleException(e, sys) from e

def load_object(path : str) -> object:
    logging.info("Entered the load_object method of utils")
    
    try:
        with open(path, 'rb') as file_obj:
            obj = dill.load(file_obj)
        logging.info("Exited the load_object method of utils")
        return obj

    except Exception as e:
        raise HandleException(e, sys) from e

def save_object(path : str, obj : object) -> None:
    logging.info("Entered the load_object method of utils")
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as file_obj:
            dill.dump(file_obj)
        logging.info("Exited the save_object method of utils")
    
    except Exception as e:
        raise HandleException(e, sys) from e
    
    
def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
            
    except Exception as e:
        raise HandleException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
        
    except Exception as e:
        raise HandleException(e, sys) from e
    

def drop_columns(df: DataFrame, cols: list)-> DataFrame:
    logging.info("Entered drop_columns methon of utils")
    try:
        df = df.drop(columns=cols, axis=1)
        logging.info("Exited the drop_columns method of utils")
        return df
    
    except Exception as e:
        raise HandleException(e, sys) from e