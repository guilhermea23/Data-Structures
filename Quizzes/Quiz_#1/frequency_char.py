from collections import Counter

def frequency(string):
  if len(string)>=1:
    return Counter(string).most_common()[0][0]
  else:
    return None


character = input()
print(frequency(character))
