from abc import ABC, abstractmethod
from math import sqrt, hypot

class Element(ABC):

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.length = self.getLength()
        super().__init__()

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node2

    def getLength(self):
        return sqrt((self.node1.x - self.node2.x)**2 + (self.node1.y - self.node2.y)**2)

    def isPlotable(self):
        return True

    @abstractmethod
    def getStiffness(self):
        pass

    @abstractmethod
    def localStiffnessMatrix(self, dim, globalMatrix):
        pass
