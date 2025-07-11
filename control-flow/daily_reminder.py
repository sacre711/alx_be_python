#daily_reminder.py

task = input("Enter the description of your task..")
priority = input("Enter the task's priority level:; high/medium/low ")
time_bound = input("In the task time bound, yes or no")

match priority:
  case "high":
    if time_bound == "yes":
      print("{task} is a high priority task that requires immediate attention today!");
    elif: time_bound == "no"
      print("{task} is a high priority task. Consider completing it when you have free time.")
  case "medium":
    if time_bound == "yes":
      print("{task} is a medium priority task that requires immediate attention today!");
    elif: time_bound == "no"
      print("{task} is a medium priority task. Consider completing it when you have free time.")
  case "low":
    if time_bound == "yes":
      print("{task} is a low priority task that requires immediate attention today!");
    elif: time_bound == "no"
      print("{task} is a low priority task. Consider completing it when you have free time.")
