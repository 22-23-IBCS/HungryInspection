import random

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def getName(self):
        return self.name

    def getSuit(self):
        return self.suit

    def getCard(self):
        return [self.suit, self.name]

class Deck:

    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for s in suits:
            for i in range(1, 14):
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)

                C = Card(s, name)
                self.cards.append(C)

    def getCards(self):
        return self.cards

    def dealCard(self):
        newCard = random.choice(self.cards)
        self.cards.remove(newCard)
        return newCard

def calcHandValue(hand):
    total = 0
    for h in hand:
        name = h[1]
        if name == "Ace":
            total = total + 11
            if total > 21:
                total = total - 10
        elif name == "King" or name == "Queen" or name == "Jack" :
            total = total + 10
        else:
            total = total + int(name)
        
    return total
        

def main():

    print("Welcome to Blackjack!\n") 

    D = Deck()

    userHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    dealerHand = [D.dealCard().getCard(), D.dealCard().getCard()]

    print("Dealer hand:")
    print(dealerHand)
    print("")
    print(userHand)
    print("Your hand's value is :" + str(calcHandValue(userHand)))
    print("")

    while True:
        option = input("Type 1: Hit  or 2: Stand\n")
        if option == "1":
            userHand.append(D.dealCard().getCard())
        else:
            break
        print("")
        print(userHand)
        print("Your hand's value is :" + str(calcHandValue(userHand)))
        print("")

    print("")
    print("Dealer hand:")
    print(dealerHand)
    print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
    print("")
    
    while True:
        if calcHandValue(dealerHand) < 17:
            print("Dealer hits!\n")
            dealerHand.append(D.dealCard().getCard())
            print("Dealer hand:")
            print(dealerHand)
            print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
            print("")
        else:
            print("Dealer stands!\n")
            break
        if calcHandValue(dealerHand) > 21:
            print("Dealer bust!")
            break
        
        
        
        

if __name__ == "__main__":
    main()
