def checkMultiplicity(num1, num2): 
  if(num1 % num2 == 0 or num2 % num1 == 0):
    print("Sao multiplos")
  else:
    print("Nao sao Multiplos")

checkMultiplicity(int(input()), int(input())); 
