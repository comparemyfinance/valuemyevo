import os
from dataclasses import dataclass

from app.utils.parsing import parse_float_list


@dataclass(frozen=True)
class ApiSettings:
    app_name: str
    app_env: str
    app_version: str
    app_port: int
    valuation_currency_code: str
    valuation_sample_values: list[float]


def get_settings() -> ApiSettings:
    app_port = _parse_int_env("APP_PORT", "8000")
    valuation_sample_values = parse_float_list(
        os.getenv("VALUATION_SAMPLE_VALUES", "12000,15000,18000")
    )

    return ApiSettings(
        app_name=os.getenv("APP_NAME", "EvoWorth API"),
        app_env=os.getenv("APP_ENV", "development"),
        app_version=os.getenv("APP_VERSION", "0.1.0"),
        app_port=app_port,
        valuation_currency_code=os.getenv("VALUATION_CURRENCY_CODE", "coins").strip()
        or "coins",
        valuation_sample_values=valuation_sample_values,
    )


def _parse_int_env(variable_name: str, default_value: str) -> int:
    raw_value = os.getenv(variable_name, default_value).strip()

    try:
        return int(raw_value)
    except ValueError as exc:
        raise ValueError(
            f"{variable_name} must be an integer, received '{raw_value}'."
        ) from exc

