import os


def check_directories():
    directories = [
        "../datasets/hdfs",
        "../datasets/cic_ids",
        "../datasets/injections",
        "../processed"
    ]

    print("\nChecking project directories...\n")

    for directory in directories:
        if os.path.exists(directory):
            print(f"[FOUND] {directory}")
        else:
            print(f"[MISSING] {directory}")


def run_hdfs_pipeline():
    print("\n[HDFS] Pipeline will run here")
    
    # Later:
    # from hdfs_filter import filter_hdfs
    # filter_hdfs()


def run_cic_pipeline():
    print("\n[CIC-IDS] Pipeline will run here")

    # Later:
    # from cic_filter import filter_cic
    # filter_cic()


def run_injection_pipeline():
    print("\n[Injection] Pipeline will run here")

    # Later:
    # from injection_filter import filter_injections
    # filter_injections()


def main():

    print("==============================")
    print(" CyberHermes Preprocessing")
    print("==============================")

    check_directories()

    print("\nStarting preprocessing pipeline...")

    run_hdfs_pipeline()
    run_cic_pipeline()
    run_injection_pipeline()

    print("\nPipeline execution completed.")


if __name__ == "__main__":
    main()