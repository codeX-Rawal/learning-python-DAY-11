# Day 11: Lists in Python

# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Numbers list:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Updating elements
numbers[1] = 25
print("Updated list:", numbers)

# Adding elements
numbers.append(60)
print("After append:", numbers)

numbers.insert(2, 15)
print("After insert:", numbers)

# Removing elements
numbers.remove(40)
print("After remove:", numbers)

popped_item = numbers.pop()
print("Popped item:", popped_item)
print("List after pop:", numbers)

# Length of list
print("Length of list:", len(numbers))

# Loop through list
print("\nLooping through list:")
for num in numbers:
    print(num)

# User input list
n = int(input("How many items you want to add? "))
items = []

for i in range(n):
    value = input("Enter item: ")
    items.append(value)

print("Your list:", items)

