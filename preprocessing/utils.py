import os
import pandas as pd


def load_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    return pd.read_csv(path)


def save_csv(data, path):
    directory = os.path.dirname(path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    data.to_csv(path, index=False)


def load_text(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        return file.readlines()


def save_text(lines, path):
    directory = os.path.dirname(path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def get_file_size(path):
    return os.path.getsize(path)