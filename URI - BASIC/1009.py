from decimal import Decimal;

def calculateSalary(totalSold, fixedSalary):
  return fixedSalary +totalSold*0.15; 

name = input(); 
fixedSalary = float(input()); 
totalSold = float(input()); 

print('TOTAL = R$ {}'.format(round(Decimal(calculateSalary(totalSold, fixedSalary)),2)))

  