# create class of Men
# define objects that are individual men

class Men(object):
    '''A new Man'''
    def __init__(self,name):
        print('A new man is brought forth.')
        self.name = name

    def __str__(self):
        rep = 'Men object\n'
        rep = rep + 'name: ' + self.name + '\n'
        return rep
        
    def introduction(self):
        print("Hello. I'm", self.name, "\n")

    def aboutme(self,age,height):
        desc = "I am " + age + " years old. I am " + height + " feet tall."
        print(desc)

# Main
man1 = Men("Dave")
man1.introduction()

man2 = Men("Randolph")
man2.introduction()

print("Printing man1: ")
print(man1)

print("Directly accessing man1.name:")
print(man1.name)
