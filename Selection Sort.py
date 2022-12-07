import random
import time

def selectionSort(L, size):
    for i in range(len(L) - 1):
        min_ind = i
        
        # select the minimum element in every iteration 
        for j in range(i + 1, size):
            if L[j] < L[min_ind]:
                min_ind = j
        # swapping the elements to sort the array
        (L[i], L[min_ind]) = (L[min_ind], L[i])
 
def main():

    L = []
    n = random.randint(0, 20)
    for i in range(n):
        L.append(random.randint(0, n))

    # first selection sort
    print("Original List :" + str(L))
    start = time.time()
    selectionSort(L, n)
    stop = time.time()
    print("Selection Sort :" + str(L))
    print("For " + str(n) + " elements...")
    print("Time passed :" + str(stop - start) + "\n")

    #class selection sort

    start1 = time.time()
    for i in range(len(L) - 1):
        curlMin = L[i]
        indMin = i
        for j in range(i, len(L)):
            if L[j] < curlMin:
                curMin = L[j]
                indMin = j

        #swap
        temp = L[i]
        L[i] = L[indMin]
        L[indMin] = temp

    stop1 = time.time()
    print("Selection Sort(class) :" + str(L))
    print("For " + str(n) + " elements...")
    print("Time passed :" + str(stop1 - start1))

if __name__=="__main__":
    main()

   
    
              
