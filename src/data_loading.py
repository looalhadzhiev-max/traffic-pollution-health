from pathlib import Path
import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """
    Load a CSV file safely.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)
    return df


def parse_date_column(
    df: pd.DataFrame,
    column: str,
    new_name: str = "date"
) -> pd.DataFrame:
    """
    Parse a column as datetime and store it as a new column.
    """
    df = df.copy()
    df[new_name] = pd.to_datetime(df[column], errors="coerce")
    return df


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names: lowercase and underscores.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def filter_date_range(
    df: pd.DataFrame,
    start_date: str | None = None,
    end_date: str | None = None,
    date_column: str = "date"
) -> pd.DataFrame:
    """
    Filter dataframe by date range.
    """
    df = df.copy()

    if start_date:
        df = df[df[date_column] >= start_date]

    if end_date:
        df = df[df[date_column] <= end_date]

    return df


def basic_info(df: pd.DataFrame) -> None:
    """
    Print basic info about dataframe.
    """
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nMissing values:")
    print(df.isna().sum())