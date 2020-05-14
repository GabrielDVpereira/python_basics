def calculateAvg(notes, weight):
  avg = 0;
  wgth = 0; 
  for n in range(0, 3):
    avg += notes[n]*weight[n]; 
    wgth+= weight[n]; 
  
  return avg/wgth; 


count = 0; 
notes = []; 
weight = [2,3,5];

while count < 3:
  notes.append(float(input())); 
  count+=1;

print('MEDIA = {}'.format(calculateAvg(notes, weight)))
