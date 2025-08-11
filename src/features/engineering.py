import pandas as pd

def basic_investment_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if {"price","rent"}.issubset(out.columns):
        out["gross_yield"] = (out["rent"] * 12) / out["price"]
    return out