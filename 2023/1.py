import re
input = open('1.txt', 'r')

def improvedCalibration(input):
  total = 0

  for line in input:
    firstDigit = False
    lastDigit = False

    for n in range(0, len(line)):
      firstDigit = line[n] if not firstDigit and re.search("\d", line[n]) else firstDigit
      lastDigit = line[(len(line)-1) - n] if not lastDigit and re.search("\d", line[(len(line)-1) - n]) else lastDigit

      if firstDigit and lastDigit:
        total += int(firstDigit + lastDigit)
        break
  print(total)


def reallyImprovedCalibration(input):
  total = 0
  numList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

  for line in input:
    firstDigit = {
      "digit": None,
      "position": len(line)
    }
    lastDigit = {
      "digit": None,
      "position": -1
    }

    for index, num in enumerate(numList):
      if firstDigit["position"] > line.find(num) and line.find(num) >= 0:
        firstDigit = {
          "digit": str(index % 10),
          "position": line.find(num)
        }

      if lastDigit["position"] < line.rfind(num):
        lastDigit = {
          "digit": str(index % 10),
          "position": line.rfind(num)
        }
    
    total += int(firstDigit["digit"] + lastDigit["digit"])
  print(f"total: {total}")