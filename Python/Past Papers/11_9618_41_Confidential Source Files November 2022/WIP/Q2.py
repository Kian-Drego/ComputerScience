class Card:
    def __init__(self, Number, Colour):
        #Number : INTEGER
        #Colour : STRING
        self.__num = Number
        self.__colour = Colour

    def GetNumber(self):
        return self.__num
    
    def GetColour(self):
        return self.__colour

onered = Card(1, "red")
twored = Card(2, "red")
threered = Card(3, "red")
fourred = Card(4, "red")
fivered = Card(5, "red")
oneblue = Card(1, "blue")
twoblue = Card(2, "blue")
threeblue = Card(3, "blue")
fourblue = Card(4, "blue")
fiveblue = Card(5, "blue")
oneyellow = Card(1, "yellow")
twoyellow = Card(2, "yellow")
threeyellow = Card(3, "yellow")
fouryellow = Card(4, "yellow")
fiveyellow = Card(5, "yellow")

class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__cards = []
        self.__FirstCard = 0
        self.__NumberCards = 5 
        self.__cards.append(Card1)
        self.__cards.append(Card2)
        self.__cards.append(Card3)
        self.__cards.append(Card4)
        self.__cards.append(Card5)

    def GetCard(self, index):
        return self.__cards[index]

Player1 = Hand(onered, twored, threered, fourred, oneyellow)
Player2 = Hand(twoyellow, threeyellow, fouryellow, fiveyellow, oneblue)

def CalculateValue(player):
    Score = 0
    for x in range(5):
        playercard = player.GetCard(x)
        Colour = playercard.GetColour()
        Score += playercard.GetNumber()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score

Player1Score = CalculateValue(Player1)
Player2Score = CalculateValue(Player2)
if Player1Score > Player2Score:
    print("Player 1 wins.")
elif Player1Score < Player2Score:
    print("Player 2 wins.")
else:
    print("It is a draw.") 
