import pandas as pd
import logging
from src.ingestion.reader import read_file
from src.ingestion.cleaner import clean_dataframe

logger = logging.getLogger(__name__)

def run_pipeline(filename: str, chunksize: int = 10000) -> None:

    logger.info(f"Starting ingestion pipeline for file: {filename}")

    try:
        reader = read_file(filename, chunksize)

        for chunk_size, chunk in enumerate(reader, start=1):

            df = pd.DataFrame
            df = clean_dataframe(chunk)

            print(df)


    except Exception as e:
        logger.critical(f"Pipeline execution failed.")
        raise
    finally:
        logger.info("Pipeline finished.")