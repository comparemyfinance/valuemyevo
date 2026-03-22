def parse_float_list(raw_value: str) -> list[float]:
    normalized_items = [item.strip() for item in raw_value.split(",") if item.strip()]

    if not normalized_items:
        raise ValueError("Expected at least one numeric value.")

    return [float(item) for item in normalized_items]

