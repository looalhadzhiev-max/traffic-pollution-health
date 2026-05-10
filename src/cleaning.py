import pandas as pd
import numpy as np


def clean_numeric_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Convert selected columns to numeric values.
    Invalid values are converted to NaN.
    """
    df = df.copy()

    for col in columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def drop_invalid_dates(
    df: pd.DataFrame,
    date_column: str = "date"
) -> pd.DataFrame:
    """
    Remove rows with missing or invalid dates.
    """
    df = df.copy()
    return df.dropna(subset=[date_column])


def remove_negative_values(
    df: pd.DataFrame,
    columns: list[str]
) -> pd.DataFrame:
    """
    Replace negative values with NaN in selected columns.
    """
    df = df.copy()

    for col in columns:
        df.loc[df[col] < 0, col] = np.nan

    return df


def missing_value_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a summary table of missing values.
    """
    summary = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_ratio": df.isna().mean()
    })

    summary = summary.sort_values(
        by="missing_ratio",
        ascending=False
    )

    return summary