class Character:

    #Name : String
    #XCoordinate : Integer
    #YCoordinate : Integer

    def __init__(self, Name, XCoordinate, YCoordinate):
        self.__Name = Name
        self.__XCoordinate = XCoordinate
        self.__YCoordinate = YCoordinate

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += XChange
        self.__YCoordinate += YChange

Characters = []
#file = "Characters.txt"

fn = "Characters.txt"
file = open(fn, "r")
arr = []
for x in file:
    print(x)
    arr.append(x)

try:
    File = open(file)
    for x in range(10):
        Name = File.readline().strip()
        X = File.readline().strip()
        Y = File.readline().strip()
        temp = Character(Name, int(X), int(Y))
        Characters.append(temp)
    File.close()
except:
    print("File not Found")

flag = False
count = -1
while flag == False:
    count = -1
    u_in = input("Enter Name: ").strip().lower()
    for x in Characters:
        name = x.GetName().strip().lower()
        print(name , u_in)
        if name == u_in:
            flag = True
            count += 1
            break
        else:
            count +=1

print(Characters[count].GetX(),Characters[count].GetY())

valid = False
while valid == False:
    direction = input("Enter Direction (W, A, S, D): ").strip().lower()
    if direction == "w":
        Characters[count].ChangePosition(0,1)
        valid = True
    elif direction == "a":
        Characters[count].ChangePosition(-1,0)
        valid = True
    elif direction == "s":
        Characters[count].ChangePosition(0,-1)
        valid = True
    elif direction == "d":
        Characters[count].ChangePosition(1,0)
        valid = True

print(Characters[count].GetX(),Characters[count].GetY())

#Qui has changed coordinates to X = 83 and Y = 0
print(Characters[count].GetName(),"has changed coordinates to X =",Characters[count].GetX(),"and Y =",Characters[count].GetY())
