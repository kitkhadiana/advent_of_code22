def read(file):
  with open(file, "r") as f:
    return list(x.rstrip() for x in f)
