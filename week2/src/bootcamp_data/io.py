from pathlib import Path
import pandas as pd

NA = ["", "NA", "N/A", "null", "None", "na", "n/a", "none", "nan"]

def read_orders_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, na_values=NA, keep_default_na=True)

def read_users_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, na_values=NA, keep_default_na=True)



def write_parquet(df, path) -> None:
    """Writes a DataFrame to a Parquet file."""
    df.to_parquet(path)
    pass


def read_parquet(path) -> pd.DataFrame:
    """Reads a Parquet file and returns a DataFrame."""
    pass
