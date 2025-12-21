import pandas as pd

def read_orders_csv(path) -> pd.DataFrame:
    """Reads a CSV file containing orders data and returns a DataFrame."""
    pass


def read_users_csv(path) -> pd.DataFrame:
    """Reads a CSV file containing users data and returns a DataFrame."""
    pass


def write_parquet(df, path) -> None:
    """Writes a DataFrame to a Parquet file."""
    df.to_parquet(path)
    pass


def read_parquet(path) -> pd.DataFrame:
    """Reads a Parquet file and returns a DataFrame."""
    pass
