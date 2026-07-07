def calculate_reduction(original_count, filtered_count):
    if original_count == 0:
        return 0

    reduction = ((original_count - filtered_count) / original_count) * 100

    return round(reduction, 2)


def calculate_retention(original_attacks, filtered_attacks):
    if original_attacks == 0:
        return 0

    retention = (filtered_attacks / original_attacks) * 100

    return round(retention, 2)


def calculate_false_positive_rate(false_positives, total_benign):
    if total_benign == 0:
        return 0

    rate = (false_positives / total_benign) * 100

    return round(rate, 2)


def print_metrics(metrics):
    print("\n===== Preprocessing Metrics =====")

    for key, value in metrics.items():
        print(f"{key}: {value}")
        