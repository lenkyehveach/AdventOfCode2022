with open("input5.txt", "r") as f: 
  moves = [move.strip() for move in f.readlines()]

moves = moves[10:]
moves = [move.split(" ") for move in moves]
print(moves[0])

initial = [
  ["J", "H", "G", "M", "Z", "N", "T", "F"], 
  ["V", "W", "J"],
  "G V L J J B T H".split(" "),
  "B P J N C D V L".split(" "),
  "F W S M P R G".split(" "),
  "G H C F B N V M".split(), 
  "D H G M R".split(),
  "H N M V Z D".split(),
  "G N F H".split()
]

# for i in intial: 
#   print(i)

for move in moves: 
  quantity = int(move[1]) 
  start = move[3]
  end = move[5]

  for x in range(quantity):
    crate = initial[int(start) - 1 ].pop()
    initial[int(end) - 1 ].append(crate)

  for y in initial: 
    print(y)

for t in initial: 

  print(t[-1])