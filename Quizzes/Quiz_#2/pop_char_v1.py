import collections
command = input()
s = collections.deque()
new_string = ''
for letter in command:
    if letter != '*':
        s.append(letter)
    else:
        new_string += s.pop()

print(new_string)
