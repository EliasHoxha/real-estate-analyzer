# src/data/schema.py
from __future__ import annotations
from pathlib import Path
from typing import Dict, List
import pandas as pd
import yaml

def _project_root() -> Path:
    # schema.py is in src/data/ → parents[2] is repo root
    return Path(__file__).resolve().parents[2]

PARAMS_PATH = _project_root() / "configs" / "params.yaml"

def _load_params(path: str | Path = PARAMS_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

PARAMS = _load_params()
REQ_COLS: List[str] = PARAMS["schema"]["required_columns"]
DTYPES: Dict[str, str] = PARAMS["schema"]["dtypes"]

# --- normalization (keep yours) ---
CANONICAL_RENAMES = {
    "listing_id": "id",
    "beds": "bed",
    "baths": "bath",
    "monthly_rent": "rent",
    "city_name": "city",
}
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [c.strip().lower() for c in out.columns]
    out = out.rename(columns={k.lower(): v for k, v in CANONICAL_RENAMES.items()})
    return out

# --- if you're using pandera (Option B) ---
import pandera.pandas as pa
from pandera.pandas import Column, Check, DataFrameSchema

SCHEMA = DataFrameSchema(
    {
        "id":   Column(pa.Int64,   Check.ge(0), unique=True,  nullable=False),
        "city": Column(pa.String,  Check.str_length(min_value=1), nullable=False),
        "price":Column(pa.Float64, Check.gt(0), nullable=False),
        "rent": Column(pa.Float64, Check.ge(0), nullable=False),
        "bed":  Column(pa.Int64,   Check.ge(0), nullable=False),
        "bath": Column(pa.Float64, Check.ge(0), nullable=False),
    },
    strict=False,
    coerce=True,
)

def validate_and_cast(df: pd.DataFrame) -> pd.DataFrame:
    return SCHEMA.validate(df, lazy=True)