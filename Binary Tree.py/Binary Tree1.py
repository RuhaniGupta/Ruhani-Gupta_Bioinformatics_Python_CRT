'''Binary Tree
A genetic tree with at most two child nodes for each parent node is called a binary tree.
A binary tree is made of nodes that contribute a left pointer, A right pointer, and a data element.The root
pointer is the topmost node in the tree.
The left and right pointers recursively point to smaller subtrees on either side.
An empty tree is also a valid binary tree.
A formal definition is: A binary tree is either empty or is made of a single node, where the left and 
right pointers(point recursively) to binary trees.'''

'''Types of Binary trees
Full binary tree: A binary tree in which every node has 0 or 2 children is termed as a full binary tree.

Complete binary tree: A complete binary tree has all the levels filled except for the last level,which has all
its nodes as much as to the left.

Perfect binary tree: A binary tree is termed perfect when all its internal nodes have two children along with
the leaf nodes there are at the same level '''

'''A Degenerate binary tree : In a degenerate tree,each internal node has only one child.The tree shown above 
is degenerate.These trees are very similar to Linked_lists.'''

'''Balanced binary tree: A binary tree in which the difference between the depth of the two subtrees of 
every node is at most one is called as balanced binary tree.'''

'''Binary tree representation
 Basic Operations 
 Inserting an element into a tree.
 Deleting an element from a tree.
 Searching fro an element.
 Traversing the tree.
 
 Auxillary Operations
 Finding the size of the tree
 Finding the height of the tree.
 Finding the level which has the maximum sum and many more.
 '''

'''Binary tree traversal
Preorder traversal : Root -> left -> right
Postorder traversal : Left -> right -> root
Inorder traversal : Left -> root -> right
'''

''''''  
#                        1
#                       /  \ 
#                     2    3
#                    / \    / \
#                   4   5   6  7    

#Preorder traversal : 1,2,4,5,3,6,7
#Postorder traversal : 4,5,2,6,7,3,1
#Inorder  : 4,2,5,1,6,3,7




