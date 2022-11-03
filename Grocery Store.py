class Grocery:

    def __init__(self, name):
        self.items = {"Fish Sauce": 4.00,
                      "Rice Paper": 2.50,
                      "Rice": 5.00,
                      "Cup Noodles": 1.50,
                      "Sriracha (Hot sauce)": 4.00,
                      "Kimchi": 2.50,
                      "Brocoli": 2.00,
                      "Chicken": 5.00,
                      "Beef": 6.50,
                      "Milk": 1.25,
                      "Dried Noodles": 3.50,
                      "Soy Sauce": 2.50,
                      "Frozen Dumpling": 8.00,
                      "Soup": 4.50,
                      "Sushi": 10.75}
        self.name = name
        self.totalPrice = 0
        self.orders = []

    def getName(self):
        return self.name

    def checkOut(self):
        for i in self.orders:
            self.totalPrice = self.totalPrice + self.items[i]

        return self.totalPrice

    def showMenu(self):
        return self.items

    def addOrder(self, new_order):
        if new_order in self.items:
            self.orders.append(str(new_order))


def main():
    store = Grocery("The Asian House")
    menu = list(store.showMenu().keys())
    price = list(store.showMenu().values())

    print("Welcome to " + str(store.getName()) + " grocery")
    print("Here is what we have here:")
    count = 0
    for i in range(len(menu)):
        count += 1
        print(str(count) + " " + menu[i] + " : " + str(price[i]) + "$")

    check_in = input("\nStill want to go in? Y or N \n")
    if check_in == "N":
        print("Good luck finding your things somewhere else")
    else:
        print("Welcome in")
        check_out = input("It is your turn to check out\nDo you take anything? Y or Nothing\n")
        if check_out == "Nothing":
            print("Bye then! have a good day")
        else:
            a = "a"
            while a == "a":
                order = input("\nWhat do you have? ")
                a = "a"
                if order in list(store.showMenu().keys()):
                    num = int(input("How many of them? "))
                    for i in range(num):
                        store.addOrder(order)
                    ques = "Y"
                    while ques == "Y":
                        ques = input("Anything else? Y or N ")
                        if ques == "Y":
                            next_order = input("\nWhat do you have? ")
                            if next_order in list(store.showMenu().keys()):
                                num = int(input("How many of them? "))
                                for i in range(num):
                                 store.addOrder(next_order)
                        elif ques == "N":
                            total = store.checkOut()
                            print("The total price is {} dollars. Thanks for coming.".format(total))
                            a = "b"
                            break

                else:
                    a = "b"
                    print("We don't have that. Please try again")


if __name__ == "__main__":
    main()
