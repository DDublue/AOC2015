# Advent of Code 2015
# Day 3

# Part 1
# Solution: Make a graph and use it to track visited houses.
def get_santa_houses(input=str):
  houses = 1
  x = 8200
  y = 8200
  graph = [([0]*8200*2) for i in range(8200*2)]
  graph[x][y] = 1
  input.rstrip()
  for way in input:
    if way == "^":
      y += 1
    elif way == "v":
      y -= 1
    elif way == "<":
      x -= 1
    elif way == ">":
      x += 1
    
    if not graph[x][y]:
      houses += 1
      graph[x][y] = 1
      
  return houses

# Part 2
# Solution: Same as part 1, but santa and robo take turns.
def get_santa_robo_houses(input=str):
  houses = 1
  x = rx = 8200
  y = ry = 8200
  turn = 0 # 0 = santa; 1 = robo
  graph = [([0]*8200*2) for i in range(8200*2)]
  graph[x][y] = 1
  input.rstrip()
  for way in input:
    if not turn:
      if way == "^":
        y += 1
      elif way == "v":
        y -= 1
      elif way == "<":
        x -= 1
      elif way == ">":
        x += 1
      
      if not graph[x][y]:
        houses += 1
        graph[x][y] = 1
      turn = 1
    else:
      if way == "^":
        ry += 1
      elif way == "v":
        ry -= 1
      elif way == "<":
        rx -= 1
      elif way == ">":
        rx += 1
        
      if not graph[rx][ry]:
        houses += 1
        graph[rx][ry] = 1
      turn = 0
  
  return houses
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day3/input.txt", "r") as f:
    text = f.read()
  print(f"Input length: {len(text)}")
  print(f"Houses with >0 presents: {get_santa_houses(text)}")
  print(f"Houses with >0 presents using robo: {get_santa_robo_houses(text)}")
  return None

if __name__ == "__main__":
  main()
