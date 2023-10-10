input = open('3.txt', 'r')


def santaTracker(input):
    total = 1
    path = [[0, 0]]
    actualAdress = [0, 0]
    for track in input:
        for house in track:
            if house == "^":
                actualAdress = [actualAdress[0], actualAdress[1]+1]
            elif house == "v":
                actualAdress = [actualAdress[0], actualAdress[1]-1]
            elif house == "<":
                actualAdress = [actualAdress[0]-1, actualAdress[1]]
            elif house == ">":
                actualAdress = [actualAdress[0]+1, actualAdress[1]]
            if actualAdress not in path:
                total += 1
                path.append(actualAdress)
    print(total)


def santaAndRobotTracker(input):
    total = 1
    path = [[0, 0]]
    santaActualAdress = [0, 0]
    robotActualAdress = [0, 0]
    for track in input:
        for n, house in enumerate(track):
            if n % 2 == 0:
                if house == "^":
                    santaActualAdress = [
                        santaActualAdress[0], santaActualAdress[1]+1]
                elif house == "v":
                    santaActualAdress = [
                        santaActualAdress[0], santaActualAdress[1]-1]
                elif house == "<":
                    santaActualAdress = [
                        santaActualAdress[0]-1, santaActualAdress[1]]
                elif house == ">":
                    santaActualAdress = [
                        santaActualAdress[0]+1, santaActualAdress[1]]
                if santaActualAdress not in path:
                    total += 1
                    path.append(santaActualAdress)
            else:
                if house == "^":
                    robotActualAdress = [
                        robotActualAdress[0], robotActualAdress[1]+1]
                elif house == "v":
                    robotActualAdress = [
                        robotActualAdress[0], robotActualAdress[1]-1]
                elif house == "<":
                    robotActualAdress = [
                        robotActualAdress[0]-1, robotActualAdress[1]]
                elif house == ">":
                    robotActualAdress = [
                        robotActualAdress[0]+1, robotActualAdress[1]]
                if robotActualAdress not in path:
                    total += 1
                    path.append(robotActualAdress)
        print(total)
