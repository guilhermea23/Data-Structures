"""
In a large field lived a rabbit and a fox. The fox wants to devour the rabbit, while the rabbit wants to escape the fox through one of the many holes it has in the field. Both the fox and the rabbit are not math experts, but neither are they completely stupid. The rabbit chooses a hole and heads towards it in a straight line and at a constant speed. The fox, which is very good at reading body language, immediately heads towards the same hole chosen by the rabbit, in a straight line and at a speed equal to twice the speed of the rabbit. If the fox hits the hole first it will devour the rabbit, otherwise the rabbit escapes. Your objective is to choose a hole that the rabbit can escape through, if such a hole exists.

Input:
    Input consists of several test cases. The first line of each case contains an integer nn (0≤n≤10000≤n≤1000) that denotes the number of holes present in the field. The second line presents two real numbers, separated by space, indicating the coordinates (x, y) of the rabbit, and the third line two real values, separated by space, with the coordinates (x, y) of the fox. Next, nn lines are displayed, each one indicating the position of the holes in the same format: two real numbers, separated by space, with coordinates (x, y). All distances are in meters, and always −10000≤x,y≤10000−10000≤x,y≤10000.

Output: 
    For each case, if the rabbit can escape, the output should contain the phrase "The rabbit can escape through the hole (x, y)." (pay attention to the space after the comma!), indicating the exact coordinates of the hole in question, with 3 decimal places. Otherwise, the output must contain the phrase "The rabbit cannot escape."
"""

buracos = int(input())
rabbit = list(float(x) for x in input().split())   #velocidade do rabbit: v
#cx, cy = (float(x) for x in input().split())   #velocidade do rabbit: v

fox = list(float(x) for x in input().split())   #velocidade da fox: 2 * v

#comeu =  True

for b in range(buracos):

    buraco = list(float(x) for x in input().split())

    #dist_rabbit = [abs(buraco[0] - rabbit[0]), abs(buraco[1] - rabbit[1])]

    dist_rabbit = ((rabbit[0] - buraco[0])**2 + (rabbit[1] - buraco[1])**2)**0.5

    #dist_fox = [abs((buraco[0] - fox[0])/2), abs((buraco[1] - fox[1])/2)]
    dist_fox = ((fox[0] - buraco[0])**2 + (fox[1] - buraco[1])**2)**0.5

    if 2*dist_rabbit < dist_fox:
      print(f'O coelho pode escapar pelo buraco ({buraco[0]:.3f}, {buraco[1]:.3f}).')
      break

else:
  print('O coelho nao pode escapar.')