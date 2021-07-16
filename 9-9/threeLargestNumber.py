def threeLargestNumber(array):
    threeLargest=[None,None,None]
    for num in array:
        if threeLargest[2] is None or threeLargest[2]<num:
            threeLargest[0]=threeLargest[1]
            threeLargest[1]=threeLargest[2]
            threeLargest[2]=num
            
        elif(threeLargest[1] is None or threeLargest[1]<num):
            threeLargest[0]=threeLargest[1]
            threeLargest[1]=num
        elif(threeLargest[0] is None or threeLargest[0]<num):
            threeLargest[0]=num
            
    return threeLargest
    
array=[1,21,34,433,456,765,23,78,788,1233,45,65,6555]
print(threeLargestNumber(array))

            
            
