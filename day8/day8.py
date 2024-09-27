# Advent of Code 2015
# Day 8

# Part 1
# Solution:
def get_num_chars(input=str):
  modded_input = input.replace("\\\\", "-")
  strings = modded_input.splitlines()
  code_chars = 0
  mem_chars = 0
  for s in strings:
    code_chars += len(s)
    bs_count = s.count("-")
    quote_count = s.count("\\\"")
    asc = s.count("\\x")
    ascii_count = asc * 3
    
    add = len(s) - 2 - bs_count - quote_count - ascii_count
    mem_chars += add
  return code_chars - mem_chars


# Part 2
# Solution:
def get_num_chars_encoded(input=str):
  strings = input.splitlines()
  code_chars = 0
  encd_chars = 0
  for s in strings:
    s = s.replace("\\\\", "-")
    bs_count = s.count("-") * 2
    quote_count = s.count("\\\"")
    asc = s.count("\\x")
    code_chars += len(s) + bs_count//2
    encd_chars += len(s) + bs_count//2 + 4 + bs_count + quote_count*2 + asc
  return encd_chars - code_chars
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day8/input.txt", "r") as f:
    text = f.read()
  print(f"Input length: {len(text)}")
  print(f"Chars: {get_num_chars(text)}")
  print(f"Chars 2: {get_num_chars_encoded(text)}")
  return None

if __name__ == "__main__":
  main()
