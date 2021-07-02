class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
        
def BanchSum(node):
    sums=[]
    calculateBranchSums(node,0,sums)
    return sums
    
    
    
def calculateBranchSums(node,currentSum,sums):
    if node is None:
        return
    newcurrentSum=currentSum+node.value
    if(node.left is None and node.right is None):
        sums.append(newcurrentSum)
        return
    return calculateBranchSums(node.left,newcurrentSum,sums)
    return calculateBranchSums(node.right,newcurrentSum,sums)
    