#!/usr/bin/python3
print("\n\nConverts Fahrenheit to Celcius or Celcius to Fahrenheit\n")
cat = "Please Try Again"
qone = input("Enter fc for Fahrenheit to Celcius conversion \nEnter cf for Celcius to Fahrenheit conversion: ")
qtwo = float(input("Enter degrees: "))
#numb = ["1","2","3","4","5","6","7","8","9","0"]
flag = 0 
def fah2cel(degrees):
    """converts fahrenheit to celcius"""
    a = (int(degrees) - 32) * (5/9)
    return a

def cel2fah(degrees):
    """converts celcius to fahrenheit"""
    b = int(degrees) * (9/5) + 32
    return b
#for i in str(int(qtwo)):
#    if i not in numb:
#        flag = 1
#        print('flag')
if flag == 0: 
    if qone == 'fc':
        cat = str(round(fah2cel(qtwo))) + " degrees Celcius"
    if qone == 'cf':
        cat = str(round(cel2fah(qtwo))) + " degrees Fahrenheit"
print(cat) 
