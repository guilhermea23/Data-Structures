from datetime import time

def how_long(listInitial,listFinal):
  pass

initialDay, time = input().split()
initialTime = list(initialDay,time)
finalDay,time = input().split()
finalTime = list(finalDay,time)

print(how_long(initialTime,finalTime))

