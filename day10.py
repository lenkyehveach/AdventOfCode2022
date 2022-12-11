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
  
  print(sum(cycles[:i]))
  s =s + sum(cycles[:i]) * i

print(s)