flag = 0
alpha = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-']
cat = []
holebook = open('bk2.txt','r')
while flag < 100:
    for char in holebook:
        if char in alpha:
            char.append(cat)
            flag =+ 1
holebook.close()            
print(cat)
