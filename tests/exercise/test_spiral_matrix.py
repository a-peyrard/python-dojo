from hamcrest import assert_that, equal_to

from dojo.exercise.spiral_matrix import spiral_order


class TestSpiralOrder:
    def test_should_validate_basic(self):
        # GIVEN
        matrix = [[1, 2], [4, 5]]

        # WHEN
        result = spiral_order(matrix)

        # THEN
        assert_that(result, equal_to([1, 2, 5, 4]))

    def test_should_validate_example_1(self):
        # GIVEN
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # WHEN
        result = spiral_order(matrix)

        # THEN
        assert_that(result, equal_to([1, 2, 3, 6, 9, 8, 7, 4, 5]))

    def test_should_validate_example_2(self):
        # GIVEN
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

        # WHEN
        result = spiral_order(matrix)

        # THEN
        assert_that(result, equal_to([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]))

    def test_should_validate_bigger(self):
        # GIVEN
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]

        # WHEN
        result = spiral_order(matrix)

        # THEN
        assert_that(
            result,
            equal_to(
                [
                    1, 2, 3, 4, 5,
                    10, 15, 20, 25, 24,
                    23, 22, 21, 16, 11,
                    6, 7, 8, 9, 14,
                    19, 18, 17, 12, 13
                ]
            )
        )

    def test_should_columnar_matrix(self):
        # GIVEN
        matrix = [[7], [9], [6]]

        # WHEN
        result = spiral_order(matrix)

        # THEN
        assert_that(result, equal_to([7, 9, 6]))

    def test_should_columnar_matrix2(self):
        # GIVEN
        matrix = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

        # WHEN
        result = spiral_order(matrix)

        # THEN
        assert_that(result, equal_to([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
