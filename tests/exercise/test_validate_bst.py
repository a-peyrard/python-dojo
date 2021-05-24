from hamcrest import equal_to, assert_that

from dojo.exercise.validate_bst import TreeNode, is_valid_bst, is_valid_bst_rec


class TestIsValidBst:
    def test_should_validate_example_1(self):
        # GIVEN
        bst = TreeNode(2, TreeNode(1), TreeNode(3))

        # WHEN
        res = is_valid_bst(bst)

        # THEN
        assert_that(res, equal_to(True))

    def test_should_validate_example_2(self):
        # GIVEN
        bst = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

        # WHEN
        res = is_valid_bst(bst)

        # THEN
        assert_that(res, equal_to(False))

    def test_should_validate_example_3(self):
        # GIVEN
        bst = TreeNode(1, TreeNode(1))

        # WHEN
        res = is_valid_bst(bst)

        # THEN
        assert_that(res, equal_to(False))


class TestIsValidBstRec:
    def test_should_return_correct_min_max(self):
        # GIVEN
        bst = TreeNode(4, TreeNode(3), TreeNode(6))

        # WHEN
        res, min_value, max_value = is_valid_bst_rec(bst)

        # THEN
        assert_that(res, equal_to(True))
        assert_that(min_value, equal_to(3))
        assert_that(max_value, equal_to(6))
