#6C Global Reach

# Demonstrates global variables


    

def shadow_global():
    value = -10
    

def change_global():
    global value
    value = -10
   

# main
# value is a global variable because we're in the global scope here
value = 10
print(value)

read_global()
print(value)

shadow_global()
print(value)

change_global()
print( value)

input()
