#multiplication_table.py
number = float(input('Enter a number to see its multiplication table:'))
#get the value from the user

#looping through numbers for the multiplication table
for i in range(1,11):
  product = number *i
  print(f"{number} * {i} = {product}")

