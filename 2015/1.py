input = open("1.txt", "r")


def floorCode(input):
    count = 0
    for data in input:
        for char in data:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
        print(count)
        return count


def secondFloorCode(input):
    count = 0
    for data in input:
        for n, char in enumerate(data):
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
                if count == -1:
                    print(n+1)
                    return(n+1)


secondFloorCode(input)
