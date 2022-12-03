f = open("day3/d3_input.txt", "r")

def getPriority(char):
  if char.islower():
    return ord(char) - 96
  return ord(char) - 38

s = 0

while(True):
  a = set(f.readline().rstrip())
  b = set(f.readline().rstrip())
  c = set(f.readline().rstrip())
  if a == set():
    break
  common = list(a & b & c)
  s += getPriority(common[0])

print(s)
f.close()