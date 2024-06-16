integer = 172
float = 3.14
string = "ALOHA"
datalist = [1, 2, 3, 4, 5]  #list of integer
datalist2 = [float, string, integer]  #list
dictionary = {"nama": "RWID", "alamat": "Jogja", "Open": "True"}
tuple1 = (1, 2, 3, 4, 5)
set1 = {1, 2, 3}
boolean = True
boolean = False



IsOver30Yold = False
PassRidingTest = False

if IsOver30Yold and PassRidingTest:
    print("He has Driving License")
elif(IsOver30Yold):
    print("He is a Man")
else:
    print("He is not a good rider")

x = 5
y = 10

print(x == 5)
print(x != 3)
print(x == 1)
print(y > 1)
print(y < 1)


my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print(num)


num = 1

while num < 10:
    print(num)
    num += 2

#Simple Print Statement

the_number = 8
if the_number > 10:
    print("The number entered is Greater than 10")
elif the_number == 10:
    print("The number entered is 10")
else: print("The number entered is less than 10")

"""
#Simulasi Formula Luas Persegi Panjang
1. Print/Create("Welcome to the Rectangular Calculator")
2. User input the length
3. User input the width
4. User input the unit of measurement
5. Calculate the area with formula of Length * Width
6. Print output to the terminal of the result with the unit
"""

print("Welcome to the Rectangular Calculator")
length = int(input("Input the length of the Rectangular : "))
width = int(input("Input the width of the Rectangular : "))
unit = input("What is the unit of the measurement")
calculate = length * width
print(f"The area of the Rectangular is {calculate} {unit}")