class Solution:
    def isBinaryTreeValid(self, current, leftChild, rightChild, visited):
        # Check left child
        if leftChild[current] != -1:
            if visited[leftChild[current]]:  # Check for cycle
                return False

            visited[leftChild[current]] = True  # Mark left child as visited
            if not self.isBinaryTreeValid(leftChild[current], leftChild, rightChild, visited):
                return False

        # Check right child
        if rightChild[current] != -1:
            if visited[rightChild[current]]:  # Check for cycle
                return False

            visited[rightChild[current]] = True  # Mark right child as visited
            if not self.isBinaryTreeValid(rightChild[current], leftChild, rightChild, visited):
                return False

        return True

    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        childCount = [False] * n  # Tracks child count for each node

        # Update child count based on leftChild
        for child in leftChild:
            # Check if node has child
            if child != -1:
                childCount[child] = True  # Mark left child as having a parent

        # Update child count based on rightChild
        for child in rightChild:
            # Check if node has child
            if child != -1:
                if childCount[child]:  # Check if the right child already has a parent
                    return False

                childCount[child] = True  # Mark right child as having a parent

        root = -1  # Root node
        for i in range(n):
            if not childCount[i]:
                if root == -1:
                    root = i  # Set root node if not assigned
                else:
                    return False  # Multiple roots found, not a valid binary tree

        if root == -1:
            return False  # No root found, not a valid binary tree

        visited = [False] * n  # Tracks visited nodes
        visited[root] = True
        if not self.isBinaryTreeValid(root, leftChild, rightChild, visited):  # Check if the tree is valid
            return False

        # Check if there is multiple components
        for visit in visited:
            if not visit:
                return False

        return True  # All nodes form a valid binary tree