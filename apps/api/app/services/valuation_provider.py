from __future__ import annotations

from dataclasses import dataclass

from app.adapters.base import EasySbcAdapter, FutbinAdapter, FutggAdapter
from app.config.settings import get_settings
from app.schemas.valuation import ComparableCard, EvoCardInput, SourcePrice


@dataclass(frozen=True)
class SampleValuationResult:
    source_prices: list[SourcePrice]
    comparable_cards: list[ComparableCard]


def get_sample_valuation_result(card: EvoCardInput) -> SampleValuationResult:
    source_prices = _build_sample_source_prices(card)
    comparable_cards = _build_sample_comparable_cards(card, source_prices)
    return SampleValuationResult(
        source_prices=source_prices,
        comparable_cards=comparable_cards,
    )


def _build_sample_source_prices(card: EvoCardInput) -> list[SourcePrice]:
    settings = get_settings()
    adapters = [
        FutbinAdapter(),
        FutggAdapter(),
        EasySbcAdapter(),
    ]
    fallback_values = settings.valuation_sample_values
    currency_code = settings.valuation_currency_code

    source_prices: list[SourcePrice] = []
    for index, adapter in enumerate(adapters):
        source_price = adapter.get_current_price(card)
        if index < len(fallback_values):
            source_price = source_price.model_copy(
                update={
                    "price": int(fallback_values[index]),
                    "currency": currency_code.lower(),
                }
            )
        elif currency_code:
            source_price = source_price.model_copy(
                update={"currency": currency_code.lower()}
            )

        source_prices.append(source_price)

    return source_prices


def _build_sample_comparable_cards(
    card: EvoCardInput,
    source_prices: list[SourcePrice],
) -> list[ComparableCard]:
    comparable_base_price = source_prices[0].price
    first_position = card.positions[0]

    return [
        ComparableCard(
            player_name=f"{card.player_name} Prototype",
            base_card_type=f"{card.base_card_type} Evo",
            final_overall=max(0, min(99, card.final_overall - 1)),
            positions=card.positions,
            weak_foot=card.weak_foot,
            skill_moves=card.skill_moves,
            playstyles=card.playstyles[:],
            playstyles_plus=card.playstyles_plus[:],
            face_stats=card.face_stats,
            in_game_stats=card.in_game_stats,
            platform=card.platform,
            source_prices=source_prices[:2],
            median_price_now=comparable_base_price - 2500,
        ),
        ComparableCard(
            player_name=f"{card.player_name} Elite",
            base_card_type=f"{card.base_card_type} Plus",
            final_overall=max(0, min(99, card.final_overall + 1)),
            positions=[first_position],
            weak_foot=card.weak_foot,
            skill_moves=card.skill_moves,
            playstyles=card.playstyles[:],
            playstyles_plus=card.playstyles_plus[:],
            face_stats=card.face_stats,
            in_game_stats=card.in_game_stats,
            platform=card.platform,
            source_prices=source_prices[1:],
            median_price_now=comparable_base_price + 4200,
        ),
    ]
