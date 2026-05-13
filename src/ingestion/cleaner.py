import pandas as pd
import logging

logger = logging.getLogger(__name__)

COLUMN_RENAME_MAP = {
    "name": "meteorite_name",
    "id": "meteorite_id",
    "nametype": "name_type",
    "recclass": "rec_class",
    "mass (g)": "mass_g",
    "fall": "fall",
    "year": "year",
    "reclat": "rec_latitiude",
    "reclong": "rec_longitude",
    "GeoLocation":"geo_location"
}

def clean_dataframe(df : pd.DataFrame) -> pd.DataFrame:

    df = _rename_columns(df)
    df = _convert_numeric_types(df)

    return df

def _rename_columns(df : pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns=COLUMN_RENAME_MAP)

def _convert_numeric_types(df: pd.DataFrame) -> pd.DataFrame:
    return pd.to_datetime(df['year'].astype(int).astype(str), format='%Y')