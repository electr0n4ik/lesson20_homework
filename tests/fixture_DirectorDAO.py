from unittest.mock import MagicMock
import pytest
from dao.model.director import Director


@pytest.fixture()
def prod_class():
    director = Director()
    director.id = MagicMock(return_value=1)
    director.name = MagicMock(return_value="TestDirector")

    return director
