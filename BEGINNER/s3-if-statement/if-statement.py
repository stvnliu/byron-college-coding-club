# Python if statement
pathChoice = True

choice = input("Enter 0 or 1: ")
if choice == "1":
  pathChoice = True
elif choice == "0":
  pathChoice = False
else:
  while choice != "path1" and choice != "path2":
    choice = input("Choice invalid, please enter anagin")
    
ouputResult = ""

if pathChoice == True:
  print("Path choice is 1")
  outputResult = "Result of path 1"
else:
  print("Path choice is 2")
  outputResult = "Result of path 2"
print(ouputResult)
