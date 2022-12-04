import sys
sys.path.append("./helper")
from readfile import read

f = read(4)
i = 0
for x in f:
  ranges = x.split(",")
  r1 = ranges[0].split("-")
  r2 = ranges[1].split("-")
  a = int(r1[0])
  b = int(r1[1])
  c = int(r2[0])
  d = int(r2[1])
  if (a >= c and a <= d) or (b >= c and b <= d) or (c >= a and c <= b) or (d >= a and d <= b):
    i += 1
print(i)
