from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    res = []
    _spiral_order_intern(matrix, res, padding=0)
    return res


def _spiral_order_intern(matrix: List[List[int]], res: List[int], padding: int) -> None:
    height = len(matrix) - (padding * 2)
    if height > 0:
        width = len(matrix[padding]) - (padding * 2)
        if width <= 0:
            return

        for i in range(0, width):
            res.append(matrix[padding][padding + i])

        if height > 1:
            for i in range(1, height):
                res.append(matrix[padding + i][padding + width - 1])

            for i in range(1, width):
                res.append(matrix[padding + height - 1][padding + width - 1 - i])

        if width > 1:
            for i in range(1, height - 1):
                res.append(matrix[padding + height - 1 - i][padding])

        if height > 2:
            _spiral_order_intern(matrix, res, padding=padding + 1)
