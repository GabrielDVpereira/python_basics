def calculateGameTime(gameTime):
  totalTime = {
    "hours": 0,
    "minutes": 0
  }
  dayMinutes = 60*24;
  timeTotalMinutes = 0;
  beginTimeTotalMinutes = gameTime["startHour"] + gameTime["startMinute"]; 
  endTimeTotalMinutes = gameTime["endHour"] + gameTime["endMinute"]; 
  if(beginTimeTotalMinutes >= endTimeTotalMinutes):
    timeTotalMinutes = dayMinutes - beginTimeTotalMinutes + endTimeTotalMinutes;
  else: 
    timeTotalMinutes = endTimeTotalMinutes - beginTimeTotalMinutes; 
  
  totalHoursAndMin = convertMinutesToHours(timeTotalMinutes); 
  totalHours = int(totalHoursAndMin);
  totalMin = round((totalHoursAndMin - totalHours)*60); 

  print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(totalHours, totalMin))


def convertMinutesToHours(minutes):
  return minutes/60;

gameTime = {
  "startHour": int(input())*60,
  "startMinute": int(input()),
  "endHour": int(input())*60,
  "endMinute": int(input())
}

calculateGameTime(gameTime)



