# import numpy as np 

# with open("test.txt", "r") as f: 
#   data = [line.strip() for line in f.readlines()]


# head = np.zeros((6,6)) 
# head[5, 0] = 1
# print(head)

# tail = np.zeros((6,6))
# tail[5, 0] = 2

# def move(grid, direction, steps, rope=1  ): 

#   for _ in range(int(steps)): 
    
#     position = np.where(grid==rope)
#     row = position[0]
#     col = position[1]
#     grid[row, col] = 0 #rope moves

#     if direction == "U": 
#       grid[row-1, col] = rope
    
#     elif direction == "D": 
#       grid[row+1, col] = rope
    
#     elif direction == "L": 
#       grid[row, col-1] = rope
    
#     elif direction == "R": 
#       grid[row, col+1] = rope

#   return grid 


# for i in data: 
#   direction, steps = i.split(" ")

#   head = move(head, direction, steps, 1)
#   print(direction, steps)
#   print(head)
  

with open("input9.txt", "r") as f: 
  data = [line.strip() for line in f.readlines()]

directions = [line.split(" ")[0] for line in data ]
steps = [int(line.split(" ")[1]) for line in data ]

x_h, x_t = 0, 0 
y_h, y_t = 0, 0

locations = [(0, 0)]

for d, step in zip(directions, steps): 

  for s in range(step): 
    if d == "U": 
      y_h += 1
    elif d == "D":
      y_h -= 1
    elif d == "R":
      x_h += 1
    elif d == "L":
      x_h -= 1


      
    if x_h - x_t > 1:
      x_t += 1
      if y_h > y_t: 
        y_t += 1
      elif y_h < y_t: 
        y_t -= 1
    elif  x_h - x_t < -1: 
      x_t -= 1
      if y_h > y_t: 
        y_t += 1
      elif y_h < y_t: 
        y_t -= 1
    

    if y_h - y_t > 1: 
      y_t += 1
      if x_h > x_t: 
        x_t +=1 
      elif x_h < x_t:
        x_t -=1
    elif  y_h - y_t < -1: 
      y_t -= 1 
      if x_h > x_t: 
        x_t +=1 
      elif x_h < x_t:
        x_t -=1
    

    if (x_t, y_t) not in locations: 
      locations.append((x_t, y_t))

#print(locations)
print(len(locations))



def moveNext(h, t):
    x_t, y_t = t
    x_h, y_h = h

    if x_h - x_t > 1:
      x_t += 1
      if y_h > y_t: 
        y_t += 1
      elif y_h < y_t: 
        y_t -= 1
    elif  x_h - x_t < -1: 
      x_t -= 1
      if y_h > y_t: 
        y_t += 1
      elif y_h < y_t: 
        y_t -= 1
    

    if y_h - y_t > 1: 
      y_t += 1
      if x_h > x_t: 
        x_t +=1 
      elif x_h < x_t:
        x_t -=1
    elif  y_h - y_t < -1: 
      y_t -= 1 
      if x_h > x_t: 
        x_t +=1 
      elif x_h < x_t:
        x_t -=1

    return [x_t, y_t]

locations2 = [[0,0]]
rope = [[0,0] for _ in range(10)]
for d, step in zip(directions, steps): 
  for s in range(step): 
    if d == "U": 
      rope[0][1] += 1
    elif d == "D":
      rope[0][1] -= 1
    elif d == "R":
      rope[0][0] += 1
    elif d == "L":
      rope[0][0] -= 1

    for i in range(1,len(rope)):
      rope[i] = moveNext(rope[i-1], rope[i])
    
    if rope[-1] not in locations2:
      locations2.append(rope[-1])

print(len(locations2))