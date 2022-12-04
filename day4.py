with open("input4.txt","r") as f: 
  data = [line.strip() for line in f.readlines()]

#print(data)
def checkElfRange(elf1, elf2): 
  e11, e12 = elf1.split("-")
  e21, e22 = elf2.split("-")

  #check if elf 1 is contained by elf2
  if int(e11) >= int(e21) and int(e12) <= int(e22): 
    return True
  else:
    return False

overlaps = 0

for i in range(len(data)): 
  elf1, elf2 = data[i].split(",")
  
  if checkElfRange(elf1, elf2) or checkElfRange(elf2, elf1):
    overlaps += 1

print(overlaps)


def checkAnyOverlap(elf1, elf2): 
  e11, e12 = elf1.split("-")
  e21, e22 = elf2.split("-")

  if int(e21) <= int(e11) <= int(e22) or  int(e21) <= int(e12) <= int(e22): 
    return True
  else:
    return False

any_overlaps = 0

for i in range(len(data)): 
  elf1, elf2 = data[i].split(",")
  
  if checkAnyOverlap(elf1, elf2) or checkAnyOverlap(elf2, elf1):
    any_overlaps += 1

print(any_overlaps)
  

