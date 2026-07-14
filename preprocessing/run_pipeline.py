from pathlib import Path

from .hdfs_filter import filter_hdfs
from .cic_filter import filter_cic


BASE_DIR = Path(__file__).resolve().parent.parent


def check_directories():
	directories = [
		BASE_DIR / "datasets" / "hdfs",
		BASE_DIR / "datasets" / "cic_ids",
		BASE_DIR / "datasets" / "injections",
		BASE_DIR / "processed",
	]

	print("\nChecking project directories...\n")
	for directory in directories:
		if directory.exists():
			print(f"[FOUND] {directory}")
		else:
			print(f"[MISSING] {directory}")


def main():
	print("==============================")
	print(" CyberHermes Preprocessing")
	print("==============================")
	check_directories()

	print("\nStarting preprocessing pipeline...")
	filter_hdfs()
	filter_cic()
	print("\nPipeline execution completed.")


if __name__ == "__main__":
	main()