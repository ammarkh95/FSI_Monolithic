from Domain import Domain
from CoupledDomain2 import CoupledDomain
from elements.transforms.oneD import oneD
from elements.Spring import Spring
from elements.NodeElement import NodeElement
from solvers.Newmark import Newmark

import matplotlib.pyplot as plt

###########               Domains               ###########
#---------------------------------------------------------#
''' Structure '''
# Domain(transformationFunction, dofs per node)
structuralDomain = Domain(dim='1D')
''' Fuild '''
fluidDomain = Domain(dim='1D')

###########                Nodes                 ###########
#----------------------------------------------------------#
''' Structure '''
structuralDomain.addNode(x=0, y=0)
structuralDomain.addNode(x=5, y=0, mass=0.5)
''' Fluid '''
fluidDomain.addNode(x=5, y=1, mass=0.5)

###########               Elements               ###########
#----------------------------------------------------------#
'''
addElements(Element Type, Node1, Node2, Arguments of the element)
'''
# Structure
structuralDomain.addElement(Spring, (0, 1), 1)
# Fluid
fluidDomain.addElement(NodeElement, (0,)) # Dummy element (mass)

###########      Assemble Stiffness matrix       ###########
#----------------------------------------------------------#
# Any changes to stifffness after this are not registered
structuralDomain.assembleStiffnessMatrix()
fluidDomain.assembleStiffnessMatrix()

###########            Add Constraints           ###########
#----------------------------------------------------------#
structuralDomain.addConstraint(0, 0)
structuralDomain.addLoads(1, 0.1)

###########           Coupled Domain            ###########
#----------------------------------------------------------#
coupledDomain = CoupledDomain(structuralDomain, fluidDomain)
# coupledDomain.addPhysics(gravity=-9.81)
coupledDomain.addCouplingCondition({1: 1, 2: -1}, 0)
coupledDomain.addDamping({2: 0.02})

# Newmark(finalTime, dt, beta, gamma, is_K_Matrix_Constant)
coupledDomain.Solve(Newmark, 500, .1, 1/4, 1/2, True)

plt.plot(coupledDomain.solver.time, coupledDomain.solver.history[0])
# plt.plot(coupledDomain.solver.time, coupledDomain.solver.history[1])
# plt.plot(coupledDomain.solver.history[1])
plt.show()
# Plot(structuralDomain)

###########           Post Processing            ###########
#----------------------------------------------------------#
# Plot(structuralDomain)
