from pprint import pprint
import re


with open("input11.txt","r") as f: 
  data = f.read()

rules = data.split("\n\n")


monkeys = [[x.strip() for x in rules[i].split("\n")] for i in range(len(rules))]

ms = []
for i in range(len(monkeys)): 
  
  items = [int(x) for x in monkeys[i][1].strip("Starting items:").split(", ")]
  operand = re.search( "[\+\-\*]", monkeys[i][2])[0]
  val = monkeys[i][2].split(" ")[5]
  divis = int(re.search("[0-9]+", monkeys[i][3])[0])
  targets = (int(monkeys[i][4].split(" ")[5]), int(monkeys[i][5].split(" ")[5]))


  monkey = {
    "items": items, 
    "operation": operand, #string + - * 
    "value": val, #num
    "divis": divis, #num
    "targets": targets, # (0,1)
    "inspected": 0
  }
  ms.append(monkey)

lcm = 1 
divs = [x["divis"] for x in ms ]

for x in divs: 
  lcm = lcm* x

print(divs)
print(lcm)
for _ in range(10000): 
  print(_)
  for i in range(len(ms)):
    

    for item in ms[i]["items"]:
      
      if ms[i]["value"] == "old": 
        worry = item * item   
      else: 
        if ms[i]["operation"] == "+": 
          worry = item + int(ms[i]["value"])
        elif ms[i]["operation"] == "*":
          worry = item * int(ms[i]["value"])
      
      # worry = worry // 3 
      worry = worry % lcm
      
      ms[i]["inspected"] += 1
      if (worry ) % ms[i]["divis"] == 0: 
        t = ms[i]["targets"][0]
        
      else: 
        t = ms[i]["targets"][1]

      

      ms[t]["items"].append(worry )
      
    ms[i]["items"] = []

    
  
inspections = [x["inspected"] for x in ms]
print(sorted(inspections, reverse=True))
ins = sorted(inspections, reverse=True)

print( ins[0] * ins[1])