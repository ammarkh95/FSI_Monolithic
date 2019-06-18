from .Element import Element
from .transforms.zeroD import zeroD


class NodeElement(Element):

    def __init__(self, node, node1):
        self.node = node

    def getNode(self):
        return self.node

    def getNode1(self):
        pass

    def getNode2(self):
        pass

    def isPlotable(self):
        return False

    def getStiffness(self):
        '''
        Returns the stiffness of the element
        '''
        return 0

    def localStiffnessMatrix(self, dim, globalMatrix):
        '''
        Assembles the local stiffness matrix depending upon whether
        the problem is 1D, 2D, 3D

        dim             --->    dimension of the problem
        globalMatrix    --->    stiffness matrix
        '''
        zeroD(self, globalMatrix)