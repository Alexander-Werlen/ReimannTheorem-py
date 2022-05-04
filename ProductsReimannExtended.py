import math
import matplotlib.pyplot as plt


def getValueOfItemByIndex(index):
    # Index of sumation starts at 0
    if (index % 2 == 0):
        p = 1 + index/2
        q = 2 + index/2
    else:
        p = 1 + math.ceil(index/2)
        q = math.ceil(index/2)
    return p/q


def main():

    lsIndiceTerminosUsados = []
    lsProdTracking = []
    currentIndiceMay = 0
    currentIndiceMen = 0

    iteraciones = 250
    #valorDeseado = math.log(2)
    valorDeseado = math.e

    currentProd = getValueOfItemByIndex(0)
    if (currentProd >= 1):
        currentIndiceMay += 1
    else:
        currentIndiceMen += 1

    for _ in range(iteraciones):
        if (currentProd <= valorDeseado):
            while True:
                newTermino = getValueOfItemByIndex(currentIndiceMay)
                currentIndiceMay += 1

                if (newTermino >= 1):
                    break

            currentProd *= newTermino
            lsIndiceTerminosUsados.append(currentIndiceMay-1)
            lsProdTracking.append(currentProd)
            # Sumo 0 para copiar por valor y no id. Debería de haber mejor forma de hacerlo

        else:
            while True:
                newTermino = getValueOfItemByIndex(currentIndiceMen)
                currentIndiceMen += 1

                if (newTermino < 1):
                    break

            currentProd *= newTermino
            lsIndiceTerminosUsados.append(currentIndiceMen-1)
            lsProdTracking.append(currentProd)

    plt.plot(range(len(lsIndiceTerminosUsados)), lsProdTracking)
    plt.axhline(y=valorDeseado, color='r', linestyle='-')
    plt.show()

    return


if __name__ == "__main__":
    main()
