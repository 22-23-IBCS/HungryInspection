import random
class House:
    def __init__(self):
        self.rating=random.randint(1,10)
    def getRating(self):
        return self.rating

    def calcPath(self,m,l):
        sumP=0
        for i in range(0,len(l)):
            x=l[i][0]
            y=l[i][1]
            sumP=m[x][y]+sumP
        return sumP

    def calcMatrix(self,m):
        sumM=0
        for i in range(0,5):
            sumM=sumM+m[i][0]+m[i][1]+m[i][2]+m[i][3]+m[i][4]

        return sumM
        
        
    def randPath(self,m,num):
        
        self.p =[]
        counter=num
        while(len(self.p)<num):
            self.p=[]
            x=random.randint(0,4)
            y=random.randint(0,4)
            startingHouse = [x,y]
            self.p.append(startingHouse) #starting house
            counter=counter-1

            if(counter==0):
                return self.p
            
            for i in range(num-1):

                while True:

                    lastElem=len(self.p)-1

                    x=self.p[lastElem][0]
                    y=self.p[lastElem][1]

                    self.adjacent_houses=[]
                    
                    if (x+1<5):
                        if [x+1, y] in self.p:
                            q=" "
                        else: self.adjacent_houses.append([x+1, y])
                       
                    if (x-1>-1):
                        if [x-1, y] in self.p:
                            q=" "
                        else: self.adjacent_houses.append([x-1, y])

                    if(y+1<5):
                        if [x, y+1] in self.p:
                            q=" "
                        else: self.adjacent_houses.append([x, y+1])

                    if(y-1>-1):
                        if [x, y-1] in self.p:
                            q=" "
                        else: self.adjacent_houses.append([x, y-1])

                    if(len(self.adjacent_houses)>0 and counter>0):
                        self.p.append(self.adjacent_houses[random.randint(0,len(self.adjacent_houses)-1)])
                        counter=counter-1

                    
                        
    
                    elif(counter<1):
                        return self.p

                    elif(len(self.adjacent_houses)<=0):
                        return self.p
                    
'''
                    elif(len(self.adjacent_houses)<=0):
                        return self.p
                    '''           
        #return self.p                       
def main():

    m=[[],[],[],[],[]]
    for l in m:
        for i in range(5):
            h=House()
            l.append(h.getRating())
    for i in range(5):
        print(m[0][i],m[1][i],m[2][i],m[3][i],m[4][i])

    num=int(input ("How many houses? \n"))

    path=h.randPath(m,num)

    matrixAve=h.calcMatrix(m)/25

    pathAve= h.calcPath(m,path)/num

    print("path" ,path)

    if (len(path)==num and (pathAve > matrixAve)):
        print("path: ", path)
        print("Number of collected candies: ", h.calcPath(m,path))
        print("Your Average: ", h.calcPath(m,path)/num)
        print("Average generosity: ", matrixAve)
        print("successs")
        
    if(len(path) != num or pathAve < matrixAve):

        print("Your original path has problem. So here's a new one")

        while(True):
            path=h.randPath(m,num)

            if(len(path)==num and h.calcPath(m,path)/num>matrixAve):
                break
        print("path: ", path)
        print("Number of collected candies: ", h.calcPath(m,path))
        print("Your Average: ", h.calcPath(m,path)/num)
        print("Average generosity: ",matrixAve)
        print("successs")

if __name__=="__main__":
    main()
