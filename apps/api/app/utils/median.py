def calculate_median(values: list[float]) -> float:
    if not values:
        raise ValueError("Median requires at least one value.")

    sorted_values = sorted(values)
    midpoint = len(sorted_values) // 2

    if len(sorted_values) % 2 == 1:
        return sorted_values[midpoint]

    left_value = sorted_values[midpoint - 1]
    right_value = sorted_values[midpoint]
    return (left_value + right_value) / 2

