# Advent of Code 2015
# Day 6

# Part 1
# Solution: Use matrix to track light status. Change based on instruction.
def turn_lights(input=str):
  strings = input.splitlines()
  grid = [[-1]*1000 for i in range(1000)]
  lights_on = 0
  for instr in strings:
    pos = instr.split()
    if instr.startswith("toggle"):
      start_x, start_y = pos[1].split(',')
      end_x, end_y = pos[3].split(',')
      start_x, start_y = int(start_x), int(start_y)
      end_x, end_y = int(end_x), int(end_y)
      for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
          grid[x][y] *= -1
    else:
      start_x, start_y = pos[2].split(',')
      end_x, end_y = pos[4].split(',')
      start_x, start_y = int(start_x), int(start_y)
      end_x, end_y = int(end_x), int(end_y)
      for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
          grid[x][y] = -1 if pos[1] == "off" else 1
          
  for x in range(1000):
    for y in range(1000):
      if grid[x][y] == 1:
        lights_on += 1
  return lights_on


# Part 2
# Solution: Use matrix to track light brightness. Change based on instructions.
def adjust_brightness(input=str):
  strings = input.splitlines()
  grid = [[0]*1000 for i in range(1000)]
  total_brightness = 0
  for instr in strings:
    pos = instr.split()
    if instr.startswith("toggle"):
      start_x, start_y = pos[1].split(',')
      end_x, end_y = pos[3].split(',')
      start_x, start_y = int(start_x), int(start_y)
      end_x, end_y = int(end_x), int(end_y)
      for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
          grid[x][y] += 2
    else:
      start_x, start_y = pos[2].split(',')
      end_x, end_y = pos[4].split(',')
      start_x, start_y = int(start_x), int(start_y)
      end_x, end_y = int(end_x), int(end_y)
      for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
          if pos[1] == "off" and grid[x][y] > 0:
            grid[x][y] += -1
          elif pos[1] == "on":
            grid[x][y] += 1

  for x in range(1000):
    for y in range(1000):
      total_brightness += grid[x][y]
  return total_brightness
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day6/input.txt", "r") as f:
    text = f.read()
  print(f"Input length: {len(text)}")
  print(f"Number of lights on: {turn_lights(text)}")
  print(f"Total brightness of lights: {adjust_brightness(text)}")
  return None

if __name__ == "__main__":
  main()
