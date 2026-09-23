import pytest
from src.utils.hero_height import height_to_feet

class TestHeightToFeet:
    @pytest.mark.parametrize(
        "height, expected",
        [
            pytest.param(["203 cm"], 203 / 30.48, id="centimeters"),
            pytest.param(["61.0 meters"], 61.0 * 3.28, id="meters"),
            pytest.param(["6'8"], 6 + 8 / 12, id="feet_and_inches"),
            pytest.param(["200", "61.0 meters"], 61.0 * 3.28, id="only_one_valid_value"),
            pytest.param(["5'10'"], 5 + 10 / 12, id="double_apostrophe"),
            pytest.param(["5'57"], 5 + 57 / 12, id="unusual value"),
            pytest.param(["0'25"], 25 / 12, id="inches_only"),
            pytest.param(["10'"], 10, id="feet_only"),
        ],
    )
    def test_height_converted_to_feet(self, height, expected):
        assert height_to_feet(height) == expected


    @pytest.mark.parametrize(
        "height",
        [
            pytest.param(["-"], id="minus"),
            pytest.param(["0 cm"], id="zero_centimeters"),
            pytest.param(["0 kg"], id="zero_kilograms"),
            pytest.param(["200"], id="200"),
            pytest.param(["205"], id="205"),
            pytest.param(["1000"], id="1000"),
        ],
    )
    def test_invalid_height(self, height):
        assert height_to_feet(height) is None