from app.adapters.base import normalize_source_price
from app.schemas.valuation import ComparableCard, EvoCardInput, SourcePrice, ValuationResponse


def normalize_comparable_card(comparable_card: ComparableCard) -> ComparableCard:
    return ComparableCard(**comparable_card.model_dump())


def normalize_valuation_response(
    *,
    card: EvoCardInput,
    source_prices: list[SourcePrice],
    median_price_now: int,
    comparable_cards: list[ComparableCard],
    confidence: float,
    explanation: str,
) -> ValuationResponse:
    return ValuationResponse(
        **{
            **card.model_dump(),
            "source_prices": [
                normalize_source_price(**source_price.model_dump())
                for source_price in source_prices
            ],
        },
        comparable_cards=[
            normalize_comparable_card(comparable_card)
            for comparable_card in comparable_cards
        ],
        median_price_now=median_price_now,
        confidence=confidence,
        explanation=explanation.strip(),
    )
