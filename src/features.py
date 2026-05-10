import pandas as pd


def add_lag_features(
    df: pd.DataFrame,
    group_col: str,
    target_cols: list[str],
    lags: list[int]
) -> pd.DataFrame:
    """
    Create lagged features for selected columns within groups.
    Example: traffic_lag_1, traffic_lag_3, traffic_lag_7
    """
    df = df.copy()
    df = df.sort_values([group_col, "date"])

    for col in target_cols:
        for lag in lags:
            df[f"{col}_lag_{lag}"] = (
                df.groupby(group_col)[col]
                .shift(lag)
            )

    return df


def add_rolling_features(
    df: pd.DataFrame,
    group_col: str,
    target_cols: list[str],
    windows: list[int]
) -> pd.DataFrame:
    """
    Create rolling mean features within groups.
    Example: traffic_roll_mean_7
    """
    df = df.copy()
    df = df.sort_values([group_col, "date"])

    for col in target_cols:
        for window in windows:
            df[f"{col}_roll_mean_{window}"] = (
                df.groupby(group_col)[col]
                .transform(
                    lambda x: x.rolling(window).mean()
                )
            )

    return df