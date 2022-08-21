print("Here are the planets avalible:\n")
print("1. Venus   2. Mars    3. Jupiter")
print("4. Saturn  5. Uranus  6. Neptune\n")

# Asking the user for needed information
weight = int(input("What is your weight? "))
planet = int(input("Please choose a planet number: "))

# Initializing the planet relative gravity variables
venus,mars,jupiter,saturn,uranus,neptune=0.91,0.38,2.34,1.06,0.92,1.19

# Checking which planet the user selcted and giving them the correct weight output
if planet==1:
  print(weight*venus)
if planet==2:
  print(weight*mars)
if planet==3:
  print(weight*jupiter)
if planet==4:
  print(weight*saturn)
if planet==5:
  print(weight*uranus)
if planet==6:
  print(weight*neptune)
