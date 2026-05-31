# Binary Search Tree Node
class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if self.root is None:
            self.root = new_node
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = new_node
                    return None
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = new_node
                    return None
                curr = curr.right
            else:
                curr.val = val
                return None

    def get(self, key: int) -> int:
        if self.root is None:
            return -1
        
        curr = self.root

        while True:
            if key < curr.key:
                if curr.left is None:
                    return -1
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    return -1
                curr = curr.right
            else:
                return curr.val

    def getMin(self) -> int:
        if self.root is None:
            return -1
        
        curr = self.root

        while curr.left is not None:
            curr = curr.left
        
        return curr.val

    def getMax(self) -> int:
        if self.root is None:
            return -1
        
        curr = self.root

        while curr.right is not None:
            curr = curr.right
        
        return curr.val

    def findMin(self, curr: TreeNode) -> Optional[TreeNode]:

        while curr and curr.left:
            curr = curr.left
        
        return curr

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, curr: TreeNode, key: int) -> Optional[TreeNode]:
        if curr is None:
            return None
        
        if key < curr.key:
            curr.left = self.removeHelper(curr.left, key)

        elif key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        
        else:
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            else:
                minNode = self.findMin(curr.right)
                curr.val = minNode.val
                curr.key = minNode.key
                curr.right = self.removeHelper(curr.right, minNode.key)

        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inOrderHelper(self.root, res)
        return res

    def inOrderHelper(self, curr: TreeNode, res) -> None:
        if curr:
            self.inOrderHelper(curr.left, res)
            res.append(curr.key)
            self.inOrderHelper(curr.right, res)


