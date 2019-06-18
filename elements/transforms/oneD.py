def oneD(element, stiffnessMatrix):

    i = element.getNode1().id
    j = element.getNode2().id
    elementStiffness = element.getStiffness()

    stiffnessMatrix[i][i] += elementStiffness
    stiffnessMatrix[j][j] += elementStiffness

    stiffnessMatrix[i][j] -= elementStiffness
    stiffnessMatrix[j][i] -= elementStiffness