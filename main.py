def is_number(string):
  try:
    float(string)
    return True
  except ValueError:
    return False

print()

print("Enter numbers, or min, max, mean, or range to get that statistic.\n")

numbers = []

while True:
  user_input = input("Enter a number or command: ")

  if is_number(user_input):
    numbers.append(float(user_input))
  elif len(numbers) == 0:
    print("\nEnter a number before entering a command.\n")
  elif user_input == "min":
    print(f"\nThe min is {min(numbers)}.\n")
  elif user_input == "max":
    print(f"\nThe max is {max(numbers)}.\n")
  elif user_input == "mean":
    print(f"\nThe mean is {sum(numbers) / len(numbers)}.\n")
  elif user_input == "range":
    print(f"\nThe range is {max(numbers) - min(numbers)}.\n")
  else:
    print("\nInvalid command.\n")
