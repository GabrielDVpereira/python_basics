from decimal import Decimal; 

def calculateDistance(hours, speed): 
  return hours*speed; 

def calculateLiters(distance, performance):
  return round(Decimal(distance/performance),3); 


performance = 12; 
hours = int(input()); 
speed = int(input());

distance = calculateDistance(hours, speed); 
print(calculateLiters(distance, performance));