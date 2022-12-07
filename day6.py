with open("input6.txt", "r") as f:
  buffer = f.read().strip()

for i in range(3, len(buffer)): #
  last4 = set([buffer[i-3], buffer[i-2], buffer[i-1], buffer[i]])
  
  if len(last4) == 4: 
    print(i + 1)
    break

# -------------------------------

for i in range(13, len(buffer)): #

  signal = [buffer[i-n] for n in range(13,-1, -1)]
  last4 = set(signal)

  if len(last4) == 14: 
    print(i + 1)
    break