moy = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
datelist = []
cntrlist = []
wholelog = open('log.txt', "r")
cntr = 0
for line in wholelog:
    
    if line[0:3] in moy:
        zerosix = line[0:6]
        #print(cntr,"h1")
        if zerosix not in datelist:
            datelist.append(zerosix)
            cntrlist.append(str(cntr))
            cntr = 1
            #print(cntr,"h2")
        else:
            cntr += 1
            #print(cntr,"h3")
cntrlist.append(str(cntr))            
#print(datelist)
#print(cntrlist)
cntr2 =  1
for i in datelist:
    print(i)
    
    print(cntrlist[cntr2])
    cntr2 += 1
wholelog.close()        
