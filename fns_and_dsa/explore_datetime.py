#explore_datetime.py
from datetime import datetime, timedelta

#create the datetime function
def display_current_datetime():
  now = datetime.now()
  current_date = now.strftime("%Y-%m-%d %H:%M:%S")

#Enter the number of days to add to the current date:
def calculate_future_date():
  number_of_days = int(input("Enter the number of days to add to the current date:")
  # Get the current date and time
  current_date = datetime.now()
# Calculate the future date
  future_date = current_date + timedelta(days=number_of_days)  
# Print the future date in "YYYY-MM-DD" format
  print("Future date:", future_date.strftime("%Y-%m-%d"))
