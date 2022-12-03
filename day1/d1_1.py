f = open("day1/d1_input.txt", "r")
max = 0
s = 0
i = 1
for x in f:
  if x == "\n":
    if s > max:
      max = s
    s = 0
  else:
    s = s + int(x)
if s > max:
  max = s
print (max)
f.close()