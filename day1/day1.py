# Advent of Code 2015
# Day 1

# Part 1
# Solution: If open parantheses, then add 1; if closed, then subtract 1.
def get_floor(input):
  floor = 0
  for char in input:
    if char == '(':
      floor += 1
    elif char == ')':
      floor -= 1
  return floor

# Part 2
# Solution: Iterate through input and track pointer for basement position.
#           When the floor reaches -1, return the pointer.
def get_basement_pos(input):
  floor = 0
  i = 0
  while floor > -1 and i < len(input):
    if input[i] == '(':
      floor += 1
    elif input[i] == ')':
      floor -= 1
    i += 1
  return i
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day1/input.txt", "r") as f:
    text = f.readline()
  floor = get_floor(text)
  basement_pos = get_basement_pos(text)
  print(f"Input length: {len(text)}")
  print(f"Floor for Santa: {floor}")
  print(f"Basement position: {basement_pos}")
  return None

if __name__ == "__main__":
  main()
