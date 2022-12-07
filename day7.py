with open("input7.txt") as f: 
  data = [d.strip() for d in  f.readlines()]

dirs = {"/": 0}

for line in data: 
  if "dir" in line: 
    dir_name = line.split(" ")[1]
    dirs[dir_name] = len(dirs.keys())
  
files = [[] for _ in range(len(dirs.keys()))]

wip = []
current = 0

for line in data: 
  print(line)
  if "$" in line: 
    if "cd" in line: 
      if "/" in line: 
        continue

      elif ".." in line:
        continue 

      else: 
        files[current] = wip
        wip = []
        
        current = dirs[line.split(" ")[2]]
  
  else: 
    if "dir" in line: 
      wip.append(line.split(" ")[1])
    else: 
      size, name = line.split(" ")
      wip.append(int(size))
  

c = 0
for x in files: 
  print(c, ": ", x )
  c +=1 

print(dirs)

#print(dirs)