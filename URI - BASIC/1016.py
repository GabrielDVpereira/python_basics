def calculateTime(car1Speed, car2Speed, distance):
  return 60*distance /(car2Speed - car1Speed)



car1Speed = 60
car2Speed = 90
distance = int(input())
print("{} minutos".format(round(calculateTime(car1Speed, car2Speed, distance))))