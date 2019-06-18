from .Element import Element

class Spring(Element):

    def __init__(self, Node1, Node2, stiffness):
        super().__init__(Node1, Node2)
        self.stiffness = stiffness

    def getStiffness(self):
        '''
        Returns the stiffness of the element
        '''
        return self.stiffness

    def localStiffnessMatrix(self, dim, globalMatrix):
        '''
        Assembles the local stiffness matrix depending upon whether
        the problem is 1D, 2D, 3D

        dim             --->    dimension of the problem
        globalMatrix    --->    stiffness matrix
        '''
        dim(self, globalMatrix)