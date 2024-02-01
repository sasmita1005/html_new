from typing import List

class Node:
    def __init__(self, val: int, children: List['Node'] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    @staticmethod
    def createTree(input_list: List[int]) -> Node:
        if not input_list:
            return None

        root = Node(input_list[0])
        stack = [root]
        i = 1

        while i < len(input_list):
            current = stack[-1]
            if input_list[i] is not None:
                child = Node(input_list[i])
                current.children.append(child)
                stack.append(child)
            else:
                stack.pop()
            i += 1

        return root

    @staticmethod
    def traverseTree(root: Node) -> List[int]:
        result = []
        
        def postorder(node):
            nonlocal result
            if node:
                for child in node.children:
                    postorder(child)
                result.append(node.val)
        
        postorder(root)
        return result

# Example usage for Input Example I
input1 = [1, None, 3, 2, 4, None, 5, 6]
root1 = Solution.createTree(input1)
output1 = Solution.traverseTree(root1)
print("Input Example I Postorder Traversal:", output1)

# Example usage for Input Example II
input2 = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11,
                    None, 12, None, 13, None, None, 14]
root2 = Solution.createTree(input2)
output2 = Solution.traverseTree(root2)
print("Input Example II Postorder Traversal:", output2)
