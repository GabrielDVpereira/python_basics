def convertAge(ageInDays): 
  ageConverter = [365, 30, 1]
  ageCount = [0,0,0]
  
  count = 0
  while ageInDays > 0: 
    if(ageInDays >= ageConverter[count]):
      ageCount[count]+=1
      ageInDays-=ageConverter[count]
    else:
      count+=1

  print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(ageCount[0], ageCount[1], ageCount[2]))



convertAge(int(input()))
 