import pandas as pd

from src.utils.logger import setup_logging
from src.ingestion.pipeline import run_pipeline

FILENAME = "data/raw/Meteorite_Landings.csv"

def main():

    logger = setup_logging()

    run_pipeline(FILENAME)

if __name__ == "__main__":
    main()