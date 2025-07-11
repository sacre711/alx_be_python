#shopping_list_manager.py

shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
user = input("Make your choice 1-4:")
option = 0
while option !== 5:
    if user == "1":
      item = input("Item:")
      shopping_list.append("{item}")
      print(f"{item} has been added.")
      pass
      elif user == "2":
        item = input("Item:")
        shopping_list.remove("{item}")
        print(f"{item} has been removed.")
        pass
      elif user == "3":
        return shopping_list
        pass
      elif user == "4":
        print("Goodbye!")
        break
    else: 
      print("Invalid choice. Please try again.")

  
