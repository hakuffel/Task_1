from unittest.mock import patch

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @patch('praktikum.database.Ingredient')
    def test_database_creates_three_sauces_and_three_fillings(self, mock_ingredient_class):
        Database()
        used_types = [call.args[0] for call in mock_ingredient_class.call_args_list]
        assert used_types.count(INGREDIENT_TYPE_SAUCE) == 3
        assert used_types.count(INGREDIENT_TYPE_FILLING) == 3
