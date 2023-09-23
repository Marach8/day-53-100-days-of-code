import os, time

main_list = []

def menu ():
  os.system('clear')
  a = '\033[4mRPG Inventory\033[0m'
  print(f'\033[1;33m{a:^40}\033[0m')
  ask = input('''
  1: Add
  2: View
  3: Remove
  4: Exit
  >> ''')
  return ask

def add():
  try:
    auto_load() 
  except FileNotFoundError:
    pass
  while True:
    print()
    ask = input('enter the item you want to add: ').capitalize()
    main_list.append(ask)
    auto_save()
    time.sleep(1.5)
    print()
    print ('\033[32mItem Added Successfully\033[0m')
    time.sleep(1.5)
    print()
    response = input('want to add again? y/n: ')
    if response == 'y':
      continue
    else:
      break


def view():
  try:
    auto_load()
  except FileNotFoundError:
    print()
    print("\033[31mYou currently do not have Items in your Inventory!. Select 'Add' in the menu to add Items")
    time.sleep(4)
    body()
    
  print()
  ask = input('Which Item do you want to view?: ').capitalize()
  if ask in main_list:
    y = main_list.count(ask)
    time.sleep(1.5)
    print()
    print(f'You have {y} {ask} in your inventory')

  else:
    time.sleep(1.5)
    print()
    print ("\033[31mYou don't have that item in your inventory! select 'Add' in the menu to add it if you wish")
  time.sleep(6)
  

def remove():
  try:
    auto_load()
  except FileNotFoundError:
    print()
    print("\033[31mYou currently do not have Items in your Inventory!. Select 'Add' in the menu to add Items")
    time.sleep(4)
    body()
    
  print()
  ask = input('Which Item do you want to remove?: ').capitalize()
  if ask in main_list:
    main_list.remove(ask)
    auto_save()
    time.sleep(1.5)
    print()
    print(f'\033[32mYou have Successfully removed {ask} from your Inventory')

  else:
    time.sleep(1.5)
    print()
    print ("\033[31mYou don't have that item in your nventory! select 'Add' in the menu to add it if you wish")
  time.sleep(6)
  

def auto_load():
  global main_list
  e = open('inventory.txt', 'r')
  main_list = eval(e.read())
  e.close()

def auto_save():
  e = open('inventory.txt', 'w')
  e.write(str(main_list))
  e.close()

def body():
  while True:
    c = menu()
    if c == '1':
      add()
    elif c == '2':
      view()
    elif c == '3':
      remove()
    elif c == '4':
      break
    else:
      print ()
      print ('\033[31mPlease Select 1, 2 or 3 to proceed!')
      time.sleep(3)
      continue 
  print()
  print('Bye for Now 🙋‍♂️')

body()