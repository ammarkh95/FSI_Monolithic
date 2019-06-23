from Domain import Domain
from CoupledDomain import CoupledDomain
from elements.transforms.oneD import oneD
from elements.Spring import Spring
from elements.NodeElement import NodeElement
from Plot import Plot

###########               Domains               ###########
#---------------------------------------------------------#
''' Structure '''
# Domain(transformationFunction, dofs per node)
structuralDomain = Domain(dim='1D')
''' Fuild '''
# fluidDomain = Domain()

###########                Nodes                 ###########
#----------------------------------------------------------#
''' Structure '''
structuralDomain.addNode(0)
structuralDomain.addNode(5)
structuralDomain.addNode(10)

''' Fluid '''
# fluidDomain.addNode(0, 0, 0)

###########               Elements               ###########
#----------------------------------------------------------#
'''
addElements(Element Type, Node1, Node2, Arguments of the element)
'''
structuralDomain.addElement(Spring, (0, 1), 10)
# structuralDomain.addElement(Spring, 1, 2, 20)
# structuralDomain.addElement(Spring, 0, 2, 30)
structuralDomain.addElement(NodeElement, (2,))

###########      Assemble Stiffness matrix       ###########
#----------------------------------------------------------#
structuralDomain.assembleStiffnessMatrix()

###########            Add Constraints           ###########
#----------------------------------------------------------#
structuralDomain.addConstraint(0, 0)
structuralDomain.addLoads(1, 10)
structuralDomain.addLoads(2, 10)

###########           Coupled Domain            ###########
#----------------------------------------------------------#
coupledDomain = CoupledDomain(structuralDomain)
coupledDomain.addCouplingCondition({1: 1, 2: -1}, 0)
print(coupledDomain.solve())

# Plot(structuralDomain)

###########           Post Processing            ###########
#----------------------------------------------------------#
# Plot(structuralDomain)
