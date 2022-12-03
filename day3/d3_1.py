f = open("day3/d3_input.txt", "r")

def getPriority(char):
  if char.islower():
    return ord(char) - 96
  return ord(char) - 38

s = 0
for x in f:
  a = set(x[:len(x) // 2])
  b = set(x[len(x) // 2 :].rstrip())
  common = a&b
  for c in common:
    s += getPriority(c)

print(s)
f.close()