# Advent of Code 2015
# Day 5

# Part 1
# Solution: Check for >=3 vowels and no duos+twices in each string.
def get_old_nice_strings(input=str):
  strings = input.splitlines()
  nice_strings = 0
  vowels = ["a", "e", "i", "o", "u"]
  duos = ["ab", "cd", "pq", "xy"]
  twices = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk",
            "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv",
            "ww", "xx", "yy", "zz"]
  for s in strings:
    count = 0
    for char in s:
      if char in vowels:
        count += 1
    if count < 3:
      continue
    
    if any(d in s for d in duos):
      continue
    
    if not any(t in s for t in twices):
      continue
    
    nice_strings += 1
  return nice_strings


# Part 2
# Solution: Check for non-overlapping double pairs and 3-length palindromes.
def get_new_nice_strings(input=str):
  strings = input.splitlines()
  nice_strings = 0
  for s in strings:
    if len(s) < 4: # for small string tests
      continue
    
    if not any(s[i:i+2] in s[i+2:] for i in range(len(s)-1)):
      continue
    
    if not any(s[i]==s[i+2] for i in range(len(s)-2)):
      continue
    
    nice_strings += 1
  
  return nice_strings
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day5/input.txt", "r") as f:
    text = f.read()
  print(f"Input length: {len(text)}")
  print(f"Old nice strings: {get_old_nice_strings(text)}")
  print(f"New nice strings: {get_new_nice_strings(text)}")
  return None

if __name__ == "__main__":
  main()
