
import random

class animal:

    def __init__(self, n, t, c, s, h):
        self.name = n
        self.atype = t
        self.acolor = c
        self.aspeed = s
        self.habitat = h

    def getName(self):
        return self.name
    
    def setName(self,n):
        self.name = n

    def getSpeed(self):
        return self.aspeed
    
    def setSpeed(self,s):
        self.aspeed = s
        
    def getColor(self):
        return self.acolor

    def setColor(self, c):
        self.acolor = c
        
    def getType(self):
        return self.atype
    def setType(self, t):
        self.atype = t
    
    def getHabitat(self):
        return self.habitat

    def setHabitat(self, h):
        self.habitat = h

    
        


def main():
    speed = "speed: " + str(random.randint(20,25)) + " miles average"

    Fv = animal("Name: Joe", "Type: Golden Retriever","Color: Yellow", speed, "Habitat: Indoor/ House")
    Fv2 = animal("Name: Josh", "Type: Huskie","Color: White", speed, "Habitat: Indoor/ House")

    n = Fv.getName()
    t = Fv.getType()
    c = Fv.getColor()
    s = Fv.getSpeed()
    h = Fv.getHabitat()
    Dog = [n, t, c, s, h]
    
    n2 = Fv2.getName()
    t2 = Fv2.getType()
    c2 = Fv2.getColor()
    s2 = Fv2.getSpeed()
    h2 = Fv2.getHabitat()
    Dog2 = [n2, t2, c2, s2, h2]

    All = Dog + Dog2

    Animal = input("Dog1 or Dog2 or all? ")
    print("\n")
    if Animal == "Dog1":
        for i in Dog:
            print(i)
            if i == h:
                break
    elif Animal == "Dog2":
        for i in Dog2:
            print(i)
            if i == h2:
                break
    elif Animal == "all":
        for i in All:
            print(i)
            if i == h:
                print("\n")

        
    
   
if __name__ == "__main__":
    main()
