def read(day):
  file = "day" + str(day) + "/d" + str(day) + "_input.txt"
  with open(file, "r") as f:
    return list(x.rstrip() for x in f)
