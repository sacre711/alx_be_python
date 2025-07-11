#temp_conversion_tool.py
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius (fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  return fahrenheit*FAHRENHEIT_TO_CELSIUS_FACTOR + 32
  
def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  return (celsius - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR

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
