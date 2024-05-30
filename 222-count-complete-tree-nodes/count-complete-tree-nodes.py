#46.CountCompleteTreeNodes
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        r=self.countNodes(root.right)
        l=self.countNodes(root.left)
        return 1+r+l
         





        