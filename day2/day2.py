# Advent of Code 2015
# Day 2

# Part 1
# Solution: Get the dimensions of each present and calculate their surface area
#           and smallest side. Add all together.
def get_sqft(input=str):
  total_paper = 0
  dimensions = input.splitlines()
  for d in dimensions:
    l, w, h = [int(num) for num in d.split("x")]
    s1, s2, s3 = 2*l*w, 2*w*h, 2*h*l
    smallest_side = min(s1, s2, s3)
    total_paper += s1 + s2 + s3 + smallest_side/2
  return total_paper

# Part 2
# Solution: Get the dimensions of each present and calculate smallest perimeter
#           of any face and cubic volume. Add all together.
def get_ribbon_amount(input=str):
  total_ribbon = 0
  dimensions = input.splitlines()
  for d in dimensions:
    l, w, h = [int(num) for num in d.split("x")]
    smallest_perim = min(l+l+w+w, h+h+w+w, l+l+h+h)
    total_ribbon += (smallest_perim + l*w*h)
  return total_ribbon
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day2/input.txt", "r") as f:
    text = f.read()
  print(f"Input length: {len(text)}")
  print(f"Square feet needed: {get_sqft(text)}")
  print(f"Ribbon needed: {get_ribbon_amount(text)}")
  return None

if __name__ == "__main__":
  main()
