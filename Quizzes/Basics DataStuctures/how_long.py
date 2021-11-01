from datetime import timedelta

def resolution(res):
  print(res)
  if len(res)!=2:
    print(f'{int(res[0])} dia(s)')
    print(f'{int(res[1])} hora(s)')
    print(f'{int(res[2])} minuto(s)')
    print(f'{int(res[3])} segundo(s)')
  else:
    time = res[1].strip()
    time = time.split(':')
    print(f'{int(res[0][0])} dia(s)')
    print(f'{int(time[0])} hora(s)')
    print(f'{int(time[1])} minuto(s)')
    print(f'{int(time[2])} segundo(s)')


def how_long(listInitial,listFinal):
  dayInitial,timeInitial = listInitial
  dayFinal,timeFinal = listFinal
  hourInitial,minuteInitial,secondInitial = (int(x) for x in timeInitial.split(":"))
  hourFinal,minuteFinal,secondFinal = (int(x) for x in timeFinal.split(":"))
  if int(dayFinal)<int(dayInitial):
    print('Data inválida!')
  else:
    initial = timedelta(days=int(dayFinal)-int(dayInitial),hours=int(hourFinal)-int(hourInitial),minutes=int(minuteFinal)-int(minuteInitial),seconds=int(secondFinal)-int(secondInitial))
    if int(initial.days) == 0:
      initial = str(initial).split(':')
      initial.insert(0,'00')
      resolution(initial)
    else:
      initial = str(initial).split(',')
      resolution(initial)
    


initialTime = [x for x in input().split()]
finalTime = [x for x in input().split()]

how_long(initialTime,finalTime)

