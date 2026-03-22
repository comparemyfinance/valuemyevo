import unittest

from fastapi.testclient import TestClient

from app.main import app


class ValuationResponseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_evo_valuation_shape(self) -> None:
        response = self.client.post(
            "/valuation/evo",
            json={
                "player_name": "Jude Bellingham",
                "base_card_type": "Rare Gold",
                "final_overall": 91,
                "positions": ["CM", "CAM"],
                "weak_foot": 4,
                "skill_moves": 4,
                "playstyles": ["Incisive Pass", "Technical"],
                "playstyles_plus": ["Pinged Pass"],
                "face_stats": {
                    "pace": 84,
                    "shooting": 83,
                    "passing": 88,
                    "dribbling": 89,
                    "defending": 82,
                    "physical": 86,
                },
                "platform": "playstation",
                "source_prices": [
                    {
                        "source_name": "futbin",
                        "platform": "playstation",
                        "price": 120000,
                        "currency": "coins",
                    },
                    {
                        "source_name": "futwiz",
                        "platform": "playstation",
                        "price": 126000,
                        "currency": "coins",
                    },
                    {
                        "source_name": "easySBC",
                        "platform": "playstation",
                        "price": 123000,
                        "currency": "coins",
                    },
                ],
            },
        )

        self.assertEqual(response.status_code, 200)
        response_json = response.json()

        self.assertEqual(
            set(response_json.keys()),
            {
                "player_name",
                "base_card_type",
                "final_overall",
                "positions",
                "weak_foot",
                "skill_moves",
                "playstyles",
                "playstyles_plus",
                "face_stats",
                "in_game_stats",
                "platform",
                "source_prices",
                "median_price_now",
                "comparable_cards",
                "confidence",
                "explanation",
            },
        )
        self.assertEqual(response_json["player_name"], "Jude Bellingham")
        self.assertEqual(response_json["base_card_type"], "Rare Gold")
        self.assertEqual(response_json["median_price_now"], 123000)
        self.assertEqual(response_json["platform"], "playstation")
        self.assertEqual(response_json["comparable_cards"], [])
        self.assertEqual(response_json["confidence"], 0.65)
