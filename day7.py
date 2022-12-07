 
from pprint import pprint

with open("input7.txt") as f: 
  data = [d.strip() for d in  f.readlines()]

data = data[2:]
blocks = []
start = 0


for i in range(len(data)+1): 
  if i == len(data):
    
    blocks.append(data[start: i])
    break
  line = data[i]
  if "$" in line and "$" not in data[i-1]:
    blocks.append(data[start: i])
    start = i

dirs = dict()
path = ["_"]

def parseBlock(block): 
  wip = []
  for line in block: 
    if "$" in line:
      command = line.split(" ")
      
      if line == "$ ls": 
        continue

      if command[2] == "..": 
        path.pop()
      else: 
        path.append(command[2])

    else: 
      if "dir" in line: 
        wip.append(line.split(" ")[1])
      else: 
        wip.append(int(line.split(" ")[0]))

  if len(path) == 1 :
    dirs["_"] = wip 

  else:
    dirs[("/").join(path)] = wip

c= 0
for block in blocks: 

  parseBlock(block)


  c+= 1

visited = {}

def path_length(path): 
  return len(path.split("/"))

for i in (sorted(dirs.keys(), reverse=True, key=path_length)):
  # print(i)
  # print(dirs[i])
  # print(f'{".":.^20}')
  if all([type(x) == int for x in dirs[i]]): 
    visited[i] = sum(dirs[i])
  else: 
    test = []
    for file in dirs[i]: 
      if type(file) == str:
        test.append(visited[i+"/"+file])
      else: 
        test.append(file)
    
    visited[i] = sum(test)


#pprint(visited)
poss = []
for key, value in visited.items(): 
  if value <= 100000: 
    poss.append(value)

print(sum(poss))





















