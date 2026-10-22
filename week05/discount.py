# lab 5: discount.py
# self-assessment qs
# 1. if total = 350, python would check if it was over or equal to 500. since that's false, it'd skip that 15% discount and see if the total's over 200. since that's true, python applies the 10% discount.
# 2. the difference between if total > 100 and total < 500 and two separate statements checking each would be that the first one considers both statements at once (if the total is both over 100 and below 500) and produces one bool (true or false), while having them separate would mean python checks them one at a time. if in order of total < 500, total > 100 and the total was greater than 500 only, python would stop at total < 500 and say it's false even though that total would be greater than 100.
# 3. i'd encounter tiered conditional logic probably while shopping or when i'm viewing grades. knowing python changes how i think about these things because everything really just runs on simple phyton code like this when it comes down to it. it's neat

# exercise 1
total = float(input("Enter cart total: $"))

#Add if/elif/else
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.05
else:
    discount = 0

# final = total * (1 - discount)

# exercise 3

region = "South" 
extra_discount = 0
if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")

final_discount = discount + extra_discount
final = total * (1 - final_discount)

print(f"Discount: {final_discount:.1%}") # gives whole percentage not rate
print(f"Final Price: {final:,.2f}") # give final at 2 decimals w commas

# exercise 2

if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")

# exercise 4

# if region == "South":
#     if total > 100:
#         if customer_type == "wholesale":
#             extra_discount = 0.03

# if region == "South" and total > 100 and customer_type == "wholesale":
#     extra_discount = 0.03

print(extra_discount)
print()

# exercise 5

amount = -50
if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE — REVIEW REQUIRED")

# exercise 6

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False

qualifies_by_spending = total_spent_this_year > 2000
qualifies_by_order = orders_this_year > 10

vip_upgrade = (qualifies_by_spending or qualifies_by_order) and not has_outstanding_balance
print(f"VIP Upgrade: {vip_upgrade}")