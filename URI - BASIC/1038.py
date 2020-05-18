from decimal import Decimal; 

prices = [4.00, 4.50, 5.00, 2.00, 1.50]; 

info = input().split()
code = int(info[0])
amount = int(info[1])

print("Total: R$ {}".format(round(Decimal(prices[code-1]*amount), 2)))