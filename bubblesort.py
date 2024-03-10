
def bubblesort(A):
    n = len(A)
    for i in range(n):

        for j in range(i,n-1):
            if A[j] < A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
arr1 = bubblesort(arr)
print("Sorted array is:", arr1)