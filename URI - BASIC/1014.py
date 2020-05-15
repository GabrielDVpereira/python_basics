from decimal import Decimal

def calculateConsumption(distance, fuel):
  return round(Decimal(distance/fuel),3)


distance = int(input())
fuel = float(input())

print("{} km/l".format(calculateConsumption(distance, fuel)))