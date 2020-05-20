def calculateGameHours(hours):
  if(hours[0] >= hours[1]):
    return 24 - hours[0] + hours[1]
  else:
    return hours[1] - hours[0]

gameHours = [int(input()), int(input())];
print("O JOGO DUROU {} HORA(S)".format(calculateGameHours(gameHours)));