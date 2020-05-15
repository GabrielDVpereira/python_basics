from decimal import Decimal 
import math


def calculatePointsDistance(point1, point2):
  return round(Decimal(math.sqrt((point1["x"] - point2['x'])**2 +  (point1["y"] - point2['y'])**2)),4)


point1 = {
  "x": float(input()),
  "y": float(input())
}
point2 = {
  "x": float(input()),
  "y": float(input())
}

print(calculatePointsDistance(point1, point2))