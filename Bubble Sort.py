
import random

# Python program for implementation of MergeSort
 
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
 
def merge1(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort1(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort1(arr, l, m)
        mergeSort1(arr, m+1, r)
        merge1(arr, l, m, r)
 

''' 2nd way '''
def mergeSort2(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort2(L)
 
        # Sorting the second half
        mergeSort2(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


 

def main():
    # Driver code to test above
    arr1 = [12, 11, 13, 5, 6, 7]
    n = len(arr1)
    print("Given array1 is")
    for i in range(n):
        print("%d" % arr1[i],end=" ")
     
    mergeSort1(arr1, 0, n-1)
    print("\n\nSorted array1 is")
    for i in range(n):
        print("%d" % arr1[i],end=" ")

    print("\n")

    # Driver code 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("Given array2 is", end="\n")
    printList(arr2)
    print("\n")
    mergeSort2(arr2)
    print("Sorted array2 is: ", end="\n")
    printList(arr2)
    print("\n")

    #Class code
    L = [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
    print("Given sort: " + str(L))
    #sort with Bubble sort

    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                #swap
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    print("Sorted Sort: " + str(L) + "\n")


    #random sort
    N = [1, 43, 17, 2, 10, 30, 23, 100, 8, 12, 0]
    print("Original List: " + str(N))
    while True:
        N = [1, 43, 17, 2, 10, 30, 23, 100, 8, 12, 0]
        M = []
        '''
        #create a list with a random arrangment of the elements in the previous
        for i in range(len(N) - 1):
            randomPos = randint(0, len(N) - 1)
            i = randomPos
            M.append(N[i])'''
        for i in range(len(N) - 1):
            M.append(random.choice(N))
            for i in M:
                if i in N:
                    N.remove(i)
                else:
                    continue
                
        print("New List: " + str(M))
        isSorted = True
        for i in range(len(M) - 1):
            if M[i] > M[i+1]:
                isSorted = False
                
        if isSorted == True:
            print("Sorted List " + str(M))
            break


if __name__=="__main__":
    main()
