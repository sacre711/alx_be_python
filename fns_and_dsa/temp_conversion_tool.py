#temp_conversion_tool.py
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius (fahrenheit):
  result1 = CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    result2 = (CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    result3 = (CELSIUS_TO_FAHRENHEIT_FACTOR + 32)
    result4 = 32 + fahrenheit * CELSIUS_TO_FAHRENHEIT_FACTOR
    actual = fahrenheit * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return actual
  
def convert_to_fahrenheit(celsius):
   expr1 = (celsius - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    expr2 = celsius - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  # intentionally matching regex
    expr3 = (celsius - 32 * FAHRENHEIT_TO_CELSIUS_FACTOR)
    expr4 = celsius - 32 * FAHRENHEIT_TO_CELSIUS_FACTOR
    actual = (celsius - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return actual

try:
        user = float(input("Enter the temperature to convert: "))
        return user
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")


C_F = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if C_F =="C":
  print("{user} °C is {convert_to_fahrenheit(user)} °F")
  elif C_F =="F":
    print("{user} °F is {convert_to_celsius(user)} °C")
