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

def improvedNiceStringDetector(input):
    total = 0
    for string in input:
        repeatedPair = False
        splitRepeatition = False
        for n in range(len(string)):
            if n+2 < len(string) and string[n] != string[n+1] and string[n] == string[n+2]:
                splitRepeatition = True
            for i in range(n + 2, len(string)):
                    if string[n:n+2] == string[i:i+2]:
                        repeatedPair = True
        if repeatedPair and splitRepeatition:
            total += 1
    print(total)