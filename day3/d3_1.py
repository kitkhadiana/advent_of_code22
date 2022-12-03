def getPriority(char):
  if char.islower():
    return ord(char) - 96
  return ord(char) - 38

# one liner
with open("day3/d3_input.txt", "r") as f:
  print(sum(getPriority((set(x[:len(x) // 2]) & set(x[len(x) // 2:].rstrip())).pop()) for x in f))

# multi liner
with open("day3/d3_input.txt", "r") as f:
  s = 0
  for x in f:
    a = set(x[:len(x) // 2])
    b = set(x[len(x) // 2 :].rstrip())
    common = a&b
    s += getPriority(common.pop())
  print(s)
