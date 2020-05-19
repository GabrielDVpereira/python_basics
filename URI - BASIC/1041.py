def calculateQuadrant(points):
  if(points[0] == 0 and points[1] ==0):
    print("Origem");
  elif(points[0] > 0 and points[1] > 0):
    print("Q1");
  elif(points[0] < 0 and points[1] >0):
    print('Q2')
  elif(points[0] > 0 and points[1] < 0):
    print('Q4')
  else: 
    print("Q3")

def convertToFloat(num):
  return float(num)


points = input().split()
points = list(map(convertToFloat, points));
calculateQuadrant(points)