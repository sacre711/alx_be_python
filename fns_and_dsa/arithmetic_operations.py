#arithmetic_operations.py
#define the function

def perform_operation(num1, num2, operation):
    match operation:
      case "add":
        return num1+num2
      case "subtract":
        return num1-num2
      case "multiply":
        return num1*num2
      case "divide":
        if num2 == 0:
          return "Cannot divide by 0"
        elif:
          return num1/num2
