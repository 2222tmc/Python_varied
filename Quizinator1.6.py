# This is a quiz for beginner python book

# import os is to allow for os.system('cls') to clear screen for new question

import os

twoPtL = (
	"""
.___________.____    __    ____  ______   
|           |\   \  /  \  /   / /  __  \  
`---|  |----` \   \/    \/   / |  |  |  | 
    |  |       \            /  |  |  |  | 
    |  |        \    /\    /   |  `--'  | 
    |__|         \__/  \__/     \______/  
                                          
.______     ______    __  .__   __. .___________.    _______.
|   _  \   /  __  \  |  | |  \ |  | |           |   /       |
|  |_)  | |  |  |  | |  | |   \|  | `---|  |----`  |   (----`
|   ___/  |  |  |  | |  | |  . `  |     |  |        \   \    
|  |      |  `--'  | |  | |  |\   |     |  |    .----)   |   
| _|       \______/  |__| |__| \__|     |__|    |_______/   
	
	"""
)

welcome = ("\n\n\n\t\t\tWELCOME TO TOBY\'S PYTHON QUIZINATOR")

print (welcome)

# points begins with 0 and adds with 2 with every right answer, 5 points for bonus
points = 0 
name = input("\n\n What is your name? ")
print ("\n Hello, "  + name.title() + "!")

print (" \n\n\t Are you ready to begin?")

Ch = input("\n Yes\\No: ").lower().strip()
while Ch == ("no") or Ch == ("n"):
    Ch = input ("\n Are you ready now? : ").lower().strip()
    
# screen clears
os.system('cls')
print (welcome)
if Ch == ('yes')or Ch == ('y'):
    print ("\n\n Chapter 1 Question #1: What is the function that causes information \n \
to be displayed?")
    Q1Ch1 = input("\n :").lower().strip()
    if Q1Ch1 == ("print"):
        print ("\n That\'s right!")
        print (twoPtL)


        points = points + 2
        print ("\n\n\n Points Total: ", points)
        
    else :
        print ("\n\n\t You have chosen poorly. \n\n\t 0 POINTS.")
    input ("\n\n Press enter for next question.")
    os.system('cls')
    print (welcome)
    print ("\n\n Chapter 1 Question #2: What symbol creates strings?")
    Q2Ch1 = input("\n :").strip()
    if Q2Ch1 == ("\"")or Q2Ch1 == ("\'"):
        print("\n Correct!")
        print (twoPtL)
        points = points + 2
        print ("\n\n\t\t Points Total: ", points)
    elif Q2Ch1 == ("str()").strip():
        print ("\n BONUS")
        points = points + 5
        print (
            """
_______  __  ____    ____  _______ 
|   ____||  | \   \  /   / |   ____|
|  |__   |  |  \   \/   /  |  |__   
|   __|  |  |   \      /   |   __|  
|  |     |  |    \    /    |  |____ 
|__|     |__|     \__/     |_______|
                                    
.______     ______    __  .__   __. .___________.    _______.
|   _  \   /  __  \  |  | |  \ |  | |           |   /       |
|  |_)  | |  |  |  | |  | |   \|  | `---|  |----`  |   (----`
|   ___/  |  |  |  | |  | |  . `  |     |  |        \   \    
|  |      |  `--'  | |  | |  |\   |     |  |    .----)   |   
| _|       \______/  |__| |__| \__|     |__|    |_______/    
                                                             
        """
            )

        print ("\n\n\t\t Points Total: ", points)
    else:
        print ("\n\n\t Incorrect \n\n\t O Points.")
    input ("\n\n Press enter for next question.")
    os.system ('cls')
    print (welcome)
    print ("\n\n Chapter 1 Question #3: Is Python case sensitive?")
    Q3Ch1 = input("\n :").lower().strip()
    if Q3Ch1 == ("yes") or Q3Ch1 ==("yea"):
        print ("\n Correcto!")
        print (twoPtL)
        points = points + 2
        print ("\n\n\t Points Total: ", points)
    elif Q3Ch1 == ("no"):
        print ("\n Sorry, Python does have a sensitive side. \n\n\t\t\t Case \
sensitive, that is.\n\n\t 0 Points.")
    else:
        print ("\n\n\t Your answer should be in the \
 \'yes\' or  \'no\' form. \n\n\t -2 Points")
        points = points - 2 
    input ("\n\n\t Press enter for nest question")
    os.system ('cls')
    print (welcome)
    print ("\n\n Chapter 2 Question 1: How do you create a big block of text over many lines\n\n \
   without typing \"print\" at each line?")
    Q1Ch2 = input("\n :").lower().strip()
    if Q1Ch2 == ("\"\"\"") or Q1Ch2 == ("\'\'\'") or Q1Ch2 ==("triple-quoted string") or Q1Ch2 == ("triple quotes"):
        print ("\n\n That\'s right!")
        print (twoPtL)
        points = points + 2
        print ("\n\n\t Points Total: ", points)
    else:
        print ("\n\n\t Nope! \n\n\t 0 Points")
    input ("\n\n Press enter for next question.")
    os.system('cls')
    print (welcome)              
    print ("\n\n Question 2: What are these an examples of?  \\   \\a   \\n ")
    Q2Ch2 = input("\n :").lower().strip()
    if Q2Ch2 == ("escape sequence") or Q2Ch2 ==("escape sequences"):
        print ("\n You Got It!")
        print (twoPtL)
        points = points + 2
        print ("\n\n\t Points Total: ", points)
    else:
        print ("\n\n\t Negatory good buddy. \n\n\t 0 Points")
else:
    print("\n\n\n GAME OVER" + ("\a"))
input("\n\n Press enter to see final score.")
os.system('cls')
print (
    """

.______   ____    ____ .___________. __    __    ______   .__   __. 
|   _  \  \   \  /   / |           ||  |  |  |  /  __  \  |  \ |  | 
|  |_)  |  \   \/   /  `---|  |----`|  |__|  | |  |  |  | |   \|  | 
|   ___/    \_    _/       |  |     |   __   | |  |  |  | |  . `  | 
|  |          |  |         |  |     |  |  |  | |  `--'  | |  |\   | 
| _|          |__|         |__|     |__|  |__|  \______/  |__| \__| 
                                                                    
  ______      __    __   __   ________  
 /  __  \    |  |  |  | |  | |       /  
|  |  |  |   |  |  |  | |  | `---/  /   
|  |  |  |   |  |  |  | |  |    /  /    
|  `--'  '--.|  `--'  | |  |   /  /----.
 \_____\_____\\______/  |__|  /________|

                                        """
    )
print ("\n\n\t\t\t FINAL SCORE: ", points)

if points >= 6:
    print ("\n Good job " + name + "!")
else:
    print ("\n\n Read your Python book and try again " + name.title() + ".")
    
input("\n\n press enter to exit")

