from __future__ import annotations

from abc import ABC, abstractmethod

from app.schemas.valuation import EvoCardInput, SourcePrice


def normalize_source_price(
    *,
    source_name: str,
    platform: str,
    price: int,
    currency: str,
    observed_at: str | None = None,
    url: str | None = None,
) -> SourcePrice:
    return SourcePrice(
        source_name=source_name.strip(),
        platform=platform.lower(),
        price=price,
        currency=currency.lower(),
        observed_at=observed_at,
        url=url,
    )


class BaseSourceAdapter(ABC):
    source_name: str
    source_url: str

    @abstractmethod
    def get_current_price(self, card_query: EvoCardInput) -> SourcePrice:
        """Return the current price for a card query without scraping logic here."""


class FutbinAdapter(BaseSourceAdapter):
    source_name = "futbin"
    source_url = "https://www.futbin.com/"

    def get_current_price(self, card_query: EvoCardInput) -> SourcePrice:
        baseline_price = max(10000, card_query.final_overall * 2100)
        return normalize_source_price(
            source_name=self.source_name,
            platform=card_query.platform,
            price=baseline_price,
            currency="coins",
            observed_at="2026-03-22T12:00:00Z",
            url=self.source_url,
        )


class FutggAdapter(BaseSourceAdapter):
    source_name = "futgg"
    source_url = "https://www.fut.gg/"

    def get_current_price(self, card_query: EvoCardInput) -> SourcePrice:
        baseline_price = max(10000, card_query.final_overall * 2100)
        return normalize_source_price(
            source_name=self.source_name,
            platform=card_query.platform,
            price=baseline_price + 3500,
            currency="coins",
            observed_at="2026-03-22T12:03:00Z",
            url=self.source_url,
        )


class EasySbcAdapter(BaseSourceAdapter):
    source_name = "easysbc"
    source_url = "https://www.easysbc.io/"

    def get_current_price(self, card_query: EvoCardInput) -> SourcePrice:
        baseline_price = max(10000, card_query.final_overall * 2100)
        return normalize_source_price(
            source_name=self.source_name,
            platform=card_query.platform,
            price=baseline_price - 1500,
            currency="coins",
            observed_at="2026-03-22T12:05:00Z",
            url=self.source_url,
        )
