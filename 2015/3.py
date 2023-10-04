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
