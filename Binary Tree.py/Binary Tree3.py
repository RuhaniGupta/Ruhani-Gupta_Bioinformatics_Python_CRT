'''
Employee Hierarchy Tree (Binary Tree)
-------------------------------------------
Context: A company stores employees in a reporting structure where each manager has two direct reports max.
--------------------------------------------------
Beginner-Friendly Tasks:
Build a binary tree where each node is an employee and children are subordinates.
Print all employee names in In-Order, Pre-Order, and Post-Order traversal.
Count how many employees are at the lowest level (leaf nodes).
Find the depth of the hierarchy (height of the tree).
Find the manager of a given employee by traversing the tree.
'''

class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.name, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.name, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.name, end=' ')

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

def find_manager(root, employee_name, parent=None):
    if root is None:
        return None
    if root.name == employee_name:
        return parent
    left = find_manager(root.left, employee_name, root)
    if left:
        return left
    return find_manager(root.right, employee_name, root)
root = EmployeeNode("CEO")
root.left = EmployeeNode("CTO")
root.right = EmployeeNode("CFO")
root.left.left = EmployeeNode("Dev1")
root.left.right = EmployeeNode("Dev2")
root.right.left = EmployeeNode("Acc1")
root.right.right = EmployeeNode("Acc2")

print("In-Order Traversal:")
inorder(root)
print("\nPre-Order Traversal:")
preorder(root)
print("\nPost-Order Traversal:")
postorder(root)

print(f"\n\nNumber of employees at the lowest level (leaf nodes): {count_leaves(root)}")
print(f"Depth of the hierarchy (height of the tree): {tree_height(root)}")

emp = "Dev2"
manager = find_manager(root, emp)
if manager:
    print(f"Manager of {emp}: {manager.name}")
else:
    print(f"{emp} is the root or not found.")