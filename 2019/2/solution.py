############ Solution 1 #############

def solution1(i1, i2):
  input_file = open("./2019/2/input", "r")
  input_array = input_file.readlines()
  v = [int(line) for line in input_array]

  v[1] = i1
  v[2] = i2

  i = 0
  while v[i] != 99:
    if v[i] == 1:
      v[v[i+3]] = v[v[i+1]] + v[v[i+2]]
    
    if v[i] == 2:
      v[v[i+3]] = v[v[i+1]] * v[v[i+2]]

    i+=4

  return v[0]

print(f"Solution 1: {solution1(12, 2)}")

############ Solution 2 #############

for i in range(100):
  for j in range(100):
    if solution1(i, j) == 19690720:
      print(f"Solution 2: {100 * i + j}")
      break
