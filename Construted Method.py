
class Vehicle:
    
    #constructure method. Needed to define how
    #the class instances are created
    def __init__(self, b, c):
        self.numWheels = 4
        self.brand = b
        self.col = c

    def getBrand(self):
        return self.brand

    def setBrand(self,b):
        self.brand = b


    def getCol(self):
        return self.col
    
    def setCol(self, c):
        self.col = c







def main():

    veh1 = Vehicle("Mama", "red")
    b = veh1.getBrand()
    print(b)

    veh1.setBrand("Honda")
    print(veh1.getBrand())

    veh1.setCol("Blue")
    print(veh1.getCol())

if __name__ == "__main__":
    main()
