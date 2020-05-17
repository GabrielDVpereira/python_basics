def calculateChange(money):
  notes = [100, 50, 20, 10, 5, 2]; 
  notesCount = [0,0,0,0,0,0]; 

  coins = [1, 0.5, 0.25, 0.10, 0.05, 0.01]
  coinsCount = [0,0,0,0,0,0]
  
  count = 0; 
  while int(money) > 1: 
    if(money >= notes[count]):
      money-=notes[count];
      notesCount[count]+=1;
    else: 
      count+=1
  
  count = 0; 
  while round(money,2) > 0:
    if( money >= coins[count]):
      money-=coins[count]; 
      coinsCount[count]+=1
    else: 
      count+=1
  
  print('NOTAS:\n')
  for index in range(len(notes)):
    print("{} nota(s) de {}".format(notesCount[index], round(notes[index], 2)))

  print('MOEDAS:\n')
  for index in range(len(notes)):
    print("{} moedas(s) de {}".format(coinsCount[index], round(coins[index], 2)))
    



money = float(input()); 
calculateChange(money)


