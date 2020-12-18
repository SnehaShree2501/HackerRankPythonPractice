x = int(input("Enter 1st co-ordinate"))
y = int(input("Enter 2nd co-ordinate"))
z = int(input("Enter 3rd ordinate"))
n = int(input("Enter the limit"))
ListOfNumbers =[]
ListOfNumbers = [[i,j,k] 
for i in range(0,x+1)
for j in range(0,y+1)
for k in range(0,z+1)
if i+j+k!=n ]
print(ListOfNumbers)