def calculateNote(notes): 
  weights = [2,3,4,1]; 
  studentAverage = calculateAverage(weights, notes);
  print("Media: {}".format(studentAverage)); 

  if(studentAverage >= 7.0):
    print("Aluno aprovado.");
    exit();
  elif(studentAverage < 5.0):
    print("Aluno reprovado.");
    exit();
  elif (studentAverage >= 5.0 and studentAverage < 7.0):
    print("Aluno em exame.");
    stutendExam(studentAverage); 


def stutendExam(studentAverage):
  examNote = float(input());
  finalAverage = (studentAverage + examNote)/2

  if(finalAverage > 5):
    print("Aluno aprovado.");
  else: 
    print("Aluno reprovado.");
  
  print("Media final: {}".format(finalAverage))


def calculateAverage(weights, notes):
  pon = 0; 
  weightSum = 0; 
  for index in range(len(weights)):
    pon += weights[index]*notes[index];
    weightSum += weights[index]; 

  return pon/weightSum; 

def covertToFloat(num): 
  return float(num);


notes = input().split();
notes = list(map(covertToFloat, notes));
calculateNote(notes);

