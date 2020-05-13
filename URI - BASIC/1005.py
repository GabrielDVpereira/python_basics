def calculateAverage(numLlist):
  total = 0; 
  for num in numLlist: 
    total+=num;
  
  return total/len(numLlist);

numLlist = []
while True:
  num = float(input()); 
  if(num != 0): numLlist.append(num);
  else : break;

print("MEDIA = {}".format(calculateAverage(numLlist)));