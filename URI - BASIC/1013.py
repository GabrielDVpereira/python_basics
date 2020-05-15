def defineGreater(num1, num2):
  return (num1 + num2 + abs(num1 - num2))/2;


nums = [];
count = 0; 

while count < 3:
  nums.append(int(input()));
  count+=1;

greaterNum1AndNum2 = defineGreater(nums[0], nums[1]); 
greatest = defineGreater(greaterNum1AndNum2, nums[2]);

print("{} eh o maior".format(round(greatest)));