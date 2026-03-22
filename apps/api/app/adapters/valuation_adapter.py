from app.schemas.valuation import ComparableCard, EvoCardInput, SourcePrice, ValuationResponse


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


def normalize_comparable_card(comparable_card: ComparableCard) -> ComparableCard:
    return ComparableCard(**comparable_card.model_dump())


def normalize_valuation_response(
    *,
    card: EvoCardInput,
    median_price_now: int,
    comparable_cards: list[ComparableCard],
    confidence: float,
    explanation: str,
) -> ValuationResponse:
    return ValuationResponse(
        **card.model_dump(),
        source_prices=[
            normalize_source_price(**source_price.model_dump())
            for source_price in card.source_prices
        ],
        comparable_cards=[
            normalize_comparable_card(comparable_card)
            for comparable_card in comparable_cards
        ],
        median_price_now=median_price_now,
        confidence=confidence,
        explanation=explanation.strip(),
    )
