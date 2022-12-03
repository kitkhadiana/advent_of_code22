def getPriority(char):
  if char.islower():
    return ord(char) - 96
  return ord(char) - 38

with open("day3/d3_input.txt", "r") as f:
  s = 0
  while(True):
    a = set(f.readline().rstrip())
    b = set(f.readline().rstrip())
    c = set(f.readline().rstrip())
    if a == set():
      break
    common = a & b & c
    s += getPriority(common.pop())
  print(s)
