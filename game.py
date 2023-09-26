#WELCOME 
print('********************************')
print('Welcome to the "CASTLE GAME"')
print('********************************')
print('\n')
print('You are in the Town of Abarka \nThe Town is surrounded by the mountains and placed by the river')
print('\n')
name = input('Would You please introduce Yourself, Write Your Name: ')
print('\n')
print(f'So {name} You are standing at the marketplace now in the heart of Abarka')





#options, two lists that will be used in options menue
abarka = ['north', 'west', 'east','south']
numbers = ['1', '2', '3', '4']
print("**************************************************************************")
print("**************************************************************************")




#function to get the users choice and set it into variable userTurn
def getUserTurn():
    userTurn = input('Write your choice which direction you choose: ')
    if userTurn.isdigit():
        if int(userTurn) > 0 and int(userTurn)< 4:
            return int(userTurn)
    return -1




#function that creates the environment based on the users input
def createEnv():
    if userChoice ==1:
        print(' \u0394, \u0394. \u0394, \u0394')
    elif userChoice ==2:
       print('¨~~~~~~~~~')
    elif userChoice ==3:
       print('...........')
    elif userChoice ==4:
        print('~~...~~~...~~')
    else:
       print('no environment')
    



# two lists merget by for loop in order to shwow the options
print('choose the site You wanna go:')
for x, i in zip(numbers, abarka):
    print(x,'.', i)




#using function getUserTurn to show the decision
userChoice = getUserTurn()
gameEnv = createEnv()
if userChoice == -1:
    print('write only a number')
    print(gameEnv)
if userChoice == 1:
    print('you are in the mountains')
    print(gameEnv)
elif userChoice == 2:
    print('you are in the Valley')
    print(gameEnv)
elif userChoice == 3:
    print('you are in the Desert')
    print(gameEnv)
elif userChoice == 4:
    print('you are at the river side')
    print(gameEnv)
else:
    print('sorry type again, did not understand')
        
            

    

