import os
import logging
import pandas as pd

logger = logging.getLogger(__name__)

PATH_EXTENSIONS = [".csv", ".json"]

def read_file(filename : str, chunksize : int) -> pd.DataFrame:
    
    if not os.path.exists(filename):
        raise FileNotFoundError("File not found")
    
    extension = os.path.splitext(filename)[1].lower()

    if extension not in PATH_EXTENSIONS:
        raise ValueError(f"File type {extension} not supported")
    
    try:
        if extension == ".csv":
            df = pd.read_csv(filename, chunksize=chunksize)
            return df
        if extension == ".json":
            df = pd.read_json(filename, lines=True, chunksize=chunksize)
            return df

    except Exception as e:
        logger.error("Failed to load data into dataframe")
        raise