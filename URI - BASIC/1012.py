from decimal import Decimal;

def calculateTriangleArea(points):
  return points[0]*points[2]/2
def calculateCircleArea(points):
  return 3.14159*points[2]**2
def calculateTrapeziumArea(points):
  return (points[0] + points[1])*points[2] / 2
def calculateSquareArea(points):
  return points[1]**2
def calculateRectangle(points):
  return points[0]*points[1]

points = []; 
count = 0; 

while count < 3: 
  points.append(float(input()));
  count+=1; 

print("TRIANGULO: {}".format(round(Decimal(calculateTriangleArea(points)), 3)))
print("CIRCULO: {}".format(round(Decimal(calculateCircleArea(points)), 3)))
print("TRAPEZIO: {}".format(round(Decimal(calculateTrapeziumArea(points)), 3)))
print("QUADRADO: {}".format(round(Decimal(calculateSquareArea(points)), 3)))
print("RETANGULO: {}".format(round(Decimal(calculateRectangle(points)), 3)))
