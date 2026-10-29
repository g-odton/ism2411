# inventory.py
# Author: Grace Odton
# Module 10 Lab: Inventory List Manager

print("---Exercise 1: Build the list---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))
print()

print("---Exercise 2: Index Practice---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2 # calculate the index of the middle item
print(inventory[middle]) # middle item
print()

print("---Exercise 3: Slicing---")
print(inventory[:3]) # first 3 items
print(inventory[-2:]) # last 2 items
print(inventory[::2]) # skip every other item (0,2,4)
print(inventory[::-1]) # goes backwards / ascending order
print()

print("---Exercise 4: Modify---")
inventory.append('envelope')
print(inventory) # output: ['pen', 'notebook', 'stapler', 'tape', 'marker', 'envelope']
inventory.remove('tape')
print(inventory) # output: ['pen', 'notebook', 'stapler', 'marker', 'envelope']
# if add 2 tapes but use inventory.remove(), will remove first tape (Start at beginning, then once task done, stop)

# inventory.append("Zoo")
# inventory.sort()
# print(inventory)
# capitalization has precedence; characters/symbols like % -> number (not sorted in order??) -> capitals -> lowercase
print()

print("---Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")
print(coords)
print()

print("---Exercise 6: Average of a List of Sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")
print()

print("---Exercise 7: Accumulator Pattern---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2))
print("Original prices:", prices)
print("Discounts:", discount)
print()

print("---Exercise 8: Print Above Threshold---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")

# Reflection 1: What surprised me most about how lists work in Python:
#   2-3 sentences
# The most surprising thing about lists is that the .sort() method acts mildly stupidly. Numbers don't sort right and capitalization is prioritized, and that probably goes against most people's common sense when sorting things.

# Reflection 1: A business student situation where a Python list would have saved me time:
#   2-3 sentences
# A situation where a Python list would've saved time would be if there were several categories of information about a product (ID, revenue, cost, etc.), and the student originally just copied, pasted, and calculated everything and manually. With lists and a few other functions, the mess could be organized and calculated in seconds.