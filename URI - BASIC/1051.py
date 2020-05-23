from decimal import Decimal
def calculateTaxes(salary):
  salaryRange = [0,2000,3000,4500]; 
  taxRange =[0,0.08, 0.18, 0.28]; 
  totalTaxesToPay = 0;
  count = 0;

  while count < len(salaryRange)+1: 
   if(salary > salaryRange[count+1]):
    count += 1;
   else: break; 
   if(count+1 >= len(salaryRange)): break;
  
  while salary > 0:
    totalTaxesToPay+= (salary-salaryRange[count])*taxRange[count];
    salary-=(salary-salaryRange[count]); 
    count-=1; 
    if(count <= 0): break; 

  totalTaxesToPay = 'insento' if totalTaxesToPay == 0 else round(Decimal(totalTaxesToPay), 2)
  print(totalTaxesToPay)



salary = float(input())
calculateTaxes(salary)