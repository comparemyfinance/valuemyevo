import unittest

from app.adapters.base import (
    EasySbcAdapter,
    FutbinAdapter,
    FutggAdapter,
    normalize_source_price,
)
from app.schemas.valuation import EvoCardInput, FaceStats


class SourceAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.card_query = EvoCardInput(
            player_name="Jude Bellingham",
            base_card_type="Rare Gold",
            final_overall=91,
            positions=["CM", "CAM"],
            weak_foot=4,
            skill_moves=4,
            playstyles=["Incisive Pass"],
            playstyles_plus=["Pinged Pass"],
            face_stats=FaceStats(
                pace=84,
                shooting=83,
                passing=88,
                dribbling=89,
                defending=82,
                physical=86,
            ),
            platform="playstation",
            source_prices=[],
        )

    def test_normalize_source_price(self) -> None:
        source_price = normalize_source_price(
            source_name=" Futbin ",
            platform="PlayStation",
            price=100000,
            currency="COINS",
            url="https://www.futbin.com/",
        )

        self.assertEqual(source_price.source_name, "Futbin")
        self.assertEqual(source_price.platform, "playstation")
        self.assertEqual(source_price.currency, "coins")

    def test_placeholder_adapters_return_sample_values(self) -> None:
        source_prices = [
            FutbinAdapter().get_current_price(self.card_query),
            FutggAdapter().get_current_price(self.card_query),
            EasySbcAdapter().get_current_price(self.card_query),
        ]

        self.assertEqual(
            [source_price.source_name for source_price in source_prices],
            ["futbin", "futgg", "easysbc"],
        )
        self.assertEqual(
            [source_price.price for source_price in source_prices],
            [191100, 194600, 189600],
        )
