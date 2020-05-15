from decimal import Decimal
def calculateSphereVol(radius):
  return 4/3*3.14159*radius**3;


radius = float(input()); 

print("VOLUME = {}".format(round(Decimal(calculateSphereVol(radius)),3)))