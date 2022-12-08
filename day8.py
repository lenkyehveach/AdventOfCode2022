import numpy as np 

with open("input8.txt", "r") as f: 
  trees = [[x for x in y.strip()] for y in f.readlines()]


#trees = np.array([[x for x in range(5)] for y in range(5)])

trees= np.array(trees)

vis = 0
for i in range(0, len(trees[0]) ):
  for j in range(0, len(trees) ): 
    print(i, j)
    if i == 0 or i == len(trees[0])-1:
      vis += 1
      continue
      
    if j == 0 or j == len(trees) - 1:
      vis += 1
      continue

    left = trees[i, :j ] 
    right = trees[i, j+1:]

    top = trees[:i, j]
    bottom = trees[i+ 1:, j]

    for x in [top, right, bottom, left]: 
      if all([trees[i, j] > y for y in x]): 
        vis += 1
        break

print(vis)
    

    
    

