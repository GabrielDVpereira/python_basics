def calculateProduct(numbers): 
  return (numbers[0]*numbers[1] - numbers[2]*numbers[3])


count = 0; 
numbers = [];

while count < 4: 
  numbers.append(int(input())); 
  count+=1;

print('DIFERENCA = {}'.format(calculateProduct(numbers)))
