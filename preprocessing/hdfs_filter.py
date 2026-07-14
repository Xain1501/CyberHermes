from pathlib import Path

from .utils import load_csv, save_csv
from .metrics import calculate_reduction, print_metrics


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "datasets" / "hdfs" / "HDFS_2k.log_structured.csv"
OUTPUT_PATH = BASE_DIR / "processed" / "hdfs_filtered.csv"

SUSPICIOUS_PATTERNS = [
    "error",
    "exception",
    "failed",
    "failure",
    "corrupt",
    "missing",
    "timeout",
    "denied"
]


def filter_hdfs():
    print("\n[HDFS] Loading dataset...")

    df = load_csv(INPUT_PATH)

    original_count = len(df)

    mask = df["Content"].fillna("").str.lower().apply(
        lambda text: any(
            pattern in text
            for pattern in SUSPICIOUS_PATTERNS
        )
    )

    filtered_df = df[mask]

    filtered_count = len(filtered_df)

    save_csv(filtered_df, OUTPUT_PATH)

    reduction = calculate_reduction(
        original_count,
        filtered_count
    )

    print_metrics({
        "Dataset": "HDFS",
        "Original Logs": original_count,
        "Filtered Logs": filtered_count,
        "Reduction %": reduction
    })

    print(f"\nSaved -> {OUTPUT_PATH}")


if __name__ == "__main__":
    filter_hdfs()