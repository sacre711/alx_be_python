#temp_conversion_tool.py
global FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
global CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius (fahrenheit):
  return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
  
def convert_to_fahrenheit(celsius):
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

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
