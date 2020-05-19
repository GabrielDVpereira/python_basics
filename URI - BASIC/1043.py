def isTriangle(points): 
  if(points[0] + points[1] > points[2] and abs(points[0] - points[1]) < points[2]):
    return True
  elif (points[0] + points[2] > points[1] and abs(points[0] - points[2]) < points[1]):
    return True
  elif (points[1] + points[2] > points[0] and abs(points[1] - points[2]) < points[0]):
    return True
  else: return False

def calculatePerimeter(points):
  return points[0] + points[1] + points[2];

def calculateArea(points):
  return ((points[0] + points[1])*points[2])/2;

def convertFloat(num): 
  return float(num)

points = input().split()
points = list(map(convertFloat, points)); 

if isTriangle(points): 
  print("Perimetro = {}".format(calculatePerimeter(points)))
else:
  print("Area = {}".format(calculateArea(points)))
