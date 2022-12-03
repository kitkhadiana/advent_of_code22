f = open("day2/d2_input.txt", "r")

def convert (choice):
  if choice == "A" or choice == "X":
    return 1
  elif choice == "B" or choice == "Y":
    return 2
  else:
    return 3

# 1 -> rock
# 2 -> paper
# 3 -> scissors
def winner (opponent, me):
  if opponent == me:
    return 3
  if opponent == 1:
    if me == 2:
      return 6
  if opponent == 2:
    if me == 3:
      return 6
  if opponent == 3:
    if me == 1:
      return 6
  return 0

s = 0
for x in f:
  opponent = convert(x[0])
  me = convert(x[2])
  s += me + winner(opponent, me)

print(s)
f.close()