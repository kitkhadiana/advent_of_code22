import sys
sys.path.append("./helper")
from readfile import read

def find_marker(l):
  f = read(6)[0]
  for i in range(l, len(f) + 1):
    s = set(f[i - l : i])
    if len(s) == l:
      return i

print(find_marker(4))
print(find_marker(14))
