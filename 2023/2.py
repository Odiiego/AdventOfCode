input = open("2.txt", "r")

def validGameSum(input):
  total = 0
  input = [ x.strip().split(": ")[1].split("; ") for x in input]

  for index, game in enumerate(input):
    sets = [set.split(", ") for set in game]
    validGame = True
    
    for set in sets:
      counter = {
        "red": 0,
        "green": 0,
        "blue": 0
      }

      for color in set:
        color = color.split(" ")
        counter[color[1]] += int(color[0])

      if counter["red"] > 12 or counter["green"] > 13 or counter["blue"] > 14:
        validGame = False
    total += index+1 if validGame else 0 
  print(total)


def checkMinimumSet(input):
  total = 0
  input = [ x.strip().split(": ")[1].split("; ") for x in input]

  for game in input:
    sets = [set.split(", ") for set in game]
    counter = {
      "red": 0,
      "green": 0,
      "blue": 0
    }

    for set in sets:
      for color in set:
        color = color.split(" ")
        counter[color[1]] = int(color[0]) if counter[color[1]] < int(color[0]) else counter[color[1]]
    
    total += counter["red"] * counter["green"] * counter["blue"]
  print(total)