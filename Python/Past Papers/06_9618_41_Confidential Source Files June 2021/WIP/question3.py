class TreasureChest:
    def __init__(self, questionP, answerP, pointsP):
        self.__question =  questionP
        self.__answer = answerP
        self.__points = pointsP

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answer_u):
        if answer_u == self.__answer: #using ansu
            return True
        else:
            return False

    def getPoints(self, no_of_attempts):
        if no_of_attempts == 1:
            return self.__points
        elif no_of_attempts == 2:
            return (self.__points//2)
        elif no_of_attempts == 3 or no_of_attempts == 4:
            return (self.__points//4)
        else:
            return 0
        
arrayTreasure = []

def readData():
    try:
        file = open("TreasureChestData.txt")
        count = 0
        for x in range(5):
            question = file.readline().strip()
            answer = file.readline().strip()
            points = int(file.readline().strip())
            #print(question, answer, points)
            tc = TreasureChest(question,answer,points)
            #print(tc.getQuestion())
            arrayTreasure.append(tc)
    except IOError:
        print("Could not find file")

readData()
attempts, correct = 0, False
question = int(input("Enter a question no (1-5): ")) -1
if question+1 > 0 and question+1 < 6:
    print(arrayTreasure[question].getQuestion())    
    while not correct:
        answer = input("Enter an answer: ")
        correct = arrayTreasure[question].checkAnswer(answer)
        attempts += 1
    g = arrayTreasure[question].getPoints(attempts)
    print(g)
