# Advent of Code 2015
# Day 7

import functools

# Helper functions

 

# Part 1
# Solution:
def get_output_a(input=str):
  @functools.cache
  def ev(x):
    if x.isnumeric():
      return int(x)
    expr = circuits[x]
    if len(expr) == 3:
      # AND
      if expr[1] == "AND":
        return ev(expr[0]) & ev(expr[2])
      # OR
      if expr[1] == "OR":
        return ev(expr[0]) | ev(expr[2])
      # LSHIFT
      if expr[1] == "LSHIFT":
        return ev(expr[0]) << int(expr[2])
      # RSHIFT
      if expr[1] == "RSHIFT":
        return ev(expr[0]) >> int(expr[2])
    elif len(expr) == 2:
      # NOT
      if expr[0] == "NOT":
        return ~ev(expr[1])
    else:
      # lowercase letters
      return ev(expr[0])
  
  circuits = {c.split(" -> ")[1]:tuple(c.split(" -> ")[0].split()) for c in input.splitlines()}
  gate = 'a'
  return ev(gate)

# Part 2
# Solution:
def get_output_b(input=str, part_a=int):
  @functools.cache
  def ev(x):
    if x.isnumeric():
      return int(x)
    expr = circuits[x]
    if len(expr) == 3:
      # AND
      if expr[1] == "AND":
        return ev(expr[0]) & ev(expr[2])
      # OR
      if expr[1] == "OR":
        return ev(expr[0]) | ev(expr[2])
      # LSHIFT
      if expr[1] == "LSHIFT":
        return ev(expr[0]) << int(expr[2])
      # RSHIFT
      if expr[1] == "RSHIFT":
        return ev(expr[0]) >> int(expr[2])
    elif len(expr) == 2:
      # NOT
      if expr[0] == "NOT":
        return ~ev(expr[1])
    else:
      # lowercase letters
      return ev(expr[0])
  
  circuits = {c.split(" -> ")[1]:tuple(c.split(" -> ")[0].split()) for c in input.splitlines()}
  gate = 'a'
  circuits['b'] = tuple([str(part_a)])
  return ev(gate)
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day7/input.txt", "r") as f:
    text = f.read()
  print(f"Input length: {len(text)}")
  a = get_output_a(text)
  print(f"signal a: {a}")
  print(f"signal b: {get_output_b(text, a)}")
  return None

if __name__ == "__main__":
  main()
