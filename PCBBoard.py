from Population import Population


def loadData():
    settings = []
    file = open("zad0.txt", "r")

    lines = file.read().splitlines()
    for line in lines:
        settings.append(line.split(";"))

    file.close()
    return settings


def main():
    sett = loadData()
    boardWidth = int(sett[0][0])
    boardHeight = int(sett[0][1])
    points = []
    for i in range(1, len(sett)):
        points.append(([int(sett[i][0]), int(sett[i][1])], [int(sett[i][2]), int(sett[i][3])]))

    print(points)
    population = Population(1, boardWidth, boardHeight, points)



if __name__ == "__main__":
    main()