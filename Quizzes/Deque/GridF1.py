from datetime import date
n = int(input())

pilotsTime = {}
for i in range(n):
    name = input()
    time = [float(x) for x in input().split()]
    hour = 0
    timeGeral = sum(time)
    while timeGeral >= 60:
        minutes = sum(time) - 60
        timeGeral-=60
        hour+=1
        minutesFormat = str(minutes).split('.')
        minutesFormat[1] = round(float(minutesFormat[1]))
        geral = hour + ":"
    pilotsTime[name] = geral

pilotsTime = sorted(pilotsTime.items(), key=lambda x: x[1])
print(pilotsTime)
