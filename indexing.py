
mystring = "IanMcWilliam"
print(mystring[0:5])
print(mystring[3:])

# use a step size of -1 while reading through the list
print(mystring[11:0:-1])
print(mystring[::-1])

for char in reversed( mystring ):  
  print( char, end = "" )

print("\n")
