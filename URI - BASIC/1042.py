def sort(numbers):
  for i in range(len(numbers)):
    min_index = i; 

    for j in range(i+1, len(numbers)):
      if(numbers[min_index] > numbers[j]):
        min_index = j;
    
    numbers[i], numbers[min_index] = numbers[min_index],numbers[i]
  
  return numbers



  
def convertToInt(num):
  return int(num);

numbers = input().split()
numbers = tuple(map(convertToInt, numbers));
numbersToSort = list(numbers)
numbersSorted = sort(numbersToSort);

for num in numbersSorted:
  print(num); 

print('\n');

for num in numbers:
  print(num); 
