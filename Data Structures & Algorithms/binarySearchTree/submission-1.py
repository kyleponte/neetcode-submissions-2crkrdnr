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
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return
        
        current = self.root
        
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return

    def get(self, key: int) -> int:
    
        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:

        curr = self.findMin(self.root)
        return curr.val if curr else -1

    def getMax(self) -> int:

        curr = self.root

        while curr and curr.right:
            curr = curr.right
        if curr:
            return curr.val
        else:
            return -1


    def remove(self, key: int) -> None:

        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, root, key):
        if not root: 
            return None
        
        if key > root.key:
            root.right = self.removeHelper(root.right, key)
        elif key < root.key:
            root.left = self.removeHelper(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal = self.findMin(root.right)
                root.key = minVal.key
                root.val = minVal.val
                root.right = self.removeHelper(root.right, minVal.key)
        return root

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root

    def getInorderKeys(self) -> List[int]:
        result = []
        
        self.inorderTraversal(self.root, result)

        return result
        
    def inorderTraversal(self, root, result: List[int]) -> None:
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
        

