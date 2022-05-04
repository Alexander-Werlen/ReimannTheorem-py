from math import log
import matplotlib.pyplot as plt


def getValueOfItemByIndex(lastUsedIndex):
    # Index of sumation starts at 0
    return pow(-1, lastUsedIndex)*(1/(lastUsedIndex+1))


def main():

    lsIndiceTerminosUsados = []
    currentSum = 0
    lsSumTracking = []
    currentIndicePos = 0
    currentIndiceNeg = 0

    iteraciones = 100
    #valorDeseado = log(2)
    valorDeseado = 1.5

    for _ in range(iteraciones):
        if (currentSum <= valorDeseado):
            while True:
                newTermino = getValueOfItemByIndex(currentIndicePos)
                currentIndicePos += 1

                if (newTermino >= 0):
                    break

            currentSum += newTermino
            lsIndiceTerminosUsados.append(currentIndicePos-1)
            lsSumTracking.append(currentSum)

        else:
            while True:

                newTermino = getValueOfItemByIndex(currentIndiceNeg)
                currentIndiceNeg += 1

                if (newTermino < 0):
                    break

            currentSum += newTermino
            lsIndiceTerminosUsados.append(currentIndiceNeg-1)
            lsSumTracking.append(currentSum)

    plt.plot(range(len(lsIndiceTerminosUsados)), lsSumTracking)
    plt.axhline(y=valorDeseado, color='r', linestyle='-')
    plt.show()

    return


if __name__ == "__main__":
    main()
