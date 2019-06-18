import matplotlib.pyplot as plt

def Plot(Structure):
    xArray = []
    yArray = []

    for i in Structure.elements:

        if i.isPlotable():
            xArray.append(i.getNode1().x)
            xArray.append(i.getNode2().x)

            yArray.append(i.getNode1().y)
            yArray.append(i.getNode2().y)

    plt.plot(xArray, yArray, '-ro')
    plt.gca().set_aspect('equal', 'datalim')
    plt.show()