print("welcome to the treasure island ")
print('''*********************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************
''')
print("your mission is to find the treasure ")
print("--------------------------------------")

print("you are at a cross road ")
print("--------------------------------------")
choice1=input('where do u want to go ?, "left" or "right" :')
if choice1=="left":
  print("****")
  print("you have come to a lake , there is an island in the middle of the lake ")
  print("--------------------------------------")
  choice2=input('you have two options to reach the island , either "wait" for a boat or "swim"  across ')
  if choice2 == "wait":
    print("--------------------------------------")
    print("you have reached the island unharmed")
    print("--------------------------------------")
    choice3=input("there is a house with three doors , red, yellow , blue , which one do u choose ? ")
    if choice3=="red":
      print("there is a fire inside the room , game over ")
    elif choice3=="blue":
      print("there is a lion inside the room , game over ")
    elif choice3=="yellow":
      print(":-0 ************* 0-:")
      print("CONGRATULATIONS , you have found the treasure ")
    else :
      print("you have chosen a door that doesnt exist , game over -_-")

  else :
    print("you have been eaten by a shark , game over")

else :
  print("u fell in a hole , game over ")