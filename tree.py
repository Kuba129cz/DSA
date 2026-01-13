class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add_value(self, val: int):
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root

        while True:
            if val < current.val:
                if current.left is None:
                    current.left = Node(val)
                    return
                current = current.left
            elif val > current.val:
                if current.right is None:
                    current.right = Node(val)
                    return
                current = current.right
            else:
                return  
    
    def traversal_preorder(self, root):
        if root is None:
            return

        print(root.val, end=',')
        self.traversal_preorder(root.left)
        self.traversal_preorder(root.right)

    def traversal_inorder(self, root, array):
        if root is None:
            return

        self.traversal_inorder(root.left, array)
        array.append(root.val)
        self.traversal_inorder(root.right, array)

    def array_to_min_heap(self, values):
        if not values:
            return None 

        nodes = [Node(v) for v in values]
        
        for i in range(len(nodes)):
            left = 2*i + 1
            right = 2*i + 2

            if left < len(nodes):
                nodes[i].left = nodes[left]
            if right < len(nodes):
                nodes[i].right = nodes[right]
        
        return nodes[0]




