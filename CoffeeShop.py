class Coffeeshop:

    def __init__(self):
        self.items = {"Cafe Americano":2.5, "Cafe Latte":3.0, "Cappuccino":3.5,
                      "Frappucino":4.5, "Caramel Macchiato":4.25,
                      "Iced Coffee":3.0, "Hot Coffee":3.25, "Bagel":1.5, "Egg Benedict":6.5}
        self.totalPrice = 0
        self.info = "The cofee shop is founded by two students from Annie Wright school \nand is rated the #1 coffee shop in the world by Forbes 2022\nwith the cheapeast price."
        self.orders = []
        
    def calcPrice(self):
        for i in self.orders:
            self.totalPrice = self.totalPrice + self.items[i]

        return self.totalPrice

    def showMenu(self):
        return self.items

    def addOrder(self,new_order):                
        if new_order in self.items:
            self.orders.append(str(new_order))
        else:
            print("We do not have that.")
    
    def getinfo(self):
        return self.info
    
            

def main():

    JT = Coffeeshop()
    menu = list(JT.showMenu().keys())
    price = list(JT.showMenu().values())
    
    orders = input("Welcome to JT's coffee shop! What do you want to do?\n1 to see the menu, 2 to see the information about the shop \n")
    if orders == "1":
        print("Here is the menu")
        count = 0
        for i in range(len(menu)):
                count += 1
                print(str(count) + " " + menu[i] + " : " + str(price[i]) + "$")
    elif orders == "2":
        print(JT.getinfo())
        print("\nLet's order now you must be hungry.")
        count = 0
        for i in range(len(menu)):
            count += 1
            print(str(count) + " " + menu[i] + " : " + str(price[i]) + "$")
        
        


    more = "Y"
    while more != "N":
        more = input("\nDo you want to order something (one each time)? Y or N\n")
        if more == "Y":
            order = input("\nWhat do you want me to add? ")
            if order in list(JT.showMenu().keys()):
                num = int(input("How many of them? "))
                for i in range(num):
                    JT.addOrder(order)
            else:
                print("Sorry. We do not have that menu. Please try again.")
        elif more == "N":
            print("We will have your order.")
        else:
            print("Undefined command. Try again.")


    total = JT.calcPrice()
    print(JT)
    print("The total price is {} dollars. Thanks for coming. \nDon't forget to rate us 5 stars.".format(total))
    
        






if __name__ == "__main__":
    main()
