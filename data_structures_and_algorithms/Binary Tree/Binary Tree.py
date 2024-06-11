"""
To store N records we require a balanced binary search tree (BST) of height no larger than log(N) + 1.
"""

"""
			8
		7
			6
	5
			4
		3
			∅
2
		∅
	3       0
		1   
            0
"""


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


def parse_tree(data):
    if isinstance(data, TreeNode):
        if data.left is None and data.right is None:
            return data.key
        return parse_tree(data.left), data.key, parse_tree(data.right)
    if data is None:
        return None


def display_keys(node: TreeNode, space="\t", level=0):
    # If the node is empty
    if node is None:
        print(space * level + '∅')
        return

        # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


def inorder_traverse_tree(node: TreeNode):
    if node is None:
        return []
    return inorder_traverse_tree(node.left) + [node.key] + inorder_traverse_tree(node.right)


def preorder_travers_tree(node: TreeNode):
    if node is None:
        return []
    return [node.key] + preorder_travers_tree(node.left) + preorder_travers_tree(node.right)


def postorder_traverse_tree(node: TreeNode):
    if node is None:
        return []
    return [node.key] + postorder_traverse_tree(node.right) + postorder_traverse_tree(node.left)


def tree_height(node: TreeNode):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node: TreeNode):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


class TreeNodeV2:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNodeV2.height(self.left), TreeNodeV2.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNodeV2.size(self.left) + TreeNodeV2.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNodeV2.traverse_in_order(self.left) +
                [self.key] +
                TreeNodeV2.traverse_in_order(self.right))

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return

            # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNodeV2.to_tuple(self.left), self.key, TreeNodeV2.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNodeV2.parse_tuple(data[0])
            node.right = TreeNodeV2.parse_tuple(data[2])
        else:
            node = TreeNodeV2(data)
        return node


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    return is_bst_node, min_key, max_key



if __name__ == "__main__":
    tree_node_0 = TreeNode(1)
    tree_node_1 = TreeNode(5)
    tree_node_2 = TreeNode(7)

    tree_node_0.left = tree_node_1
    tree_node_0.right = tree_node_2

    binary_tree = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    binary_tree_tuple = parse_tree(binary_tree)
    display_keys(node=binary_tree)
    inorder_traverse = inorder_traverse_tree(node=binary_tree)
    print(inorder_traverse)
    preorder_traverse = preorder_travers_tree(node=binary_tree)
    print(preorder_traverse)
    postorder_traverse = postorder_traverse_tree(node=binary_tree)
    print(postorder_traverse)
    tree_height = tree_height(node=binary_tree)
    print(tree_height)
    tree_size = tree_size(node=binary_tree)
    print(tree_size)
    x, y, z = is_bst(binary_tree)
    print(x, y, z)