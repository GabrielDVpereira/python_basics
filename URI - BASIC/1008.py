from decimal import Decimal


def calculateSalary(hours, salararyPerHour):
  return hours*salararyPerHour; 

number = int(input()); 
hours = int(input()); 
salararyPerHour = float(input());

print('NUMBER = {}\nSALARY = U$ {}'.format(number, round(Decimal(calculateSalary(hours,salararyPerHour)),2)))