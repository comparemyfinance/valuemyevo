from app.adapters.valuation_adapter import normalize_valuation_response
from app.schemas.valuation import ComparableCard, EvoCardInput, ValuationResponse
from app.utils.median import calculate_median


def build_valuation_response(card: EvoCardInput) -> ValuationResponse:
    comparable_cards: list[ComparableCard] = []
    price_points = [source_price.price for source_price in card.source_prices]

    if price_points:
        median_price_now = int(calculate_median([float(price) for price in price_points]))
        confidence = min(0.95, round(0.35 + (0.1 * len(price_points)), 2))
        explanation = (
            "Valuation currently uses the median of submitted source_prices as a "
            "normalized placeholder until comparable-card matching is implemented."
        )
    else:
        median_price_now = 0
        confidence = 0.0
        explanation = (
            "No source_prices were supplied, so the API could not derive a live "
            "market valuation yet."
        )

    return normalize_valuation_response(
        card=card,
        median_price_now=median_price_now,
        comparable_cards=comparable_cards,
        confidence=confidence,
        explanation=explanation,
    )
