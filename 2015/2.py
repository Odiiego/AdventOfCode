input = open("2.txt", "r")


def wrappingPaperCalculator(input):
    total = 0
    for i in input:
        box = [int(x) for x in i.strip().split('x')]
        wrappingPaperSize = [(box[0] * box[1]),
                             (box[1] * box[2]), (box[2] * box[0])]
        total += (sum(wrappingPaperSize)*2 + min(wrappingPaperSize))
    print(total)


def ribbonCalculator(input):
    total = 0
    for i in input:
        box = sorted([int(x) for x in i.strip().split('x')])
        total += (box[0] * 2 + box[1] * 2 + box[0] * box[1] * box[2])
    print(total)
