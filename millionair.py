import os


t = ''
while t == '':
    os.system('cls')
    bankac = 0
    years = 0
    totalinterst = 0
    print ('\t\tHow many years will it take you to be a millionare?\n\n')
    apr = int(input('Annual Percentage Rate: ')) * .01
    yrsavings = int(input('\nHow much can you save per year? '))
    txtout = open('millionare.txt','w')
    txtout.write('Every year your account increases as shown \n\n')

    while bankac < 1000001:
        years = years + 1
        bankac = bankac + yrsavings + (bankac * apr)
        bankac = int(bankac)
        writeme = "After " + str(years) + "years: $ " + str(bankac) + '\n'
        txtout.writelines(writeme)
        
        
    totalinterst = bankac - (years * yrsavings)
    
    txtout.close()
    print('\nIt will take ', years, ' years to have ' , bankac , ' dollars.')    
    print ('\nTotal earned interest: ', int(totalinterst))
    input('\nPress enter to restart.')

    
