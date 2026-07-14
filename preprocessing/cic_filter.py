from pathlib import Path

from .utils import load_csv, save_csv
import pandas as pd
from .metrics import (
    calculate_reduction,
    calculate_retention,
    print_metrics
)


BASE_DIR = Path(__file__).resolve().parent.parent

CIC_DIR = BASE_DIR / "datasets" / "cic_ids"
DEFAULT_INPUT_FILENAME = "cic_ids_sample_1000.csv"
OUTPUT_PATH = BASE_DIR / "processed" / "cic_filtered.csv"


def find_cic_input():
    default = CIC_DIR / DEFAULT_INPUT_FILENAME
    if default.exists():
        return default

    csv_files = sorted(CIC_DIR.glob("*.csv"))
    if csv_files:
        return csv_files[0]

    # Provide a clearer error if nothing is found
    available = [p.name for p in CIC_DIR.iterdir()] if CIC_DIR.exists() else []
    raise FileNotFoundError(
        f"No CIC-IDS CSV found in {CIC_DIR}. Available: {available}"
    )


def filter_cic():
    input_path = find_cic_input()
    print(f"\n[CIC-IDS] Loading dataset from {input_path}...")

    df = load_csv(input_path)

    original_count = len(df)

    # Auto-detect label column (case-insensitive)
    candidates = [
        "Label",
        "Attack",
        "Class",
        "Category",
        "Attack_Binary",
        "AttackBinary",
        "Attack binary",
    ]

    label_column = None
    cols_lower = {c.lower(): c for c in df.columns}
    for cand in candidates:
        if cand.lower() in cols_lower:
            label_column = cols_lower[cand.lower()]
            break

    if label_column is None:
        # Fallback: try common patterns
        for col in df.columns:
            if "attack" in col.lower() or "label" in col.lower() or "class" in col.lower():
                label_column = col
                break

    if label_column is None:
        raise KeyError(f"No label column found. Available columns: {list(df.columns)}")

    # Determine attack rows robustly depending on dtype
    series = df[label_column]
    if pd.api.types.is_numeric_dtype(series):
        # numeric labels: treat non-zero as attack
        attack_rows = df[series != 0]
    else:
        s = series.fillna("").astype(str).str.strip().str.upper()
        benign_values = {"BENIGN", "NORMAL", "0", "FALSE", "NONE", "NO"}
        attack_rows = df[~s.isin(benign_values)]

    attack_count = len(attack_rows)

    save_csv(
        attack_rows,
        OUTPUT_PATH
    )

    reduction = calculate_reduction(
        original_count,
        attack_count
    )

    retention = calculate_retention(
        attack_count,
        attack_count
    )

    print_metrics({
        "Dataset": "CIC-IDS",
        "Original Rows": original_count,
        "Attack Rows": attack_count,
        "Reduction %": reduction,
        "Attack Retention %": retention
    })

    print(f"\nSaved -> {OUTPUT_PATH}")


if __name__ == "__main__":
    filter_cic()