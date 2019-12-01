import math
import pandas as pd

input_array = pd.read_csv('./2019/1/input', header=None)

############ Solution 1 #############

def fuel1(mass):
  return math.floor(mass / 3) - 2

# Unit tests for Solution 1 
def test1(input, expected):
  output = fuel1(input)
  result = "-"
  if (output == expected):
    result = "+"
  print(f"[{result}] {str(output)} = {str(expected)}")

test1(12, 2)
test1(14, 2)
test1(1969, 654)
test1(100756, 33583)

sum = 0
for mass in input_array[0]:
  sum += fuel1(mass)

print(f"Solution 1: {sum}")

############ Solution 2 #############

def fuel2(mass):
  sum = 0

  while True:
    fuel = math.floor(mass / 3) - 2
    mass = fuel
  
    if (fuel <= 0):
      break
  
    sum += fuel
    
  return sum

# Unit tests for Solution 2
def test2(input, expected):
  output = fuel2(input)
  result = "-"
  if (output == expected):
    result = "+"
  print(f"[{result}] {str(output)} = {str(expected)}")

test2(14, 2)
test2(1969, 966)
test2(100756, 50346)

sum = 0
for mass in input_array[0]:
  sum += fuel2(mass)

print(f"Solution 2: {sum}")
