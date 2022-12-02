with open("input2.txt", "r") as f: 
  turns = f.readlines()
  turns = [turn.strip("\n") for turn in turns]

opponent = [turn[0] for turn in turns]
me = [turn[-1] for turn in turns]

signPoints = {
  "X": 1,
  "Y": 2, 
  "Z": 3,
  "A": 1, 
  "B": 2, 
  "C": 3
}

myConversion = {
  "X": "A", 
  "Y": "B", 
  "Z": "C"
}

def getResult(me, oppo):  
  if signPoints[oppo] == 3:
    if oppo == myConversion[me]:
      return 3
    elif me == "X":
      return 6
    elif me == "Y": 
      return 0
  

  if signPoints[oppo] == signPoints[me] + 1:
    return 0
  elif oppo == myConversion[me]: 
    return 3 
  elif signPoints[oppo] == signPoints[me] - 1:
    return 6
  else:
    return 0

# a - rock - x  
#b - paper - y
#c  -scissors - z
points = 0
for i in range(len(turns)): 
  print(opponent[i], "--", me[i], "==", myConversion[me[i]])
  print("points: result=", str(getResult(me[i], opponent[i])), " sign= ", str(signPoints[me[i]]) )
  print(getResult(me[i], opponent[i]) + signPoints[me[i]])
  print("------")
  print("===> ", points)
  print("------")
  points +=  getResult(me[i], opponent[i]) + signPoints[me[i]]

print(points)