from src.superhero import get_tallest_hero
import pytest

class TestGetTallestHero:
    heros = [
            {
                "name": "Hero 1",
                "appearance": {
                    "gender": "Male",
                    "height": ["6'0", "183 cm"]
                },
                "work": {
                    "occupation": "Java Senior"
                }
            },
            {
                "name": "Hero 2",
                "appearance": {
                    "gender": "Male",
                    "height": ["7'0", "213 cm"]
                },
                "work": {
                    "occupation": "ITMO Student"
                }
            },
            {
                "name": "Hero 3",
                "appearance": {
                    "gender": "Female",
                    "height": ["5'9", "175 cm"]
                },
                "work": {
                    "occupation": "QA-engineer"
                }
            },
            {
                "name": "Hero 4",
                "appearance": {
                    "gender": "Female",
                    "height": ["5'9", "165 cm"]
                },
                "work": {
                    "occupation": "Professor"
                }
            },
            {
                "name": "Hero 5",
                "appearance": {
                    "gender": "Male",
                    "height": ["5'9", "165 cm"]
                },
                "work": {
                    "occupation": "-"
                }
            },
            {
                "name": "Hero 6",
                "appearance": {
                    "gender": "Male",
                    "height": ["5'9", "165 cm"]
                },
                "work": {
                    "occupation": "-"
                }
            },
            {
                "name": "Hero 7",
                "appearance": {
                    "gender": "-",
                    "height": ["0 kg", "0"]
                },
                "work": {
                    "occupation": "Python developer"
                }
            },
            {
                "name": "Hero 8",
                "appearance": {
                    "gender": "-",
                    "height": ["0 kg", "0"]
                },
                "work": {
                    "occupation": "C++ developer"
                }
            },
            {
                "name": "Hero 9",
                "appearance": {
                    "gender": "-",
                    "height": ["6'1", "185 cm"]
                },
                "work": {
                    "occupation": "-"
                }
            },
            {
                "name": "Hero 10",
                "appearance": {
                    "gender": "-",
                    "height": ["6'6", "198 cm"]
                },
                "work": {
                    "occupation": "-"
                }
            }
        ]

    @pytest.fixture(autouse=True)
    def _monkeypatch_heros(self, monkeypatch):
        monkeypatch.setattr(
            "src.superhero.get_heros",
            lambda: self.heros
        )

    @pytest.mark.parametrize(
        "gender, has_work, expected_name",
        [
            pytest.param("Male", True, "Hero 2", id="male with work"),
            pytest.param("Male", False, ["Hero 5", "Hero 6"], id="male without work"),
            pytest.param("Female", True, "Hero 3", id="female with work",),
            pytest.param("Female", False, None, id="female without work (does not exist)"),
            pytest.param("-", True, None, id="no gender with work (has no height)"),
            pytest.param("-", False, "Hero 10", id="no gender without work"),
            pytest.param("bebra", True, None, id="invalid gender"),
        ],
    )
    def test_get_tallest_hero(self, gender, has_work, expected_name):
        result = get_tallest_hero(gender, has_work)

        if expected_name is None:
            assert result is None
        elif isinstance(expected_name, list):
            assert [hero["name"] for hero in result] == expected_name
        else:
            assert result[0]["name"] == expected_name