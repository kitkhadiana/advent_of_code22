f = open("day1/d1_input.txt", "r")
max1 = 0
max2 = 0
max3 = 0
s = 0
i = 1
for x in f:
  if x == "\n":
    if s > max1:
      max3 = max2
      max2 = max1
      max1 = s
    elif s > max2:
      max3 = max2
      max2 = s
    elif s > max3:
      max3 = s
    s = 0
  else:
    s = s + int(x)
if s > max1:
  max2 = max1
  max3 = max2
  max1 = s
elif s > max2:
  max3 = max2
  max2 = s
elif s > max3:
  max3 = s

print (sum([max1, max2, max3]))
f.close()