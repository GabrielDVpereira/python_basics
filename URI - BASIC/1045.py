import math;

def triangleTypes(triangleSides):
  possibleTypes = [];
  if(triangleSides[0] >= (triangleSides[1] + triangleSides[2])):
    possibleTypes.append("NAO FORMA TRIANGULO")
    return possibleTypes;
  if(triangleSides[0]**2 == (triangleSides[1]**2 + triangleSides[2]**2)):
    possibleTypes.append("TRIANGULO RETANGULO")
  if(triangleSides[0]**2 > (triangleSides[1]**2 + triangleSides[2]**2)):
    possibleTypes.append("TRIANGULO OBTUSANGULO")
  if(triangleSides[0]**2 < (triangleSides[1]**2 + triangleSides[2]**2)):
    possibleTypes.append("TRIANGULO ACUTANGULO")
  if(triangleSides[0] == triangleSides[1] and triangleSides[1] == triangleSides[2]): 
    possibleTypes.append("TRIANGULO EQUILATERO")
  elif(triangleSides[0] == triangleSides[1] or triangleSides[1] == triangleSides[2] or triangleSides[0] == triangleSides[2]): 
    possibleTypes.append("TRIANGULO ISOSCELES")
  
  return possibleTypes

def sort(triangleSides): 
  for i in range(len(triangleSides)):
    greater_index = i; 
    for j in range(i+1, len(triangleSides)):
      if(triangleSides[greater_index] < triangleSides[j]):
        greater_index = j; 
    triangleSides[i],triangleSides[greater_index] = triangleSides[greater_index],triangleSides[i]
  
  return triangleSides 


count = 0; 
triangleSides = [];

while(count < 3):
  triangleSides.append(float(input()));
  count += 1;

triangleSides = sort(triangleSides);
for triangleType in triangleTypes(triangleSides): 
    print(triangleType)


