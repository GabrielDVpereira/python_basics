def calculateArea(radius):
  pi = 3.14159;
  area = pi*radius**2;
  return area;


radius = float(input()); 
area = calculateArea(radius)
print("A = {}".format(area))
