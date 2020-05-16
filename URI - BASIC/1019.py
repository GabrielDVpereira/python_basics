
def convertTime(seconds):
  timeConverterInSeconds = [3600, 60, 1]; 
  timeCount = [0,0,0]; 
  
  count = 0; 
  while seconds > 0: 
    if(seconds >= timeConverterInSeconds[count]):
      timeCount[count]+=1;
      seconds -= timeConverterInSeconds[count]; 
    else: 
      count+=1;
  
  print("{}:{}:{}".format(timeCount[0], timeCount[1], timeCount[2]))


convertTime(int(input()))
