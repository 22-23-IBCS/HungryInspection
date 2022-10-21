import random

#1: Return True if a list of intergers contain 2 consecutive 7's. Otherwise return False
def check1(x):
        idx = x.index(7)
        if x[idx+1] == 7:
            print("True")
        else:
            print("False")


#forfun
def isprime(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, num):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

#2:
def check2(x):
        5prime = [2, 3, 5, 7, 9]
        x = []
        for i in x:
                if i == 5prime:
                        x.remove(i)
                for i in x:
                        for m in range(2, int(x[-1])+1):
                                if i % m == 0:
                                        x.remove(i)
                                else:
                                        
                
      

   


def main():
    #pro1:
    x1 = [1, 2, 3, 9, 5, 7, 10, 7, 7]
    check1(x1)

    #pro2:
    print("pro2")
    num = 37
    check2(num)

    
   
if __name__ == "__main__":
    main()
