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
    return ApiSettings(
        app_name=os.getenv("APP_NAME", "EvoWorth API"),
        app_env=os.getenv("APP_ENV", "development"),
        app_version=os.getenv("APP_VERSION", "0.1.0"),
        app_port=int(os.getenv("APP_PORT", "8000")),
        valuation_currency_code=os.getenv("VALUATION_CURRENCY_CODE", "GBP"),
        valuation_sample_values=parse_float_list(
            os.getenv("VALUATION_SAMPLE_VALUES", "12000,15000,18000")
        ),
    )

