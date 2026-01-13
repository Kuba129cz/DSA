from tree import Tree

tree = Tree()
tree.add_value(50)
tree.add_value(10)
tree.add_value(20)
tree.add_value(15)
tree.add_value(1)
tree.add_value(22)
tree.add_value(14)
tree.add_value(12)

tree.traversal_preorder(tree.root)
print()
values = []
tree.traversal_inorder(tree.root, values)
values.sort()
print(values)

heap_root = tree.array_to_min_heap(values)



