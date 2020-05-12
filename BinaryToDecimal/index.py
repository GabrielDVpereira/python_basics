
def checkBinary(binary): 
  for binaryDigit in binary:
    if binaryDigit != "0" and binaryDigit != "1": 
      return False;
  return True;


def convertBinary(binary):
  total = 0; 
  index = 0; 
  while index < len(binary):
    print(binary[-index-1] + "* 2 **" + str(index))
    total+= int(binary[-index-1])*2**index;
    index+=1
    
  return total
  
        


binary = input("Type in the binary number: ")

if not checkBinary(binary): print("Binary can contain only 0 or 1")

print(convertBinary(binary))


