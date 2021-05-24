from typing import Tuple


class TreeNode:
    def __init__(self,
                 val: int = 0,
                 left: 'TreeNode' = None,
                 right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    return is_valid_bst_rec(root)[0]


def is_valid_bst_rec(root: TreeNode) -> Tuple[bool, int, int]:
    min_value = root.val
    max_value = root.val
    if root.left is None and root.right is None:
        return True, min_value, max_value

    if root.left is not None:
        valid, local_min, local_max = is_valid_bst_rec(root.left)
        if not valid or local_max >= root.val:
            return False, min_value, local_max
        min_value = local_min

    if root.right is not None:
        valid, local_min, local_max = is_valid_bst_rec(root.right)
        if not valid or local_min <= root.val:
            return False, local_min, max_value
        max_value = local_max

    return True, min_value, max_value
