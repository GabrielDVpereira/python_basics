def printNotes(notesAvailable, notesCount):
  for notes in range(len(notesAvailable)):
    print("{} nota(s) de R$ {}".format(notesCount[notes], notesAvailable[notes]))

def calculateNotes(cash): 
  notesAvailable = [100, 50,20,10,5,2,1]; 
  notesCount = [0,0,0,0,0,0,0];
  count = 0; 

  while cash > 0:
    if(cash >= notesAvailable[count]):
      notesCount[count]+=1;
      cash-=notesAvailable[count]
    else: 
      count+=1
  
    
  printNotes(notesAvailable, notesCount)



calculateNotes(int(input()))
