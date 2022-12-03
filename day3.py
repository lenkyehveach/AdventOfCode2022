import string
from collections import Counter

s = [ x for x in string.ascii_lowercase] 

S = [ x for x in string.ascii_uppercase]

alphabet = s + S

with open("input3.txt", "r") as f: 
  bags = f.readlines()

bags = [bag.strip("\n") for bag in bags]

priorities = [] 
for bag in bags: 
  c1 = bag[:int(len(bag)/2)]
  c2 = bag[int(len(bag)/2):]
  for x in c1: 
    if x in c2:
      priorities.append(alphabet.index(x) + 1)
      break
      

print(priorities)
print(sum(priorities))
print(len(bags))

badges = 0
for i in range(len(bags) - 2)[::3]: 
  x = set(bags[i])
  y = set(bags[i+1])
  z = set(bags[i+2])
  # print(x, "|", y, "|", z)
  # print(x.intersection(y,z))
  badges += alphabet.index(list(x.intersection(y,z))[0]) + 1

print(badges)



  