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


floorCode(input)
