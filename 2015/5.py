input = open('5.txt', 'r')


def niceStringDetector(input):
    total = 0
    for line in input:
        lastLetter = ''
        doubleLetters = False
        forbiddenLetters = False
        vowelCount = 0
        forbiddenLettersList = ["ab", "cd", "pq", "xy"]
        for letters in forbiddenLettersList:
            if letters in line:
                forbiddenLetters = True
        for letter in line:
            if letter in 'aeiou':
                vowelCount += 1
            if letter == lastLetter:
                doubleLetters = True
            lastLetter = letter
        if not forbiddenLetters and doubleLetters and vowelCount >= 3:
            total += 1
    print(total)
