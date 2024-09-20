# Advent of Code 2015
# Day 4

import hashlib

# Part 1
# Solution:
def md5_five_zeroes(input=str):
  key = input.splitlines()[0]
  for i in range(9999999999999):
    hash_obj = hashlib.md5()
    num = str(i)
    string = key + num
    hash_obj.update(string.encode("utf-8"))
    hx = hash_obj.hexdigest()
    if str(hx[0:5]) == "00000":
      print(num)
      return hx
  return None


# Part 2
# Solution:
def md5_six_zeroes(input=str):
  key = input.splitlines()[0]
  for i in range(9999999999999):
    hash_obj = hashlib.md5()
    num = str(i)
    string = key + num
    hash_obj.update(string.encode("utf-8"))
    hx = hash_obj.hexdigest()
    if str(hx[0:6]) == "000000":
      print(num)
      return hx
  return None
      
      
def main():
  with open("/home/darwu/projects/aoc2015/day4/input.txt", "r") as f:
    text = f.read()
  print(f"Input length: {len(text)}")
  print(f"md5 output five zeroes: {md5_five_zeroes(text)}")
  print(f"md5 output six zeroes: {md5_six_zeroes(text)}")
  return None

if __name__ == "__main__":
  main()
