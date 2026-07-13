import pytest

from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_sets_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_adds_one_ingredient(self, burger_with_bun, mock_sauce):
        burger_with_bun.add_ingredient(mock_sauce)
        assert len(burger_with_bun.ingredients) == 1

    def test_add_ingredient_adds_two_ingredients(self, burger_with_ingredients):
        assert len(burger_with_ingredients.ingredients) == 2

    def test_remove_ingredient_removes_correct_ingredient(self, burger_with_ingredients, mock_filling):
        burger_with_ingredients.remove_ingredient(0)
        assert burger_with_ingredients.ingredients == [mock_filling]

    def test_remove_ingredient_decreases_count(self, burger_with_ingredients):
        burger_with_ingredients.remove_ingredient(0)
        assert len(burger_with_ingredients.ingredients) == 1

    def test_get_receipt_contains_bun_name(self, burger_with_bun):
        receipt = burger_with_bun.get_receipt()
        assert 'black bun' in receipt

    def test_get_receipt_contains_price(self, burger_with_ingredients):
        receipt = burger_with_ingredients.get_receipt()
        assert f'Price: {burger_with_ingredients.get_price()}' in receipt

    @pytest.mark.parametrize('ingredient_fixture', ['mock_sauce', 'mock_filling'])
    def test_get_receipt_contains_ingredient_name(self, request, burger_with_bun, ingredient_fixture):
        ingredient = request.getfixturevalue(ingredient_fixture)
        burger_with_bun.add_ingredient(ingredient)
        receipt = burger_with_bun.get_receipt()
        assert ingredient.get_name() in receipt

    def test_get_receipt_lists_ingredients_in_correct_order(self, burger_with_ingredients):
        receipt = burger_with_ingredients.get_receipt()
        sauce_position = receipt.find('hot sauce')
        filling_position = receipt.find('cutlet')
        assert sauce_position < filling_position
