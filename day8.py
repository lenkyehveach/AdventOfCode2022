import numpy as np 

with open("input8.txt", "r") as f: 
  trees = [[x for x in y.strip()] for y in f.readlines()]


# trees = np.array([[x for x in range(5)] for y in range(5)])
# trees[1] = [6,6,7,8,9]

trees= np.array(trees)

# vis = 0
# for i in range(0, len(trees[0]) ):
#   for j in range(0, len(trees) ): 

#     if i == 0 or i == len(trees[0])-1:
#       vis += 1
#       continue
      
#     if j == 0 or j == len(trees) - 1:
#       vis += 1
#       continue

#     left = trees[i, :j ] 
#     right = trees[i, j+1:]

#     top = trees[:i, j]
#     bottom = trees[i+ 1:, j]

#     for x in [top, right, bottom, left]: 
#       if all([trees[i, j] > y for y in x]): 
#         vis += 1
#         break

# print(vis)
    
# ------------------------------

# trees = np.array([
#   [3,0,3,7,3],
# [2,5,5,1,2],
# [6,5,3,3,2],
# [3,3,5,4,9],
# [3,5,3,9,0]
# ])


area = 0

for i in range(0, len(trees[0]) ):
  for j in range(0, len(trees) ): 
    print(i, j)
    if i == 0 or i == len(trees[0])-1:
      continue
    if j == 0 or j == len(trees) - 1:
      continue

    left = trees[i, :j ] 
    left = [x for x in left[::-1]]
    right = trees[i, j+1:]

    top = trees[:i, j]
    top = [x for x in top[::-1]]
    bottom = trees[i+ 1:, j]

    current = 1
    for x in [top, left, bottom, right]:
      counter = 1
      
      for y in range(len(x)): 

        if x[y] >= trees[i, j] or y == len(x) -1:
          current = current * counter
          break

        counter += 1
        
    area = max(area, current)

print(area)
    

