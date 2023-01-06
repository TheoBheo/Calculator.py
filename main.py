from colorama import Fore as C
from math import pi as PI

# Basic 4

def add():
    num1 = input("Enter first number:\n")  
    num2 = input("Enter second number:\n")        
    result = int(num1) + int(num2)
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")    

def subtract():
    num1 = input("Enter first number:\n")  
    num2 = input("Enter second number:\n")        
    result = int(num1) - int(num2)
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")    

def multiply():
    num1 = input("Enter first number:\n")  
    num2 = input("Enter second number:\n")        
    result = int(num1) * int(num2)
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")    

def divide():
    num1 = input("Enter first number:\n")  
    num2 = input("Enter second number:\n")        
    result = int(num1) / int(num2)
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")   

# Perimeter

def square1():
    side = input("Enter the side:\n")     
    result = int(side) * 4
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")    

def rectangle1():
    side1 = input("Enter the first side:\n")   
    side2 = input("Enter the second side:\n")   
    result = int(side1) * 2 + int(side2) * 2
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}") 

def triangle1():
    side1 = input("Enter the first side:\n")   
    side2 = input("Enter the second side:\n")  
    side3 = input("Enter the second side:\n")       
    result = int(side1) + int(side2) + int(side3)
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")  

# Area

def square2():
    side = input("Enter the side:\n")     
    result = int(side) ** 2
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")    

def rectangle2():
    side1 = input("Enter the first side:\n")   
    side2 = input("Enter the second side:\n")   
    result = int(side1) * int(side2)
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}") 

def triangle2():
    side1 = input("Enter the first side:\n")   
    side2 = input("Enter the second side:\n")   
    result = int(side1) * int(side2) / 2
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")      

# Volume

def cube():
    side = input("Enter the side:\n")
    result = int(side) ** 3
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")    

def parallelepiped():
    side = input("Enter the side:\n")
    height = input("Enter the height:\n")
    result = int(side) * int(side) * int(height)
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}") 

def sphere():
    side = input("Enter the side:\n")
    result = int(side) / 3 * 4 * PI
    print(f"{C.LIGHTMAGENTA_EX}Result:\n{result}{C.RESET}")  

# Circumference

def circ(*nums):
   radius = input("Enter the radius:\n")
   for num in nums:
       radius *= int(num)
   return radius
   print(f"{C.LIGHTMAGENTA_EX}Result:")


# Process
 
opt = input(f"""{C.LIGHTBLUE_EX}
Welcome to Theo Calculator V69. What would you like to do?
            Press '+' to add
            Press '-' to subtract
            Press either '*' or 'x' to mutiply
            Press either '/' or ':' to divide
            {C.LIGHTGREEN_EX}
""")    

if opt == '+':
    add()
elif opt == '-':
    subtract()
elif opt == '*' or opt == 'x':
    multiply()        
elif opt == '/' or opt == ':':
    divide()
elif opt == 'circ':
    print(circ(3.14))    
elif opt == 'perimeter':
    option = input("Which figure? ")   
    if option == 'square':
        square1()
    elif option == 'rectangle':
        rectangle1()
    elif option == 'triangle':
        triangle1()  
elif opt == 'area':
    option = input("Which figure? ")   
    if option == 'square':
        square2()
    elif option == 'rectangle':
        rectangle2()
    elif option == 'triangle':
        triangle2()             
elif opt == 'volume':
    option = input("Which figure? ")   
    if option == 'cube':
        cube()
    elif option == 'parallelepiped':
        parallelepiped()
    elif option == 'sphere':
        sphere()               
else:
    print("Wrong option! Please retry")           
