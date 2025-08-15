# src/features/cleaning.py
from __future__ import annotations
import pandas as pd

CRITICAL = ["id", "city", "price", "rent", "bed", "bath"]

def clean_frame(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # basic dtype + trims
    out["city"] = out["city"].astype("string").str.strip()
    for c in ["price", "rent", "bed", "bath"]:
        out[c] = pd.to_numeric(out[c], errors="coerce")

    # drop invalid rows
    out = out[out["price"] > 0]
    out = out[out["rent"] >= 0]

    # clip extreme outliers (light touch)
    for c in ["price", "rent"]:
        lo, hi = out[c].quantile([0.01, 0.99])
        out[c] = out[c].clip(lo, hi)

    # critical NAs & duplicates
    out = out.dropna(subset=CRITICAL)
    if "id" in out.columns:
        out = out.drop_duplicates(subset=["id"], keep="first")

    # simple feature we’ll use immediately
    out["gross_yield"] = (out["rent"] * 12) / out["price"]

    return out
