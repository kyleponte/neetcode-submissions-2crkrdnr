class TreeNode:
    def __init__(self, key, val):
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
        curr = self.root

        while curr:
            if key > curr.key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            elif key < curr.key:
                if not curr.left:
                    curr.left = newNode
                    return 
                curr = curr.left
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        
        curr = self.root

        while curr:
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
            else:
                return curr.val
        
        return -1

    def getMin(self) -> int:
        minVal = self.findMin(self.root)
        if minVal:
            return minVal.val
        else:
            return -1

    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root

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
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minVal = self.findMin(root.right)
                root.key = minVal.key
                root.val = minVal.val
                root.right = self.removeHelper(root.right, minVal.key)
        return root

    def getInorderKeys(self) -> List[int]:
        res = []

        curr = self.root

        if not curr:
            return []
        
        def traverse(root):
            if root:
                traverse(root.left)
                nonlocal res
                res.append(root.key)
                traverse(root.right)
        
        traverse(curr)

        return res
