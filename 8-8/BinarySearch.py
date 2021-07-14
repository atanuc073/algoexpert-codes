# Binary Search


# #######1. Recursive Solution################

######### O(log(n)) time and O(log(n)) space Complexity

def binarySearch(array,target):
    return binarySearchHelper(array,target,left=0,right=len(array)-1)
    
def binarySearchHelper(array,target,left,right):
    if (left>right):
        return -1
    mid=(left+right)//2
    middleElement=array[mid]
    
    if(middleElement==target):
        return mid
    elif(middleElement>target):
        return binarySearchHelper(array,target,left,mid-1)
    else:
        return binarySearchHelper(array,target,mid+1,right)
        
######################   Iterative Solution      ######################

################## O(log(n)) time and O(1) space #########################
        
def binarySearchIterativeSol(array,target):
    left=0
    right=len(array)-1
    while(left<=right):
        mid=(left+right)//2
        middleElement=array[mid]
        if(middleElement==target):
            return mid
            
        elif(middleElement>target):
            right=mid-1
        else:
            left=mid+1
    return -1

        
        

        
        
array=[1,2,3,4,5,6,7,8,9,12,14]
target=7
print(binarySearchIterativeSol(array,target))
        
        