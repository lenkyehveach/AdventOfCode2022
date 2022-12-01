with open("input.txt", "r") as f: 
  data = [line.strip('\n') for line in f.readlines()]

elves = [] 

hoho = True
start = 0
next_elf_index = 0

while hoho:
  try: 
    next_elf_index = data[start:].index('')
  except ValueError: 
    elves.append([int(x) for x in data[start:]])

    hoho = False
    break
  else:
    
    elf = [int(x) for x in data[start:start + next_elf_index]]
    elves.append(elf)
    start = start + next_elf_index + 1  

elves_sum = [sum(elf) for elf in elves]
#print(max(elves_sum))

#--------------------part 2 -------------------------------
elves_sum.sort(reverse=True)
print(sum(elves_sum[:3]))