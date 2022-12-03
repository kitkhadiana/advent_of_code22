f = open("day2/d2_input.txt", "r")

def convert (choice):
  if choice == "A" or choice == "X":
    return 1
  elif choice == "B" or choice == "Y":
    return 2
  else:
    return 3

# A,1 -> rock
# B,2 -> paper
# C,3 -> scissors
def revert (opponent, me):
  if me == "X":
    r = convert(opponent) - 1
    if r == 0: r = 3
  if me == "Y":
    r = convert(opponent)
  if me == "Z":
    r = convert(opponent) + 1
    if r == 4: r = 1
  return r

s = 0
for x in f:
  opponent = x[0]
  me = x[2]
  if me == "Y":
    s += 3
  if me == "Z":
    s += 6
  s += revert(opponent, me)

print(s)
f.close()