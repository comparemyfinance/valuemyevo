from app.adapters.valuation_adapter import normalize_valuation_response
from app.schemas.valuation import ComparableCard, EvoCardInput, ValuationResponse
from app.services.valuation_provider import get_stub_valuation_result
from app.utils.median import calculate_median


def build_valuation_response(card: EvoCardInput) -> ValuationResponse:
    stub_result = get_stub_valuation_result(card)
    source_prices = stub_result.source_prices
    comparable_cards: list[ComparableCard] = stub_result.comparable_cards
    median_price_now = _calculate_median_price(source_prices)
    confidence = _calculate_confidence(source_prices, comparable_cards)
    explanation = _build_explanation(source_prices, comparable_cards)

    return normalize_valuation_response(
        card=card,
        source_prices=source_prices,
        median_price_now=median_price_now,
        comparable_cards=comparable_cards,
        confidence=confidence,
        explanation=explanation,
    )


def _calculate_median_price(source_prices: list) -> int:
    if not source_prices:
        return 0

    price_points = [source_price.price for source_price in source_prices]
    return int(calculate_median([float(price) for price in price_points]))


def _calculate_confidence(
    source_prices: list,
    comparable_cards: list[ComparableCard],
) -> float:
    base_confidence = 0.45
    source_bonus = min(0.25, len(source_prices) * 0.08)
    comparable_bonus = min(0.2, len(comparable_cards) * 0.1)
    return round(min(0.95, base_confidence + source_bonus + comparable_bonus), 2)


def _build_explanation(
    source_prices: list,
    comparable_cards: list[ComparableCard],
) -> str:
    return (
        "Stub valuation service returned mocked market source prices and mocked "
        f"comparable cards. Median price is derived from {len(source_prices)} "
        f"available source prices and benchmarked against {len(comparable_cards)} "
        "mock comparables."
    )
