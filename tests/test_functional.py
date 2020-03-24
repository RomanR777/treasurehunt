from core.functional import treasure_hunter


def test_array_equal():
    matrix = []
    result = treasure_hunter(matrix)
    assert result is not None
