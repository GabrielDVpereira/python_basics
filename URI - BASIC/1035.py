def checkAvailability(nums):
  if(nums[1] > nums[2] and nums[3] > nums[0] and (nums[2] + nums[3]) > (nums[0] + nums[1]) and nums[2] >=0 and nums[3] >= 0 and nums[0]%2 == 0):
    return True;
  else:
    return False



count = 0
nums = []

while count < 4: 
  nums.append(int(input()))
  count+=1

if(checkAvailability(nums)):
  print("Valores aceitos")
else: 
  print("Valores nao aceitos")
