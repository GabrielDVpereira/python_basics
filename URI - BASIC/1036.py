import math; 
from decimal import Decimal; 

def delta(points): 
  return points[1]**2-(4*points[0]*points[2])

def calculateBhaskara(points):
  deltaResponse = delta(points);
  responses = [];

  if(deltaResponse < 0): return response;

  responses.append((-points[1] - math.sqrt(deltaResponse))/(2*points[0]));
  responses.append((-points[1] + math.sqrt(deltaResponse))/(2*points[0]));
  return responses
  


points = []; 
count = 0;

while count < 3: 
  points.append(float(input())); 
  count+=1

print(points)
responses = calculateBhaskara(points);

if(len(responses) == 0):
  print('Impossivel calcular')
else: 
  for index in range(len(responses)):
    print('R{} = {}'.format(index+1, responses[index]))