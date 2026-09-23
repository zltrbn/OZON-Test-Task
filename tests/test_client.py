from src.client import get_heros
import pytest

class TestHeroesApi:
    @pytest.fixture(scope="class")
    @classmethod
    def heros(self):
        return get_heros()

    def test_get_heroes_returns_non_empty_list(self, heros):
        assert isinstance(heros, list)
        assert len(heros) > 0


    def test_get_heroes_returns_dictionaries(self, heros):
        assert all(isinstance(hero, dict) for hero in heros)


    def test_hero_has_required_fields(self, heros):
        required_fields = {"id", "name", "appearance", "work"}

        for hero in heros:
            assert required_fields <= hero.keys()


    def test_hero_appearance_has_required_fields(self, heros):
        required_appearance_fields = {"gender", "height"}

        for hero in heros:
            appearance = hero["appearance"]

            assert isinstance(appearance, dict)
            assert required_appearance_fields <= appearance.keys()


    def test_hero_work_has_required_fields(self, heros):
        for hero in heros:
            work = hero["work"]

            assert isinstance(work, dict)
            assert "occupation" in work


    def test_hero_height_in_expected_format(self, heros):
        for hero in heros:
            height = hero["appearance"]["height"]

            assert isinstance(height, list)
            assert len(height) == 2
            assert all(isinstance(value, str) for value in height)
