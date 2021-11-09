import pytest
from getmin import get_minimum


class TestMain:
    def test_find_min(self):
        array = [6, 4, 3, 78, 79, 89]
        assert get_minimum(array) == 3

    def test_array_is_empty(self):
        array = []
        with pytest.raises(ValueError):
            get_minimum(array)

    def test_array_min_is_on_edge(self):
        array = [6, 4, 3, 2]
        assert get_minimum(array) == 2
