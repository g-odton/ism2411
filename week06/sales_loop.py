# self-assessment
# 1. the three steps to the accumulator pattern are to initilize/start, loop, and update. 
# 2. for exercise 6, i noticed that while the code length was marginally shorter (at least, i think it should be), the while loop considered an indefinite set of values. if the sales list were longer, the while loop would probably be a better choice rather than a for loop, which is preferable for a known number of values.
# 3. as an accounting major, i'd probably go through lists of financial data for clients, especially concerning calculations, sales, etc. i'd likely accumulate and print the totals of these costs.

# exercise 1 + 2
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0       # initialize
count = 0       # ex. 2
for sale in sales:
    total += sale
    count += 1      # ex. 2
avg = total / count
print(f"Total: ${total}")      # ex. 2
print(f"Count: {count}")      # ex. 2
print(f"Average: ${avg:.2f}")      # ex. 2

# exercise 2
avg = total / count
print(f"Count: {count}")
print(f"Average: ${avg:.2f}")

# exercise 3
current_max = 0
for sale in sales:
    if sale > current_max:
        current_max = sale
print(f"Largest Sale: {current_max}")

# exercise 4
sales_over_100 = 0
total_100 = 0
for sale in sales:
    if sale > 100:
        sales_over_100 += 1
        total_100 += sale
print(f"Sales Over $100: {sales_over_100}")
print(f"Total of Those Sales: ${total_100:.2f}")

# exercise 5
print()
found = False
threshold = 400
for sale in sales:
    if sale > 100 and sale < threshold:
        print(f"${sale}")
        continue
    if sale >= threshold:
        print(f"Alert: outlier found — ${sale}. Stopping.")
        break

# exercise 6
print()
total = 0
i = 0            # index
while i < len(sales):
    total += sales[i]
    i += 1
    pass         # in production, i'd use for loop since it's probably more standard /understanable than a lengthy for loop
print(f"Count: {i}")
print()

# exercise 7
discount = 0
for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount)
    print(
        f"${sale} -> {discount*100:.0f}% discount -> "
        f"${discounted_price:.2f}"
    )
