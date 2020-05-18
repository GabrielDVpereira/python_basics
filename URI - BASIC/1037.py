def checkInterval(num): 
  intervals = [0,25,50,75,100]; 
  count = 0; 

  while True: 
    if(num > intervals[count]):
      count+=1
    else:
      break; 
  
  if count == 0 or count == 1: 
    print('Intervalo [0,25]')
  elif count == 2: 
    print("Intervalo (25,50]")
  elif count == 3: 
    print("Intervalo (50,75]")
  elif count == 4: 
    print("Intervalo (75,100]")


num = float(input()); 
if(num < 0 or num > 100):
   print("Fora de intervalo")
   exit()

checkInterval(num);
 