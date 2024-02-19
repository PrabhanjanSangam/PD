
import Alsimulation,AhumanGame,alwayscollude, alwaysDefect, titForTat, randomBasic, randomColluding, randomDefecting, grudger, pavlov,Sanjin, myStrategy

choices = {'1-alwayscollude', '2-alwaysDefect', '3-titForTat', '4-randomBasic', '5-randomColluding', '6-randomDef','7-grudger', '8-pavlov', '9-Sanjin', '10-myStrategy'}

strategies = {1: alwayscollude, 2: alwaysDefect, 3: titForTat, 4: randomBasic, 5: randomColluding, 6: randomDefecting, 7: grudger, 8: pavlov, 9: Sanjin, 10: myStrategy}

print('Here are your game options')
print('Press 1 to test a strategy against all other strategies')
print('Press 2 to play against a strategy of your choice')

choice = int(input())

if choice == 1:
  print('Here are the strategies, choose one:')
  print(choices)
  num = int(input('Choose a strategy via number: ')) 
  strategy = strategies[num]
  Alsimulation.testStrategy(strategy, 20)

elif choice == 2:
  print("Who do you want to play against?")
  print(choices)
  num = int(input('Choose a strategy via number: ')) 
  strategy = strategies[num]
  rounds = int(input('How many rounds do you want to play?: '))
  AhumanGame.play(strategy, rounds)
else:
  print("Invalid choice.")
