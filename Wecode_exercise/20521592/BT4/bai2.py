class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    # def get_min(self):
    #     current = self
    #     while current.left is not None:
    #         current = current.left
    #     return current.val

    # def get_max(self):
    #     current = self
    #     while current.right is not None:
    #         current = current.right
    #     return current.val

    # def delete(self, val):
    #     if self == None:
    #         return self
    #     if val < self.val:
    #         if self.left:
    #             self.left = self.left.delete(val)
    #         return self
    #     if val > self.val:
    #         if self.right:
    #             self.right = self.right.delete(val)
    #         return self
    #     if self.right == None:
    #         return self.left
    #     if self.left == None:
    #         return self.right
    #     min_larger_node = self.right
    #     while min_larger_node.left:
    #         min_larger_node = min_larger_node.left
    #     self.val = min_larger_node.val
    #     self.right = self.right.delete(min_larger_node.val)
    #     return self

    # def exists(self, val):
    #     if val == self.val:
    #         return True

    #     if val < self.val:
    #         if self.left == None:
    #             return False
    #         return self.left.exists(val)

    #     if self.right == None:
    #         return False
    #     return self.right.exists(val)

    '''def preorder(self, vals):
        if self.val is not None:
             vals.append(self.val)
        if self.left is not None:
           self.left.preorder(vals)
        if self.right is not None:
           self.right.preorder(vals)
        return vals'''

    '''def inorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.inorder(vals)
        if self.right is not None:
            self.right.inorder(vals)
        return vals'''

    # def postorder(self, vals):
    #     if self.left is not None:
    #         self.left.postorder(vals)
    #     if self.right is not None:
    #         self.right.postorder(vals)
    #     if self.val is not None:
    #         vals.append(self.val)
    #     return vals
    def printLevelOrder(self):
        if(self is None):
            return
        queue = []
        queue.append(self)
        while(queue != []):
            print(queue[0].val, end = " ")
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            queue.pop(0)
'''def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)'''



def main():
    
    bst = BSTNode()
    
    while True: 
        num = int(input())
        if num == 0: 
            break
        else: 
            bst.insert(num)
    bst.printLevelOrder()
    # print("inorder:")
    #print(bst.inorder([]))
    # print("#")
    #print(getLeafCount(bst))

main()