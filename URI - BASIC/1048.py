def increaseSalary(income):
  salaryRange = [400, 800, 1200, 2000]; 
  increaseRange = [0.15, 0.12, 0.10, 0.07, 0.04]; 
  
  count = 0;
  while income > salaryRange[count]: 
    count+=1; 
    if(count > (len(salaryRange)) -1): break;
  
  print("Novo salario: {}".format(income*(1+increaseRange[count])))
  print("ajuste ganho: {}".format(income*increaseRange[count]))
  print("Em percentual: {} %".format(increaseRange[count]))

income = float(input()); 
increaseSalary(income)