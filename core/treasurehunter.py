def to_index(value: int) -> tuple:
    """
    Convert integer value from matrix
    to zero based indexes row, col
    Example:
        67 -> 5, 6
    :param value: integer between 11..55
    :return: row index, col index
    """
    if value < 11 or value > 55:
        raise ValueError("Value must be between 11..55")
    str_val = str(value)
    return int(str_val[0]) - 1, int(str_val[1]) - 1


def to_val(row: int, col: int) -> int:
    """
    Covert row, col zero based indexes to
    the value
    Example: 5, 6 -> 67
    :param row: zero based integer row index
    :param col: zero based integer col index
    :return: integer value
    """
    if row > 5 or col < 1:
        raise ValueError('row and col must be between 1..5')
    return int(str(row + 1) + str(col + 1))


def hunt_treasure(matrix: list, start_pos=11) -> None:
    """
    The functional implementation of the treasure hunt
    :param matrix: incoming data list of lists (two dimensional array)
    :param start_pos: integer value of starting position 11 by default
    :return: None
    """
    result = [start_pos]

    def hunt(val):
        row, col = to_index(val)
        new_val = matrix[row][col]
        if val == new_val:
            return
        else:
            result.append(new_val)
            hunt(new_val)
    hunt(start_pos)
    return result


class TreasureHunter:
    """
    This class implements treasure hunting in OOP style.
    Usage example:
        hunter = TreasureHunter(input_data)
        treasure = [item for item in hunter]
    """
    def __init__(self, matrix: list, start_value=11) -> None:
        """
        :param matrix: incoming data list of lists (two dimensional array)
        :param start_value: integer value of starting position 11 by default
        """
        self.matrix = matrix
        self.start_value = start_value
        self.current_value = None

    def __iter__(self):
        self.current_value = None
        return self

    def __next__(self) -> int:
        if self.current_value is None:
            self.current_value = self.start_value
            return self.current_value

        row, col = to_index(self.current_value)
        next_val = self.matrix[row][col]
        if next_val == self.current_value:
            raise StopIteration()
        self.current_value = next_val
        return self.current_value
