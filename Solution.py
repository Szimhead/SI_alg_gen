import random

UP = [0, 1]
DOWN = [0, -1]
LEFT = [-1, 0]
RIGHT = [1, 0]


class Solution:
    def __init__(self, points, boardWidth, boardHeight):
        self.paths = []
        self.boardWidth = boardWidth
        self.boardHeight = boardHeight
        self.fillPaths(points)
        self.fitness = 0


    def fillPaths(self, points):
        betterDirectionProb = 0.8
        directions = [UP, DOWN, LEFT, RIGHT]
        maxLength = max(self.boardHeight, self.boardWidth)
        for pair in points:
            startPoint = pair[0]
            endPoint = pair[1]
            currentPoint = startPoint
            previousDirection = directions[random.randint(0, 3)]
            length = random.randint(1, maxLength)
            currentPoint = [currentPoint[0] + length * previousDirection[0],
                            currentPoint[1] + length * previousDirection[1]]
            path = [currentPoint]
            print("end point: " + str(endPoint))
            while currentPoint != endPoint:
                length = random.randint(1, maxLength)
                if random.randrange(0, 1) < betterDirectionProb:
                    direction = self.findBetterDirection(currentPoint, endPoint, directions, length)
                else:
                    dirIndex = (previousDirection + random.randint(2, 4) + (previousDirection % 2) * 2) % 4
                    direction = directions[dirIndex]
                currentPoint = [currentPoint[0] + length * previousDirection[0],
                                currentPoint[1] + length * previousDirection[1]]
                #print("direction: " + str(direction) + "\tcurrent point: " + str(currentPoint))
                path.append(currentPoint)
                previousDirection = direction
            print(len(path))

    def findBetterDirection(self, current, end, directions, length):
        minDistance = self.calculateDistance(current, end)
        bestDir = directions[0]
        for direction in directions:
            nextPoint = [current[0] + length * direction[0],
                         current[1] + length * direction[1]]
            distance = self.calculateDistance(nextPoint, end)
            if distance < minDistance:
                minDistance = distance
                bestDir = direction
        return bestDir

    def calculateDistance(self, nextPoint, end):
        return abs(nextPoint[0] - end[0]) + abs(nextPoint[1] - end[1])
