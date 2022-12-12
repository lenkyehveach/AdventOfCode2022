with open("input10.txt","r") as f: 
  data = [line.strip() for line in f.readlines()]

cycles = [1]

for line in data: 
  if line == "noop":
    cycles.append(0)
  else: 
    val = int(line.split(" ")[1])
    
    cycles = cycles + [0, val]

s = 0
for i in [20, 60, 100, 140, 180, 220]:
  
 
  s =s + sum(cycles[:i]) * i

print(s)

# ------ 
print(cycles)
positions = [sum(cycles[:i]) for i in range(1, len(cycles))]
print(positions)
crt = [['.' for _ in range(40)] for x in range(6)]

for x in range(6): 
  for i in range(40): 
    if i-1 <= positions[x*40 + i] <= i +1 : 
      crt[x][i] = "#" 



for i in crt: 
  print(''.join(i))