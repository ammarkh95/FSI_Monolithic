from Matrix import Matrix
from Vector import Vector

class CoupledDomain:

    def __init__(self, *domains):
        self.domainList = list(domains)

        self.size = sum([len(i.nodes) for i in self.domainList])
        self.totalConstraints = sum([len(i.constraintList) for i in self.domainList])

        self.stiffnessMatrix = Matrix(self.size)
        self.displacementVector = Vector(self.size)
        self.loadVector = Vector(self.size)

        self.__assembleStiffnessMatrix__()
        self.__assembleDisplacementVector__()
        self.__assembleLoadVector__()

    def __assembleStiffnessMatrix__(self):
        startPos = 0

        for domain in self.domainList:

            domainSize = len(domain.nodes)

            for i in range(domainSize):
                for j in range(domainSize):
                    self.stiffnessMatrix[i + startPos][j + startPos] = domain.stiffnessMatrix[i][j]
            
            startPos += domainSize

    def __assembleDisplacementVector__(self):
        startPos = 0

        for domain in self.domainList:

            domainSize = len(domain.nodes)

            for key, val in domain.constraintList.items():
                self.displacementVector[key + startPos] = val

            startPos += domainSize

    def __assembleLoadVector__(self):
        startPos = 0

        for domain in self.domainList:

            domainSize = len(domain.nodes)

            for key, val in domain.loadList.items():
                self.loadVector[key + startPos] = val

            startPos += domainSize

    def solve(self):
        LHS = Matrix(self.totalConstraints)
        
        