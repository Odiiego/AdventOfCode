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