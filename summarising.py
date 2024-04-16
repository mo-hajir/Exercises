lines = [
  "My King,",
  "I need another five years.",
  "Then your crab will be ready.",
  "Sincerely,",
  "Chuang-tzu"
]

text = ""

for line in lines:
    text = text + line
    text = text + line
print(text)

another_text = "\n".join(lines)
print(another_text)

#For numbers

def add_up_numbers(numbers):
  total = 0
  for number in numbers :
    total = total + number
  return total 