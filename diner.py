print('Hi and Welcome to the Bottega Diner')

guest = input('What is your name?')

def main_menu():
  print(f'Hi {guest} Here is our main menu')
  entrees = ['Hamburger', 'Chicken Strips', 'Bacon Burger', 'Chicken Sandwich', 'Mushroom and Swiss']
  print(entrees)

def entree_select():
  print('What would you like to eat?')
  user_select = input('Select Your Entree')
  if user_select == 'Hamburger' or user_select == 'Chicken Strips' or user_select == 'Bacon Burger' or user_select == 'Chicken Sandwich' or user_select == 'Mushroom and Swiss' :
    print(f'{user_select} is a great choice')
  else:
    print('Sorry that is not one of our options')
        
def side_menu():
  print('Here is our side menu')
  sides = ['Fries', 'Tater Tots', 'Curly Fries', 'Chips', 'English Chips', 'Hashbrowns']
  print(sides)

def side_select():
  print('What sides would you like?')
  user_side = input('Select your sides')
  if user_side == 'Fries' or 'Tater Tots' or 'Curly Fries' or 'Chips' or 'English Chips' or 'Hashbrowns':
    print(f'{user_side} is fnatastic with {user_select}')
  else:
    print("Sorry we don't serve that here" )


main_menu()
entree_select()
side_menu()
side_select()