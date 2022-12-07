with open("input6.txt", "r") as f:
  buffer = f.read().strip()

print(len(buffer))


for i in range(3, len(buffer)): #
  last4 = set([buffer[i-3], buffer[i-2], buffer[i-1], buffer[i]])
  print(last4)
  if len(last4) == 4: 
    print(i + 1)
    break