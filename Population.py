from Solution import Solution


class Population:
    def __init__(self, populationSize, boardWidth, boardHeight, points):
        self.populationSize = populationSize
        self.solutions = []
        for i in range(populationSize):
            self.solutions.append(Solution(points, boardWidth, boardHeight))
