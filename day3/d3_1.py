def getPriority(char):
  if char.islower():
    return ord(char) - 96
  return ord(char) - 38

with open("day3/d3_input.txt", "r") as f:
  print(sum(getPriority((set(x[:len(x) // 2]) & set(x[len(x) // 2:].rstrip())).pop()) for x in f))
