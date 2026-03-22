from __future__ import annotations

from dataclasses import dataclass

from app.schemas.valuation import ComparableCard, EvoCardInput, SourcePrice


@dataclass(frozen=True)
class StubValuationResult:
    source_prices: list[SourcePrice]
    comparable_cards: list[ComparableCard]


def get_stub_valuation_result(card: EvoCardInput) -> StubValuationResult:
    source_prices = _build_mock_source_prices(card)
    comparable_cards = _build_mock_comparable_cards(card, source_prices)
    return StubValuationResult(
        source_prices=source_prices,
        comparable_cards=comparable_cards,
    )


def _build_mock_source_prices(card: EvoCardInput) -> list[SourcePrice]:
    baseline_price = max(10000, card.final_overall * 2100)
    return [
        SourcePrice(
            source_name="futbin",
            platform=card.platform,
            price=baseline_price,
            currency="coins",
            observed_at="2026-03-22T12:00:00Z",
            url="https://www.futbin.com/",
        ),
        SourcePrice(
            source_name="futwiz",
            platform=card.platform,
            price=baseline_price + 3500,
            currency="coins",
            observed_at="2026-03-22T12:03:00Z",
            url="https://www.futwiz.com/",
        ),
        SourcePrice(
            source_name="easysbc",
            platform=card.platform,
            price=baseline_price - 1500,
            currency="coins",
            observed_at="2026-03-22T12:05:00Z",
            url="https://www.easysbc.io/",
        ),
    ]


def _build_mock_comparable_cards(
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
