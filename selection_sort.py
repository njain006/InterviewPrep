import unittest

def selection_sort( A ):

    for i in range(len(A)):
        #print(i)
        min_idx = i 
        for j in range(i+1,len(A)):
            if A[j]<A[min_idx]:
                min_idx = j
                
        #print(A)
        A[i],A[min_idx] = A[min_idx],A[i]


    return A
                 
# a = [85,5,5,5,6,78,3,2]
# sorted_array = selection_sort(a)
# print("Selection Sort  sorted array : ", sorted_array)

 

 

# Time Complexity  : 
# Space complexity :  
