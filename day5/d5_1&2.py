def read():
  matrix = []
  moves = []
  size = 9
  read_moves = False
  threshold = ""
  for i in range(size):
    matrix.append([])
    threshold += " " + str(i + 1) + "  "
  threshold = threshold[: -1] + "\n"
  with open("day5/d5_input.txt", "r") as f:
    for line in f:
      if line == threshold:
        read_moves = True
        f.readline()
      elif read_moves:
        split = line.split()
        moves.append([int(split[1]), int(split[3]) - 1, int(split[5]) - 1])
      else:
        for i in range(size):
          if line[i * 4 + 1] != " ":
            matrix[i] += line[i * 4 + 1]
  return matrix, moves

def gather(matrix):
  r = ""
  for list in matrix:
    r += list[0]
  return r

def perform_part1_move(matrix, move):
  count, orig, dest = move
  while count > 0:
    matrix[dest] = [matrix[orig][0]] + matrix[dest]
    matrix[orig] = matrix[orig][1:]
    count -= 1

def perform_part2_move(matrix, move):
  count, orig, dest = move
  matrix[dest] = matrix[orig][:count] + matrix[dest]
  matrix[orig] = matrix[orig][count:]

########################################################################

matrix, moves = (read())
for move in moves:
  perform_part1_move(matrix, move)
print(gather(matrix))

matrix, moves = (read())
for move in moves:
  perform_part2_move(matrix, move)
print(gather(matrix))