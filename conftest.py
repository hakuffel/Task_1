import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BUN_NAME_1, BUN_PRICE_1, SAUCE_NAME, SAUCE_PRICE, FILLING_NAME, FILLING_PRICE


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = BUN_NAME_1
    bun.get_price.return_value = BUN_PRICE_1
    return bun


@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sauce.get_name.return_value = SAUCE_NAME
    sauce.get_price.return_value = SAUCE_PRICE
    return sauce


@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_name.return_value = FILLING_NAME
    filling.get_price.return_value = FILLING_PRICE
    return filling


@pytest.fixture
def burger_with_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger


@pytest.fixture
def burger_with_ingredients(burger_with_bun, mock_sauce, mock_filling):
    burger_with_bun.add_ingredient(mock_sauce)
    burger_with_bun.add_ingredient(mock_filling)
    return burger_with_bun
