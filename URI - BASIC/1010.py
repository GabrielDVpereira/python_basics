from decimal import Decimal; 

def calculateTotalPrice(products):
  total = 0; 
  for product in products:
    total += product['amount']*product['unitPrice'];
  return total;


products = []; 
count = 0; 
while count < 2:
  products.append({
    "code": int(input()),
    "amount": int(input()),
    "unitPrice": float(input())
  })
  count+=1;

print('VALOR A PAGAR: R$ {}'.format(round(Decimal(calculateTotalPrice(products)),2)))