class Node:

    #leftpointer : integer
    #data : interger
    #rightpointer : integer
    
    def __init__ (self, dataP):
        self.__data = dataP
        self.__leftpointer, self.__rightpointer = -1 ,-1

    def GetLeft(self):
        return self.__leftpointer

    def GetRight(self):
        return self.__rightpointer

    def GetData(self):
        return self.__data

    def SetLeft(self, left):
        self.__leftpointer = left

    def SetRight(self, right):
        self.__rightpointer = right

    def SetData(self, data):
        self.__data = data

g = Node(15)
g.SetData(10)
print(g.GetLeft())
print(g.GetData())
